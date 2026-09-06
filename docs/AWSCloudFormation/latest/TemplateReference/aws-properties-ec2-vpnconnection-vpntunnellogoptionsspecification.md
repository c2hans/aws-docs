---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-vpnconnection-vpntunnellogoptionsspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPNConnection VpnTunnelLogOptionsSpecification
<a name="aws-properties-ec2-vpnconnection-vpntunnellogoptionsspecification"></a>

Options for logging VPN tunnel activity.

## Syntax
<a name="aws-properties-ec2-vpnconnection-vpntunnellogoptionsspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-vpnconnection-vpntunnellogoptionsspecification-syntax.json"></a>

```
{
  "[CloudwatchLogOptions](#cfn-ec2-vpnconnection-vpntunnellogoptionsspecification-cloudwatchlogoptions)" : {{CloudwatchLogOptionsSpecification}}
}
```

### YAML
<a name="aws-properties-ec2-vpnconnection-vpntunnellogoptionsspecification-syntax.yaml"></a>

```
  [CloudwatchLogOptions](#cfn-ec2-vpnconnection-vpntunnellogoptionsspecification-cloudwatchlogoptions): {{
    CloudwatchLogOptionsSpecification}}
```

## Properties
<a name="aws-properties-ec2-vpnconnection-vpntunnellogoptionsspecification-properties"></a>

`CloudwatchLogOptions`  <a name="cfn-ec2-vpnconnection-vpntunnellogoptionsspecification-cloudwatchlogoptions"></a>
Options for sending VPN tunnel logs to CloudWatch.
*Required*: No
*Type*: [CloudwatchLogOptionsSpecification](aws-properties-ec2-vpnconnection-cloudwatchlogoptionsspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
