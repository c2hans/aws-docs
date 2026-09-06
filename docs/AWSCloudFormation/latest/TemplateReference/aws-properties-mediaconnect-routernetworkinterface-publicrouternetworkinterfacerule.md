---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfacerule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterNetworkInterface PublicRouterNetworkInterfaceRule
<a name="aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfacerule"></a>

A rule that allows a specific CIDR block to access the public router network interface.

## Syntax
<a name="aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfacerule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfacerule-syntax.json"></a>

```
{
  "[Cidr](#cfn-mediaconnect-routernetworkinterface-publicrouternetworkinterfacerule-cidr)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfacerule-syntax.yaml"></a>

```
  [Cidr](#cfn-mediaconnect-routernetworkinterface-publicrouternetworkinterfacerule-cidr): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfacerule-properties"></a>

`Cidr`  <a name="cfn-mediaconnect-routernetworkinterface-publicrouternetworkinterfacerule-cidr"></a>
The CIDR block that is allowed to access the public router network interface.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
