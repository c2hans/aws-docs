---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_S3Bucket.html
---

# S3Bucket
<a name="API_S3Bucket"></a>

Contains information about the Amazon S3 bucket policies and encryption.

## Contents
<a name="API_S3Bucket_Contents"></a>

 ** accountPublicAccess **   <a name="guardduty-Type-S3Bucket-accountPublicAccess"></a>
Contains information about the public access policies that apply to the Amazon S3 bucket at the account level.
Type: [PublicAccessConfiguration](API_PublicAccessConfiguration.md) object
Required: No

 ** bucketPublicAccess **   <a name="guardduty-Type-S3Bucket-bucketPublicAccess"></a>
Contains information about public access policies that apply to the Amazon S3 bucket.
Type: [PublicAccessConfiguration](API_PublicAccessConfiguration.md) object
Required: No

 ** createdAt **   <a name="guardduty-Type-S3Bucket-createdAt"></a>
The timestamp at which the Amazon S3 bucket was created.
Type: Timestamp
Required: No

 ** effectivePermission **   <a name="guardduty-Type-S3Bucket-effectivePermission"></a>
Describes the effective permissions on this S3 bucket, after factoring all the attached policies.
Type: String
Required: No

 ** encryptionKeyArn **   <a name="guardduty-Type-S3Bucket-encryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the encryption key that is used to encrypt the Amazon S3 bucket and its objects.
Type: String
Required: No

 ** encryptionType **   <a name="guardduty-Type-S3Bucket-encryptionType"></a>
The type of encryption used for the Amazon S3 buckets and its objects. For more information, see [Protecting data with server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html) in the *Amazon S3 User Guide*.
Type: String
Required: No

 ** ownerId **   <a name="guardduty-Type-S3Bucket-ownerId"></a>
The owner ID of the associated S3Amazon S3bucket.
Type: String
Required: No

 ** publicReadAccess **   <a name="guardduty-Type-S3Bucket-publicReadAccess"></a>
Indicates whether or not the public read access is allowed for an Amazon S3 bucket.
Type: String
Valid Values: `BLOCKED | ALLOWED`
Required: No

 ** publicWriteAccess **   <a name="guardduty-Type-S3Bucket-publicWriteAccess"></a>
Indicates whether or not the public write access is allowed for an Amazon S3 bucket.
Type: String
Valid Values: `BLOCKED | ALLOWED`
Required: No

 ** s3ObjectUids **   <a name="guardduty-Type-S3Bucket-s3ObjectUids"></a>
Represents a list of Amazon S3 object identifiers.
Type: Array of strings
Required: No

## See Also
<a name="API_S3Bucket_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/S3Bucket)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/S3Bucket)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/S3Bucket)
