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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
