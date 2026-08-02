---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProcessingS3Output.html
---

# ProcessingS3Output
<a name="API_ProcessingS3Output"></a>

Configuration for uploading output data to Amazon S3 from the processing container.

## Contents
<a name="API_ProcessingS3Output_Contents"></a>

 ** S3UploadMode **   <a name="sagemaker-Type-ProcessingS3Output-S3UploadMode"></a>
Whether to upload the results of the processing job continuously or after the job completes.
Type: String
Valid Values: `Continuous | EndOfJob`
Required: Yes

 ** S3Uri **   <a name="sagemaker-Type-ProcessingS3Output-S3Uri"></a>
A URI that identifies the Amazon S3 bucket where you want Amazon SageMaker to save the results of a processing job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** LocalPath **   <a name="sagemaker-Type-ProcessingS3Output-LocalPath"></a>
The local path of a directory where you want Amazon SageMaker to upload its contents to Amazon S3. `LocalPath` is an absolute path to a directory containing output files. This directory will be created by the platform and exist when your container's entrypoint is invoked.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

## See Also
<a name="API_ProcessingS3Output_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProcessingS3Output)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProcessingS3Output)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProcessingS3Output)
