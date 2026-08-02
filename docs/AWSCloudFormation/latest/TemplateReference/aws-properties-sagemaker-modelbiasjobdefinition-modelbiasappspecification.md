---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelBiasJobDefinition ModelBiasAppSpecification
<a name="aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification"></a>

Docker container image configuration object for the model bias job.

## Syntax
<a name="aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification-syntax.json"></a>

```
{
  "[ConfigUri](#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-configuri)" : {{String}},
  "[Environment](#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-environment)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ImageUri](#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-imageuri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification-syntax.yaml"></a>

```
  [ConfigUri](#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-configuri): {{String}}
  [Environment](#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-environment): {{
    {{Key}}: {{Value}}}}
  [ImageUri](#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-imageuri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification-properties"></a>

`ConfigUri`  <a name="cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-configuri"></a>
JSON formatted S3 file that defines bias parameters. For more information on this JSON configuration file, see [Configure bias parameters](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-config-json-monitor-bias-parameters.html).
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Environment`  <a name="cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-environment"></a>
Sets the environment variables in the Docker container.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z_][a-zA-Z0-9_]*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ImageUri`  <a name="cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-imageuri"></a>
The container image to be run by the model bias job.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
