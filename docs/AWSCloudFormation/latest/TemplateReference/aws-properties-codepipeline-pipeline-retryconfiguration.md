---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-retryconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline RetryConfiguration
<a name="aws-properties-codepipeline-pipeline-retryconfiguration"></a>

The retry configuration specifies automatic retry for a failed stage, along with the configured retry mode.

## Syntax
<a name="aws-properties-codepipeline-pipeline-retryconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-retryconfiguration-syntax.json"></a>

```
{
  "[RetryMode](#cfn-codepipeline-pipeline-retryconfiguration-retrymode)" : {{String}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-retryconfiguration-syntax.yaml"></a>

```
  [RetryMode](#cfn-codepipeline-pipeline-retryconfiguration-retrymode): {{String}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-retryconfiguration-properties"></a>

`RetryMode`  <a name="cfn-codepipeline-pipeline-retryconfiguration-retrymode"></a>
The method that you want to configure for automatic stage retry on stage failure. You can specify to retry only failed action in the stage or all actions in the stage.
*Required*: No
*Type*: String
*Allowed values*: `ALL_ACTIONS | FAILED_ACTIONS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
