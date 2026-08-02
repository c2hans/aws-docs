---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-projection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::Table Projection
<a name="aws-properties-dynamodb-table-projection"></a>

Represents attributes that are copied (projected) from the table into an index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

## Syntax
<a name="aws-properties-dynamodb-table-projection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-table-projection-syntax.json"></a>

```
{
  "[NonKeyAttributes](#cfn-dynamodb-table-projection-nonkeyattributes)" : {{[ String, ... ]}},
  "[ProjectionType](#cfn-dynamodb-table-projection-projectiontype)" : {{String}}
}
```

### YAML
<a name="aws-properties-dynamodb-table-projection-syntax.yaml"></a>

```
  [NonKeyAttributes](#cfn-dynamodb-table-projection-nonkeyattributes): {{
    - String}}
  [ProjectionType](#cfn-dynamodb-table-projection-projectiontype): {{String}}
```

## Properties
<a name="aws-properties-dynamodb-table-projection-properties"></a>

`NonKeyAttributes`  <a name="cfn-dynamodb-table-projection-nonkeyattributes"></a>
Represents the non-key attribute names which will be projected into the index.
For global and local secondary indexes, the total count of `NonKeyAttributes` summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of `INCLUDE`. You still can specify the ProjectionType of `ALL` to project all attributes from the source table, even if the table has more than 100 attributes.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: Updates are not supported.

`ProjectionType`  <a name="cfn-dynamodb-table-projection-projectiontype"></a>
The set of attributes that are projected into the index:
+ `KEYS_ONLY` - Only the index and primary keys are projected into the index.
+ `INCLUDE` - In addition to the attributes described in `KEYS_ONLY`, the secondary index will include other non-key attributes that you specify.
+ `ALL` - All of the table attributes are projected into the index.
When using the DynamoDB console, `ALL` is selected by default.
*Required*: No
*Type*: String
*Allowed values*: `ALL | KEYS_ONLY | INCLUDE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
