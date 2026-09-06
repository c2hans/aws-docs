---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3ObjectDetails.html
---

# AwsS3ObjectDetails
<a name="API_AwsS3ObjectDetails"></a>

Details about an Amazon S3 object.

## Contents
<a name="API_AwsS3ObjectDetails_Contents"></a>

 ** ContentType **   <a name="securityhub-Type-AwsS3ObjectDetails-ContentType"></a>
A standard MIME type describing the format of the object data.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ETag **   <a name="securityhub-Type-AwsS3ObjectDetails-ETag"></a>
The opaque identifier assigned by a web server to a specific version of a resource found at a URL.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LastModified **   <a name="securityhub-Type-AwsS3ObjectDetails-LastModified"></a>
Indicates when the object was last modified.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** ServerSideEncryption **   <a name="securityhub-Type-AwsS3ObjectDetails-ServerSideEncryption"></a>
If the object is stored using server-side encryption, the value of the server-side encryption algorithm used when storing this object in Amazon S3.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SSEKMSKeyId **   <a name="securityhub-Type-AwsS3ObjectDetails-SSEKMSKeyId"></a>
The identifier of the AWS KMS symmetric customer managed key that was used for the object.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VersionId **   <a name="securityhub-Type-AwsS3ObjectDetails-VersionId"></a>
The version of the object.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsS3ObjectDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3ObjectDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3ObjectDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3ObjectDetails)
