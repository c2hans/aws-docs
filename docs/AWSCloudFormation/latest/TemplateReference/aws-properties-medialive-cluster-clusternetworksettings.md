---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-cluster-clusternetworksettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Cluster ClusterNetworkSettings
<a name="aws-properties-medialive-cluster-clusternetworksettings"></a>

On-premises settings for the interface network mappings and default output logical interface.

## Syntax
<a name="aws-properties-medialive-cluster-clusternetworksettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-cluster-clusternetworksettings-syntax.json"></a>

```
{
  "[DefaultRoute](#cfn-medialive-cluster-clusternetworksettings-defaultroute)" : {{String}},
  "[InterfaceMappings](#cfn-medialive-cluster-clusternetworksettings-interfacemappings)" : {{[ InterfaceMapping, ... ]}}
}
```

### YAML
<a name="aws-properties-medialive-cluster-clusternetworksettings-syntax.yaml"></a>

```
  [DefaultRoute](#cfn-medialive-cluster-clusternetworksettings-defaultroute): {{String}}
  [InterfaceMappings](#cfn-medialive-cluster-clusternetworksettings-interfacemappings): {{
    - InterfaceMapping}}
```

## Properties
<a name="aws-properties-medialive-cluster-clusternetworksettings-properties"></a>

`DefaultRoute`  <a name="cfn-medialive-cluster-clusternetworksettings-defaultroute"></a>
The default route for the network. This value is used if you don't define a route in the channel output API.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InterfaceMappings`  <a name="cfn-medialive-cluster-clusternetworksettings-interfacemappings"></a>
Network mappings for the cluster.
*Required*: No
*Type*: Array of [InterfaceMapping](aws-properties-medialive-cluster-interfacemapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
