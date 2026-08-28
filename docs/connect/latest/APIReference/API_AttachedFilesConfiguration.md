---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AttachedFilesConfiguration.html
---

# AttachedFilesConfiguration
<a name="API_AttachedFilesConfiguration"></a>

The configuration for attached files for a specific attachment scope.

## Contents
<a name="API_AttachedFilesConfiguration_Contents"></a>

 ** AttachmentScope **   <a name="connect-Type-AttachedFilesConfiguration-AttachmentScope"></a>
The scope of the attachment. Valid values are `EMAIL`, `CHAT`, `CASE`, and `TASK`.
Type: String
Valid Values: `EMAIL | CHAT | CASE | TASK`
Required: Yes

 ** InstanceId **   <a name="connect-Type-AttachedFilesConfiguration-InstanceId"></a>
The identifier of the Connect Customer instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** ExtensionConfiguration **   <a name="connect-Type-AttachedFilesConfiguration-ExtensionConfiguration"></a>
The configuration for allowed file extensions.
Type: [ExtensionConfiguration](API_ExtensionConfiguration.md) object
Required: No

 ** LastModifiedTime **   <a name="connect-Type-AttachedFilesConfiguration-LastModifiedTime"></a>
The timestamp when the configuration was last modified.
Type: Timestamp
Required: No

 ** MaximumSizeLimitInBytes **   <a name="connect-Type-AttachedFilesConfiguration-MaximumSizeLimitInBytes"></a>
The maximum size limit for attached files in bytes.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 104857600.
Required: No

## See Also
<a name="API_AttachedFilesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AttachedFilesConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AttachedFilesConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AttachedFilesConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
