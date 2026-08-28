---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-routeserverpeer-bgpoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::RouteServerPeer BgpOptions
<a name="aws-properties-ec2-routeserverpeer-bgpoptions"></a>

The BGP configuration options for this peer, including ASN (Autonomous System Number) and BFD (Bidrectional Forwarding Detection) settings.

## Syntax
<a name="aws-properties-ec2-routeserverpeer-bgpoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-routeserverpeer-bgpoptions-syntax.json"></a>

```
{
  "[PeerAsn](#cfn-ec2-routeserverpeer-bgpoptions-peerasn)" : {{Integer}},
  "[PeerLivenessDetection](#cfn-ec2-routeserverpeer-bgpoptions-peerlivenessdetection)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-routeserverpeer-bgpoptions-syntax.yaml"></a>

```
  [PeerAsn](#cfn-ec2-routeserverpeer-bgpoptions-peerasn): {{Integer}}
  [PeerLivenessDetection](#cfn-ec2-routeserverpeer-bgpoptions-peerlivenessdetection): {{String}}
```

## Properties
<a name="aws-properties-ec2-routeserverpeer-bgpoptions-properties"></a>

`PeerAsn`  <a name="cfn-ec2-routeserverpeer-bgpoptions-peerasn"></a>
The Border Gateway Protocol (BGP) Autonomous System Number (ASN) for the appliance. Valid values are from 1 to 4294967295. We recommend using a private ASN in the 64512–65534 (16-bit ASN) or 4200000000–4294967294 (32-bit ASN) range.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `4294967294`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerLivenessDetection`  <a name="cfn-ec2-routeserverpeer-bgpoptions-peerlivenessdetection"></a>
The liveness detection protocol used for the BGP peer.
The requested liveness detection protocol for the BGP peer.
+ `bgp-keepalive`: The standard BGP keep alive mechanism ([RFC4271](https://www.rfc-editor.org/rfc/rfc4271#page-21)) that is stable but may take longer to fail-over in cases of network impact or router failure.
+ `bfd`: An additional Bidirectional Forwarding Detection (BFD) protocol ([RFC5880](https://www.rfc-editor.org/rfc/rfc5880)) that enables fast failover by using more sensitive liveness detection.
Defaults to `bgp-keepalive`.
*Required*: No
*Type*: String
*Allowed values*: `bfd | bgp-keepalive`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
