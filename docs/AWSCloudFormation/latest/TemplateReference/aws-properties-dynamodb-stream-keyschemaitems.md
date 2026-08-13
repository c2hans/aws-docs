---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-stream-keyschemaitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::Stream KeySchemaItems
<a name="aws-properties-dynamodb-stream-keyschemaitems"></a>

<a name="aws-properties-dynamodb-stream-keyschemaitems-description"></a>The `KeySchemaItems` property type specifies Property description not available. for an [AWS::DynamoDB::Stream](aws-resource-dynamodb-stream.md).

## Syntax
<a name="aws-properties-dynamodb-stream-keyschemaitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-stream-keyschemaitems-syntax.json"></a>

```
{
  "[AttributeName](#cfn-dynamodb-stream-keyschemaitems-attributename)" : {{String}},
  "[KeyType](#cfn-dynamodb-stream-keyschemaitems-keytype)" : {{String}}
}
```

### YAML
<a name="aws-properties-dynamodb-stream-keyschemaitems-syntax.yaml"></a>

```
  [AttributeName](#cfn-dynamodb-stream-keyschemaitems-attributename): {{String}}
  [KeyType](#cfn-dynamodb-stream-keyschemaitems-keytype): {{String}}
```

## Properties
<a name="aws-properties-dynamodb-stream-keyschemaitems-properties"></a>

`AttributeName`  <a name="cfn-dynamodb-stream-keyschemaitems-attributename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyType`  <a name="cfn-dynamodb-stream-keyschemaitems-keytype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `HASH | RANGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
