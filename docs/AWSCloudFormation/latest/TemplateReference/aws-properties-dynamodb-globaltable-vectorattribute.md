---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-vectorattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable VectorAttribute
<a name="aws-properties-dynamodb-globaltable-vectorattribute"></a>

The definition of a vector attribute for a vector index.

## Syntax
<a name="aws-properties-dynamodb-globaltable-vectorattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-globaltable-vectorattribute-syntax.json"></a>

```
{
  "[AttributeName](#cfn-dynamodb-globaltable-vectorattribute-attributename)" : {{String}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-vectorattribute-syntax.yaml"></a>

```
  [AttributeName](#cfn-dynamodb-globaltable-vectorattribute-attributename): {{String}}
```

## Properties
<a name="aws-properties-dynamodb-globaltable-vectorattribute-properties"></a>

`AttributeName`  <a name="cfn-dynamodb-globaltable-vectorattribute-attributename"></a>
The name of the vector attribute.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: Updates are not supported.
