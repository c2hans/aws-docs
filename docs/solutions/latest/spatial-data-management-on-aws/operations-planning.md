---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/operations-planning.html
---

# Operations planning
<a name="operations-planning"></a>

## Monitoring and Operations
<a name="monitoring-and-operations"></a>

For detailed information on monitoring, backup, and recovery best practices, see the following sections:
+ For monitoring and operational visibility, see [Infrastructure Security](infrastructure-security.md) in the Security section
+ For backup and disaster recovery strategies, see [Resilience](resilience.md) in the Security section
+ For architecture details on monitoring services, see [AWS Services](aws-services.md) in the Architecture Overview

## Quotas
<a name="quotas"></a>

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

### Quotas for AWS Services in This Solution
<a name="quotas-for-aws-services"></a>

Make sure you have sufficient quota for each of the services implemented in this solution. For more information, refer to [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

Use the following links to view service quotas for the AWS services used in this solution:

| Service | Documentation Link |
| --- | --- |
| Amazon API Gateway |  [API Gateway quotas](https://docs.aws.amazon.com/general/latest/gr/apigateway.html)  |
| Amazon CloudFront |  [CloudFront quotas](https://docs.aws.amazon.com/general/latest/gr/cf_region.html)  |
| Amazon CloudWatch |  [CloudWatch quotas](https://docs.aws.amazon.com/general/latest/gr/cloudwatch_limits.html)  |
| Amazon Cognito |  [Cognito quotas](https://docs.aws.amazon.com/general/latest/gr/cognito_identity.html)  |
| Amazon DynamoDB |  [DynamoDB quotas](https://docs.aws.amazon.com/general/latest/gr/ddb.html)  |
| Amazon EventBridge |  [EventBridge quotas](https://docs.aws.amazon.com/general/latest/gr/cwe_region.html)  |
| Amazon OpenSearch Serverless |  [OpenSearch Serverless quotas](https://docs.aws.amazon.com/general/latest/gr/opensearch-service.html)  |
| Amazon S3 |  [S3 quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html)  |
| Amazon SQS |  [SQS quotas](https://docs.aws.amazon.com/general/latest/gr/sqs-service.html)  |
| Amazon Verified Permissions |  [Verified Permissions quotas](https://docs.aws.amazon.com/general/latest/gr/verifiedpermissions.html)  |
| AWS CloudFormation |  [CloudFormation quotas](https://docs.aws.amazon.com/general/latest/gr/cfn.html)  |
| AWS KMS |  [KMS quotas](https://docs.aws.amazon.com/general/latest/gr/kms.html)  |
| AWS Lambda |  [Lambda quotas](https://docs.aws.amazon.com/general/latest/gr/lambda-service.html)  |
| AWS Secrets Manager |  [Secrets Manager quotas](https://docs.aws.amazon.com/general/latest/gr/asm.html)  |

### Key Quota Considerations
<a name="key-quota-considerations"></a>

Before deploying this solution, verify the following quotas in your AWS account:

 **AWS Lambda:**
+ Concurrent executions: Default 1000 (solution reserves up to 500)
+ Function storage: Default 75 GB
+ If your account has reduced quotas, request an increase before deployment

 **Amazon DynamoDB:**
+ Tables per region: Default 2500 (solution creates 11 tables)
+ On-demand throughput: No fixed limit, but subject to account-level limits

 **Amazon S3:**
+ Buckets per account: Default 100 (solution creates 5 buckets)
+ Objects per bucket: Unlimited

 **VPC:**
+ VPCs per Region: Default 5 (the solution creates 1 VPC when not using an existing VPC)
+ VPC endpoints per VPC: Default 50 (the solution creates up to 14 endpoints when not using an existing VPC)

**Note**
If you deploy into an existing VPC using the `ExistingVpcId` parameter, the solution does not create a new VPC and does not consume a VPC quota slot. You must pre-create all required VPC endpoints before deploying — the solution validates that they exist but does not create them.

 **Amazon API Gateway:**
+ Regional APIs per account: Default 600 (solution creates 1 API)
+ Requests per second: Default 10,000 (solution throttles at 500 req/s)

To view your current quotas and request increases, use the [Service Quotas console](https://console.aws.amazon.com/servicequotas/).
