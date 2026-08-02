---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DataTransformationS3Configuration.html
---

# DataTransformationS3Configuration
<a name="API_DataTransformationS3Configuration"></a>

The Amazon S3 output configuration for a data transformation job, including the output location and encryption settings.

## Contents
<a name="API_DataTransformationS3Configuration_Contents"></a>

 ** KmsKeyId **   <a name="HealthLake-Type-DataTransformationS3Configuration-KmsKeyId"></a>
The AWS Key Management Service (AWS KMS) key identifier used to encrypt the transformation job output written to Amazon S3.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** S3Uri **   <a name="HealthLake-Type-DataTransformationS3Configuration-S3Uri"></a>
The Amazon S3 URI where AWS HealthLake writes the converted output files.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 2048.
Pattern: `s3://[a-z0-9][a-z0-9.\-]{1,61}[a-z0-9](/.+)?`
Required: Yes

## See Also
<a name="API_DataTransformationS3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/DataTransformationS3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/DataTransformationS3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/DataTransformationS3Configuration)
