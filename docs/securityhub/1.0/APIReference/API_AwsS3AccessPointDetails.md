---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3AccessPointDetails.html
---

# AwsS3AccessPointDetails
<a name="API_AwsS3AccessPointDetails"></a>

 Returns configuration information about the specified Amazon S3 access point. S3 access points are named network endpoints that are attached to buckets that you can use to perform S3 object operations.

## Contents
<a name="API_AwsS3AccessPointDetails_Contents"></a>

 ** AccessPointArn **   <a name="securityhub-Type-AwsS3AccessPointDetails-AccessPointArn"></a>
 The Amazon Resource Name (ARN) of the access point.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Alias **   <a name="securityhub-Type-AwsS3AccessPointDetails-Alias"></a>
 The name or alias of the access point.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Bucket **   <a name="securityhub-Type-AwsS3AccessPointDetails-Bucket"></a>
 The name of the S3 bucket associated with the specified access point.
Type: String
Pattern: `.*\S.*`
Required: No

 ** BucketAccountId **   <a name="securityhub-Type-AwsS3AccessPointDetails-BucketAccountId"></a>
 The AWS account ID associated with the S3 bucket associated with this access point.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsS3AccessPointDetails-Name"></a>
 The name of the specified access point.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NetworkOrigin **   <a name="securityhub-Type-AwsS3AccessPointDetails-NetworkOrigin"></a>
 Indicates whether this access point allows access from the public internet.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PublicAccessBlockConfiguration **   <a name="securityhub-Type-AwsS3AccessPointDetails-PublicAccessBlockConfiguration"></a>
provides information about the Amazon S3 Public Access Block configuration for accounts.
Type: [AwsS3AccountPublicAccessBlockDetails](API_AwsS3AccountPublicAccessBlockDetails.md) object
Required: No

 ** VpcConfiguration **   <a name="securityhub-Type-AwsS3AccessPointDetails-VpcConfiguration"></a>
 Contains the virtual private cloud (VPC) configuration for the specified access point.
Type: [AwsS3AccessPointVpcConfigurationDetails](API_AwsS3AccessPointVpcConfigurationDetails.md) object
Required: No

## See Also
<a name="API_AwsS3AccessPointDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3AccessPointDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3AccessPointDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3AccessPointDetails)
