---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ConversionTask.html
---

# ConversionTask
<a name="API_ConversionTask"></a>

Describes a conversion task.

## Contents
<a name="API_ConversionTask_Contents"></a>

 ** conversionTaskId **
The ID of the conversion task.
Type: String
Required: No

 ** expirationTime **
The time when the task expires. If the upload isn't complete before the expiration time, we automatically cancel the task.
Type: String
Required: No

 ** importInstance **
If the task is for importing an instance, this contains information about the import instance task.
Type: [ImportInstanceTaskDetails](API_ImportInstanceTaskDetails.md) object
Required: No

 ** importVolume **
If the task is for importing a volume, this contains information about the import volume task.
Type: [ImportVolumeTaskDetails](API_ImportVolumeTaskDetails.md) object
Required: No

 ** state **
The state of the conversion task.
Type: String
Valid Values: `active | cancelling | cancelled | completed`
Required: No

 ** statusMessage **
The status message related to the conversion task.
Type: String
Required: No

 ** TagSet.N **
Any tags assigned to the task.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ConversionTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ConversionTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ConversionTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ConversionTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
