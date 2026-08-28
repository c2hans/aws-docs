---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-medialive-channelplacementgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::ChannelPlacementGroup
<a name="aws-resource-medialive-channelplacementgroup"></a>

Creates a channel placement group in a cluster. A channel placement group lets you control which cluster nodes run specific channels.

## Syntax
<a name="aws-resource-medialive-channelplacementgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-medialive-channelplacementgroup-syntax.json"></a>

```
{
  "Type" : "AWS::MediaLive::ChannelPlacementGroup",
  "Properties" : {
      "[ClusterId](#cfn-medialive-channelplacementgroup-clusterid)" : {{String}},
      "[Name](#cfn-medialive-channelplacementgroup-name)" : {{String}},
      "[Nodes](#cfn-medialive-channelplacementgroup-nodes)" : {{[ String, ... ]}},
      "[Tags](#cfn-medialive-channelplacementgroup-tags)" : {{[ Tags, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-medialive-channelplacementgroup-syntax.yaml"></a>

```
Type: AWS::MediaLive::ChannelPlacementGroup
Properties:
  [ClusterId](#cfn-medialive-channelplacementgroup-clusterid): {{String}}
  [Name](#cfn-medialive-channelplacementgroup-name): {{String}}
  [Nodes](#cfn-medialive-channelplacementgroup-nodes): {{
    - String}}
  [Tags](#cfn-medialive-channelplacementgroup-tags): {{
    - Tags}}
```

## Properties
<a name="aws-resource-medialive-channelplacementgroup-properties"></a>

`ClusterId`  <a name="cfn-medialive-channelplacementgroup-clusterid"></a>
The ID of the cluster the channel placement group belongs to.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-medialive-channelplacementgroup-name"></a>
The name of the channel placement group.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Nodes`  <a name="cfn-medialive-channelplacementgroup-nodes"></a>
List of nodes added to the channel placement group.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-medialive-channelplacementgroup-tags"></a>
Property description not available.
*Required*: No
*Type*: [Array](aws-properties-medialive-channelplacementgroup-tags.md) of [Tags](aws-properties-medialive-channelplacementgroup-tags.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-medialive-channelplacementgroup-return-values"></a>

### Ref
<a name="aws-resource-medialive-channelplacementgroup-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-medialive-channelplacementgroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-medialive-channelplacementgroup-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the channel placement group.

`Channels`  <a name="Channels-fn::getatt"></a>
List of channel IDs added to the channel placement group.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the channel placement group.

`State`  <a name="State-fn::getatt"></a>
The current state of the channel placement group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
