---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

 This section provides a reference implementation architecture diagram for the components deployed with this Guidance.

## Architecture diagram
<a name="architecture-diagram"></a>

 Deploying this Guidance with the default parameters deploys the following components in your AWS account.

![AWS Step Functions orchestrates Lambda functions that perform the data transfer between your S3 Glacier vault and an S3 bucket.](http://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/images/architecture-diagram.png)

**Note**
 AWS CloudFormation resources are created from [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) (AWS CDK) constructs.

 The high-level process flow for the Guidance components deployed with the [AWS CloudFormation](https://aws.amazon.com/cloudformation/) template is as follows:

1.  Invoke a transfer workflow by using a [Systems Manager](https://aws.amazon.com/systems-manager/) [document](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents.html) (SSM document).

1.  The Systems Manager document starts an [AWS Step Functions](https://aws.amazon.com/step-functions/) `Orchestrator` execution.

1.  The Step Functions `Orchestrator` execution initiates a nested Step Functions `Get Inventory` workflow to retrieve the inventory file.

1.  Upon completion of the inventory retrieval, the Guidance invokes the `Initiate Retrieval` nested Step Functions workflow.

1.  When a job is ready, the [Amazon Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html) service sends a notification to an [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS) topic indicating job completion.

1.  The Guidance stores all job completion notifications in the [Amazon Simple Queue Service](https://aws.amazon.com/sqs/) (Amazon SQS) `Notifications` queue.

1.  When an archive job is ready, the Amazon SQS `Notifications` queue invokes the [AWS Lambda](https://aws.amazon.com/lambda/) `Notifications Processor` function. This Lambda function prepares the initial steps for archive retrieval.

1.  The Lambda `Notifications Processor` function places chunks retrieval messages in Amazon SQS `Chunks Retrieval` queue for chunk processing.

1.  The Amazon SQS `Chunks Retrieval` queue invokes the Lambda `Chunk Retrieval` function to process each chunk.

1.  The Lambda `Chunk Retrieval` function downloads the chunk from the Amazon Glacier service.

1.  The Lambda `Chunk Retrieval` function uploads a [multipart upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html) part to the [Amazon S3](https://aws.amazon.com/s3/) service.

1.  After a new chunk is downloaded, the Guidance stores chunk metadata in [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) (`etag`, `checksum_sha_256`, `tree_checksum`).

1.  The Lambda `Chunk Retrieval` function verifies whether all chunks for that archive have been processed. If yes, it inserts an event into the Amazon SQS `Validation` queue to invoke the Lambda `Validate` function.

1.  The Lambda `Validate` function does the following:

   1. Performs an integrity check against the tree hash in the inventory.

   1. Calculates a checksum and passes it to the into the close multipart upload call. If that hash is wrong, Amazon S3 rejects the request.

1.  A DynamoDB [stream](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) invokes the Lambda `Metrics Processor` function to update the transfer process metrics in DynamoDB.

1.  The Step Functions `Orchestrator` execution enters an `async` wait, pausing until the archive retrieval workflow concludes before initiating the Step Functions `Cleanup` workflow.

1.  The DynamoDB stream invokes the Lambda `Async Facilitator` function, which unlocks asynchronous waits in Step Functions.

1.  The [Amazon EventBridge](https://aws.amazon.com/eventbridge/) rules periodically initiate Step Functions `Extend Download Window` and `Update CloudWatch Dashboard` workflows.

1.  Customers monitor the transfer progress by using the Amazon CloudWatch dashboard.

### Translation of Amazon Glacier vault archive descriptions to S3 object names
<a name="translation-of-s3-glacier-vault-archive-descriptions-to-s3-object-names"></a>

 To create the key name for each of the new objects in the Amazon S3 service, this Guidance uses the **ArchiveDescription** value for each **ArchiveId** listed in the Amazon Glacier inventory file. The following are examples.

1.  If the **ArchiveDescription** is a single string value, such as `data01`, the Guidance translates that value to an S3 object key name in the destination S3 bucket.
![Amazon S3 object labeled data01.](http://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/images/image3.png)

1.  If the **ArchiveDescription** value is blank, then the Guidance does the following:

   1.  Copies the archive.

   1.  Uses the **ArchiveId** as the S3 object key name.

   1.  Adds the prefix `00undefined` to the S3 object key names and stores the objects in the destination S3 bucket.
![Amazon S3 object labeled with a randomized alpha-numeric name.](http://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/images/image4.png)

1.  If multiple **ArchiveId** entries have the same value for the **ArchiveDescription** field (for example, `duplicatefile02.txt`), then the Guidance appends a timestamp suffix to the name of the original file. This resolves the potential issue of having duplicate S3 object key names copied over one another. The timestamp used is the CreationDate of the archive.

![Three Amazon S3 objects labeled duplicatefile02.txt with timestamps.](http://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/images/image5.png)

### Creating custom file names for S3 objects
<a name="creating-custom-file-names-for-s3-objects"></a>

 You can provide custom S3 object key names for each **ArchiveId** that's copied to your S3 bucket. To do this, provide a **NamingOverrideFile** to the Guidance when you [launch the transfer workflow](step-2-launch-the-transfer-workflow.md), using the **NamingOverrideFile** input parameter. Use the following process.

1.  Create a data file in CSV format. The file must contain only two columns: **GlacierArchiveID** and **FileName** (separated by a comma). The following table is an example.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/architecture-overview.html)

1.  Obtain a copy of your vault inventory file for the Amazon Glacier service. For more information, see [Downloading a Vault Inventory in Amazon Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-inventory.html) in the *Amazon Glacier Developer Guide*.

1.  Copy all the **ArchiveId** values from your Amazon Glacier vault inventory file. Paste them into the **GlacierArchiveID** column of your **NamingOverride** CSV file.

1.  In the **FileName** column, for each **ArchiveID**, enter your desired S3 object key name.
**Note**
 If you provide an empty value for the **FileName**, the Guidance uses the original value for **ArchiveDescription** from the Amazon Glacier archive.

1.  Upload the CSV file to any S3 bucket and [create a presigned URL for the file](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html).

1.  Use this presigned URL as the value of the **NamingOverride File** input parameter used when [launching the transfer workflow](step-2-launch-the-transfer-workflow.md).
