---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cassandra-table-clusteringkeycolumn.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Table ClusteringKeyColumn
<a name="aws-properties-cassandra-table-clusteringkeycolumn"></a>

Defines an individual column within the clustering key.

## Syntax
<a name="aws-properties-cassandra-table-clusteringkeycolumn-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cassandra-table-clusteringkeycolumn-syntax.json"></a>

```
{
  "[Column](#cfn-cassandra-table-clusteringkeycolumn-column)" : {{Column}},
  "[OrderBy](#cfn-cassandra-table-clusteringkeycolumn-orderby)" : {{String}}
}
```

### YAML
<a name="aws-properties-cassandra-table-clusteringkeycolumn-syntax.yaml"></a>

```
  [Column](#cfn-cassandra-table-clusteringkeycolumn-column): {{
    Column}}
  [OrderBy](#cfn-cassandra-table-clusteringkeycolumn-orderby): {{String}}
```

## Properties
<a name="aws-properties-cassandra-table-clusteringkeycolumn-properties"></a>

`Column`  <a name="cfn-cassandra-table-clusteringkeycolumn-column"></a>
The name and data type of this clustering key column.
*Required*: Yes
*Type*: [Column](aws-properties-cassandra-table-column.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OrderBy`  <a name="cfn-cassandra-table-clusteringkeycolumn-orderby"></a>
The order in which this column's data is stored:
+ `ASC` (default) - The column's data is stored in ascending order.
+ `DESC` - The column's data is stored in descending order.
*Required*: No
*Type*: String
*Allowed values*: `ASC | DESC`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
