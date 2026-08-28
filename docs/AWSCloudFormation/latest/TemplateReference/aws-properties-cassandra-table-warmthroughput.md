---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cassandra-table-warmthroughput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Table WarmThroughput
<a name="aws-properties-cassandra-table-warmthroughput"></a>

<a name="aws-properties-cassandra-table-warmthroughput-description"></a>The `WarmThroughput` property type specifies Property description not available. for an [AWS::Cassandra::Table](aws-resource-cassandra-table.md).

## Syntax
<a name="aws-properties-cassandra-table-warmthroughput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cassandra-table-warmthroughput-syntax.json"></a>

```
{
  "[ReadUnitsPerSecond](#cfn-cassandra-table-warmthroughput-readunitspersecond)" : {{Integer}},
  "[WriteUnitsPerSecond](#cfn-cassandra-table-warmthroughput-writeunitspersecond)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cassandra-table-warmthroughput-syntax.yaml"></a>

```
  [ReadUnitsPerSecond](#cfn-cassandra-table-warmthroughput-readunitspersecond): {{Integer}}
  [WriteUnitsPerSecond](#cfn-cassandra-table-warmthroughput-writeunitspersecond): {{Integer}}
```

## Properties
<a name="aws-properties-cassandra-table-warmthroughput-properties"></a>

`ReadUnitsPerSecond`  <a name="cfn-cassandra-table-warmthroughput-readunitspersecond"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WriteUnitsPerSecond`  <a name="cfn-cassandra-table-warmthroughput-writeunitspersecond"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
