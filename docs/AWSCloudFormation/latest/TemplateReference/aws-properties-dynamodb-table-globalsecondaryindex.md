---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-globalsecondaryindex.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::Table GlobalSecondaryIndex
<a name="aws-properties-dynamodb-table-globalsecondaryindex"></a>

Represents the properties of a global secondary index.

## Syntax
<a name="aws-properties-dynamodb-table-globalsecondaryindex-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-table-globalsecondaryindex-syntax.json"></a>

```
{
  "[ContributorInsightsSpecification](#cfn-dynamodb-table-globalsecondaryindex-contributorinsightsspecification)" : {{ContributorInsightsSpecification}},
  "[IndexName](#cfn-dynamodb-table-globalsecondaryindex-indexname)" : {{String}},
  "[KeySchema](#cfn-dynamodb-table-globalsecondaryindex-keyschema)" : {{[ KeySchema, ... ]}},
  "[OnDemandThroughput](#cfn-dynamodb-table-globalsecondaryindex-ondemandthroughput)" : {{OnDemandThroughput}},
  "[Projection](#cfn-dynamodb-table-globalsecondaryindex-projection)" : {{Projection}},
  "[ProvisionedThroughput](#cfn-dynamodb-table-globalsecondaryindex-provisionedthroughput)" : {{ProvisionedThroughput}},
  "[WarmThroughput](#cfn-dynamodb-table-globalsecondaryindex-warmthroughput)" : {{WarmThroughput}}
}
```

### YAML
<a name="aws-properties-dynamodb-table-globalsecondaryindex-syntax.yaml"></a>

```
  [ContributorInsightsSpecification](#cfn-dynamodb-table-globalsecondaryindex-contributorinsightsspecification): {{
    ContributorInsightsSpecification}}
  [IndexName](#cfn-dynamodb-table-globalsecondaryindex-indexname): {{String}}
  [KeySchema](#cfn-dynamodb-table-globalsecondaryindex-keyschema): {{
    - KeySchema}}
  [OnDemandThroughput](#cfn-dynamodb-table-globalsecondaryindex-ondemandthroughput): {{
    OnDemandThroughput}}
  [Projection](#cfn-dynamodb-table-globalsecondaryindex-projection): {{
    Projection}}
  [ProvisionedThroughput](#cfn-dynamodb-table-globalsecondaryindex-provisionedthroughput): {{
    ProvisionedThroughput}}
  [WarmThroughput](#cfn-dynamodb-table-globalsecondaryindex-warmthroughput): {{
    WarmThroughput}}
```

## Properties
<a name="aws-properties-dynamodb-table-globalsecondaryindex-properties"></a>

`ContributorInsightsSpecification`  <a name="cfn-dynamodb-table-globalsecondaryindex-contributorinsightsspecification"></a>
The settings used to specify whether to enable CloudWatch Contributor Insights for the global table and define which events to monitor.
*Required*: No
*Type*: [ContributorInsightsSpecification](aws-properties-dynamodb-table-contributorinsightsspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IndexName`  <a name="cfn-dynamodb-table-globalsecondaryindex-indexname"></a>
The name of the global secondary index. The name must be unique among all other indexes on this table.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9_.-]+`
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: Updates are not supported.

`KeySchema`  <a name="cfn-dynamodb-table-globalsecondaryindex-keyschema"></a>
The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:
+ `HASH` - partition key
+ `RANGE` - sort key
The partition key of an item is also known as its *hash attribute*. The term "hash attribute" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its *range attribute*. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.
*Required*: Yes
*Type*: [Array](aws-properties-dynamodb-table-keyschema.md) of [KeySchema](aws-properties-dynamodb-table-keyschema.md)
*Minimum*: `1`
*Update requires*: Updates are not supported.

`OnDemandThroughput`  <a name="cfn-dynamodb-table-globalsecondaryindex-ondemandthroughput"></a>
The maximum number of read and write units for the specified global secondary index. If you use this parameter, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both. You must use either `OnDemandThroughput` or `ProvisionedThroughput` based on your table's capacity mode.
*Required*: No
*Type*: [OnDemandThroughput](aws-properties-dynamodb-table-ondemandthroughput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Projection`  <a name="cfn-dynamodb-table-globalsecondaryindex-projection"></a>
Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.
*Required*: Yes
*Type*: [Projection](aws-properties-dynamodb-table-projection.md)
*Update requires*: Updates are not supported.

`ProvisionedThroughput`  <a name="cfn-dynamodb-table-globalsecondaryindex-provisionedthroughput"></a>
Represents the provisioned throughput settings for the specified global secondary index. You must use either `OnDemandThroughput` or `ProvisionedThroughput` based on your table's capacity mode.
For current minimum and maximum provisioned throughput values, see [Service, Account, and Table Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide*.
*Required*: No
*Type*: [ProvisionedThroughput](aws-properties-dynamodb-table-provisionedthroughput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WarmThroughput`  <a name="cfn-dynamodb-table-globalsecondaryindex-warmthroughput"></a>
Represents the warm throughput value (in read units per second and write units per second) for the specified secondary index. If you use this parameter, you must specify `ReadUnitsPerSecond`, `WriteUnitsPerSecond`, or both.
*Required*: No
*Type*: [WarmThroughput](aws-properties-dynamodb-table-warmthroughput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
