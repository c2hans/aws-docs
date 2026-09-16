---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-connectorproperty.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType ConnectorProperty
<a name="aws-properties-glue-connectiontype-connectorproperty"></a>

<a name="aws-properties-glue-connectiontype-connectorproperty-description"></a>The `ConnectorProperty` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-connectorproperty-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-connectorproperty-syntax.json"></a>

```
{
  "[AllowedValues](#cfn-glue-connectiontype-connectorproperty-allowedvalues)" : {{[ String, ... ]}},
  "[DefaultValue](#cfn-glue-connectiontype-connectorproperty-defaultvalue)" : {{String}},
  "[KeyOverride](#cfn-glue-connectiontype-connectorproperty-keyoverride)" : {{String}},
  "[Name](#cfn-glue-connectiontype-connectorproperty-name)" : {{String}},
  "[PropertyLocation](#cfn-glue-connectiontype-connectorproperty-propertylocation)" : {{String}},
  "[PropertyType](#cfn-glue-connectiontype-connectorproperty-propertytype)" : {{String}},
  "[Required](#cfn-glue-connectiontype-connectorproperty-required)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-connectorproperty-syntax.yaml"></a>

```
  [AllowedValues](#cfn-glue-connectiontype-connectorproperty-allowedvalues): {{
    - String}}
  [DefaultValue](#cfn-glue-connectiontype-connectorproperty-defaultvalue): {{String}}
  [KeyOverride](#cfn-glue-connectiontype-connectorproperty-keyoverride): {{String}}
  [Name](#cfn-glue-connectiontype-connectorproperty-name): {{String}}
  [PropertyLocation](#cfn-glue-connectiontype-connectorproperty-propertylocation): {{String}}
  [PropertyType](#cfn-glue-connectiontype-connectorproperty-propertytype): {{String}}
  [Required](#cfn-glue-connectiontype-connectorproperty-required): {{Boolean}}
```

## Properties
<a name="aws-properties-glue-connectiontype-connectorproperty-properties"></a>

`AllowedValues`  <a name="cfn-glue-connectiontype-connectorproperty-allowedvalues"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefaultValue`  <a name="cfn-glue-connectiontype-connectorproperty-defaultvalue"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KeyOverride`  <a name="cfn-glue-connectiontype-connectorproperty-keyoverride"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-glue-connectiontype-connectorproperty-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PropertyLocation`  <a name="cfn-glue-connectiontype-connectorproperty-propertylocation"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `HEADER | BODY | QUERY_PARAM | PATH`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PropertyType`  <a name="cfn-glue-connectiontype-connectorproperty-propertytype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `USER_INPUT | SECRET | READ_ONLY | UNUSED | SECRET_OR_USER_INPUT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Required`  <a name="cfn-glue-connectiontype-connectorproperty-required"></a>
Property description not available.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
