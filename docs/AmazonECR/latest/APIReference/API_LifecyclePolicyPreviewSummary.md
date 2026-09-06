---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_LifecyclePolicyPreviewSummary.html
---

# LifecyclePolicyPreviewSummary
<a name="API_LifecyclePolicyPreviewSummary"></a>

The summary of the lifecycle policy preview request.

## Contents
<a name="API_LifecyclePolicyPreviewSummary_Contents"></a>

 ** expiringImageTotalCount **   <a name="ECR-Type-LifecyclePolicyPreviewSummary-expiringImageTotalCount"></a>
The number of expiring images.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** transitioningImageTotalCounts **   <a name="ECR-Type-LifecyclePolicyPreviewSummary-transitioningImageTotalCounts"></a>
The total count of images that will be transitioned to each storage class. This field is only present if at least one image will be transitoned in the summary.
Type: Array of [TransitioningImageTotalCount](API_TransitioningImageTotalCount.md) objects
Required: No

## See Also
<a name="API_LifecyclePolicyPreviewSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/LifecyclePolicyPreviewSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/LifecyclePolicyPreviewSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/LifecyclePolicyPreviewSummary)
