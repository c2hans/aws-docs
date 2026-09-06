---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-experimentdefinition-attributevalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::ExperimentDefinition AttributeValue
<a name="aws-properties-appconfig-experimentdefinition-attributevalue"></a>

A value for a feature flag attribute. Only one of the members can be set.

## Syntax
<a name="aws-properties-appconfig-experimentdefinition-attributevalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appconfig-experimentdefinition-attributevalue-syntax.json"></a>

```
{
  "[BooleanValue](#cfn-appconfig-experimentdefinition-attributevalue-booleanvalue)" : {{Boolean}},
  "[NumberArray](#cfn-appconfig-experimentdefinition-attributevalue-numberarray)" : {{[ Number, ... ]}},
  "[NumberValue](#cfn-appconfig-experimentdefinition-attributevalue-numbervalue)" : {{Number}},
  "[StringArray](#cfn-appconfig-experimentdefinition-attributevalue-stringarray)" : {{[ String, ... ]}},
  "[StringValue](#cfn-appconfig-experimentdefinition-attributevalue-stringvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-appconfig-experimentdefinition-attributevalue-syntax.yaml"></a>

```
  [BooleanValue](#cfn-appconfig-experimentdefinition-attributevalue-booleanvalue): {{
    Boolean}}
  [NumberArray](#cfn-appconfig-experimentdefinition-attributevalue-numberarray): {{
    - Number}}
  [NumberValue](#cfn-appconfig-experimentdefinition-attributevalue-numbervalue): {{
    Number}}
  [StringArray](#cfn-appconfig-experimentdefinition-attributevalue-stringarray): {{
    - String}}
  [StringValue](#cfn-appconfig-experimentdefinition-attributevalue-stringvalue): {{
    String}}
```

## Properties
<a name="aws-properties-appconfig-experimentdefinition-attributevalue-properties"></a>

`BooleanValue`  <a name="cfn-appconfig-experimentdefinition-attributevalue-booleanvalue"></a>
A Boolean value for the attribute.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberArray`  <a name="cfn-appconfig-experimentdefinition-attributevalue-numberarray"></a>
An array of numeric values for the attribute.
*Required*: No
*Type*: Array of Number
*Minimum*: `0`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberValue`  <a name="cfn-appconfig-experimentdefinition-attributevalue-numbervalue"></a>
A numeric value for the attribute.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringArray`  <a name="cfn-appconfig-experimentdefinition-attributevalue-stringarray"></a>
An array of string values for the attribute.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringValue`  <a name="cfn-appconfig-experimentdefinition-attributevalue-stringvalue"></a>
A string value for the attribute.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
