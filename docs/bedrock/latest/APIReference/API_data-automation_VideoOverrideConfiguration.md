---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_VideoOverrideConfiguration.html
---

# VideoOverrideConfiguration
<a name="API_data-automation_VideoOverrideConfiguration"></a>

Sets whether your project will process videos or not.

## Contents
<a name="API_data-automation_VideoOverrideConfiguration_Contents"></a>

 ** modalityProcessing **   <a name="bedrock-Type-data-automation_VideoOverrideConfiguration-modalityProcessing"></a>
Sets modality processing for video files. All modalities are enabled by default.
Type: [ModalityProcessingConfiguration](API_data-automation_ModalityProcessingConfiguration.md) object
Required: No

 ** sensitiveDataConfiguration **   <a name="bedrock-Type-data-automation_VideoOverrideConfiguration-sensitiveDataConfiguration"></a>
Configuration for sensitive data detection and redaction for video files.
Type: [SensitiveDataConfiguration](API_data-automation_SensitiveDataConfiguration.md) object
Required: No

## See Also
<a name="API_data-automation_VideoOverrideConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/VideoOverrideConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/VideoOverrideConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/VideoOverrideConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
