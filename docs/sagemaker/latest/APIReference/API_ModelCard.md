---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelCard.html
---

# ModelCard
<a name="API_ModelCard"></a>

An Amazon SageMaker Model Card.

## Contents
<a name="API_ModelCard_Contents"></a>

 ** Content **   <a name="sagemaker-Type-ModelCard-Content"></a>
The content of the model card. Content uses the [model card JSON schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html#model-cards-json-schema) and provided as a string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100000.
Pattern: `.*`
Required: No

 ** CreatedBy **   <a name="sagemaker-Type-ModelCard-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** CreationTime **   <a name="sagemaker-Type-ModelCard-CreationTime"></a>
The date and time that the model card was created.
Type: Timestamp
Required: No

 ** LastModifiedBy **   <a name="sagemaker-Type-ModelCard-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-ModelCard-LastModifiedTime"></a>
The date and time that the model card was last modified.
Type: Timestamp
Required: No

 ** ModelCardArn **   <a name="sagemaker-Type-ModelCard-ModelCardArn"></a>
The Amazon Resource Name (ARN) of the model card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-card/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ModelCardName **   <a name="sagemaker-Type-ModelCard-ModelCardName"></a>
The unique name of the model card.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ModelCardStatus **   <a name="sagemaker-Type-ModelCard-ModelCardStatus"></a>
The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.
+  `Draft`: The model card is a work in progress.
+  `PendingReview`: The model card is pending review.
+  `Approved`: The model card is approved.
+  `Archived`: The model card is archived. No more updates should be made to the model card, but it can still be exported.
Type: String
Valid Values: `Draft | PendingReview | Approved | Archived`
Required: No

 ** ModelCardVersion **   <a name="sagemaker-Type-ModelCard-ModelCardVersion"></a>
The version of the model card.
Type: Integer
Required: No

 ** ModelId **   <a name="sagemaker-Type-ModelCard-ModelId"></a>
The unique name (ID) of the model.
Type: String
Required: No

 ** ModelPackageGroupName **   <a name="sagemaker-Type-ModelCard-ModelPackageGroupName"></a>
The model package group that contains the model package. Only relevant for model cards created for model packages in the Amazon SageMaker Model Registry.
Type: String
Required: No

 ** RiskRating **   <a name="sagemaker-Type-ModelCard-RiskRating"></a>
The risk rating of the model. Different organizations might have different criteria for model card risk ratings. For more information, see [Risk ratings](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards-risk-rating.html).
Type: String
Required: No

 ** SecurityConfig **   <a name="sagemaker-Type-ModelCard-SecurityConfig"></a>
The security configuration used to protect model card data.
Type: [ModelCardSecurityConfig](API_ModelCardSecurityConfig.md) object
Required: No

 ** Tags **   <a name="sagemaker-Type-ModelCard-Tags"></a>
Key-value pairs used to manage metadata for the model card.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_ModelCard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelCard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelCard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelCard)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
