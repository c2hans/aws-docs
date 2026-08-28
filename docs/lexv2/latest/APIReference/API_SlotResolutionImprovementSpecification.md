---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SlotResolutionImprovementSpecification.html
---

# SlotResolutionImprovementSpecification
<a name="API_SlotResolutionImprovementSpecification"></a>

Contains specifications for the assisted slot resolution feature.

## Contents
<a name="API_SlotResolutionImprovementSpecification_Contents"></a>

 ** enabled **   <a name="lexv2-Type-SlotResolutionImprovementSpecification-enabled"></a>
Specifies whether assisted slot resolution is turned on or off.
Type: Boolean
Required: Yes

 ** bedrockModelSpecification **   <a name="lexv2-Type-SlotResolutionImprovementSpecification-bedrockModelSpecification"></a>
An object containing information about the Amazon Bedrock model used to assist slot resolution.
Type: [BedrockModelSpecification](API_BedrockModelSpecification.md) object
Required: No

## See Also
<a name="API_SlotResolutionImprovementSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SlotResolutionImprovementSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SlotResolutionImprovementSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SlotResolutionImprovementSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
