---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Initiator.html
---

# Initiator
<a name="API_Initiator"></a>

Container element that identifies who initiated the multipart upload.

## Contents
<a name="API_Initiator_Contents"></a>

 ** DisplayName **   <a name="AmazonS3-Type-Initiator-DisplayName"></a>

This functionality is not supported for directory buckets.
Type: String
Required: No

 ** ID **   <a name="AmazonS3-Type-Initiator-ID"></a>
If the principal is an AWS account, it provides the Canonical User ID. If the principal is an IAM User, it provides a user ARN value.
 **Directory buckets** - If the principal is an AWS account, it provides the AWS account ID. If the principal is an IAM User, it provides a user ARN value.
Type: String
Required: No

## See Also
<a name="API_Initiator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Initiator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Initiator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Initiator)
