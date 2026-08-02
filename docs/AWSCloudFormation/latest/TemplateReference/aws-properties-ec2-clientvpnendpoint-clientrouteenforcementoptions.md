---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-clientvpnendpoint-clientrouteenforcementoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ClientVpnEndpoint ClientRouteEnforcementOptions
<a name="aws-properties-ec2-clientvpnendpoint-clientrouteenforcementoptions"></a>

Client Route Enforcement is a feature of Client VPN that helps enforce administrator defined routes on devices connected through the VPN. This feature helps improve your security posture by ensuring that network traffic originating from a connected client is not inadvertently sent outside the VPN tunnel.

Client Route Enforcement works by monitoring the route table of a connected device for routing policy changes to the VPN connection. If the feature detects any VPN routing policy modifications, it will automatically force an update to the route table, reverting it back to the expected route configurations.

## Syntax
<a name="aws-properties-ec2-clientvpnendpoint-clientrouteenforcementoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-clientvpnendpoint-clientrouteenforcementoptions-syntax.json"></a>

```
{
  "[Enforced](#cfn-ec2-clientvpnendpoint-clientrouteenforcementoptions-enforced)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ec2-clientvpnendpoint-clientrouteenforcementoptions-syntax.yaml"></a>

```
  [Enforced](#cfn-ec2-clientvpnendpoint-clientrouteenforcementoptions-enforced): {{Boolean}}
```

## Properties
<a name="aws-properties-ec2-clientvpnendpoint-clientrouteenforcementoptions-properties"></a>

`Enforced`  <a name="cfn-ec2-clientvpnendpoint-clientrouteenforcementoptions-enforced"></a>
Enable or disable Client Route Enforcement. The state can either be `true` (enabled) or `false` (disabled). The default is `false`.
Valid values: `true | false`
Default value: `false`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
