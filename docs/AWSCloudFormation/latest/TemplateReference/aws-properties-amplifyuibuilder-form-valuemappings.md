---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-form-valuemappings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Form ValueMappings
<a name="aws-properties-amplifyuibuilder-form-valuemappings"></a>

The `ValueMappings` property specifies the data binding configuration for a value map.

## Syntax
<a name="aws-properties-amplifyuibuilder-form-valuemappings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-form-valuemappings-syntax.json"></a>

```
{
  "[BindingProperties](#cfn-amplifyuibuilder-form-valuemappings-bindingproperties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Values](#cfn-amplifyuibuilder-form-valuemappings-values)" : {{[ ValueMapping, ... ]}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-form-valuemappings-syntax.yaml"></a>

```
  [BindingProperties](#cfn-amplifyuibuilder-form-valuemappings-bindingproperties): {{
    {{Key}}: {{Value}}}}
  [Values](#cfn-amplifyuibuilder-form-valuemappings-values): {{
    - ValueMapping}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-form-valuemappings-properties"></a>

`BindingProperties`  <a name="cfn-amplifyuibuilder-form-valuemappings-bindingproperties"></a>
The information to bind fields to data at runtime.
*Required*: No
*Type*: Object of [FormInputBindingPropertiesValue](aws-properties-amplifyuibuilder-form-forminputbindingpropertiesvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-amplifyuibuilder-form-valuemappings-values"></a>
The value and display value pairs.
*Required*: Yes
*Type*: Array of [ValueMapping](aws-properties-amplifyuibuilder-form-valuemapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
