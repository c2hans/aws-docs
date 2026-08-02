---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3AccountPublicAccessBlockDetails.html
---

# AwsS3AccountPublicAccessBlockDetails
<a name="API_AwsS3AccountPublicAccessBlockDetails"></a>

provides information about the Amazon S3 Public Access Block configuration for accounts.

## Contents
<a name="API_AwsS3AccountPublicAccessBlockDetails_Contents"></a>

 ** BlockPublicAcls **   <a name="securityhub-Type-AwsS3AccountPublicAccessBlockDetails-BlockPublicAcls"></a>
Indicates whether to reject calls to update an S3 bucket if the calls include a public access control list (ACL).
Type: Boolean
Required: No

 ** BlockPublicPolicy **   <a name="securityhub-Type-AwsS3AccountPublicAccessBlockDetails-BlockPublicPolicy"></a>
Indicates whether to reject calls to update the access policy for an S3 bucket or access point if the policy allows public access.
Type: Boolean
Required: No

 ** IgnorePublicAcls **   <a name="securityhub-Type-AwsS3AccountPublicAccessBlockDetails-IgnorePublicAcls"></a>
Indicates whether Amazon S3 ignores public ACLs that are associated with an S3 bucket.
Type: Boolean
Required: No

 ** RestrictPublicBuckets **   <a name="securityhub-Type-AwsS3AccountPublicAccessBlockDetails-RestrictPublicBuckets"></a>
Indicates whether to restrict access to an access point or S3 bucket that has a public policy to only AWS service principals and authorized users within the S3 bucket owner's account.
Type: Boolean
Required: No

## See Also
<a name="API_AwsS3AccountPublicAccessBlockDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3AccountPublicAccessBlockDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3AccountPublicAccessBlockDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3AccountPublicAccessBlockDetails)
