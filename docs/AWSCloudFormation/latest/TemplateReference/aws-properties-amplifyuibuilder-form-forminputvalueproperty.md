---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-form-forminputvalueproperty.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Form FormInputValueProperty
<a name="aws-properties-amplifyuibuilder-form-forminputvalueproperty"></a>

The `FormInputValueProperty` property specifies the configuration for an input field on a form. Use `FormInputValueProperty` to specify the values to render or bind by default.

## Syntax
<a name="aws-properties-amplifyuibuilder-form-forminputvalueproperty-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-form-forminputvalueproperty-syntax.json"></a>

```
{
  "[BindingProperties](#cfn-amplifyuibuilder-form-forminputvalueproperty-bindingproperties)" : {{FormInputValuePropertyBindingProperties}},
  "[Concat](#cfn-amplifyuibuilder-form-forminputvalueproperty-concat)" : {{[ FormInputValueProperty, ... ]}},
  "[Value](#cfn-amplifyuibuilder-form-forminputvalueproperty-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-form-forminputvalueproperty-syntax.yaml"></a>

```
  [BindingProperties](#cfn-amplifyuibuilder-form-forminputvalueproperty-bindingproperties): {{
    FormInputValuePropertyBindingProperties}}
  [Concat](#cfn-amplifyuibuilder-form-forminputvalueproperty-concat): {{
    - FormInputValueProperty}}
  [Value](#cfn-amplifyuibuilder-form-forminputvalueproperty-value): {{String}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-form-forminputvalueproperty-properties"></a>

`BindingProperties`  <a name="cfn-amplifyuibuilder-form-forminputvalueproperty-bindingproperties"></a>
The information to bind fields to data at runtime.
*Required*: No
*Type*: [FormInputValuePropertyBindingProperties](aws-properties-amplifyuibuilder-form-forminputvaluepropertybindingproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Concat`  <a name="cfn-amplifyuibuilder-form-forminputvalueproperty-concat"></a>
A list of form properties to concatenate to create the value to assign to this field property.
*Required*: No
*Type*: Array of [FormInputValueProperty](#aws-properties-amplifyuibuilder-form-forminputvalueproperty)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-amplifyuibuilder-form-forminputvalueproperty-value"></a>
The value to assign to the input field.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
