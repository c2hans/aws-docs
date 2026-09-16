---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-searchschemaelement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable SearchSchemaElement
<a name="aws-properties-dynamodb-globaltable-searchschemaelement"></a>

An element in the search schema of a vector index.

## Syntax
<a name="aws-properties-dynamodb-globaltable-searchschemaelement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-globaltable-searchschemaelement-syntax.json"></a>

```
{
  "[AttributeName](#cfn-dynamodb-globaltable-searchschemaelement-attributename)" : {{String}},
  "[SearchSchemaElementType](#cfn-dynamodb-globaltable-searchschemaelement-searchschemaelementtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-searchschemaelement-syntax.yaml"></a>

```
  [AttributeName](#cfn-dynamodb-globaltable-searchschemaelement-attributename): {{String}}
  [SearchSchemaElementType](#cfn-dynamodb-globaltable-searchschemaelement-searchschemaelementtype): {{String}}
```

## Properties
<a name="aws-properties-dynamodb-globaltable-searchschemaelement-properties"></a>

`AttributeName`  <a name="cfn-dynamodb-globaltable-searchschemaelement-attributename"></a>
The name of the attribute. This attribute must also be declared in the table's `AttributeDefinitions`.
*Required*: Yes
*Type*: String
*Maximum*: `65535`
*Update requires*: Updates are not supported.

`SearchSchemaElementType`  <a name="cfn-dynamodb-globaltable-searchschemaelement-searchschemaelementtype"></a>
The role of the attribute in the search schema. Valid values:
+ `HASH` - A partition key that partitions the vector index for independent scaling. When specified, you must provide this attribute's value in the `SearchConditionExpression`.
+ `INLINE_FILTER` - An attribute projected into the vector index for filtering at the storage layer during search. Inline filters are optional in the `SearchConditionExpression`.
*Required*: Yes
*Type*: String
*Allowed values*: `HASH | INLINE_FILTER`
*Update requires*: Updates are not supported.
