---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelDashboardModelCard.html
---

# ModelDashboardModelCard
<a name="API_ModelDashboardModelCard"></a>

The model card for a model displayed in the Amazon SageMaker Model Dashboard.

## Contents
<a name="API_ModelDashboardModelCard_Contents"></a>

 ** CreatedBy **   <a name="sagemaker-Type-ModelDashboardModelCard-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** CreationTime **   <a name="sagemaker-Type-ModelDashboardModelCard-CreationTime"></a>
A timestamp that indicates when the model card was created.
Type: Timestamp
Required: No

 ** LastModifiedBy **   <a name="sagemaker-Type-ModelDashboardModelCard-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-ModelDashboardModelCard-LastModifiedTime"></a>
A timestamp that indicates when the model card was last updated.
Type: Timestamp
Required: No

 ** ModelCardArn **   <a name="sagemaker-Type-ModelDashboardModelCard-ModelCardArn"></a>
The Amazon Resource Name (ARN) for a model card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-card/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ModelCardName **   <a name="sagemaker-Type-ModelDashboardModelCard-ModelCardName"></a>
The name of a model card.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ModelCardStatus **   <a name="sagemaker-Type-ModelDashboardModelCard-ModelCardStatus"></a>
The model card status.
Type: String
Valid Values: `Draft | PendingReview | Approved | Archived`
Required: No

 ** ModelCardVersion **   <a name="sagemaker-Type-ModelDashboardModelCard-ModelCardVersion"></a>
The model card version.
Type: Integer
Required: No

 ** ModelId **   <a name="sagemaker-Type-ModelDashboardModelCard-ModelId"></a>
For models created in SageMaker, this is the model ARN. For models created outside of SageMaker, this is a user-customized string.
Type: String
Required: No

 ** RiskRating **   <a name="sagemaker-Type-ModelDashboardModelCard-RiskRating"></a>
A model card's risk rating. Can be low, medium, or high.
Type: String
Required: No

 ** SecurityConfig **   <a name="sagemaker-Type-ModelDashboardModelCard-SecurityConfig"></a>
The KMS Key ID (`KMSKeyId`) for encryption of model card information.
Type: [ModelCardSecurityConfig](API_ModelCardSecurityConfig.md) object
Required: No

 ** Tags **   <a name="sagemaker-Type-ModelDashboardModelCard-Tags"></a>
The tags associated with a model card.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_ModelDashboardModelCard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelDashboardModelCard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelDashboardModelCard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelDashboardModelCard)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
