---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CategoricalParameterRange.html
---

# CategoricalParameterRange
<a name="API_CategoricalParameterRange"></a>

A list of categorical hyperparameters to tune.

## Contents
<a name="API_CategoricalParameterRange_Contents"></a>

 ** Name **   <a name="sagemaker-Type-CategoricalParameterRange-Name"></a>
The name of the categorical hyperparameter to tune.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** Values **   <a name="sagemaker-Type-CategoricalParameterRange-Values"></a>
A list of the categories for the hyperparameter.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_CategoricalParameterRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CategoricalParameterRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CategoricalParameterRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CategoricalParameterRange)
