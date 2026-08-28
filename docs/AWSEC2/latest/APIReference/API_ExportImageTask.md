---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportImageTask.html
---

# ExportImageTask
<a name="API_ExportImageTask"></a>

Describes an export image task.

## Contents
<a name="API_ExportImageTask_Contents"></a>

 ** description **
A description of the image being exported.
Type: String
Required: No

 ** exportImageTaskId **
The ID of the export image task.
Type: String
Required: No

 ** imageId **
The ID of the image.
Type: String
Required: No

 ** progress **
The percent complete of the export image task.
Type: String
Required: No

 ** s3ExportLocation **
Information about the destination Amazon S3 bucket.
Type: [ExportTaskS3Location](API_ExportTaskS3Location.md) object
Required: No

 ** status **
The status of the export image task. The possible values are `active`, `completed`, `deleting`, and `deleted`.
Type: String
Required: No

 ** statusMessage **
The status message for the export image task.
Type: String
Required: No

 ** TagSet.N **
Any tags assigned to the export image task.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ExportImageTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ExportImageTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ExportImageTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ExportImageTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
