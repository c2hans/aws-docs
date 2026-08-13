---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cassandra-stream.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Stream
<a name="aws-resource-cassandra-stream"></a>

<a name="aws-resource-cassandra-stream-description"></a>The `AWS::Cassandra::Stream` resource Property description not available. for Cassandra.

## Syntax
<a name="aws-resource-cassandra-stream-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cassandra-stream-syntax.json"></a>

```
{
  "Type" : "AWS::Cassandra::Stream",
  "Properties" : {
      "[KeyspaceName](#cfn-cassandra-stream-keyspacename)" : {{String}},
      "[StreamViewType](#cfn-cassandra-stream-streamviewtype)" : {{String}},
      "[TableName](#cfn-cassandra-stream-tablename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cassandra-stream-syntax.yaml"></a>

```
Type: AWS::Cassandra::Stream
Properties:
  [KeyspaceName](#cfn-cassandra-stream-keyspacename): {{String}}
  [StreamViewType](#cfn-cassandra-stream-streamviewtype): {{String}}
  [TableName](#cfn-cassandra-stream-tablename): {{String}}
```

## Properties
<a name="aws-resource-cassandra-stream-properties"></a>

`KeyspaceName`  <a name="cfn-cassandra-stream-keyspacename"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_]{0,47}$`
*Minimum*: `1`
*Maximum*: `48`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StreamViewType`  <a name="cfn-cassandra-stream-streamviewtype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `NEW_IMAGE | OLD_IMAGE | NEW_AND_OLD_IMAGES | KEYS_ONLY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableName`  <a name="cfn-cassandra-stream-tablename"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_]{0,47}$`
*Minimum*: `1`
*Maximum*: `48`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cassandra-stream-return-values"></a>

### Ref
<a name="aws-resource-cassandra-stream-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cassandra-stream-return-values-fn--getatt"></a>

####
<a name="aws-resource-cassandra-stream-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreationRequestDateTime`  <a name="CreationRequestDateTime-fn::getatt"></a>
Property description not available.

`StreamLabel`  <a name="StreamLabel-fn::getatt"></a>
Property description not available.

`StreamStatus`  <a name="StreamStatus-fn::getatt"></a>
Property description not available.
