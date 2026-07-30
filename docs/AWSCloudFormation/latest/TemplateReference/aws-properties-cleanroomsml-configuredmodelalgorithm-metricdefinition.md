---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-configuredmodelalgorithm-metricdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithm MetricDefinition
<a name="aws-properties-cleanroomsml-configuredmodelalgorithm-metricdefinition"></a>

Information about the model metric that is reported for a trained model.

## Syntax
<a name="aws-properties-cleanroomsml-configuredmodelalgorithm-metricdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-configuredmodelalgorithm-metricdefinition-syntax.json"></a>

```
{
  "[Name](#cfn-cleanroomsml-configuredmodelalgorithm-metricdefinition-name)" : {{String}},
  "[Regex](#cfn-cleanroomsml-configuredmodelalgorithm-metricdefinition-regex)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-configuredmodelalgorithm-metricdefinition-syntax.yaml"></a>

```
  [Name](#cfn-cleanroomsml-configuredmodelalgorithm-metricdefinition-name): {{String}}
  [Regex](#cfn-cleanroomsml-configuredmodelalgorithm-metricdefinition-regex): {{String}}
```

## Properties
<a name="aws-properties-cleanroomsml-configuredmodelalgorithm-metricdefinition-properties"></a>

`Name`  <a name="cfn-cleanroomsml-configuredmodelalgorithm-metricdefinition-name"></a>
The name of the model metric.
*Required*: Yes
*Type*: String
*Pattern*: `^.+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Regex`  <a name="cfn-cleanroomsml-configuredmodelalgorithm-metricdefinition-regex"></a>
The regular expression statement that defines how the model metric is reported.
*Required*: Yes
*Type*: String
*Pattern*: `^.+$`
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
