---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_PromptTemplate.html
---

# PromptTemplate
<a name="API_PromptTemplate"></a>

The template for the prompt that's sent to the model for response generation.

## Contents
<a name="API_PromptTemplate_Contents"></a>

 ** textPromptTemplate **   <a name="bedrock-Type-PromptTemplate-textPromptTemplate"></a>
The template for the prompt that's sent to the model for response generation. You can include prompt placeholders, which become replaced before the prompt is sent to the model to provide instructions and context to the model. In addition, you can include XML tags to delineate meaningful sections of the prompt template.
For more information, see [Knowledge base prompt template](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html) and [Use XML tags with Anthropic Claude models](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.
Required: No

## See Also
<a name="API_PromptTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/PromptTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/PromptTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/PromptTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
