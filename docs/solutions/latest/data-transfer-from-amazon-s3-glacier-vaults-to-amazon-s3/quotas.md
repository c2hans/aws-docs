---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/quotas.html
---

# Quotas
<a name="quotas"></a>

 Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

## Quotas for AWS services in this Guidance
<a name="quotas-for-aws-services-in-this-guidance"></a>

 Make sure you have a sufficient quota for each of the [services implemented in this Guidance](architecture-details.md#aws-services-in-this-guidance). For more information, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

 Use the following links to go to the page for that service. To view the service quotas for all AWS services in the documentation without switching pages, view the information in the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf#aws-service-information) page in the PDF instead.

## AWS CloudFormation quotas
<a name="aws-cloudformation-quotas"></a>

 Your AWS account has AWS CloudFormation quotas that you should be aware of when [launching the stack](step-1-launch-the-stack.md) in this Guidance. By understanding these quotas, you can avoid limitation errors that would prevent you from deploying this Guidance successfully. For more information, see [AWS CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the AWS CloudFormation User Guide.

## Lambda concurrent execution quota
<a name="lambda-concurrent-execution-quota"></a>

 Your AWS account has a quota on the number of concurrent Lambda executions that can be running. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) in the *AWS Lambda Developer Guide.* This Guidance uses 230–250 concurrent Lambda executions when running at maximum capacity.

## Amazon Glacier Initiate Job quota
<a name="amazon-s3-glacier-initiate-job-quota"></a>

This Guidance optimizes your transfer by requesting archives in order. Other random restore requests can impact throughput.

 The Amazon Glacier service maintains a service quota of [35 random restore requests](https://docs.aws.amazon.com/general/latest/gr/glacier-service.html) per PiB stored per day. If you continue to initiate your archive retrievals as the Guidance runs, Amazon Glacier responses might slow down. You might also see Amazon Glacier [ThrottlingExceptions](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-error-responses.html) if you initiate archive retrievals external to the Guidance.

## Amazon S3 file size limit
<a name="amazon-s3-file-size-limit"></a>

 The Amazon S3 service restricts file sizes to 5 TB. The Guidance won't transfer archives larger than 5 TB. The Guidance's CloudWatch dashboard indicates the number of archives that meet this condition. The Guidance stores inventory data for these archives in the Inventory S3 bucket under `$WORKFLOW_RUN/not_migrated/`.
