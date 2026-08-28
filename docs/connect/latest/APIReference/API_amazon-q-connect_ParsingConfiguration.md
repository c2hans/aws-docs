---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_ParsingConfiguration.html
---

# ParsingConfiguration
<a name="API_amazon-q-connect_ParsingConfiguration"></a>

Settings for parsing document contents. By default, the service converts the contents of each document into text before splitting it into chunks. To improve processing of PDF files with tables and images, you can configure the data source to convert the pages of text into images and use a model to describe the contents of each page.

## Contents
<a name="API_amazon-q-connect_ParsingConfiguration_Contents"></a>

 ** parsingStrategy **   <a name="connect-Type-amazon-q-connect_ParsingConfiguration-parsingStrategy"></a>
The parsing strategy for the data source.
Type: String
Valid Values: `BEDROCK_FOUNDATION_MODEL`
Required: Yes

 ** bedrockFoundationModelConfiguration **   <a name="connect-Type-amazon-q-connect_ParsingConfiguration-bedrockFoundationModelConfiguration"></a>
Settings for a foundation model used to parse documents for a data source.
Type: [BedrockFoundationModelConfigurationForParsing](API_amazon-q-connect_BedrockFoundationModelConfigurationForParsing.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_ParsingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ParsingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ParsingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ParsingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
