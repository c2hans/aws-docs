---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProcessingInput.html
---

# ProcessingInput
<a name="API_ProcessingInput"></a>

The inputs for a processing job. The processing input must specify exactly one of either `S3Input` or `DatasetDefinition` types.

## Contents
<a name="API_ProcessingInput_Contents"></a>

 ** InputName **   <a name="sagemaker-Type-ProcessingInput-InputName"></a>
The name for the processing job input.
Type: String
Required: Yes

 ** AppManaged **   <a name="sagemaker-Type-ProcessingInput-AppManaged"></a>
When `True`, input operations such as data download are managed natively by the processing job application. When `False` (default), input operations are managed by Amazon SageMaker.
Type: Boolean
Required: No

 ** DatasetDefinition **   <a name="sagemaker-Type-ProcessingInput-DatasetDefinition"></a>
Configuration for a Dataset Definition input.
Type: [DatasetDefinition](API_DatasetDefinition.md) object
Required: No

 ** S3Input **   <a name="sagemaker-Type-ProcessingInput-S3Input"></a>
Configuration for downloading input data from Amazon S3 into the processing container.
Type: [ProcessingS3Input](API_ProcessingS3Input.md) object
Required: No

## See Also
<a name="API_ProcessingInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProcessingInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProcessingInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProcessingInput)
