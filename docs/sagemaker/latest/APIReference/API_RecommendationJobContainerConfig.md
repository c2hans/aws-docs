---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RecommendationJobContainerConfig.html
---

# RecommendationJobContainerConfig
<a name="API_RecommendationJobContainerConfig"></a>

Specifies mandatory fields for running an Inference Recommender job directly in the [CreateInferenceRecommendationsJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) API. The fields specified in `ContainerConfig` override the corresponding fields in the model package. Use `ContainerConfig` if you want to specify these fields for the recommendation job but don't want to edit them in your model package.

## Contents
<a name="API_RecommendationJobContainerConfig_Contents"></a>

 ** DataInputConfig **   <a name="sagemaker-Type-RecommendationJobContainerConfig-DataInputConfig"></a>
Specifies the name and shape of the expected data inputs for your trained model with a JSON dictionary form. This field is used for optimizing your model using SageMaker Neo. For more information, see [DataInputConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InputConfig.html#sagemaker-Type-InputConfig-DataInputConfig).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S\s]+`
Required: No

 ** Domain **   <a name="sagemaker-Type-RecommendationJobContainerConfig-Domain"></a>
The machine learning domain of the model and its components.
Valid Values: `COMPUTER_VISION | NATURAL_LANGUAGE_PROCESSING | MACHINE_LEARNING`
Type: String
Required: No

 ** Framework **   <a name="sagemaker-Type-RecommendationJobContainerConfig-Framework"></a>
The machine learning framework of the container image.
Valid Values: `TENSORFLOW | PYTORCH | XGBOOST | SAGEMAKER-SCIKIT-LEARN`
Type: String
Required: No

 ** FrameworkVersion **   <a name="sagemaker-Type-RecommendationJobContainerConfig-FrameworkVersion"></a>
The framework version of the container image.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 10.
Pattern: `[0-9]\.[A-Za-z0-9.-]+`
Required: No

 ** NearestModelName **   <a name="sagemaker-Type-RecommendationJobContainerConfig-NearestModelName"></a>
The name of a pre-trained machine learning model benchmarked by Amazon SageMaker Inference Recommender that matches your model.
Valid Values: `efficientnetb7 | unet | xgboost | faster-rcnn-resnet101 | nasnetlarge | vgg16 | inception-v3 | mask-rcnn | sagemaker-scikit-learn | densenet201-gluon | resnet18v2-gluon | xception | densenet201 | yolov4 | resnet152 | bert-base-cased | xceptionV1-keras | resnet50 | retinanet`
Type: String
Required: No

 ** PayloadConfig **   <a name="sagemaker-Type-RecommendationJobContainerConfig-PayloadConfig"></a>
Specifies the `SamplePayloadUrl` and all other sample payload-related fields.
Type: [RecommendationJobPayloadConfig](API_RecommendationJobPayloadConfig.md) object
Required: No

 ** SupportedEndpointType **   <a name="sagemaker-Type-RecommendationJobContainerConfig-SupportedEndpointType"></a>
The endpoint type to receive recommendations for. By default this is null, and the results of the inference recommendation job return a combined list of both real-time and serverless benchmarks. By specifying a value for this field, you can receive a longer list of benchmarks for the desired endpoint type.
Type: String
Valid Values: `RealTime | Serverless`
Required: No

 ** SupportedInstanceTypes **   <a name="sagemaker-Type-RecommendationJobContainerConfig-SupportedInstanceTypes"></a>
A list of the instance types that are used to generate inferences in real-time.
Type: Array of strings
Required: No

 ** SupportedResponseMIMETypes **   <a name="sagemaker-Type-RecommendationJobContainerConfig-SupportedResponseMIMETypes"></a>
The supported MIME types for the output data.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[-\w]+\/.+`
Required: No

 ** Task **   <a name="sagemaker-Type-RecommendationJobContainerConfig-Task"></a>
The machine learning task that the model accomplishes.
Valid Values: `IMAGE_CLASSIFICATION | OBJECT_DETECTION | TEXT_GENERATION | IMAGE_SEGMENTATION | FILL_MASK | CLASSIFICATION | REGRESSION | OTHER`
Type: String
Required: No

## See Also
<a name="API_RecommendationJobContainerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RecommendationJobContainerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RecommendationJobContainerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RecommendationJobContainerConfig)
