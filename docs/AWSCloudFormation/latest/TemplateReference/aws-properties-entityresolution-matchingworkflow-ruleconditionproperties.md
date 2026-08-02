---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-matchingworkflow-ruleconditionproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::MatchingWorkflow RuleConditionProperties
<a name="aws-properties-entityresolution-matchingworkflow-ruleconditionproperties"></a>

The properties of a rule condition that provides the ability to use more complex syntax.

## Syntax
<a name="aws-properties-entityresolution-matchingworkflow-ruleconditionproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-matchingworkflow-ruleconditionproperties-syntax.json"></a>

```
{
  "[MatchingConfig](#cfn-entityresolution-matchingworkflow-ruleconditionproperties-matchingconfig)" : {{MatchingConfig}},
  "[Rules](#cfn-entityresolution-matchingworkflow-ruleconditionproperties-rules)" : {{[ RuleCondition, ... ]}}
}
```

### YAML
<a name="aws-properties-entityresolution-matchingworkflow-ruleconditionproperties-syntax.yaml"></a>

```
  [MatchingConfig](#cfn-entityresolution-matchingworkflow-ruleconditionproperties-matchingconfig): {{
    MatchingConfig}}
  [Rules](#cfn-entityresolution-matchingworkflow-ruleconditionproperties-rules): {{
    - RuleCondition}}
```

## Properties
<a name="aws-properties-entityresolution-matchingworkflow-ruleconditionproperties-properties"></a>

`MatchingConfig`  <a name="cfn-entityresolution-matchingworkflow-ruleconditionproperties-matchingconfig"></a>
An object that contains configuration settings for the matching process.
*Required*: No
*Type*: [MatchingConfig](aws-properties-entityresolution-matchingworkflow-matchingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rules`  <a name="cfn-entityresolution-matchingworkflow-ruleconditionproperties-rules"></a>
 A list of rule objects, each of which have fields `ruleName` and `condition`.
*Required*: Yes
*Type*: Array of [RuleCondition](aws-properties-entityresolution-matchingworkflow-rulecondition.md)
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
