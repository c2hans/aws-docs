---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingImageConfig.html
---

# TrainingImageConfig
<a name="API_TrainingImageConfig"></a>

The configuration to use an image from a private Docker registry for a training job.

## Contents
<a name="API_TrainingImageConfig_Contents"></a>

 ** TrainingRepositoryAccessMode **   <a name="sagemaker-Type-TrainingImageConfig-TrainingRepositoryAccessMode"></a>
The method that your training job will use to gain access to the images in your private Docker registry. For access to an image in a private Docker registry, set to `Vpc`.
Type: String
Valid Values: `Platform | Vpc`
Required: Yes

 ** TrainingRepositoryAuthConfig **   <a name="sagemaker-Type-TrainingImageConfig-TrainingRepositoryAuthConfig"></a>
An object containing authentication information for a private Docker registry containing your training images.
Type: [TrainingRepositoryAuthConfig](API_TrainingRepositoryAuthConfig.md) object
Required: No

## See Also
<a name="API_TrainingImageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrainingImageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrainingImageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrainingImageConfig)
