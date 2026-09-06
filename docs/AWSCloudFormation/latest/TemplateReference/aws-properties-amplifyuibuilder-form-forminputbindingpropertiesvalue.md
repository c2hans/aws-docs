---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-form-forminputbindingpropertiesvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Form FormInputBindingPropertiesValue
<a name="aws-properties-amplifyuibuilder-form-forminputbindingpropertiesvalue"></a>

Represents the data binding configuration for a form's input fields at runtime.You can use `FormInputBindingPropertiesValue` to add exposed properties to a form to allow different values to be entered when a form is reused in different places in an app.

## Syntax
<a name="aws-properties-amplifyuibuilder-form-forminputbindingpropertiesvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-form-forminputbindingpropertiesvalue-syntax.json"></a>

```
{
  "[BindingProperties](#cfn-amplifyuibuilder-form-forminputbindingpropertiesvalue-bindingproperties)" : {{FormInputBindingPropertiesValueProperties}},
  "[Type](#cfn-amplifyuibuilder-form-forminputbindingpropertiesvalue-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-form-forminputbindingpropertiesvalue-syntax.yaml"></a>

```
  [BindingProperties](#cfn-amplifyuibuilder-form-forminputbindingpropertiesvalue-bindingproperties): {{
    FormInputBindingPropertiesValueProperties}}
  [Type](#cfn-amplifyuibuilder-form-forminputbindingpropertiesvalue-type): {{String}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-form-forminputbindingpropertiesvalue-properties"></a>

`BindingProperties`  <a name="cfn-amplifyuibuilder-form-forminputbindingpropertiesvalue-bindingproperties"></a>
Describes the properties to customize with data at runtime.
*Required*: No
*Type*: [FormInputBindingPropertiesValueProperties](aws-properties-amplifyuibuilder-form-forminputbindingpropertiesvalueproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-amplifyuibuilder-form-forminputbindingpropertiesvalue-type"></a>
The property type.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
