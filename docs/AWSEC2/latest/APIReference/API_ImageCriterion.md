---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImageCriterion.html
---

# ImageCriterion
<a name="API_ImageCriterion"></a>

The criteria that are evaluated to determine which AMIs are discoverable and usable in your account for the specified AWS Region.

For more information, see [How Allowed AMIs works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html#how-allowed-amis-works) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_ImageCriterion_Contents"></a>

 ** creationDateCondition **
The maximum age for allowed images.
Type: [CreationDateCondition](API_CreationDateCondition.md) object
Required: No

 ** deprecationTimeCondition **
The maximum period since deprecation for allowed images.
Type: [DeprecationTimeCondition](API_DeprecationTimeCondition.md) object
Required: No

 ** ImageNameSet.N **
The names of allowed images. Names can include wildcards (`?` and `*`).
Length: 1–128 characters. With `?`, the minimum is 3 characters.
Valid characters:
+ Letters: `A–Z, a–z`
+ Numbers: `0–9`
+ Special characters: `( ) [ ] . / - ' @ _ * ?`
+ Spaces
Maximum: 50 values
Type: Array of strings
Required: No

 ** ImageProviderSet.N **
The image providers whose images are allowed.
Possible values:
+  `amazon`: Allow AMIs created by Amazon or verified providers.
+  `aws-marketplace`: Allow AMIs created by verified providers in the AWS Marketplace.
+  `aws-backup-vault`: Allow AMIs created by AWS Backup.
+ 12-digit account ID: Allow AMIs created by this account. One or more account IDs can be specified.
+  `none`: Allow AMIs created by your own account only.
Maximum: 200 values
Type: Array of strings
Required: No

 ** ImageWatermarkSet.N **
The watermark criteria that an AMI must match to be allowed. An AMI is allowed if it carries at least one watermark that satisfies an ImageWatermarkFilter. A watermark satisfies a filter when all specified fields in the ImageWatermarkFilter match the corresponding values on the watermark of the AMI.
Maximum: 50 values
Type: Array of [ImageWatermarkFilterResponse](API_ImageWatermarkFilterResponse.md) objects
Required: No

 ** MarketplaceProductCodeSet.N **
The AWS Marketplace product codes for allowed images.
Length: 1-25 characters
Valid characters: Letters (`A–Z, a–z`) and numbers (`0–9`)
Maximum: 50 values
Type: Array of strings
Required: No

## See Also
<a name="API_ImageCriterion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImageCriterion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImageCriterion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImageCriterion)
