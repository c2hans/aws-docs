---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codeconnections-host-vpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeConnections::Host VpcConfiguration
<a name="aws-properties-codeconnections-host-vpcconfiguration"></a>

The VPC configuration provisioned for the host.

## Syntax
<a name="aws-properties-codeconnections-host-vpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codeconnections-host-vpcconfiguration-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-codeconnections-host-vpcconfiguration-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-codeconnections-host-vpcconfiguration-subnetids)" : {{[ String, ... ]}},
  "[TlsCertificate](#cfn-codeconnections-host-vpcconfiguration-tlscertificate)" : {{String}},
  "[VpcId](#cfn-codeconnections-host-vpcconfiguration-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-codeconnections-host-vpcconfiguration-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-codeconnections-host-vpcconfiguration-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-codeconnections-host-vpcconfiguration-subnetids): {{
    - String}}
  [TlsCertificate](#cfn-codeconnections-host-vpcconfiguration-tlscertificate): {{String}}
  [VpcId](#cfn-codeconnections-host-vpcconfiguration-vpcid): {{String}}
```

## Properties
<a name="aws-properties-codeconnections-host-vpcconfiguration-properties"></a>

`SecurityGroupIds`  <a name="cfn-codeconnections-host-vpcconfiguration-securitygroupids"></a>
The ID of the security group or security groups associated with the Amazon VPC connected to the infrastructure where your provider type is installed.
*Required*: Yes
*Type*: Array of String
*Minimum*: `11 | 1`
*Maximum*: `20 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-codeconnections-host-vpcconfiguration-subnetids"></a>
The ID of the subnet or subnets associated with the Amazon VPC connected to the infrastructure where your provider type is installed.
*Required*: Yes
*Type*: Array of String
*Minimum*: `15 | 1`
*Maximum*: `24 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TlsCertificate`  <a name="cfn-codeconnections-host-vpcconfiguration-tlscertificate"></a>
The value of the Transport Layer Security (TLS) certificate associated with the infrastructure where your provider type is installed.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `16384`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-codeconnections-host-vpcconfiguration-vpcid"></a>
The ID of the Amazon VPC connected to the infrastructure where your provider type is installed.
*Required*: Yes
*Type*: String
*Pattern*: `^vpc-\w{8}(\w{9})?$`
*Minimum*: `12`
*Maximum*: `21`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
