---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-secretconnectorproperty.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType SecretConnectorProperty
<a name="aws-properties-glue-connectiontype-secretconnectorproperty"></a>

<a name="aws-properties-glue-connectiontype-secretconnectorproperty-description"></a>The `SecretConnectorProperty` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-secretconnectorproperty-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-secretconnectorproperty-syntax.json"></a>

```
{
  "[KeyOverride](#cfn-glue-connectiontype-secretconnectorproperty-keyoverride)" : {{String}},
  "[Name](#cfn-glue-connectiontype-secretconnectorproperty-name)" : {{String}},
  "[PropertyLocation](#cfn-glue-connectiontype-secretconnectorproperty-propertylocation)" : {{String}},
  "[PropertyType](#cfn-glue-connectiontype-secretconnectorproperty-propertytype)" : {{String}},
  "[Required](#cfn-glue-connectiontype-secretconnectorproperty-required)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-secretconnectorproperty-syntax.yaml"></a>

```
  [KeyOverride](#cfn-glue-connectiontype-secretconnectorproperty-keyoverride): {{String}}
  [Name](#cfn-glue-connectiontype-secretconnectorproperty-name): {{String}}
  [PropertyLocation](#cfn-glue-connectiontype-secretconnectorproperty-propertylocation): {{String}}
  [PropertyType](#cfn-glue-connectiontype-secretconnectorproperty-propertytype): {{String}}
  [Required](#cfn-glue-connectiontype-secretconnectorproperty-required): {{Boolean}}
```

## Properties
<a name="aws-properties-glue-connectiontype-secretconnectorproperty-properties"></a>

`KeyOverride`  <a name="cfn-glue-connectiontype-secretconnectorproperty-keyoverride"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-glue-connectiontype-secretconnectorproperty-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PropertyLocation`  <a name="cfn-glue-connectiontype-secretconnectorproperty-propertylocation"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `HEADER | BODY | QUERY_PARAM | PATH`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PropertyType`  <a name="cfn-glue-connectiontype-secretconnectorproperty-propertytype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `SECRET`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Required`  <a name="cfn-glue-connectiontype-secretconnectorproperty-required"></a>
Property description not available.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
