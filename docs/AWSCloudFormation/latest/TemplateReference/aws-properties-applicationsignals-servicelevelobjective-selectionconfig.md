---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-selectionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective SelectionConfig
<a name="aws-properties-applicationsignals-servicelevelobjective-selectionconfig"></a>

Defines how operations are selected for a service-level SLO.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-selectionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-selectionconfig-syntax.json"></a>

```
{
  "[Pattern](#cfn-applicationsignals-servicelevelobjective-selectionconfig-pattern)" : {{String}},
  "[Type](#cfn-applicationsignals-servicelevelobjective-selectionconfig-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-selectionconfig-syntax.yaml"></a>

```
  [Pattern](#cfn-applicationsignals-servicelevelobjective-selectionconfig-pattern): {{String}}
  [Type](#cfn-applicationsignals-servicelevelobjective-selectionconfig-type): {{String}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-selectionconfig-properties"></a>

`Pattern`  <a name="cfn-applicationsignals-servicelevelobjective-selectionconfig-pattern"></a>
A prefix string or regular expression that specifies which operations to include in a service-level SLO. When `SelectionType` is `PREFIX`, this value is a prefix string that matches the beginning of operation names. When `SelectionType` is `REGEX`, this value is a regular expression that matches operation names.
*Required*: No
*Type*: String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-applicationsignals-servicelevelobjective-selectionconfig-type"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `EXPLICIT | PREFIX | REGEX`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
