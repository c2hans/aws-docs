---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-warmthroughput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::Table WarmThroughput
<a name="aws-properties-dynamodb-table-warmthroughput"></a>

Provides visibility into the number of read and write operations your table or secondary index can instantaneously support. The settings can be modified using the `UpdateTable` operation to meet the throughput requirements of an upcoming peak event.

## Syntax
<a name="aws-properties-dynamodb-table-warmthroughput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-table-warmthroughput-syntax.json"></a>

```
{
  "[ReadUnitsPerSecond](#cfn-dynamodb-table-warmthroughput-readunitspersecond)" : {{Integer}},
  "[WriteUnitsPerSecond](#cfn-dynamodb-table-warmthroughput-writeunitspersecond)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-dynamodb-table-warmthroughput-syntax.yaml"></a>

```
  [ReadUnitsPerSecond](#cfn-dynamodb-table-warmthroughput-readunitspersecond): {{Integer}}
  [WriteUnitsPerSecond](#cfn-dynamodb-table-warmthroughput-writeunitspersecond): {{Integer}}
```

## Properties
<a name="aws-properties-dynamodb-table-warmthroughput-properties"></a>

`ReadUnitsPerSecond`  <a name="cfn-dynamodb-table-warmthroughput-readunitspersecond"></a>
Represents the number of read operations your base table can instantaneously support.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WriteUnitsPerSecond`  <a name="cfn-dynamodb-table-warmthroughput-writeunitspersecond"></a>
Represents the number of write operations your base table can instantaneously support.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
