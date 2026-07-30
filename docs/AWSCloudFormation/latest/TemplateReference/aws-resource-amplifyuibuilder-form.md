---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-amplifyuibuilder-form.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Form
<a name="aws-resource-amplifyuibuilder-form"></a>

The AWS::AmplifyUIBuilder::Form resource specifies all of the information that is required to create a form.

## Syntax
<a name="aws-resource-amplifyuibuilder-form-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-amplifyuibuilder-form-syntax.json"></a>

```
{
  "Type" : "AWS::AmplifyUIBuilder::Form",
  "Properties" : {
      "[AppId](#cfn-amplifyuibuilder-form-appid)" : {{String}},
      "[Cta](#cfn-amplifyuibuilder-form-cta)" : {{FormCTA}},
      "[DataType](#cfn-amplifyuibuilder-form-datatype)" : {{FormDataTypeConfig}},
      "[EnvironmentName](#cfn-amplifyuibuilder-form-environmentname)" : {{String}},
      "[Fields](#cfn-amplifyuibuilder-form-fields)" : {{{{{Key}}: {{Value}}, ...}}},
      "[FormActionType](#cfn-amplifyuibuilder-form-formactiontype)" : {{String}},
      "[LabelDecorator](#cfn-amplifyuibuilder-form-labeldecorator)" : {{String}},
      "[Name](#cfn-amplifyuibuilder-form-name)" : {{String}},
      "[SchemaVersion](#cfn-amplifyuibuilder-form-schemaversion)" : {{String}},
      "[SectionalElements](#cfn-amplifyuibuilder-form-sectionalelements)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Style](#cfn-amplifyuibuilder-form-style)" : {{FormStyle}},
      "[Tags](#cfn-amplifyuibuilder-form-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-amplifyuibuilder-form-syntax.yaml"></a>

```
Type: AWS::AmplifyUIBuilder::Form
Properties:
  [AppId](#cfn-amplifyuibuilder-form-appid): {{String}}
  [Cta](#cfn-amplifyuibuilder-form-cta): {{
    FormCTA}}
  [DataType](#cfn-amplifyuibuilder-form-datatype): {{
    FormDataTypeConfig}}
  [EnvironmentName](#cfn-amplifyuibuilder-form-environmentname): {{String}}
  [Fields](#cfn-amplifyuibuilder-form-fields): {{
    {{Key}}: {{Value}}}}
  [FormActionType](#cfn-amplifyuibuilder-form-formactiontype): {{String}}
  [LabelDecorator](#cfn-amplifyuibuilder-form-labeldecorator): {{String}}
  [Name](#cfn-amplifyuibuilder-form-name): {{String}}
  [SchemaVersion](#cfn-amplifyuibuilder-form-schemaversion): {{String}}
  [SectionalElements](#cfn-amplifyuibuilder-form-sectionalelements): {{
    {{Key}}: {{Value}}}}
  [Style](#cfn-amplifyuibuilder-form-style): {{
    FormStyle}}
  [Tags](#cfn-amplifyuibuilder-form-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-amplifyuibuilder-form-properties"></a>

`AppId`  <a name="cfn-amplifyuibuilder-form-appid"></a>
The unique ID of the Amplify app associated with the form.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Cta`  <a name="cfn-amplifyuibuilder-form-cta"></a>
The `FormCTA` object that stores the call to action configuration for the form.
*Required*: No
*Type*: [FormCTA](aws-properties-amplifyuibuilder-form-formcta.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataType`  <a name="cfn-amplifyuibuilder-form-datatype"></a>
The type of data source to use to create the form.
*Required*: No
*Type*: [FormDataTypeConfig](aws-properties-amplifyuibuilder-form-formdatatypeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentName`  <a name="cfn-amplifyuibuilder-form-environmentname"></a>
The name of the backend environment that is a part of the Amplify app.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Fields`  <a name="cfn-amplifyuibuilder-form-fields"></a>
The configuration information for the form's fields.
*Required*: No
*Type*: Object of [FieldConfig](aws-properties-amplifyuibuilder-form-fieldconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FormActionType`  <a name="cfn-amplifyuibuilder-form-formactiontype"></a>
Specifies whether to perform a create or update action on the form.
*Required*: No
*Type*: String
*Allowed values*: `create | update`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LabelDecorator`  <a name="cfn-amplifyuibuilder-form-labeldecorator"></a>
Specifies an icon or decoration to display on the form.
*Required*: No
*Type*: String
*Allowed values*: `required | optional | none`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-amplifyuibuilder-form-name"></a>
The name of the form.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaVersion`  <a name="cfn-amplifyuibuilder-form-schemaversion"></a>
The schema version of the form.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SectionalElements`  <a name="cfn-amplifyuibuilder-form-sectionalelements"></a>
The configuration information for the visual helper elements for the form. These elements are not associated with any data.
*Required*: No
*Type*: Object of [SectionalElement](aws-properties-amplifyuibuilder-form-sectionalelement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Style`  <a name="cfn-amplifyuibuilder-form-style"></a>
The configuration for the form's style.
*Required*: No
*Type*: [FormStyle](aws-properties-amplifyuibuilder-form-formstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-amplifyuibuilder-form-tags"></a>
One or more key-value pairs to use when tagging the form data.
*Required*: No
*Type*: Object of String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-amplifyuibuilder-form-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-amplifyuibuilder-form-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-amplifyuibuilder-form-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The ID for the form.
