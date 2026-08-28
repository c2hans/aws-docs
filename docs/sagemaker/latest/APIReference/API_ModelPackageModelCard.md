---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelPackageModelCard.html
---

# ModelPackageModelCard
<a name="API_ModelPackageModelCard"></a>

The model card associated with the model package. Since `ModelPackageModelCard` is tied to a model package, it is a specific usage of a model card and its schema is simplified compared to the schema of `ModelCard`. The `ModelPackageModelCard` schema does not include `model_package_details`, and `model_overview` is composed of the `model_creator` and `model_artifact` properties. For more information about the model package model card schema, see [Model package model card schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html#model-card-schema). For more information about the model card associated with the model package, see [View the Details of a Model Version](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html).

## Contents
<a name="API_ModelPackageModelCard_Contents"></a>

 ** ModelCardContent **   <a name="sagemaker-Type-ModelPackageModelCard-ModelCardContent"></a>
The content of the model card. The content must follow the schema described in [Model Package Model Card Schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html#model-card-schema).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100000.
Pattern: `.*`
Required: No

 ** ModelCardStatus **   <a name="sagemaker-Type-ModelPackageModelCard-ModelCardStatus"></a>
The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.
+  `Draft`: The model card is a work in progress.
+  `PendingReview`: The model card is pending review.
+  `Approved`: The model card is approved.
+  `Archived`: The model card is archived. No more updates can be made to the model card content. If you try to update the model card content, you will receive the message `Model Card is in Archived state`.
Type: String
Valid Values: `Draft | PendingReview | Approved | Archived`
Required: No

## See Also
<a name="API_ModelPackageModelCard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelPackageModelCard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelPackageModelCard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelPackageModelCard)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
