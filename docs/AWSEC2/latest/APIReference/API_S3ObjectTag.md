---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_S3ObjectTag.html
---

# S3ObjectTag
<a name="API_S3ObjectTag"></a>

The tags to apply to the AMI object that will be stored in the Amazon S3 bucket. For more information, see [Categorizing your storage using tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html) in the *Amazon Simple Storage Service User Guide*.

## Contents
<a name="API_S3ObjectTag_Contents"></a>

 ** Key **
The key of the tag.
Constraints: Tag keys are case-sensitive and can be up to 128 Unicode characters in length. May not begin with `aws`:.
Type: String
Required: No

 ** Value **
The value of the tag.
Constraints: Tag values are case-sensitive and can be up to 256 Unicode characters in length.
Type: String
Required: No

## See Also
<a name="API_S3ObjectTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/S3ObjectTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/S3ObjectTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/S3ObjectTag)
