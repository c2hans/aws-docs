---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Form FieldValidationConfiguration
<a name="aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration"></a>

The `FieldValidationConfiguration` property specifies the validation configuration for a field.

## Syntax
<a name="aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration-syntax.json"></a>

```
{
  "[NumValues](#cfn-amplifyuibuilder-form-fieldvalidationconfiguration-numvalues)" : {{[ Number, ... ]}},
  "[StrValues](#cfn-amplifyuibuilder-form-fieldvalidationconfiguration-strvalues)" : {{[ String, ... ]}},
  "[Type](#cfn-amplifyuibuilder-form-fieldvalidationconfiguration-type)" : {{String}},
  "[ValidationMessage](#cfn-amplifyuibuilder-form-fieldvalidationconfiguration-validationmessage)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration-syntax.yaml"></a>

```
  [NumValues](#cfn-amplifyuibuilder-form-fieldvalidationconfiguration-numvalues): {{
    - Number}}
  [StrValues](#cfn-amplifyuibuilder-form-fieldvalidationconfiguration-strvalues): {{
    - String}}
  [Type](#cfn-amplifyuibuilder-form-fieldvalidationconfiguration-type): {{String}}
  [ValidationMessage](#cfn-amplifyuibuilder-form-fieldvalidationconfiguration-validationmessage): {{String}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration-properties"></a>

`NumValues`  <a name="cfn-amplifyuibuilder-form-fieldvalidationconfiguration-numvalues"></a>
The validation to perform on a number value.
*Required*: No
*Type*: Array of Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StrValues`  <a name="cfn-amplifyuibuilder-form-fieldvalidationconfiguration-strvalues"></a>
The validation to perform on a string value.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-amplifyuibuilder-form-fieldvalidationconfiguration-type"></a>
The validation to perform on an object type.``
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValidationMessage`  <a name="cfn-amplifyuibuilder-form-fieldvalidationconfiguration-validationmessage"></a>
The validation message to display.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
