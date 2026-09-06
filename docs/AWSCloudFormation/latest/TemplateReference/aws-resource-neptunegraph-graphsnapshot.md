---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-neptunegraph-graphsnapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NeptuneGraph::GraphSnapshot
<a name="aws-resource-neptunegraph-graphsnapshot"></a>

<a name="aws-resource-neptunegraph-graphsnapshot-description"></a>The `AWS::NeptuneGraph::GraphSnapshot` resource Property description not available. for NeptuneGraph.

## Syntax
<a name="aws-resource-neptunegraph-graphsnapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-neptunegraph-graphsnapshot-syntax.json"></a>

```
{
  "Type" : "AWS::NeptuneGraph::GraphSnapshot",
  "Properties" : {
      "[GraphIdentifier](#cfn-neptunegraph-graphsnapshot-graphidentifier)" : {{String}},
      "[SnapshotName](#cfn-neptunegraph-graphsnapshot-snapshotname)" : {{String}},
      "[Tags](#cfn-neptunegraph-graphsnapshot-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-neptunegraph-graphsnapshot-syntax.yaml"></a>

```
Type: AWS::NeptuneGraph::GraphSnapshot
Properties:
  [GraphIdentifier](#cfn-neptunegraph-graphsnapshot-graphidentifier): {{String}}
  [SnapshotName](#cfn-neptunegraph-graphsnapshot-snapshotname): {{String}}
  [Tags](#cfn-neptunegraph-graphsnapshot-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-neptunegraph-graphsnapshot-properties"></a>

`GraphIdentifier`  <a name="cfn-neptunegraph-graphsnapshot-graphidentifier"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^g-[a-z0-9]{10}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotName`  <a name="cfn-neptunegraph-graphsnapshot-snapshotname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!gs-)[a-z][a-z0-9]*(-[a-z0-9]+)*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-neptunegraph-graphsnapshot-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-neptunegraph-graphsnapshot-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-neptunegraph-graphsnapshot-return-values"></a>

### Ref
<a name="aws-resource-neptunegraph-graphsnapshot-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-neptunegraph-graphsnapshot-return-values-fn--getatt"></a>

####
<a name="aws-resource-neptunegraph-graphsnapshot-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the graph snapshot.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the graph snapshot.

`KmsKeyIdentifier`  <a name="KmsKeyIdentifier-fn::getatt"></a>
The ID of the KMS key used to encrypt and decrypt the snapshot.

`SnapshotCreateTime`  <a name="SnapshotCreateTime-fn::getatt"></a>
The time when the snapshot was created.

`Status`  <a name="Status-fn::getatt"></a>
The status of the graph snapshot.
