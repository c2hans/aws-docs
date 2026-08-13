---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fis-experiment-experimentoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FIS::Experiment ExperimentOptions
<a name="aws-properties-fis-experiment-experimentoptions"></a>

Describes the options for an experiment.

## Syntax
<a name="aws-properties-fis-experiment-experimentoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fis-experiment-experimentoptions-syntax.json"></a>

```
{
  "[ActionsMode](#cfn-fis-experiment-experimentoptions-actionsmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-fis-experiment-experimentoptions-syntax.yaml"></a>

```
  [ActionsMode](#cfn-fis-experiment-experimentoptions-actionsmode): {{String}}
```

## Properties
<a name="aws-properties-fis-experiment-experimentoptions-properties"></a>

`ActionsMode`  <a name="cfn-fis-experiment-experimentoptions-actionsmode"></a>
The actions mode of the experiment that is set from the StartExperiment API command.
*Required*: No
*Type*: String
*Allowed values*: `skip-all | run-all`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
