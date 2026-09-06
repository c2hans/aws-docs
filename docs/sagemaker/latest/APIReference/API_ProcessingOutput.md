---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProcessingOutput.html
---

# ProcessingOutput
<a name="API_ProcessingOutput"></a>

Describes the results of a processing job. The processing output must specify exactly one of either `S3Output` or `FeatureStoreOutput` types.

## Contents
<a name="API_ProcessingOutput_Contents"></a>

 ** OutputName **   <a name="sagemaker-Type-ProcessingOutput-OutputName"></a>
The name for the processing job output.
Type: String
Required: Yes

 ** AppManaged **   <a name="sagemaker-Type-ProcessingOutput-AppManaged"></a>
When `True`, output operations such as data upload are managed natively by the processing job application. When `False` (default), output operations are managed by Amazon SageMaker.
Type: Boolean
Required: No

 ** FeatureStoreOutput **   <a name="sagemaker-Type-ProcessingOutput-FeatureStoreOutput"></a>
Configuration for processing job outputs in Amazon SageMaker Feature Store. This processing output type is only supported when `AppManaged` is specified.
Type: [ProcessingFeatureStoreOutput](API_ProcessingFeatureStoreOutput.md) object
Required: No

 ** S3Output **   <a name="sagemaker-Type-ProcessingOutput-S3Output"></a>
Configuration for processing job outputs in Amazon S3.
Type: [ProcessingS3Output](API_ProcessingS3Output.md) object
Required: No

## See Also
<a name="API_ProcessingOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProcessingOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProcessingOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProcessingOutput)
