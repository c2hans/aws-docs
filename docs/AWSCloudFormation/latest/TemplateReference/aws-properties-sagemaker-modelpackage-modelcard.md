---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-modelcard.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage ModelCard
<a name="aws-properties-sagemaker-modelpackage-modelcard"></a>

An Amazon SageMaker Model Card.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-modelcard-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-modelcard-syntax.json"></a>

```
{
  "[ModelCardContent](#cfn-sagemaker-modelpackage-modelcard-modelcardcontent)" : {{String}},
  "[ModelCardStatus](#cfn-sagemaker-modelpackage-modelcard-modelcardstatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-modelcard-syntax.yaml"></a>

```
  [ModelCardContent](#cfn-sagemaker-modelpackage-modelcard-modelcardcontent): {{String}}
  [ModelCardStatus](#cfn-sagemaker-modelpackage-modelcard-modelcardstatus): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-modelcard-properties"></a>

`ModelCardContent`  <a name="cfn-sagemaker-modelpackage-modelcard-modelcardcontent"></a>
The content of the model card associated with the model package.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `100000`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ModelCardStatus`  <a name="cfn-sagemaker-modelpackage-modelcard-modelcardstatus"></a>
The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.
+ `Draft`: The model card is a work in progress.
+ `PendingReview`: The model card is pending review.
+ `Approved`: The model card is approved.
+ `Archived`: The model card is archived. No more updates should be made to the model card, but it can still be exported.
*Required*: Yes
*Type*: String
*Allowed values*: `Draft | PendingReview | Approved | Archived`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
