---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AttachedFilesConfigurationSummary.html
---

# AttachedFilesConfigurationSummary
<a name="API_AttachedFilesConfigurationSummary"></a>

A summary of the attached files configuration.

## Contents
<a name="API_AttachedFilesConfigurationSummary_Contents"></a>

 ** AttachmentScope **   <a name="connect-Type-AttachedFilesConfigurationSummary-AttachmentScope"></a>
The scope of the attachment. Valid values are `EMAIL`, `CHAT`, `CASE`, and `TASK`.
Type: String
Valid Values: `EMAIL | CHAT | CASE | TASK`
Required: Yes

 ** InstanceId **   <a name="connect-Type-AttachedFilesConfigurationSummary-InstanceId"></a>
The identifier of the Connect Customer instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** ExtensionConfiguration **   <a name="connect-Type-AttachedFilesConfigurationSummary-ExtensionConfiguration"></a>
The configuration for allowed file extensions.
Type: [ExtensionConfiguration](API_ExtensionConfiguration.md) object
Required: No

 ** MaximumSizeLimitInBytes **   <a name="connect-Type-AttachedFilesConfigurationSummary-MaximumSizeLimitInBytes"></a>
The maximum size limit for attached files in bytes. The minimum value is 1 and the maximum value is 104857600 (100 MB).
Type: Long
Valid Range: Minimum value of 1. Maximum value of 104857600.
Required: No

## See Also
<a name="API_AttachedFilesConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AttachedFilesConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AttachedFilesConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AttachedFilesConfigurationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
