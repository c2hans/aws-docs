---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-medialive-cluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Cluster
<a name="aws-resource-medialive-cluster"></a>

Creates a cluster. A cluster is a group of nodes that work together to run MediaLive channels on your own hardware.

## Syntax
<a name="aws-resource-medialive-cluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-medialive-cluster-syntax.json"></a>

```
{
  "Type" : "AWS::MediaLive::Cluster",
  "Properties" : {
      "[ClusterType](#cfn-medialive-cluster-clustertype)" : {{String}},
      "[InstanceRoleArn](#cfn-medialive-cluster-instancerolearn)" : {{String}},
      "[Name](#cfn-medialive-cluster-name)" : {{String}},
      "[NetworkSettings](#cfn-medialive-cluster-networksettings)" : {{ClusterNetworkSettings}},
      "[Tags](#cfn-medialive-cluster-tags)" : {{[ Tags, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-medialive-cluster-syntax.yaml"></a>

```
Type: AWS::MediaLive::Cluster
Properties:
  [ClusterType](#cfn-medialive-cluster-clustertype): {{String}}
  [InstanceRoleArn](#cfn-medialive-cluster-instancerolearn): {{String}}
  [Name](#cfn-medialive-cluster-name): {{String}}
  [NetworkSettings](#cfn-medialive-cluster-networksettings): {{
    ClusterNetworkSettings}}
  [Tags](#cfn-medialive-cluster-tags): {{
    - Tags}}
```

## Properties
<a name="aws-resource-medialive-cluster-properties"></a>

`ClusterType`  <a name="cfn-medialive-cluster-clustertype"></a>
The hardware type for the cluster.
*Required*: No
*Type*: String
*Allowed values*: `ON_PREMISES | OUTPOSTS_RACK | OUTPOSTS_SERVER | EC2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceRoleArn`  <a name="cfn-medialive-cluster-instancerolearn"></a>
The IAM role your nodes will use.
*Required*: No
*Type*: String
*Pattern*: `^arn:.+:iam:.+:role/.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-medialive-cluster-name"></a>
The user-specified name of the cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkSettings`  <a name="cfn-medialive-cluster-networksettings"></a>
On-premises network settings for the cluster.
*Required*: No
*Type*: [ClusterNetworkSettings](aws-properties-medialive-cluster-clusternetworksettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-medialive-cluster-tags"></a>
Property description not available.
*Required*: No
*Type*: [Array](aws-properties-medialive-cluster-tags.md) of [Tags](aws-properties-medialive-cluster-tags.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-medialive-cluster-return-values"></a>

### Ref
<a name="aws-resource-medialive-cluster-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-medialive-cluster-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-medialive-cluster-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the cluster.

`ChannelIds`  <a name="ChannelIds-fn::getatt"></a>
The MediaLive channels that are currently running on nodes in this cluster.

`Id`  <a name="Id-fn::getatt"></a>
The unique ID of the cluster.

`State`  <a name="State-fn::getatt"></a>
The current state of the cluster.
