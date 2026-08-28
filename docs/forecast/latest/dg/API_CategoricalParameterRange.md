---
source_url: https://docs.aws.amazon.com/forecast/latest/dg/API_CategoricalParameterRange.html
---

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# CategoricalParameterRange
<a name="API_CategoricalParameterRange"></a>

Specifies a categorical hyperparameter and it's range of tunable values. This object is part of the [ParameterRanges](API_ParameterRanges.md) object.

## Contents
<a name="API_CategoricalParameterRange_Contents"></a>

 ** Name **   <a name="forecast-Type-CategoricalParameterRange-Name"></a>
The name of the categorical hyperparameter to tune.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`
Required: Yes

 ** Values **   <a name="forecast-Type-CategoricalParameterRange-Values"></a>
A list of the tunable categories for the hyperparameter.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Maximum length of 256.
Pattern: `^[a-zA-Z0-9\_\-]+$`
Required: Yes

## See Also
<a name="API_CategoricalParameterRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/CategoricalParameterRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/CategoricalParameterRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/CategoricalParameterRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Forecast. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query forecast` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
