---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-cluster-interfacemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Cluster InterfaceMapping
<a name="aws-properties-medialive-cluster-interfacemapping"></a>

Network mappings for the cluster.

## Syntax
<a name="aws-properties-medialive-cluster-interfacemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-cluster-interfacemapping-syntax.json"></a>

```
{
  "[LogicalInterfaceName](#cfn-medialive-cluster-interfacemapping-logicalinterfacename)" : {{String}},
  "[NetworkId](#cfn-medialive-cluster-interfacemapping-networkid)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-cluster-interfacemapping-syntax.yaml"></a>

```
  [LogicalInterfaceName](#cfn-medialive-cluster-interfacemapping-logicalinterfacename): {{String}}
  [NetworkId](#cfn-medialive-cluster-interfacemapping-networkid): {{String}}
```

## Properties
<a name="aws-properties-medialive-cluster-interfacemapping-properties"></a>

`LogicalInterfaceName`  <a name="cfn-medialive-cluster-interfacemapping-logicalinterfacename"></a>
The logical interface name, unique in the list.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkId`  <a name="cfn-medialive-cluster-interfacemapping-networkid"></a>
The network ID to be associated with the logical interface name.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
