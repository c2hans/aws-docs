---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-shuffleconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob ShuffleConfig
<a name="aws-properties-sagemaker-trainingjob-shuffleconfig"></a>

A configuration for a shuffle option for input data in a channel. If you use `S3Prefix` for `S3DataType`, the results of the S3 key prefix matches are shuffled. If you use `ManifestFile`, the order of the S3 object references in the `ManifestFile` is shuffled. If you use `AugmentedManifestFile`, the order of the JSON lines in the `AugmentedManifestFile` is shuffled. The shuffling order is determined using the `Seed` value.

For Pipe input mode, when `ShuffleConfig` is specified shuffling is done at the start of every epoch. With large datasets, this ensures that the order of the training data is different for each epoch, and it helps reduce bias and possible overfitting. In a multi-node training job when `ShuffleConfig` is combined with `S3DataDistributionType` of `ShardedByS3Key`, the data is shuffled across nodes so that the content sent to a particular node on the first epoch might be sent to a different node on the second epoch.

## Syntax
<a name="aws-properties-sagemaker-trainingjob-shuffleconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-shuffleconfig-syntax.json"></a>

```
{
  "[Seed](#cfn-sagemaker-trainingjob-shuffleconfig-seed)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-shuffleconfig-syntax.yaml"></a>

```
  [Seed](#cfn-sagemaker-trainingjob-shuffleconfig-seed): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-shuffleconfig-properties"></a>

`Seed`  <a name="cfn-sagemaker-trainingjob-shuffleconfig-seed"></a>
Determines the shuffling order in `ShuffleConfig` value.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
