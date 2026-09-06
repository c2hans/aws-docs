---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DirectDeploySettings.html
---

# DirectDeploySettings
<a name="API_DirectDeploySettings"></a>

The model deployment settings for the SageMaker Canvas application.

**Note**
In order to enable model deployment for Canvas, the SageMaker Domain's or user profile's AWS IAM execution role must have the `AmazonSageMakerCanvasDirectDeployAccess` policy attached. You can also turn on model deployment permissions through the SageMaker Domain's or user profile's settings in the SageMaker console.

## Contents
<a name="API_DirectDeploySettings_Contents"></a>

 ** Status **   <a name="sagemaker-Type-DirectDeploySettings-Status"></a>
Describes whether model deployment permissions are enabled or disabled in the Canvas application.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_DirectDeploySettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DirectDeploySettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DirectDeploySettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DirectDeploySettings)
