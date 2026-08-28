---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-datasource-documentattributevalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataSource DocumentAttributeValue
<a name="aws-properties-qbusiness-datasource-documentattributevalue"></a>

The value of a document attribute. You can only provide one value for a document attribute.

## Syntax
<a name="aws-properties-qbusiness-datasource-documentattributevalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-datasource-documentattributevalue-syntax.json"></a>

```
{
  "[DateValue](#cfn-qbusiness-datasource-documentattributevalue-datevalue)" : {{String}},
  "[LongValue](#cfn-qbusiness-datasource-documentattributevalue-longvalue)" : {{Number}},
  "[StringListValue](#cfn-qbusiness-datasource-documentattributevalue-stringlistvalue)" : {{[ String, ... ]}},
  "[StringValue](#cfn-qbusiness-datasource-documentattributevalue-stringvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-datasource-documentattributevalue-syntax.yaml"></a>

```
  [DateValue](#cfn-qbusiness-datasource-documentattributevalue-datevalue): {{String}}
  [LongValue](#cfn-qbusiness-datasource-documentattributevalue-longvalue): {{Number}}
  [StringListValue](#cfn-qbusiness-datasource-documentattributevalue-stringlistvalue): {{
    - String}}
  [StringValue](#cfn-qbusiness-datasource-documentattributevalue-stringvalue): {{
    String}}
```

## Properties
<a name="aws-properties-qbusiness-datasource-documentattributevalue-properties"></a>

`DateValue`  <a name="cfn-qbusiness-datasource-documentattributevalue-datevalue"></a>
A date expressed as an ISO 8601 string.
It's important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10\+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LongValue`  <a name="cfn-qbusiness-datasource-documentattributevalue-longvalue"></a>
A long integer value.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringListValue`  <a name="cfn-qbusiness-datasource-documentattributevalue-stringlistvalue"></a>
A list of strings.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringValue`  <a name="cfn-qbusiness-datasource-documentattributevalue-stringvalue"></a>
A string.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
