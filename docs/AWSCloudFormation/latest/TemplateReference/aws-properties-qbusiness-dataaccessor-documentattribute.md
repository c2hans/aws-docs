---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-dataaccessor-documentattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataAccessor DocumentAttribute
<a name="aws-properties-qbusiness-dataaccessor-documentattribute"></a>

A document attribute or metadata field.

## Syntax
<a name="aws-properties-qbusiness-dataaccessor-documentattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-dataaccessor-documentattribute-syntax.json"></a>

```
{
  "[Name](#cfn-qbusiness-dataaccessor-documentattribute-name)" : {{String}},
  "[Value](#cfn-qbusiness-dataaccessor-documentattribute-value)" : {{DocumentAttributeValue}}
}
```

### YAML
<a name="aws-properties-qbusiness-dataaccessor-documentattribute-syntax.yaml"></a>

```
  [Name](#cfn-qbusiness-dataaccessor-documentattribute-name): {{String}}
  [Value](#cfn-qbusiness-dataaccessor-documentattribute-value): {{
    DocumentAttributeValue}}
```

## Properties
<a name="aws-properties-qbusiness-dataaccessor-documentattribute-properties"></a>

`Name`  <a name="cfn-qbusiness-dataaccessor-documentattribute-name"></a>
The identifier for the attribute.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_][a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-qbusiness-dataaccessor-documentattribute-value"></a>
The value of the attribute.
*Required*: Yes
*Type*: [DocumentAttributeValue](aws-properties-qbusiness-dataaccessor-documentattributevalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
