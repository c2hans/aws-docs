---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StoreImageTaskResult.html
---

# StoreImageTaskResult
<a name="API_StoreImageTaskResult"></a>

The information about the AMI store task, including the progress of the task.

## Contents
<a name="API_StoreImageTaskResult_Contents"></a>

 ** amiId **
The ID of the AMI that is being stored.
Type: String
Required: No

 ** bucket **
The name of the Amazon S3 bucket that contains the stored AMI object.
Type: String
Required: No

 ** progressPercentage **
The progress of the task as a percentage.
Type: Integer
Required: No

 ** s3objectKey **
The name of the stored AMI object in the bucket.
Type: String
Required: No

 ** storeTaskFailureReason **
If the tasks fails, the reason for the failure is returned. If the task succeeds, `null` is returned.
Type: String
Required: No

 ** storeTaskState **
The state of the store task (`InProgress`, `Completed`, or `Failed`).
Type: String
Required: No

 ** taskStartTime **
The time the task started.
Type: Timestamp
Required: No

## See Also
<a name="API_StoreImageTaskResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/StoreImageTaskResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/StoreImageTaskResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/StoreImageTaskResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
