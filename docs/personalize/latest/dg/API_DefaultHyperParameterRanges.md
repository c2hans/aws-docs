---
source_url: https://docs.aws.amazon.com/personalize/latest/dg/API_DefaultHyperParameterRanges.html
---

# DefaultHyperParameterRanges
<a name="API_DefaultHyperParameterRanges"></a>

Specifies the hyperparameters and their default ranges. Hyperparameters can be categorical, continuous, or integer-valued.

## Contents
<a name="API_DefaultHyperParameterRanges_Contents"></a>

 ** categoricalHyperParameterRanges **   <a name="personalize-Type-DefaultHyperParameterRanges-categoricalHyperParameterRanges"></a>
The categorical hyperparameters and their default ranges.
Type: Array of [DefaultCategoricalHyperParameterRange](API_DefaultCategoricalHyperParameterRange.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** continuousHyperParameterRanges **   <a name="personalize-Type-DefaultHyperParameterRanges-continuousHyperParameterRanges"></a>
The continuous hyperparameters and their default ranges.
Type: Array of [DefaultContinuousHyperParameterRange](API_DefaultContinuousHyperParameterRange.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** integerHyperParameterRanges **   <a name="personalize-Type-DefaultHyperParameterRanges-integerHyperParameterRanges"></a>
The integer-valued hyperparameters and their default ranges.
Type: Array of [DefaultIntegerHyperParameterRange](API_DefaultIntegerHyperParameterRange.md) objects
Array Members: Maximum number of 100 items.
Required: No

## See Also
<a name="API_DefaultHyperParameterRanges_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/DefaultHyperParameterRanges)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/DefaultHyperParameterRanges)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/DefaultHyperParameterRanges)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Personalize. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query personalize` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
