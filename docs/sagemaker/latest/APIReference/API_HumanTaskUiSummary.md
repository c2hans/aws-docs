---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HumanTaskUiSummary.html
---

# HumanTaskUiSummary
<a name="API_HumanTaskUiSummary"></a>

Container for human task user interface information.

## Contents
<a name="API_HumanTaskUiSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-HumanTaskUiSummary-CreationTime"></a>
A timestamp when SageMaker created the human task user interface.
Type: Timestamp
Required: Yes

 ** HumanTaskUiArn **   <a name="sagemaker-Type-HumanTaskUiSummary-HumanTaskUiArn"></a>
The Amazon Resource Name (ARN) of the human task user interface.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]+:[0-9]{12}:human-task-ui/.*`
Required: Yes

 ** HumanTaskUiName **   <a name="sagemaker-Type-HumanTaskUiSummary-HumanTaskUiName"></a>
The name of the human task user interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z0-9](-*[a-z0-9])*`
Required: Yes

## See Also
<a name="API_HumanTaskUiSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HumanTaskUiSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HumanTaskUiSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HumanTaskUiSummary)
