---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketDetails.html
---

# AwsS3BucketDetails
<a name="API_AwsS3BucketDetails"></a>

The details of an Amazon Simple Storage Service (Amazon S3) bucket.

## Contents
<a name="API_AwsS3BucketDetails_Contents"></a>

 ** AccessControlList **   <a name="securityhub-Type-AwsS3BucketDetails-AccessControlList"></a>
The access control list for the S3 bucket.
Type: String
Pattern: `.*\S.*`
Required: No

 ** BucketLifecycleConfiguration **   <a name="securityhub-Type-AwsS3BucketDetails-BucketLifecycleConfiguration"></a>
The lifecycle configuration for objects in the specified bucket.
Type: [AwsS3BucketBucketLifecycleConfigurationDetails](API_AwsS3BucketBucketLifecycleConfigurationDetails.md) object
Required: No

 ** BucketLoggingConfiguration **   <a name="securityhub-Type-AwsS3BucketDetails-BucketLoggingConfiguration"></a>
The logging configuration for the S3 bucket.
Type: [AwsS3BucketLoggingConfiguration](API_AwsS3BucketLoggingConfiguration.md) object
Required: No

 ** BucketNotificationConfiguration **   <a name="securityhub-Type-AwsS3BucketDetails-BucketNotificationConfiguration"></a>
The notification configuration for the S3 bucket.
Type: [AwsS3BucketNotificationConfiguration](API_AwsS3BucketNotificationConfiguration.md) object
Required: No

 ** BucketVersioningConfiguration **   <a name="securityhub-Type-AwsS3BucketDetails-BucketVersioningConfiguration"></a>
The versioning state of an S3 bucket.
Type: [AwsS3BucketBucketVersioningConfiguration](API_AwsS3BucketBucketVersioningConfiguration.md) object
Required: No

 ** BucketWebsiteConfiguration **   <a name="securityhub-Type-AwsS3BucketDetails-BucketWebsiteConfiguration"></a>
The website configuration parameters for the S3 bucket.
Type: [AwsS3BucketWebsiteConfiguration](API_AwsS3BucketWebsiteConfiguration.md) object
Required: No

 ** CreatedAt **   <a name="securityhub-Type-AwsS3BucketDetails-CreatedAt"></a>
Indicates when the S3 bucket was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsS3BucketDetails-Name"></a>
 The name of the bucket.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ObjectLockConfiguration **   <a name="securityhub-Type-AwsS3BucketDetails-ObjectLockConfiguration"></a>
 Specifies which rule Amazon S3 applies by default to every new object placed in the bucket.
Type: [AwsS3BucketObjectLockConfiguration](API_AwsS3BucketObjectLockConfiguration.md) object
Required: No

 ** OwnerAccountId **   <a name="securityhub-Type-AwsS3BucketDetails-OwnerAccountId"></a>
The AWS account identifier of the account that owns the S3 bucket.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OwnerId **   <a name="securityhub-Type-AwsS3BucketDetails-OwnerId"></a>
The canonical user ID of the owner of the S3 bucket.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OwnerName **   <a name="securityhub-Type-AwsS3BucketDetails-OwnerName"></a>
The display name of the owner of the S3 bucket.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PublicAccessBlockConfiguration **   <a name="securityhub-Type-AwsS3BucketDetails-PublicAccessBlockConfiguration"></a>
Provides information about the Amazon S3 Public Access Block configuration for the S3 bucket.
Type: [AwsS3AccountPublicAccessBlockDetails](API_AwsS3AccountPublicAccessBlockDetails.md) object
Required: No

 ** ServerSideEncryptionConfiguration **   <a name="securityhub-Type-AwsS3BucketDetails-ServerSideEncryptionConfiguration"></a>
The encryption rules that are applied to the S3 bucket.
Type: [AwsS3BucketServerSideEncryptionConfiguration](API_AwsS3BucketServerSideEncryptionConfiguration.md) object
Required: No

## See Also
<a name="API_AwsS3BucketDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketDetails)
