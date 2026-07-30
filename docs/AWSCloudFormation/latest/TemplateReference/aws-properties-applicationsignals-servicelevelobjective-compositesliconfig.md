---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-compositesliconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective CompositeSliConfig
<a name="aws-properties-applicationsignals-servicelevelobjective-compositesliconfig"></a>

This structure contains the configuration for a composite service level indicator (SLI) that aggregates metrics across multiple operations of a service for service-level SLOs.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-compositesliconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-compositesliconfig-syntax.json"></a>

```
{
  "[CompositeSliComponents](#cfn-applicationsignals-servicelevelobjective-compositesliconfig-compositeslicomponents)" : {{[ CompositeSliComponent, ... ]}},
  "[SelectionConfig](#cfn-applicationsignals-servicelevelobjective-compositesliconfig-selectionconfig)" : {{SelectionConfig}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-compositesliconfig-syntax.yaml"></a>

```
  [CompositeSliComponents](#cfn-applicationsignals-servicelevelobjective-compositesliconfig-compositeslicomponents): {{
    - CompositeSliComponent}}
  [SelectionConfig](#cfn-applicationsignals-servicelevelobjective-compositesliconfig-selectionconfig): {{
    SelectionConfig}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-compositesliconfig-properties"></a>

`CompositeSliComponents`  <a name="cfn-applicationsignals-servicelevelobjective-compositesliconfig-compositeslicomponents"></a>
Property description not available.
*Required*: No
*Type*: Array of [CompositeSliComponent](aws-properties-applicationsignals-servicelevelobjective-compositeslicomponent.md)
*Minimum*: `2`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectionConfig`  <a name="cfn-applicationsignals-servicelevelobjective-compositesliconfig-selectionconfig"></a>
Specifies how operations are selected for this service-level SLO. Operations can be selected explicitly by listing them, by specifying a prefix to match operation names, or by providing a regular expression pattern.
*Required*: Yes
*Type*: [SelectionConfig](aws-properties-applicationsignals-servicelevelobjective-selectionconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
