---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ZonalStatisticsConfigInput.html
---

# ZonalStatisticsConfigInput
<a name="API_geospatial_ZonalStatisticsConfigInput"></a>

The structure representing input configuration of ZonalStatistics operation.

## Contents
<a name="API_geospatial_ZonalStatisticsConfigInput_Contents"></a>

 ** Statistics **   <a name="sagemaker-Type-geospatial_ZonalStatisticsConfigInput-Statistics"></a>
List of zonal statistics to compute.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `MEAN | MEDIAN | STANDARD_DEVIATION | MAX | MIN | SUM`
Required: Yes

 ** ZoneS3Path **   <a name="sagemaker-Type-geospatial_ZonalStatisticsConfigInput-ZoneS3Path"></a>
The Amazon S3 path pointing to the GeoJSON containing the polygonal zones.
Type: String
Pattern: `s3://([^/]+)/?(.*)`
Required: Yes

 ** TargetBands **   <a name="sagemaker-Type-geospatial_ZonalStatisticsConfigInput-TargetBands"></a>
Bands used in the operation. If no target bands are specified, it uses all bands available input.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

 ** ZoneS3PathKmsKeyId **   <a name="sagemaker-Type-geospatial_ZonalStatisticsConfigInput-ZoneS3PathKmsKeyId"></a>
The Amazon Resource Name (ARN) or an ID of a AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to decrypt your output artifacts with Amazon S3 server-side encryption. The SageMaker execution role must have `kms:GenerateDataKey` permission.
The `KmsKeyId` can be any of the following formats:
+ // KMS Key ID

   `"1234abcd-12ab-34cd-56ef-1234567890ab"`
+ // Amazon Resource Name (ARN) of a KMS Key

   `"arn:aws:kms:<region>:<account>:key/<key-id-12ab-34cd-56ef-1234567890ab>"`
For more information about key identifiers, see [Key identifiers (KeyID)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id) in the AWS Key Management Service (AWS KMS) documentation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_geospatial_ZonalStatisticsConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/ZonalStatisticsConfigInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/ZonalStatisticsConfigInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/ZonalStatisticsConfigInput)
