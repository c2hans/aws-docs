---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-dataaccessor-documentattributevalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataAccessor DocumentAttributeValue
<a name="aws-properties-qbusiness-dataaccessor-documentattributevalue"></a>

The value of a document attribute. You can only provide one value for a document attribute.

## Syntax
<a name="aws-properties-qbusiness-dataaccessor-documentattributevalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-dataaccessor-documentattributevalue-syntax.json"></a>

```
{
  "[DateValue](#cfn-qbusiness-dataaccessor-documentattributevalue-datevalue)" : {{String}},
  "[LongValue](#cfn-qbusiness-dataaccessor-documentattributevalue-longvalue)" : {{Number}},
  "[StringListValue](#cfn-qbusiness-dataaccessor-documentattributevalue-stringlistvalue)" : {{[ String, ... ]}},
  "[StringValue](#cfn-qbusiness-dataaccessor-documentattributevalue-stringvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-dataaccessor-documentattributevalue-syntax.yaml"></a>

```
  [DateValue](#cfn-qbusiness-dataaccessor-documentattributevalue-datevalue): {{String}}
  [LongValue](#cfn-qbusiness-dataaccessor-documentattributevalue-longvalue): {{Number}}
  [StringListValue](#cfn-qbusiness-dataaccessor-documentattributevalue-stringlistvalue): {{
    - String}}
  [StringValue](#cfn-qbusiness-dataaccessor-documentattributevalue-stringvalue): {{
    String}}
```

## Properties
<a name="aws-properties-qbusiness-dataaccessor-documentattributevalue-properties"></a>

`DateValue`  <a name="cfn-qbusiness-dataaccessor-documentattributevalue-datevalue"></a>
A date expressed as an ISO 8601 string.
It's important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10\+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LongValue`  <a name="cfn-qbusiness-dataaccessor-documentattributevalue-longvalue"></a>
A long integer value.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringListValue`  <a name="cfn-qbusiness-dataaccessor-documentattributevalue-stringlistvalue"></a>
A list of strings.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringValue`  <a name="cfn-qbusiness-dataaccessor-documentattributevalue-stringvalue"></a>
A string.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
