---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_BedrockFoundationModelConfigurationForParsing.html
---

# BedrockFoundationModelConfigurationForParsing
<a name="API_amazon-q-connect_BedrockFoundationModelConfigurationForParsing"></a>

Settings for a foundation model used to parse documents for a data source.

## Contents
<a name="API_amazon-q-connect_BedrockFoundationModelConfigurationForParsing_Contents"></a>

 ** modelArn **   <a name="connect-Type-amazon-q-connect_BedrockFoundationModelConfigurationForParsing-modelArn"></a>
The ARN of the foundation model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/anthropic.claude-3-haiku-20240307-v1:0`
Required: Yes

 ** parsingPrompt **   <a name="connect-Type-amazon-q-connect_BedrockFoundationModelConfigurationForParsing-parsingPrompt"></a>
Instructions for interpreting the contents of a document.
Type: [ParsingPrompt](API_amazon-q-connect_ParsingPrompt.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_BedrockFoundationModelConfigurationForParsing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/BedrockFoundationModelConfigurationForParsing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/BedrockFoundationModelConfigurationForParsing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/BedrockFoundationModelConfigurationForParsing)
