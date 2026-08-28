---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_SpeakerLabelingConfiguration.html
---

# SpeakerLabelingConfiguration
<a name="API_data-automation_SpeakerLabelingConfiguration"></a>

Enables or disables speaker labeling. Speaker labeling, when enabled will assign a number to each speaker, and indicate which speaker is talking in each portion of the transcript. This appears in the response as "spk\_0" for the first speaker, "spk\_1" for the second, and so on for up to 30 speakers.

## Contents
<a name="API_data-automation_SpeakerLabelingConfiguration_Contents"></a>

 ** state **   <a name="bedrock-Type-data-automation_SpeakerLabelingConfiguration-state"></a>
State of speaker labeling, either enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## See Also
<a name="API_data-automation_SpeakerLabelingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/SpeakerLabelingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/SpeakerLabelingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/SpeakerLabelingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
