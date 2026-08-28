---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-form-valuemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Form ValueMapping
<a name="aws-properties-amplifyuibuilder-form-valuemapping"></a>

The `ValueMapping` property specifies the association between a complex object and a display value. Use `ValueMapping` to store how to represent complex objects when they are displayed.

## Syntax
<a name="aws-properties-amplifyuibuilder-form-valuemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-form-valuemapping-syntax.json"></a>

```
{
  "[DisplayValue](#cfn-amplifyuibuilder-form-valuemapping-displayvalue)" : {{FormInputValueProperty}},
  "[Value](#cfn-amplifyuibuilder-form-valuemapping-value)" : {{FormInputValueProperty}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-form-valuemapping-syntax.yaml"></a>

```
  [DisplayValue](#cfn-amplifyuibuilder-form-valuemapping-displayvalue): {{
    FormInputValueProperty}}
  [Value](#cfn-amplifyuibuilder-form-valuemapping-value): {{
    FormInputValueProperty}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-form-valuemapping-properties"></a>

`DisplayValue`  <a name="cfn-amplifyuibuilder-form-valuemapping-displayvalue"></a>
The value to display for the complex object.
*Required*: No
*Type*: [FormInputValueProperty](aws-properties-amplifyuibuilder-form-forminputvalueproperty.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-amplifyuibuilder-form-valuemapping-value"></a>
The complex object.
*Required*: Yes
*Type*: [FormInputValueProperty](aws-properties-amplifyuibuilder-form-forminputvalueproperty.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
