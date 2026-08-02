---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/quotas.html
---

# Quotas
<a name="quotas"></a>

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

## Quotas for AWS services in this solution
<a name="quotas-for-aws-services-in-this-solution"></a>

Make sure you have sufficient quota for each of the [services implemented in this solution](aws-services-in-this-solution.md). For more information, refer to [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

Use the following links to view service quotas. To view the service quotas for all AWS services in the documentation without switching pages, refer to the [Service endpoints and quotas](https://docs.aws.amazon.com/pdfs/general/latest/gr/aws-general.pdf#aws-service-information) page.

|  |  |
| --- |--- |
|  [Amazon EventBridge](https://docs.aws.amazon.com/general/latest/gr/cwe_region.html)  |  [AWS CodeBuild](https://docs.aws.amazon.com/general/latest/gr/codebuild.html)  |
|  [Amazon CloudFront](https://docs.aws.amazon.com/general/latest/gr/cf_region.html)  |  [Amazon API Gateway](https://docs.aws.amazon.com/general/latest/gr/apigateway.html)  |
|  [AWS AppConfig](https://docs.aws.amazon.com/general/latest/gr/appconfig.html)  |  [AWS CloudFormation](https://docs.aws.amazon.com/general/latest/gr/cfn.html)  |
|  [Amazon DynamoDB](https://docs.aws.amazon.com/general/latest/gr/ddb.html)  |  [AWS IAM Identity Center](https://docs.aws.amazon.com/general/latest/gr/sso.html)  |
|  [AWS KMS](https://docs.aws.amazon.com/general/latest/gr/kms.html)  |  [AWS Lambda](https://docs.aws.amazon.com/general/latest/gr/lambda-service.html)  |
|  [Amazon CloudWatch Logs](https://docs.aws.amazon.com/general/latest/gr/cwl_region.html)  |  [AWS Organizations](https://docs.aws.amazon.com/general/latest/gr/ao.html)  |
|  [AWS RAM](https://docs.aws.amazon.com/general/latest/gr/ram.html)  |  [Amazon S3](https://docs.aws.amazon.com/general/latest/gr/s3.html)  |
|  [AWS Secrets Manager](https://docs.aws.amazon.com/general/latest/gr/asm.html)  |  [Amazon SQS](https://docs.aws.amazon.com/general/latest/gr/sqs-service.html)  |
|  [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/general/latest/gr/ssm.html#parameter-store)  |  [AWS Step Functions](https://docs.aws.amazon.com/general/latest/gr/step-functions.html)  |

## AWS CloudFormation quotas
<a name="aws-cloudformation-quotas"></a>

Make sure you are aware of AWS CloudFormation quotas when [launching the stack](launch-the-stack.md) in this solution. By understanding these quotas, you can avoid limitation errors that would prevent you from deploying this solution successfully. For more information, refer to [AWS CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the *AWS CloudFormation User’s Guide*.

## AWS Lambda quotas
<a name="aws-lambda-quotas"></a>

Your account has an AWS Lambda concurrent execution quota of 1000. If the solution is used in an account where there are other workloads running and using Lambda, set this quota to an appropriate value. This value is adjustable; for more information, see [AWS Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) in the *AWS Lambda User’s Guide*.

## AWS CodeBuild quotas
<a name="aws-codebuild-quotas"></a>

Make sure you are aware of [AWS CodeBuild quotas](https://docs.aws.amazon.com/codebuild/latest/userguide/limits.html) when [launching the stack](launch-the-stack.md) in this solution.

**Note**
By default, concurrent CodeBuild quotas are low. To efficiently handle account recycling with this solution, we recommend you request a higher concurrent build quota before you launch the solution.
