---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterNetworkInterface RouterNetworkInterfaceConfiguration
<a name="aws-properties-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration"></a>

The configuration settings for a router network interface.

## Syntax
<a name="aws-properties-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration-syntax.json"></a>

```
{
  "[Public](#cfn-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration-public)" : {{PublicRouterNetworkInterfaceConfiguration}},
  "[Vpc](#cfn-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration-vpc)" : {{VpcRouterNetworkInterfaceConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration-syntax.yaml"></a>

```
  [Public](#cfn-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration-public): {{
    PublicRouterNetworkInterfaceConfiguration}}
  [Vpc](#cfn-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration-vpc): {{
    VpcRouterNetworkInterfaceConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration-properties"></a>

`Public`  <a name="cfn-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration-public"></a>
The configuration settings for a public router network interface, including the list of allowed CIDR blocks.
*Required*: No
*Type*: [PublicRouterNetworkInterfaceConfiguration](aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfaceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Vpc`  <a name="cfn-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration-vpc"></a>
The configuration settings for a router network interface within a VPC, including the security group IDs and subnet ID.
*Required*: No
*Type*: [VpcRouterNetworkInterfaceConfiguration](aws-properties-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
