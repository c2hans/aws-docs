---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PipelineDefinitionS3Location.html
---

# PipelineDefinitionS3Location
<a name="API_PipelineDefinitionS3Location"></a>

The location of the pipeline definition stored in Amazon S3.

## Contents
<a name="API_PipelineDefinitionS3Location_Contents"></a>

 ** Bucket **   <a name="sagemaker-Type-PipelineDefinitionS3Location-Bucket"></a>
Name of the S3 bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
Required: Yes

 ** ObjectKey **   <a name="sagemaker-Type-PipelineDefinitionS3Location-ObjectKey"></a>
The object key (or key name) uniquely identifies the object in an S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: Yes

 ** VersionId **   <a name="sagemaker-Type-PipelineDefinitionS3Location-VersionId"></a>
Version Id of the pipeline definition file. If not specified, Amazon SageMaker will retrieve the latest version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

## See Also
<a name="API_PipelineDefinitionS3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PipelineDefinitionS3Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PipelineDefinitionS3Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PipelineDefinitionS3Location)
