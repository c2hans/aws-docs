---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cassandra-table-cdcspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Table CdcSpecification
<a name="aws-properties-cassandra-table-cdcspecification"></a>

The settings for the CDC stream of a table. For more information about CDC streams, see [Working with change data capture (CDC) streams in Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/cdc.html) in the *Amazon Keyspaces Developer Guide*.

## Syntax
<a name="aws-properties-cassandra-table-cdcspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cassandra-table-cdcspecification-syntax.json"></a>

```
{
  "[Status](#cfn-cassandra-table-cdcspecification-status)" : {{String}},
  "[Tags](#cfn-cassandra-table-cdcspecification-tags)" : {{[ Tag, ... ]}},
  "[ViewType](#cfn-cassandra-table-cdcspecification-viewtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-cassandra-table-cdcspecification-syntax.yaml"></a>

```
  [Status](#cfn-cassandra-table-cdcspecification-status): {{String}}
  [Tags](#cfn-cassandra-table-cdcspecification-tags): {{
    - Tag}}
  [ViewType](#cfn-cassandra-table-cdcspecification-viewtype): {{String}}
```

## Properties
<a name="aws-properties-cassandra-table-cdcspecification-properties"></a>

`Status`  <a name="cfn-cassandra-table-cdcspecification-status"></a>
The status of the CDC stream. You can enable or disable a stream for a table.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cassandra-table-cdcspecification-tags"></a>
The tags (key-value pairs) that you want to apply to the stream.
*Required*: No
*Type*: Array of [Tag](aws-properties-cassandra-table-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ViewType`  <a name="cfn-cassandra-table-cdcspecification-viewtype"></a>
The view type specifies the changes Amazon Keyspaces records for each changed row in the stream. After you create the stream, you can't make changes to this selection.
The options are:
+ `NEW_AND_OLD_IMAGES` - both versions of the row, before and after the change. This is the default.
+ `NEW_IMAGE` - the version of the row after the change.
+ `OLD_IMAGE` - the version of the row before the change.
+ `KEYS_ONLY` - the partition and clustering keys of the row that was changed.
*Required*: No
*Type*: String
*Allowed values*: `NEW_IMAGE | OLD_IMAGE | KEYS_ONLY | NEW_AND_OLD_IMAGES`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
