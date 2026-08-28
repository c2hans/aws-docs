---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportTask.html
---

# ExportTask
<a name="API_ExportTask"></a>

Describes an export instance task.

## Contents
<a name="API_ExportTask_Contents"></a>

 ** description **
A description of the resource being exported.
Type: String
Required: No

 ** exportTaskId **
The ID of the export task.
Type: String
Required: No

 ** exportToS3 **
Information about the export task.
Type: [ExportToS3Task](API_ExportToS3Task.md) object
Required: No

 ** instanceExport **
Information about the instance to export.
Type: [InstanceExportDetails](API_InstanceExportDetails.md) object
Required: No

 ** state **
The state of the export task.
Type: String
Valid Values: `active | cancelling | cancelled | completed`
Required: No

 ** statusMessage **
The status message related to the export task.
Type: String
Required: No

 ** TagSet.N **
The tags for the export task.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ExportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ExportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ExportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ExportTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
