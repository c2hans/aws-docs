---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfaceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterNetworkInterface PublicRouterNetworkInterfaceConfiguration
<a name="aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfaceconfiguration"></a>

The configuration settings for a public router network interface, including the list of allowed CIDR blocks.

## Syntax
<a name="aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfaceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfaceconfiguration-syntax.json"></a>

```
{
  "[AllowRules](#cfn-mediaconnect-routernetworkinterface-publicrouternetworkinterfaceconfiguration-allowrules)" : {{[ PublicRouterNetworkInterfaceRule, ... ]}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfaceconfiguration-syntax.yaml"></a>

```
  [AllowRules](#cfn-mediaconnect-routernetworkinterface-publicrouternetworkinterfaceconfiguration-allowrules): {{
    - PublicRouterNetworkInterfaceRule}}
```

## Properties
<a name="aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfaceconfiguration-properties"></a>

`AllowRules`  <a name="cfn-mediaconnect-routernetworkinterface-publicrouternetworkinterfaceconfiguration-allowrules"></a>
The list of allowed CIDR blocks for the public router network interface.
*Required*: Yes
*Type*: Array of [PublicRouterNetworkInterfaceRule](aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfacerule.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
