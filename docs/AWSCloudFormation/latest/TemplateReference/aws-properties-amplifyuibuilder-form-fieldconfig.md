---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-form-fieldconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Form FieldConfig
<a name="aws-properties-amplifyuibuilder-form-fieldconfig"></a>

The `FieldConfig` property specifies the configuration information for a field in a table.

## Syntax
<a name="aws-properties-amplifyuibuilder-form-fieldconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-form-fieldconfig-syntax.json"></a>

```
{
  "[Excluded](#cfn-amplifyuibuilder-form-fieldconfig-excluded)" : {{Boolean}},
  "[InputType](#cfn-amplifyuibuilder-form-fieldconfig-inputtype)" : {{FieldInputConfig}},
  "[Label](#cfn-amplifyuibuilder-form-fieldconfig-label)" : {{String}},
  "[Position](#cfn-amplifyuibuilder-form-fieldconfig-position)" : {{FieldPosition}},
  "[Validations](#cfn-amplifyuibuilder-form-fieldconfig-validations)" : {{[ FieldValidationConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-form-fieldconfig-syntax.yaml"></a>

```
  [Excluded](#cfn-amplifyuibuilder-form-fieldconfig-excluded): {{Boolean}}
  [InputType](#cfn-amplifyuibuilder-form-fieldconfig-inputtype): {{
    FieldInputConfig}}
  [Label](#cfn-amplifyuibuilder-form-fieldconfig-label): {{String}}
  [Position](#cfn-amplifyuibuilder-form-fieldconfig-position): {{
    FieldPosition}}
  [Validations](#cfn-amplifyuibuilder-form-fieldconfig-validations): {{
    - FieldValidationConfiguration}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-form-fieldconfig-properties"></a>

`Excluded`  <a name="cfn-amplifyuibuilder-form-fieldconfig-excluded"></a>
Specifies whether to hide a field.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputType`  <a name="cfn-amplifyuibuilder-form-fieldconfig-inputtype"></a>
Describes the configuration for the default input value to display for a field.
*Required*: No
*Type*: [FieldInputConfig](aws-properties-amplifyuibuilder-form-fieldinputconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Label`  <a name="cfn-amplifyuibuilder-form-fieldconfig-label"></a>
The label for the field.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Position`  <a name="cfn-amplifyuibuilder-form-fieldconfig-position"></a>
Specifies the field position.
*Required*: No
*Type*: [FieldPosition](aws-properties-amplifyuibuilder-form-fieldposition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Validations`  <a name="cfn-amplifyuibuilder-form-fieldconfig-validations"></a>
The validations to perform on the value in the field.
*Required*: No
*Type*: Array of [FieldValidationConfiguration](aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
