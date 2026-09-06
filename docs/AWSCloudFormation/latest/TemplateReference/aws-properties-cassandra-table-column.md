---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cassandra-table-column.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Table Column
<a name="aws-properties-cassandra-table-column"></a>

The name and data type of an individual column in a table. In addition to the data type, you can also use the following two keywords:
+ `STATIC` if the table has a clustering column. Static columns store values that are shared by all rows in the same partition.
+ `FROZEN` for collection data types. In frozen collections the values of the collection are serialized into a single immutable value, and Amazon Keyspaces treats them like a `BLOB`.

## Syntax
<a name="aws-properties-cassandra-table-column-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cassandra-table-column-syntax.json"></a>

```
{
  "[ColumnName](#cfn-cassandra-table-column-columnname)" : {{String}},
  "[ColumnType](#cfn-cassandra-table-column-columntype)" : {{String}}
}
```

### YAML
<a name="aws-properties-cassandra-table-column-syntax.yaml"></a>

```
  [ColumnName](#cfn-cassandra-table-column-columnname): {{String}}
  [ColumnType](#cfn-cassandra-table-column-columntype): {{String}}
```

## Properties
<a name="aws-properties-cassandra-table-column-properties"></a>

`ColumnName`  <a name="cfn-cassandra-table-column-columnname"></a>
The name of the column. For more information, see [Identifiers](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.elements.identifier) in the *Amazon Keyspaces Developer Guide*.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_]{1,47}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ColumnType`  <a name="cfn-cassandra-table-column-columntype"></a>
The data type of the column. For more information, see [Data types](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.data-types) in the *Amazon Keyspaces Developer Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
