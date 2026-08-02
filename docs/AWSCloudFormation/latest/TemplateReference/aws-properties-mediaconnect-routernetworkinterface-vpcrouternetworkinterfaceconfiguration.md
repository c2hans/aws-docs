---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterNetworkInterface VpcRouterNetworkInterfaceConfiguration
<a name="aws-properties-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration"></a>

The configuration settings for a router network interface within a VPC, including the security group IDs and subnet ID.

## Syntax
<a name="aws-properties-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetId](#cfn-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration-subnetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration-securitygroupids): {{
    - String}}
  [SubnetId](#cfn-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration-subnetid): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration-properties"></a>

`SecurityGroupIds`  <a name="cfn-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration-securitygroupids"></a>
The IDs of the security groups to associate with the router network interface within the VPC.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration-subnetid"></a>
The ID of the subnet within the VPC to associate the router network interface with.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
