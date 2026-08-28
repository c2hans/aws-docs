---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-sourcealgorithm.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard SourceAlgorithm
<a name="aws-properties-sagemaker-modelcard-sourcealgorithm"></a>

Specifies an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your SageMaker account or an algorithm in AWS Marketplace that you are subscribed to.

## Syntax
<a name="aws-properties-sagemaker-modelcard-sourcealgorithm-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-sourcealgorithm-syntax.json"></a>

```
{
  "[AlgorithmName](#cfn-sagemaker-modelcard-sourcealgorithm-algorithmname)" : {{String}},
  "[ModelDataUrl](#cfn-sagemaker-modelcard-sourcealgorithm-modeldataurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-sourcealgorithm-syntax.yaml"></a>

```
  [AlgorithmName](#cfn-sagemaker-modelcard-sourcealgorithm-algorithmname): {{String}}
  [ModelDataUrl](#cfn-sagemaker-modelcard-sourcealgorithm-modeldataurl): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-sourcealgorithm-properties"></a>

`AlgorithmName`  <a name="cfn-sagemaker-modelcard-sourcealgorithm-algorithmname"></a>
The name of an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your SageMaker account or an algorithm in AWS Marketplace that you are subscribed to.
*Required*: Yes
*Type*: String
*Maximum*: `170`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelDataUrl`  <a name="cfn-sagemaker-modelcard-sourcealgorithm-modeldataurl"></a>
The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single `gzip` compressed tar archive (`.tar.gz` suffix).
The model artifacts must be in an S3 bucket that is in the same AWS region as the algorithm.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
