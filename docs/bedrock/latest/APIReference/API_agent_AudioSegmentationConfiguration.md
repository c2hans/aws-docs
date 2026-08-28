---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_AudioSegmentationConfiguration.html
---

# AudioSegmentationConfiguration
<a name="API_agent_AudioSegmentationConfiguration"></a>

Configuration for segmenting audio content during multimodal knowledge base ingestion. Determines how audio files are divided into chunks for processing.

## Contents
<a name="API_agent_AudioSegmentationConfiguration_Contents"></a>

 ** fixedLengthDuration **   <a name="bedrock-Type-agent_AudioSegmentationConfiguration-fixedLengthDuration"></a>
The duration in seconds for each audio segment. Audio files will be divided into chunks of this length for processing.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 30.
Required: Yes

## See Also
<a name="API_agent_AudioSegmentationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/AudioSegmentationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/AudioSegmentationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/AudioSegmentationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
