---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImageCriterionRequest.html
---

# ImageCriterionRequest
<a name="API_ImageCriterionRequest"></a>

The criteria that are evaluated to determine which AMIs are discoverable and usable in your account for the specified AWS Region.

The `ImageCriteria` can include up to:
+ 10 `ImageCriterion`

Each `ImageCriterion` can include up to:
+ 200 values for `ImageProviders`
+ 50 values for `ImageNames`
+ 50 values for `MarketplaceProductCodes`
+ 50 values for `ImageWatermarks`

For more information, see [How Allowed AMIs works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html#how-allowed-amis-works) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_ImageCriterionRequest_Contents"></a>

 ** CreationDateCondition **
The maximum age for allowed images.
Type: [CreationDateConditionRequest](API_CreationDateConditionRequest.md) object
Required: No

 ** DeprecationTimeCondition **
The maximum period since deprecation for allowed images.
Type: [DeprecationTimeConditionRequest](API_DeprecationTimeConditionRequest.md) object
Required: No

 ** ImageName.N **
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

 ** ImageProvider.N **
The image providers whose images are allowed.
Possible values:
+  `amazon`: Allow AMIs created by Amazon or verified providers.
+  `aws-marketplace`: Allow AMIs created by verified providers in the AWS Marketplace.
+  `aws-backup-vault`: Allow AMIs created by AWS Backup.
+ 12-digit account ID: Allow AMIs created by the specified accounts. One or more account IDs can be specified.
+  `none`: Allow AMIs created by your own account only. When `none` is specified, no other values can be specified.
Maximum: 200 values
Type: Array of strings
Required: No

 ** ImageWatermark.N **
The watermark criteria that an AMI must match to be allowed. An AMI is allowed if it carries at least one watermark that satisfies an ImageWatermarkFilter. A watermark satisfies a filter when all specified fields in the ImageWatermarkFilter match the corresponding values on the watermark of the AMI.
Maximum: 50 values
Type: Array of [ImageWatermarkFilterRequest](API_ImageWatermarkFilterRequest.md) objects
Required: No

 ** MarketplaceProductCode.N **
The AWS Marketplace product codes for allowed images.
Length: 1-25 characters
Valid characters: Letters (`A–Z, a–z`) and numbers (`0–9`)
Maximum: 50 values
Type: Array of strings
Required: No

## See Also
<a name="API_ImageCriterionRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImageCriterionRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImageCriterionRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImageCriterionRequest)
