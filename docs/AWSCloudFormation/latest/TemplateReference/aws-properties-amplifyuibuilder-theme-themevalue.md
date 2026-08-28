---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-theme-themevalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Theme ThemeValue
<a name="aws-properties-amplifyuibuilder-theme-themevalue"></a>

The `ThemeValue` property specifies the configuration of a theme's properties.

## Syntax
<a name="aws-properties-amplifyuibuilder-theme-themevalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-theme-themevalue-syntax.json"></a>

```
{
  "[Children](#cfn-amplifyuibuilder-theme-themevalue-children)" : {{[ ThemeValues, ... ]}},
  "[Value](#cfn-amplifyuibuilder-theme-themevalue-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-theme-themevalue-syntax.yaml"></a>

```
  [Children](#cfn-amplifyuibuilder-theme-themevalue-children): {{
    - ThemeValues}}
  [Value](#cfn-amplifyuibuilder-theme-themevalue-value): {{String}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-theme-themevalue-properties"></a>

`Children`  <a name="cfn-amplifyuibuilder-theme-themevalue-children"></a>
A list of key-value pairs that define the theme's properties.
*Required*: No
*Type*: Array of [ThemeValues](aws-properties-amplifyuibuilder-theme-themevalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-amplifyuibuilder-theme-themevalue-value"></a>
The value of a theme property.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
