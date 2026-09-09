---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelSummary.html
---

# ModelSummary
<a name="API_ModelSummary"></a>

Provides summary information about a model.

## Contents
<a name="API_ModelSummary_Contents"></a>

 ** ModelArn **   <a name="sagemaker-Type-ModelSummary-ModelArn"></a>
The Amazon Resource Name (ARN) of the model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:model/.*`
Required: Yes

 ** ModelName **   <a name="sagemaker-Type-ModelSummary-ModelName"></a>
The name of the model that you want a summary for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: Yes

## See Also
<a name="API_ModelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelSummary)
