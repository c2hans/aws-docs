---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trialcomponent-trialcomponentstatus.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrialComponent TrialComponentStatus
<a name="aws-properties-sagemaker-trialcomponent-trialcomponentstatus"></a>

The status of the trial component.

## Syntax
<a name="aws-properties-sagemaker-trialcomponent-trialcomponentstatus-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trialcomponent-trialcomponentstatus-syntax.json"></a>

```
{
  "[Message](#cfn-sagemaker-trialcomponent-trialcomponentstatus-message)" : {{String}},
  "[PrimaryStatus](#cfn-sagemaker-trialcomponent-trialcomponentstatus-primarystatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-trialcomponent-trialcomponentstatus-syntax.yaml"></a>

```
  [Message](#cfn-sagemaker-trialcomponent-trialcomponentstatus-message): {{String}}
  [PrimaryStatus](#cfn-sagemaker-trialcomponent-trialcomponentstatus-primarystatus): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-trialcomponent-trialcomponentstatus-properties"></a>

`Message`  <a name="cfn-sagemaker-trialcomponent-trialcomponentstatus-message"></a>
If the component failed, a message describing why.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryStatus`  <a name="cfn-sagemaker-trialcomponent-trialcomponentstatus-primarystatus"></a>
The status of the trial component.
*Required*: No
*Type*: String
*Allowed values*: `InProgress | Completed | Failed | Stopping | Stopped`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
