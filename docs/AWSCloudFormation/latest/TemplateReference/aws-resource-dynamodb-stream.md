---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-stream.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::Stream
<a name="aws-resource-dynamodb-stream"></a>

<a name="aws-resource-dynamodb-stream-description"></a>The `AWS::DynamoDB::Stream` resource Property description not available. for DynamoDB.

## Syntax
<a name="aws-resource-dynamodb-stream-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-dynamodb-stream-syntax.json"></a>

```
{
  "Type" : "AWS::DynamoDB::Stream",
  "Properties" : {
      "[StreamViewType](#cfn-dynamodb-stream-streamviewtype)" : {{String}},
      "[TableName](#cfn-dynamodb-stream-tablename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-dynamodb-stream-syntax.yaml"></a>

```
Type: AWS::DynamoDB::Stream
Properties:
  [StreamViewType](#cfn-dynamodb-stream-streamviewtype): {{String}}
  [TableName](#cfn-dynamodb-stream-tablename): {{String}}
```

## Properties
<a name="aws-resource-dynamodb-stream-properties"></a>

`StreamViewType`  <a name="cfn-dynamodb-stream-streamviewtype"></a>
 When an item in the table is modified, `StreamViewType` determines what information is written to the stream for this table. Valid values for `StreamViewType` are:
+ `KEYS_ONLY` - Only the key attributes of the modified item are written to the stream.
+ `NEW_IMAGE` - The entire item, as it appears after it was modified, is written to the stream.
+ `OLD_IMAGE` - The entire item, as it appeared before it was modified, is written to the stream.
+ `NEW_AND_OLD_IMAGES` - Both the new and the old item images of the item are written to the stream.
*Required*: No
*Type*: String
*Allowed values*: `KEYS_ONLY | NEW_IMAGE | OLD_IMAGE | NEW_AND_OLD_IMAGES`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableName`  <a name="cfn-dynamodb-stream-tablename"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-dynamodb-stream-return-values"></a>

### Ref
<a name="aws-resource-dynamodb-stream-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-dynamodb-stream-return-values-fn--getatt"></a>

####
<a name="aws-resource-dynamodb-stream-return-values-fn--getatt-fn--getatt"></a>

`CreationRequestDateTime`  <a name="CreationRequestDateTime-fn::getatt"></a>
Property description not available.

`KeySchema`  <a name="KeySchema-fn::getatt"></a>
Property description not available.

`StreamArn`  <a name="StreamArn-fn::getatt"></a>
The ARN for a specific Kinesis data stream.

`StreamLabel`  <a name="StreamLabel-fn::getatt"></a>
Property description not available.

`StreamStatus`  <a name="StreamStatus-fn::getatt"></a>
Property description not available.
