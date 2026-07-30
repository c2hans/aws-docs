---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-form-formdatatypeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Form FormDataTypeConfig
<a name="aws-properties-amplifyuibuilder-form-formdatatypeconfig"></a>

The `FormDataTypeConfig` property specifies the data type configuration for the data source associated with a form.

## Syntax
<a name="aws-properties-amplifyuibuilder-form-formdatatypeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-form-formdatatypeconfig-syntax.json"></a>

```
{
  "[DataSourceType](#cfn-amplifyuibuilder-form-formdatatypeconfig-datasourcetype)" : {{String}},
  "[DataTypeName](#cfn-amplifyuibuilder-form-formdatatypeconfig-datatypename)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-form-formdatatypeconfig-syntax.yaml"></a>

```
  [DataSourceType](#cfn-amplifyuibuilder-form-formdatatypeconfig-datasourcetype): {{String}}
  [DataTypeName](#cfn-amplifyuibuilder-form-formdatatypeconfig-datatypename): {{String}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-form-formdatatypeconfig-properties"></a>

`DataSourceType`  <a name="cfn-amplifyuibuilder-form-formdatatypeconfig-datasourcetype"></a>
The data source type, either an Amplify DataStore model or a custom data type.
*Required*: Yes
*Type*: String
*Allowed values*: `DataStore | Custom`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataTypeName`  <a name="cfn-amplifyuibuilder-form-formdatatypeconfig-datatypename"></a>
The unique name of the data type you are using as the data source for the form.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
