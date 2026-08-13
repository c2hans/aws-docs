---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-debughookconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob DebugHookConfig
<a name="aws-properties-sagemaker-trainingjob-debughookconfig"></a>

Configuration information for the Amazon SageMaker Debugger hook parameters, metric and tensor collections, and storage paths. To learn more about how to configure the `DebugHookConfig` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html).

## Syntax
<a name="aws-properties-sagemaker-trainingjob-debughookconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-debughookconfig-syntax.json"></a>

```
{
  "[CollectionConfigurations](#cfn-sagemaker-trainingjob-debughookconfig-collectionconfigurations)" : {{[ CollectionConfiguration, ... ]}},
  "[HookParameters](#cfn-sagemaker-trainingjob-debughookconfig-hookparameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[LocalPath](#cfn-sagemaker-trainingjob-debughookconfig-localpath)" : {{String}},
  "[S3OutputPath](#cfn-sagemaker-trainingjob-debughookconfig-s3outputpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-debughookconfig-syntax.yaml"></a>

```
  [CollectionConfigurations](#cfn-sagemaker-trainingjob-debughookconfig-collectionconfigurations): {{
    - CollectionConfiguration}}
  [HookParameters](#cfn-sagemaker-trainingjob-debughookconfig-hookparameters): {{
    {{Key}}: {{Value}}}}
  [LocalPath](#cfn-sagemaker-trainingjob-debughookconfig-localpath): {{String}}
  [S3OutputPath](#cfn-sagemaker-trainingjob-debughookconfig-s3outputpath): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-debughookconfig-properties"></a>

`CollectionConfigurations`  <a name="cfn-sagemaker-trainingjob-debughookconfig-collectionconfigurations"></a>
Configuration information for Amazon SageMaker Debugger tensor collections. To learn more about how to configure the `CollectionConfiguration` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html).
*Required*: No
*Type*: Array of [CollectionConfiguration](aws-properties-sagemaker-trainingjob-collectionconfiguration.md)
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HookParameters`  <a name="cfn-sagemaker-trainingjob-debughookconfig-hookparameters"></a>
Configuration information for the Amazon SageMaker Debugger hook parameters.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LocalPath`  <a name="cfn-sagemaker-trainingjob-debughookconfig-localpath"></a>
Path to local storage location for metrics and tensors. Defaults to `/opt/ml/output/tensors/`.
*Required*: No
*Type*: String
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3OutputPath`  <a name="cfn-sagemaker-trainingjob-debughookconfig-s3outputpath"></a>
Path to Amazon S3 storage location for metrics and tensors.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
