---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BedrockModelSpecification.html
---

# BedrockModelSpecification
<a name="API_BedrockModelSpecification"></a>

Contains information about the Amazon Bedrock model used to interpret the prompt used in descriptive bot building.

## Contents
<a name="API_BedrockModelSpecification_Contents"></a>

 ** modelArn **   <a name="lexv2-Type-BedrockModelSpecification-modelArn"></a>
The ARN of the foundation model used in descriptive bot building.
Type: String
Pattern: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model\/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}$`
Required: Yes

 ** customPrompt **   <a name="lexv2-Type-BedrockModelSpecification-customPrompt"></a>
The custom prompt used in the Bedrock model specification details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Required: No

 ** guardrail **   <a name="lexv2-Type-BedrockModelSpecification-guardrail"></a>
The guardrail configuration in the Bedrock model specification details.
Type: [BedrockGuardrailConfiguration](API_BedrockGuardrailConfiguration.md) object
Required: No

 ** traceStatus **   <a name="lexv2-Type-BedrockModelSpecification-traceStatus"></a>
The Bedrock trace status in the Bedrock model specification details.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_BedrockModelSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BedrockModelSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BedrockModelSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BedrockModelSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
