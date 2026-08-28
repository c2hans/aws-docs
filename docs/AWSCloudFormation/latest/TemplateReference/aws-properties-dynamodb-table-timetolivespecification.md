---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-timetolivespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::Table TimeToLiveSpecification
<a name="aws-properties-dynamodb-table-timetolivespecification"></a>

Represents the settings used to enable or disable Time to Live (TTL) for the specified table.

## Syntax
<a name="aws-properties-dynamodb-table-timetolivespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-table-timetolivespecification-syntax.json"></a>

```
{
  "[AttributeName](#cfn-dynamodb-table-timetolivespecification-attributename)" : {{String}},
  "[Enabled](#cfn-dynamodb-table-timetolivespecification-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-dynamodb-table-timetolivespecification-syntax.yaml"></a>

```
  [AttributeName](#cfn-dynamodb-table-timetolivespecification-attributename): {{String}}
  [Enabled](#cfn-dynamodb-table-timetolivespecification-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-dynamodb-table-timetolivespecification-properties"></a>

`AttributeName`  <a name="cfn-dynamodb-table-timetolivespecification-attributename"></a>
The name of the TTL attribute used to store the expiration time for items in the table.
+ The `AttributeName` property is required when enabling the TTL, or when TTL is already enabled.
+ To update this property, you must first disable TTL and then enable TTL with the new attribute name.
*Required*: Conditional
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-dynamodb-table-timetolivespecification-enabled"></a>
Indicates whether TTL is to be enabled (true) or disabled (false) on the table.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
