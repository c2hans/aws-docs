---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-processingjob-featurestoreoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ProcessingJob FeatureStoreOutput
<a name="aws-properties-sagemaker-processingjob-featurestoreoutput"></a>

Configuration for processing job outputs in Amazon SageMaker Feature Store.

## Syntax
<a name="aws-properties-sagemaker-processingjob-featurestoreoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-processingjob-featurestoreoutput-syntax.json"></a>

```
{
  "[FeatureGroupName](#cfn-sagemaker-processingjob-featurestoreoutput-featuregroupname)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-processingjob-featurestoreoutput-syntax.yaml"></a>

```
  [FeatureGroupName](#cfn-sagemaker-processingjob-featurestoreoutput-featuregroupname): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-processingjob-featurestoreoutput-properties"></a>

`FeatureGroupName`  <a name="cfn-sagemaker-processingjob-featurestoreoutput-featuregroupname"></a>
The name of the Amazon SageMaker FeatureGroup to use as the destination for processing job output. Note that your processing script is responsible for putting records into your Feature Store.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9]([_-]*[a-zA-Z0-9]){0,63}`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
