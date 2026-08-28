---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_AudioStandardGenerativeField.html
---

# AudioStandardGenerativeField
<a name="API_data-automation_AudioStandardGenerativeField"></a>

Settings for generating descriptions of audio.

## Contents
<a name="API_data-automation_AudioStandardGenerativeField_Contents"></a>

 ** state **   <a name="bedrock-Type-data-automation_AudioStandardGenerativeField-state"></a>
Whether generating descriptions is enabled for audio.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** types **   <a name="bedrock-Type-data-automation_AudioStandardGenerativeField-types"></a>
The types of description to generate.
Type: Array of strings
Valid Values: `AUDIO_SUMMARY | TOPIC_SUMMARY`
Required: No

## See Also
<a name="API_data-automation_AudioStandardGenerativeField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/AudioStandardGenerativeField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/AudioStandardGenerativeField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/AudioStandardGenerativeField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
