---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationinsights-application-customcomponent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationInsights::Application CustomComponent
<a name="aws-properties-applicationinsights-application-customcomponent"></a>

The `AWS::ApplicationInsights::Application CustomComponent` property type describes a custom component by grouping similar standalone instances to monitor.

## Syntax
<a name="aws-properties-applicationinsights-application-customcomponent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationinsights-application-customcomponent-syntax.json"></a>

```
{
  "[ComponentName](#cfn-applicationinsights-application-customcomponent-componentname)" : {{String}},
  "[ResourceList](#cfn-applicationinsights-application-customcomponent-resourcelist)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-applicationinsights-application-customcomponent-syntax.yaml"></a>

```
  [ComponentName](#cfn-applicationinsights-application-customcomponent-componentname): {{String}}
  [ResourceList](#cfn-applicationinsights-application-customcomponent-resourcelist): {{
    - String}}
```

## Properties
<a name="aws-properties-applicationinsights-application-customcomponent-properties"></a>

`ComponentName`  <a name="cfn-applicationinsights-application-customcomponent-componentname"></a>
The name of the component.
*Required*: Yes
*Type*: String
*Pattern*: `^[\d\w\-_.+]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceList`  <a name="cfn-applicationinsights-application-customcomponent-resourcelist"></a>
The list of resource ARNs that belong to the component.
*Required*: Yes
*Type*: Array of String
*Maximum*: `300`
*Minimum*: `20 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
