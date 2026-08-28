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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
