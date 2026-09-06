---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsKinesisStreamDetails.html
---

# AwsKinesisStreamDetails
<a name="API_AwsKinesisStreamDetails"></a>

Provides information about an Amazon Kinesis data stream.

## Contents
<a name="API_AwsKinesisStreamDetails_Contents"></a>

 ** Arn **   <a name="securityhub-Type-AwsKinesisStreamDetails-Arn"></a>
The Amazon Resource Name (ARN) of the Kinesis data stream.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsKinesisStreamDetails-Name"></a>
The name of the Kinesis stream. If you don't specify a name, CloudFront generates a unique physical ID and uses that ID for the stream name.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RetentionPeriodHours **   <a name="securityhub-Type-AwsKinesisStreamDetails-RetentionPeriodHours"></a>
The number of hours for the data records that are stored in shards to remain accessible.
Type: Integer
Required: No

 ** ShardCount **   <a name="securityhub-Type-AwsKinesisStreamDetails-ShardCount"></a>
The number of shards that the stream uses.
Type: Integer
Required: No

 ** StreamEncryption **   <a name="securityhub-Type-AwsKinesisStreamDetails-StreamEncryption"></a>
When specified, enables or updates server-side encryption using an AWS KMS key for a specified stream. Removing this property from your stack template and updating your stack disables encryption.
Type: [AwsKinesisStreamStreamEncryptionDetails](API_AwsKinesisStreamStreamEncryptionDetails.md) object
Required: No

## See Also
<a name="API_AwsKinesisStreamDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsKinesisStreamDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsKinesisStreamDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsKinesisStreamDetails)
