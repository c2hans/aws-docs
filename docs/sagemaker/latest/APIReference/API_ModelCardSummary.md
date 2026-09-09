---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelCardSummary.html
---

# ModelCardSummary
<a name="API_ModelCardSummary"></a>

A summary of the model card.

## Contents
<a name="API_ModelCardSummary_Contents"></a>

 ** ModelCardArn **   <a name="sagemaker-Type-ModelCardSummary-ModelCardArn"></a>
The Amazon Resource Name (ARN) of the model card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-card/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ModelCardName **   <a name="sagemaker-Type-ModelCardSummary-ModelCardName"></a>
The name of the model card.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ModelCardStatus **   <a name="sagemaker-Type-ModelCardSummary-ModelCardStatus"></a>
The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.
+  `Draft`: The model card is a work in progress.
+  `PendingReview`: The model card is pending review.
+  `Approved`: The model card is approved.
+  `Archived`: The model card is archived. No more updates should be made to the model card, but it can still be exported.
Type: String
Valid Values: `Draft | PendingReview | Approved | Archived`
Required: Yes

## See Also
<a name="API_ModelCardSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelCardSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelCardSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelCardSummary)
