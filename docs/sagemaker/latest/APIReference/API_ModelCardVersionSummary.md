---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelCardVersionSummary.html
---

# ModelCardVersionSummary
<a name="API_ModelCardVersionSummary"></a>

A summary of a specific version of the model card.

## Contents
<a name="API_ModelCardVersionSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-ModelCardVersionSummary-CreationTime"></a>
The date and time that the model card version was created.
Type: Timestamp
Required: Yes

 ** ModelCardArn **   <a name="sagemaker-Type-ModelCardVersionSummary-ModelCardArn"></a>
The Amazon Resource Name (ARN) of the model card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-card/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ModelCardName **   <a name="sagemaker-Type-ModelCardVersionSummary-ModelCardName"></a>
The name of the model card.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ModelCardStatus **   <a name="sagemaker-Type-ModelCardVersionSummary-ModelCardStatus"></a>
The approval status of the model card version within your organization. Different organizations might have different criteria for model card review and approval.
+  `Draft`: The model card is a work in progress.
+  `PendingReview`: The model card is pending review.
+  `Approved`: The model card is approved.
+  `Archived`: The model card is archived. No more updates should be made to the model card, but it can still be exported.
Type: String
Valid Values: `Draft | PendingReview | Approved | Archived`
Required: Yes

 ** ModelCardVersion **   <a name="sagemaker-Type-ModelCardVersionSummary-ModelCardVersion"></a>
A version of the model card.
Type: Integer
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-ModelCardVersionSummary-LastModifiedTime"></a>
The time date and time that the model card version was last modified.
Type: Timestamp
Required: No

## See Also
<a name="API_ModelCardVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelCardVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelCardVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelCardVersionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
