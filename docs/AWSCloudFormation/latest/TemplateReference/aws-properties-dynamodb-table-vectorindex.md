---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-vectorindex.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::Table VectorIndex
<a name="aws-properties-dynamodb-table-vectorindex"></a>

Contains the configuration settings for a vector index, including the index name, vector attribute, dimensions, distance function, search schema, and projection.

## Syntax
<a name="aws-properties-dynamodb-table-vectorindex-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-table-vectorindex-syntax.json"></a>

```
{
  "[Dimensions](#cfn-dynamodb-table-vectorindex-dimensions)" : {{Integer}},
  "[DistanceFunction](#cfn-dynamodb-table-vectorindex-distancefunction)" : {{String}},
  "[IndexName](#cfn-dynamodb-table-vectorindex-indexname)" : {{String}},
  "[Projection](#cfn-dynamodb-table-vectorindex-projection)" : {{Projection}},
  "[SearchSchema](#cfn-dynamodb-table-vectorindex-searchschema)" : {{[ SearchSchemaElement, ... ]}},
  "[VectorAttribute](#cfn-dynamodb-table-vectorindex-vectorattribute)" : {{VectorAttribute}}
}
```

### YAML
<a name="aws-properties-dynamodb-table-vectorindex-syntax.yaml"></a>

```
  [Dimensions](#cfn-dynamodb-table-vectorindex-dimensions): {{Integer}}
  [DistanceFunction](#cfn-dynamodb-table-vectorindex-distancefunction): {{String}}
  [IndexName](#cfn-dynamodb-table-vectorindex-indexname): {{String}}
  [Projection](#cfn-dynamodb-table-vectorindex-projection): {{
    Projection}}
  [SearchSchema](#cfn-dynamodb-table-vectorindex-searchschema): {{
    - SearchSchemaElement}}
  [VectorAttribute](#cfn-dynamodb-table-vectorindex-vectorattribute): {{
    VectorAttribute}}
```

## Properties
<a name="aws-properties-dynamodb-table-vectorindex-properties"></a>

`Dimensions`  <a name="cfn-dynamodb-table-vectorindex-dimensions"></a>
The number of dimensions in each vector.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: Updates are not supported.

`DistanceFunction`  <a name="cfn-dynamodb-table-vectorindex-distancefunction"></a>
The distance function used to calculate similarity between vectors. Valid values: `COSINE`, `EUCLIDEAN`, `DOT_PRODUCT`.
*Required*: Yes
*Type*: String
*Allowed values*: `COSINE | DOT_PRODUCT | EUCLIDEAN`
*Update requires*: Updates are not supported.

`IndexName`  <a name="cfn-dynamodb-table-vectorindex-indexname"></a>
The name of the vector index.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9_.-]+`
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: Updates are not supported.

`Projection`  <a name="cfn-dynamodb-table-vectorindex-projection"></a>
Specifies attributes that are copied (projected) from the table into the vector index.
*Required*: Yes
*Type*: [Projection](aws-properties-dynamodb-table-projection.md)
*Update requires*: Updates are not supported.

`SearchSchema`  <a name="cfn-dynamodb-table-vectorindex-searchschema"></a>
The search schema that defines partition key and inline filter attributes for the vector index.
Every attribute that you reference in `SearchSchema` must also be declared in the table's `AttributeDefinitions`, the same way key attributes are declared for a global secondary index. Otherwise, the request fails with a `ValidationException`.
*Required*: No
*Type*: Array of [SearchSchemaElement](aws-properties-dynamodb-table-searchschemaelement.md)
*Minimum*: `1`
*Update requires*: Updates are not supported.

`VectorAttribute`  <a name="cfn-dynamodb-table-vectorindex-vectorattribute"></a>
The vector attribute configuration for the index.
*Required*: Yes
*Type*: [VectorAttribute](aws-properties-dynamodb-table-vectorattribute.md)
*Update requires*: Updates are not supported.
