---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AttachedFile.html
---

# AttachedFile
<a name="API_AttachedFile"></a>

Information about the attached file.

## Contents
<a name="API_AttachedFile_Contents"></a>

 ** CreationTime **   <a name="connect-Type-AttachedFile-CreationTime"></a>
The time of Creation of the file resource as an ISO timestamp. It's specified in ISO 8601 format: `yyyy-MM-ddThh:mm:ss.SSSZ`. For example, `2024-05-03T02:41:28.172Z`.
Type: String
Required: Yes

 ** FileArn **   <a name="connect-Type-AttachedFile-FileArn"></a>
The unique identifier of the attached file resource (ARN).
Type: String
Required: Yes

 ** FileId **   <a name="connect-Type-AttachedFile-FileId"></a>
The unique identifier of the attached file resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** FileName **   <a name="connect-Type-AttachedFile-FileName"></a>
A case-sensitive name of the attached file being uploaded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^\P{C}*$`
Required: Yes

 ** FileSizeInBytes **   <a name="connect-Type-AttachedFile-FileSizeInBytes"></a>
The size of the attached file in bytes.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

 ** FileStatus **   <a name="connect-Type-AttachedFile-FileStatus"></a>
The current status of the attached file.
Type: String
Valid Values: `APPROVED | REJECTED | PROCESSING | FAILED`
Required: Yes

 ** AssociatedResourceArn **   <a name="connect-Type-AttachedFile-AssociatedResourceArn"></a>
The resource to which the attached file is (being) uploaded to. The supported resources are [Cases](https://docs.aws.amazon.com/connect/latest/adminguide/cases.html), [Email](https://docs.aws.amazon.com/connect/latest/adminguide/setup-email-channel.html), and [Task](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-getting-started-tasks.html).
This value must be a valid ARN.
Type: String
Required: No

 ** CreatedBy **   <a name="connect-Type-AttachedFile-CreatedBy"></a>
Represents the identity that created the file.
Type: [CreatedByInfo](API_CreatedByInfo.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** FileUseCaseType **   <a name="connect-Type-AttachedFile-FileUseCaseType"></a>
The use case for the file.
Type: String
Valid Values: `CONTACT_ANALYSIS | EMAIL_MESSAGE | EMAIL_MESSAGE_PLAIN_TEXT | EMAIL_MESSAGE_REDACTED | EMAIL_MESSAGE_PLAIN_TEXT_REDACTED | ATTACHMENT | VOICE_RECORDING`
Required: No

 ** Tags **   <a name="connect-Type-AttachedFile-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, `{ "Tags": {"key1":"value1", "key2":"value2"} }`.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_AttachedFile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AttachedFile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AttachedFile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AttachedFile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
