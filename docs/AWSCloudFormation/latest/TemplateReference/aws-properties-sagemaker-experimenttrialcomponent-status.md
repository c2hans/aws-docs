---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-experimenttrialcomponent-status.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ExperimentTrialComponent Status
<a name="aws-properties-sagemaker-experimenttrialcomponent-status"></a>

<a name="aws-properties-sagemaker-experimenttrialcomponent-status-description"></a>The `Status` property type specifies Property description not available. for an [AWS::SageMaker::ExperimentTrialComponent](aws-resource-sagemaker-experimenttrialcomponent.md).

## Syntax
<a name="aws-properties-sagemaker-experimenttrialcomponent-status-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-experimenttrialcomponent-status-syntax.json"></a>

```
{
  "[Message](#cfn-sagemaker-experimenttrialcomponent-status-message)" : {{String}},
  "[PrimaryStatus](#cfn-sagemaker-experimenttrialcomponent-status-primarystatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-experimenttrialcomponent-status-syntax.yaml"></a>

```
  [Message](#cfn-sagemaker-experimenttrialcomponent-status-message): {{String}}
  [PrimaryStatus](#cfn-sagemaker-experimenttrialcomponent-status-primarystatus): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-experimenttrialcomponent-status-properties"></a>

`Message`  <a name="cfn-sagemaker-experimenttrialcomponent-status-message"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryStatus`  <a name="cfn-sagemaker-experimenttrialcomponent-status-primarystatus"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `InProgress | Completed | Failed | Stopping | Stopped`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
