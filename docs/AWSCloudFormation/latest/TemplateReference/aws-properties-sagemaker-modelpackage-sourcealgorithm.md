---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-sourcealgorithm.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage SourceAlgorithm
<a name="aws-properties-sagemaker-modelpackage-sourcealgorithm"></a>

Specifies an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your SageMaker account or an algorithm in AWS Marketplace that you are subscribed to.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-sourcealgorithm-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-sourcealgorithm-syntax.json"></a>

```
{
  "[AlgorithmName](#cfn-sagemaker-modelpackage-sourcealgorithm-algorithmname)" : {{String}},
  "[ModelDataUrl](#cfn-sagemaker-modelpackage-sourcealgorithm-modeldataurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-sourcealgorithm-syntax.yaml"></a>

```
  [AlgorithmName](#cfn-sagemaker-modelpackage-sourcealgorithm-algorithmname): {{String}}
  [ModelDataUrl](#cfn-sagemaker-modelpackage-sourcealgorithm-modeldataurl): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-sourcealgorithm-properties"></a>

`AlgorithmName`  <a name="cfn-sagemaker-modelpackage-sourcealgorithm-algorithmname"></a>
The name of an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your SageMaker account or an algorithm in AWS Marketplace that you are subscribed to.
*Required*: Yes
*Type*: String
*Pattern*: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*\/)?([a-zA-Z0-9]([a-zA-Z0-9-]){0,62})(?<!-)$`
*Minimum*: `1`
*Maximum*: `170`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelDataUrl`  <a name="cfn-sagemaker-modelpackage-sourcealgorithm-modeldataurl"></a>
The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single `gzip` compressed tar archive (`.tar.gz` suffix).
The model artifacts must be in an S3 bucket that is in the same AWS region as the algorithm.
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
