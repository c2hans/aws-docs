---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescriptiveBotBuilderSpecification.html
---

# DescriptiveBotBuilderSpecification
<a name="API_DescriptiveBotBuilderSpecification"></a>

Contains specifications for the descriptive bot building feature.

## Contents
<a name="API_DescriptiveBotBuilderSpecification_Contents"></a>

 ** enabled **   <a name="lexv2-Type-DescriptiveBotBuilderSpecification-enabled"></a>
Specifies whether the descriptive bot building feature is activated or not.
Type: Boolean
Required: Yes

 ** bedrockModelSpecification **   <a name="lexv2-Type-DescriptiveBotBuilderSpecification-bedrockModelSpecification"></a>
An object containing information about the Amazon Bedrock model used to interpret the prompt used in descriptive bot building.
Type: [BedrockModelSpecification](API_BedrockModelSpecification.md) object
Required: No

## See Also
<a name="API_DescriptiveBotBuilderSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DescriptiveBotBuilderSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DescriptiveBotBuilderSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DescriptiveBotBuilderSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
