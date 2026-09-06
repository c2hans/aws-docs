---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-medialive-node.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Node
<a name="aws-resource-medialive-node"></a>

<a name="aws-resource-medialive-node-description"></a>The `AWS::MediaLive::Node` resource Property description not available. for MediaLive.

## Syntax
<a name="aws-resource-medialive-node-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-medialive-node-syntax.json"></a>

```
{
  "Type" : "AWS::MediaLive::Node",
  "Properties" : {
      "[ClusterId](#cfn-medialive-node-clusterid)" : {{String}},
      "[Name](#cfn-medialive-node-name)" : {{String}},
      "[NodeInterfaceMappings](#cfn-medialive-node-nodeinterfacemappings)" : {{[ NodeInterfaceMapping, ... ]}},
      "[Role](#cfn-medialive-node-role)" : {{String}},
      "[SdiSourceMappings](#cfn-medialive-node-sdisourcemappings)" : {{[ SdiSourceMapping, ... ]}},
      "[Tags](#cfn-medialive-node-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-medialive-node-syntax.yaml"></a>

```
Type: AWS::MediaLive::Node
Properties:
  [ClusterId](#cfn-medialive-node-clusterid): {{String}}
  [Name](#cfn-medialive-node-name): {{String}}
  [NodeInterfaceMappings](#cfn-medialive-node-nodeinterfacemappings): {{
    - NodeInterfaceMapping}}
  [Role](#cfn-medialive-node-role): {{String}}
  [SdiSourceMappings](#cfn-medialive-node-sdisourcemappings): {{
    - SdiSourceMapping}}
  [Tags](#cfn-medialive-node-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-medialive-node-properties"></a>

`ClusterId`  <a name="cfn-medialive-node-clusterid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-medialive-node-name"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NodeInterfaceMappings`  <a name="cfn-medialive-node-nodeinterfacemappings"></a>
Property description not available.
*Required*: No
*Type*: Array of [NodeInterfaceMapping](aws-properties-medialive-node-nodeinterfacemapping.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Role`  <a name="cfn-medialive-node-role"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `BACKUP | ACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SdiSourceMappings`  <a name="cfn-medialive-node-sdisourcemappings"></a>
Property description not available.
*Required*: No
*Type*: Array of [SdiSourceMapping](aws-properties-medialive-node-sdisourcemapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-medialive-node-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-medialive-node-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-medialive-node-return-values"></a>

### Ref
<a name="aws-resource-medialive-node-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-medialive-node-return-values-fn--getatt"></a>

####
<a name="aws-resource-medialive-node-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`ChannelPlacementGroups`  <a name="ChannelPlacementGroups-fn::getatt"></a>
Property description not available.

`ConnectionState`  <a name="ConnectionState-fn::getatt"></a>
Property description not available.

`InstanceArn`  <a name="InstanceArn-fn::getatt"></a>
Property description not available.

`State`  <a name="State-fn::getatt"></a>
Property description not available.
