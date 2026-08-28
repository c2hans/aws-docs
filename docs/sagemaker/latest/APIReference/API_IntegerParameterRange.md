---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IntegerParameterRange.html
---

# IntegerParameterRange
<a name="API_IntegerParameterRange"></a>

For a hyperparameter of the integer type, specifies the range that a hyperparameter tuning job searches.

## Contents
<a name="API_IntegerParameterRange_Contents"></a>

 ** MaxValue **   <a name="sagemaker-Type-IntegerParameterRange-MaxValue"></a>
The maximum value of the hyperparameter to search.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** MinValue **   <a name="sagemaker-Type-IntegerParameterRange-MinValue"></a>
The minimum value of the hyperparameter to search.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** Name **   <a name="sagemaker-Type-IntegerParameterRange-Name"></a>
The name of the hyperparameter to search.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** ScalingType **   <a name="sagemaker-Type-IntegerParameterRange-ScalingType"></a>
The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see [Hyperparameter Scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type). One of the following values:
Auto
SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.
Linear
Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.
Logarithmic
Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.
Logarithmic scaling works only for ranges that have only values greater than 0.
Type: String
Valid Values: `Auto | Linear | Logarithmic | ReverseLogarithmic`
Required: No

## See Also
<a name="API_IntegerParameterRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/IntegerParameterRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/IntegerParameterRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/IntegerParameterRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
