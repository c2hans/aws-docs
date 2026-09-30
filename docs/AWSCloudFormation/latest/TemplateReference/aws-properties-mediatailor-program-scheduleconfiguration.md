---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-program-scheduleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Program ScheduleConfiguration
<a name="aws-properties-mediatailor-program-scheduleconfiguration"></a>

Schedule configuration parameters. A channel must be stopped before changes can be made to the schedule.

## Syntax
<a name="aws-properties-mediatailor-program-scheduleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-program-scheduleconfiguration-syntax.json"></a>

```
{
  "[ClipRange](#cfn-mediatailor-program-scheduleconfiguration-cliprange)" : {{ClipRange}},
  "[Transition](#cfn-mediatailor-program-scheduleconfiguration-transition)" : {{Transition}}
}
```

### YAML
<a name="aws-properties-mediatailor-program-scheduleconfiguration-syntax.yaml"></a>

```
  [ClipRange](#cfn-mediatailor-program-scheduleconfiguration-cliprange): {{
    ClipRange}}
  [Transition](#cfn-mediatailor-program-scheduleconfiguration-transition): {{
    Transition}}
```

## Properties
<a name="aws-properties-mediatailor-program-scheduleconfiguration-properties"></a>

`ClipRange`  <a name="cfn-mediatailor-program-scheduleconfiguration-cliprange"></a>
Program clip range configuration.
*Required*: No
*Type*: [ClipRange](aws-properties-mediatailor-program-cliprange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Transition`  <a name="cfn-mediatailor-program-scheduleconfiguration-transition"></a>
Program transition configurations.
*Required*: Yes
*Type*: [Transition](aws-properties-mediatailor-program-transition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
