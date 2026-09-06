---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

 This section describes the components and AWS services that make up this Guidance and the architecture details on how these components work together.

## AWS services in this Guidance
<a name="aws-services-in-this-guidance"></a>

|  AWS service  |  Description  |
| --- | --- |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  Core. Stores inventory and archives transferred from the Amazon Glacier service.  |
|  [Amazon Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)  |  Core. Maintains the vault being transferred to the Amazon S3 service.  |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  |  Core. Stores workflow-related data, including hash validation values and progress metrics for Amazon Glacier archives.  |
|  [AWS Glue](https://aws.amazon.com/glue/)  |  Core. Reorders and splits the Amazon Glacier vault inventory file into partitions for processing by multiple Lambda invocations. Parses file names from Inventory/OverrideNaming file.  |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  Core. Performs workflow compute, including archive transfer and validation.  |
|  [Amazon SNS](https://aws.amazon.com/sns/)  |  Supporting. Decouples Lambda workflows by providing communication between the Guidance, the Amazon Glacier service, and Amazon SQS queues.  |
|  [Amazon SQS](https://aws.amazon.com/sqs/)  |  Supporting. Decouples Lambda workflows.  |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  |  Supporting. Stores the Guidance logs and metrics. Presents a custom dashboard to provide visibility of the archive copy operation progress.  |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)  |  Supporting. Invokes supporting workflows that promote the smooth operation of the Guidance.  |
|  [IAM](https://aws.amazon.com/iam/)  |  Supporting. Provides permissions for this Guidance's resources to perform actions.  |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  Supporting. Provides a Systems Manager [document](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents.html) (SSM document) for Guidance's workflow invocations.  |
|  [AWS Step Functions](https://aws.amazon.com/step-functions/)  |  Supporting. Orchestrates partitioning the inventory with AWS Glue. Also orchestrates Lambda invocations to request Amazon Glacier vault archive retrieval.  |
