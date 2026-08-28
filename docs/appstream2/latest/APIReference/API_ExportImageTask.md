---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ExportImageTask.html
---

# ExportImageTask
<a name="API_ExportImageTask"></a>

Information about an export image task, including its current state, timestamps, and any error details.

## Contents
<a name="API_ExportImageTask_Contents"></a>

 ** AmiName **   <a name="WorkSpacesApplications-Type-ExportImageTask-AmiName"></a>
The name of the EC2 AMI that will be created by this export task.
Type: String
Pattern: `^[a-zA-Z0-9().\-/_]{3,128}$`
Required: Yes

 ** CreatedDate **   <a name="WorkSpacesApplications-Type-ExportImageTask-CreatedDate"></a>
The date and time when the export image task was created.
Type: Timestamp
Required: Yes

 ** ImageArn **   <a name="WorkSpacesApplications-Type-ExportImageTask-ImageArn"></a>
The ARN of the WorkSpaces Applications image being exported.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: Yes

 ** TaskId **   <a name="WorkSpacesApplications-Type-ExportImageTask-TaskId"></a>
The unique identifier for the export image task. Use this ID to track the task's progress and retrieve its details.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** AmiDescription **   <a name="WorkSpacesApplications-Type-ExportImageTask-AmiDescription"></a>
The description that will be applied to the exported EC2 AMI.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** AmiId **   <a name="WorkSpacesApplications-Type-ExportImageTask-AmiId"></a>
The ID of the EC2 AMI that was created by this export task. This field is only populated when the task completes successfully.
Type: String
Pattern: `^ami-[a-z0-9]{8,17}$`
Required: No

 ** ErrorDetails **   <a name="WorkSpacesApplications-Type-ExportImageTask-ErrorDetails"></a>
Details about any errors that occurred during the export process. This field is only populated when the task fails.
Type: Array of [ErrorDetails](API_ErrorDetails.md) objects
Required: No

 ** State **   <a name="WorkSpacesApplications-Type-ExportImageTask-State"></a>
The current state of the export image task, such as PENDING, RUNNING, COMPLETED, or FAILED.
Type: String
Valid Values: `EXPORTING | COMPLETED | FAILED | TIMED_OUT`
Required: No

 ** TagSpecifications **   <a name="WorkSpacesApplications-Type-ExportImageTask-TagSpecifications"></a>
The tags that will be applied to the exported EC2 AMI.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(^(?!aws:).[\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_ExportImageTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ExportImageTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ExportImageTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ExportImageTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
