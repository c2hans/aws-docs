---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrialComponentParameterValue.html
---

# TrialComponentParameterValue
<a name="API_TrialComponentParameterValue"></a>

The value of a hyperparameter. Only one of `NumberValue` or `StringValue` can be specified.

This object is specified in the [CreateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html) request.

## Contents
<a name="API_TrialComponentParameterValue_Contents"></a>

 ** NumberValue **   <a name="sagemaker-Type-TrialComponentParameterValue-NumberValue"></a>
The numeric value of a numeric hyperparameter. If you specify a value for this parameter, you can't specify the `StringValue` parameter.
Type: Double
Required: No

 ** StringValue **   <a name="sagemaker-Type-TrialComponentParameterValue-StringValue"></a>
The string value of a categorical hyperparameter. If you specify a value for this parameter, you can't specify the `NumberValue` parameter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2500.
Pattern: `.*`
Required: No

## See Also
<a name="API_TrialComponentParameterValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrialComponentParameterValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrialComponentParameterValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrialComponentParameterValue)
