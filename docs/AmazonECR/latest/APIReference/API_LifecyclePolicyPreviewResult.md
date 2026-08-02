---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_LifecyclePolicyPreviewResult.html
---

# LifecyclePolicyPreviewResult
<a name="API_LifecyclePolicyPreviewResult"></a>

The result of the lifecycle policy preview.

## Contents
<a name="API_LifecyclePolicyPreviewResult_Contents"></a>

 ** action **   <a name="ECR-Type-LifecyclePolicyPreviewResult-action"></a>
The type of action to be taken.
Type: [LifecyclePolicyRuleAction](API_LifecyclePolicyRuleAction.md) object
Required: No

 ** appliedRulePriority **   <a name="ECR-Type-LifecyclePolicyPreviewResult-appliedRulePriority"></a>
The priority of the applied rule.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** imageDigest **   <a name="ECR-Type-LifecyclePolicyPreviewResult-imageDigest"></a>
The `sha256` digest of the image manifest.
Type: String
Required: No

 ** imagePushedAt **   <a name="ECR-Type-LifecyclePolicyPreviewResult-imagePushedAt"></a>
The date and time, expressed in standard JavaScript date format, at which the current image was pushed to the repository.
Type: Timestamp
Required: No

 ** imageTags **   <a name="ECR-Type-LifecyclePolicyPreviewResult-imageTags"></a>
The list of tags associated with this image.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** storageClass **   <a name="ECR-Type-LifecyclePolicyPreviewResult-storageClass"></a>
The storage class of the image.
Type: String
Valid Values: `ARCHIVE | STANDARD`
Required: No

## See Also
<a name="API_LifecyclePolicyPreviewResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/LifecyclePolicyPreviewResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/LifecyclePolicyPreviewResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/LifecyclePolicyPreviewResult)
