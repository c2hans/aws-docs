---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/infrastructure-security.html
---

# Infrastructure Security
<a name="infrastructure-security"></a>

The solution implements multiple layers of infrastructure security controls.

## Network Isolation
<a name="network-isolation"></a>

 **VPC Architecture**
+ Dedicated VPC with RFC 1918 private IP addressing
+ Three subnet tiers: Public, Private, and Isolated
+ Network ACLs provide subnet-level filtering
+ Security groups provide instance-level filtering

 **Internet Access Control**
+ Lambda functions in isolated subnets have no internet access
+ Lambda functions in private subnets access internet via NAT Gateway
+ All AWS service access uses VPC endpoints (no internet required)
+ S3 and DynamoDB use gateway endpoints

 **VPC Endpoint Security**
+ Interface endpoints use security groups to control access
+ Gateway endpoints use route table associations
+ Endpoint policies restrict access to specific resources
+ Private DNS ensures traffic stays within AWS network

## Resource Isolation
<a name="resource-isolation"></a>

 **Compute Isolation**

Lambda functions are isolated at multiple levels. For details on Lambda isolation requirements and implementation, see [AWS Lambda Runtime Environment](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html) and [Lambda VPC Configuration](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html).

 **Data Isolation**
+ Each deployment gets unique S3 bucket names (deployment UUID)
+ No cross-deployment data access
+ IAM policies enforce resource-level permissions

 **Multi-Tenancy**
+ Single-tenant deployment model (one deployment per AWS account)

## Security Groups
<a name="security-groups"></a>

 **Lambda Function Security Group**
+ Inbound: None (Lambda doesn’t accept inbound connections)
+ Outbound: HTTPS (443) to VPC endpoints and internet (via NAT)
+ Attached to: All Lambda functions in VPC

 **VPC Endpoint Security Group**
+ Inbound: HTTPS (443) from Lambda security group
+ Outbound: All traffic
+ Attached to: All interface VPC endpoints

 **OpenSearch Security Group**
+ Inbound: HTTPS (443) from Lambda security group
+ Outbound: None
+ Attached to: OpenSearch VPC endpoint

## Cross-Service Confused Deputy Prevention
<a name="cross-service-confused-deputy-prevention"></a>

The confused deputy problem is a security issue where an entity that doesn’t have permission to perform an action can coerce a more-privileged entity to perform the action. In AWS, cross-service impersonation can result in the confused deputy problem.

### How SDMA Prevents Confused Deputy
<a name="how-sdma-prevents-confused-deputy"></a>

The solution uses the `aws:SourceArn` condition key in resource-based policies to prevent confused deputy attacks. These policies are automatically configured by AWS CDK during deployment.

 **Lambda Invocation from API Gateway**

The Resource Operation Lambda function has a resource-based policy that restricts API Gateway invocations to only the deployed API. This policy ensures that only the specific API Gateway instance can invoke the Lambda function, preventing other API Gateway instances from impersonating the service.

```
{
  "Version": "2012-10-17",			 	 	 &TCX5-2025-waiver;
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "apigateway.amazonaws.com"
      },
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:us-west-2:111122223333:function:SpatialDataManagement-ResourceOperationFunction",
      "Condition": {
        "ArnLike": {
          "AWS:SourceArn": "arn:aws:execute-api:us-west-2:111122223333:api-id/*/*/*"
        }
      }
    }
  ]
}
```

 **EventBridge to SQS Queue**

SQS queues that receive events from EventBridge have policies that restrict message sending to specific EventBridge rules. This policy ensures that only the specific EventBridge rule can send messages to the queue, preventing unauthorized event sources from injecting messages.

```
{
  "Version": "2012-10-17",			 	 	 &TCX5-2025-waiver;
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "events.amazonaws.com"
      },
      "Action": [
        "sqs:SendMessage",
        "sqs:GetQueueAttributes",
        "sqs:GetQueueUrl"
      ],
      "Resource": "arn:aws:sqs:us-west-2:111122223333:asset-file-notification-queue",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:events:us-west-2:111122223333:rule/file-object-created-rule"
        }
      }
    }
  ]
}
```
