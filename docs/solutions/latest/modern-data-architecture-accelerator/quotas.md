---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/quotas.html
---

# Quotas
<a name="quotas"></a>

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

## Quotas for AWS services in this solution
<a name="quotas-for-aws-services-in-this-solution"></a>

Make sure you have sufficient quota for the services to be deployed by your configuration. For more information, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

Use the following links to go to the page for that service. To view the service quotas for all AWS services in the documentation without switching pages, view the information in the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf#aws-service-information) page in the PDF instead.

|  |  |
| --- |--- |
|  [Amplify](https://docs.aws.amazon.com/general/latest/gr/amplify.html)  |  [Amazon ECR](https://docs.aws.amazon.com/general/latest/gr/ecr.html)  |
|  [Athena](https://docs.aws.amazon.com/general/latest/gr/athena.html)  |  [Lambda](https://docs.aws.amazon.com/general/latest/gr/lambda-service.html)  |
|  [CloudFront](https://docs.aws.amazon.com/general/latest/gr/cf_region.html)  |  [OpenSearch Service](https://docs.aws.amazon.com/general/latest/gr/opensearch-service.html)  |
|  [Cognito](https://docs.aws.amazon.com/general/latest/gr/cognito_identity.html)  |  [Neptune](https://docs.aws.amazon.com/general/latest/gr/neptune.html)  |
|  [Config](https://docs.aws.amazon.com/general/latest/gr/awsconfig.html)  |  [Amazon S3](https://docs.aws.amazon.com/general/latest/gr/s3.html)  |
|  [Amazon ECS](https://docs.aws.amazon.com/general/latest/gr/ecs-service.html)  |  |

## AWS CloudFormation quotas
<a name="aws-cloudformation-quotas"></a>

Your AWS account has AWS CloudFormation quotas that you should be aware of when launching this solution. By understanding these quotas, you can avoid limitation errors that would prevent you from deploying this solution successfully. For more information, see [AWS CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the in the *AWS CloudFormation User’s Guide*.

## AWS Lambda quotas
<a name="aws-lambda-quotas"></a>

Your account has an AWS Lambda concurrent execution quota of 1000. If the solution is used in an account where there are other workloads running and using Lambda, then set this quota to an appropriate value. This value is adjustable; for more information, see [AWS Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) in the *AWS Lambda User’s Guide*.

**Note**
This solution requires 150 executions from the concurrent execution quota to be available in the account to which the solution is being deployed. If there are fewer than 150 executions available in that account, the CloudFormation deployment will fail.

## Amazon VPC quotas
<a name="amazon-vpc-quotas"></a>

Your AWS account can contain five VPCs and two Elastic IPs (EIPs). If the solution is used in an account with other VPCs or EIPs, this could prevent you from deploying this solution successfully. If you are at risk of reaching this quota, you may provide your own VPC for deployment by providing it in your configuration. For more information, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html) in the * [Amazon VPC User’s Guide](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html).*
