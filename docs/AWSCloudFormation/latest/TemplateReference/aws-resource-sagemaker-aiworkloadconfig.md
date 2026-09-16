---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-aiworkloadconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AIWorkloadConfig
<a name="aws-resource-sagemaker-aiworkloadconfig"></a>

Creates a reusable AI workload configuration that defines datasets, data sources, and benchmark tool settings for consistent performance testing of generative AI inference deployments on Amazon SageMaker AI.

## Syntax
<a name="aws-resource-sagemaker-aiworkloadconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-aiworkloadconfig-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::AIWorkloadConfig",
  "Properties" : {
      "[AIWorkloadConfigName](#cfn-sagemaker-aiworkloadconfig-aiworkloadconfigname)" : {{String}},
      "[AIWorkloadConfigs](#cfn-sagemaker-aiworkloadconfig-aiworkloadconfigs)" : {{AIWorkloadConfigs}},
      "[DatasetConfig](#cfn-sagemaker-aiworkloadconfig-datasetconfig)" : {{AIDatasetConfig}},
      "[Tags](#cfn-sagemaker-aiworkloadconfig-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-aiworkloadconfig-syntax.yaml"></a>

```
Type: AWS::SageMaker::AIWorkloadConfig
Properties:
  [AIWorkloadConfigName](#cfn-sagemaker-aiworkloadconfig-aiworkloadconfigname): {{String}}
  [AIWorkloadConfigs](#cfn-sagemaker-aiworkloadconfig-aiworkloadconfigs): {{
    AIWorkloadConfigs}}
  [DatasetConfig](#cfn-sagemaker-aiworkloadconfig-datasetconfig): {{
    AIDatasetConfig}}
  [Tags](#cfn-sagemaker-aiworkloadconfig-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-aiworkloadconfig-properties"></a>

`AIWorkloadConfigName`  <a name="cfn-sagemaker-aiworkloadconfig-aiworkloadconfigname"></a>
The name of the AI workload configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9](-*[a-z0-9]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AIWorkloadConfigs`  <a name="cfn-sagemaker-aiworkloadconfig-aiworkloadconfigs"></a>
The benchmark tool configuration for an AI workload.
*Required*: No
*Type*: [AIWorkloadConfigs](aws-properties-sagemaker-aiworkloadconfig-aiworkloadconfigs.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatasetConfig`  <a name="cfn-sagemaker-aiworkloadconfig-datasetconfig"></a>
Property description not available.
*Required*: No
*Type*: [AIDatasetConfig](aws-properties-sagemaker-aiworkloadconfig-aidatasetconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-aiworkloadconfig-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-aiworkloadconfig-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-aiworkloadconfig-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-aiworkloadconfig-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-aiworkloadconfig-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-aiworkloadconfig-return-values-fn--getatt-fn--getatt"></a>

`AIWorkloadConfigArn`  <a name="AIWorkloadConfigArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the AI workload configuration.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
A timestamp that indicates when the configuration was created.
