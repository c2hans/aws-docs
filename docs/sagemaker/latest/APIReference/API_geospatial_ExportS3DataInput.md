---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ExportS3DataInput.html
---

# ExportS3DataInput
<a name="API_geospatial_ExportS3DataInput"></a>

The structure containing the Amazon S3 path to export the Earth Observation job output.

## Contents
<a name="API_geospatial_ExportS3DataInput_Contents"></a>

 ** S3Uri **   <a name="sagemaker-Type-geospatial_ExportS3DataInput-S3Uri"></a>
The URL to the Amazon S3 data input.
Type: String
Pattern: `s3://([^/]+)/?(.*)`
Required: Yes

 ** KmsKeyId **   <a name="sagemaker-Type-geospatial_ExportS3DataInput-KmsKeyId"></a>
The Key Management Service key ID for server-side encryption.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_geospatial_ExportS3DataInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/ExportS3DataInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/ExportS3DataInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/ExportS3DataInput)
