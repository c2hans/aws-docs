---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-networkinterface-connectiontrackingspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInterface ConnectionTrackingSpecification
<a name="aws-properties-ec2-networkinterface-connectiontrackingspecification"></a>

Configurable options for connection tracking on a network interface. For more information, see [Connection tracking timeouts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts) in the *Amazon Elastic Compute Cloud User Guide*.

## Syntax
<a name="aws-properties-ec2-networkinterface-connectiontrackingspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-networkinterface-connectiontrackingspecification-syntax.json"></a>

```
{
  "[TcpEstablishedTimeout](#cfn-ec2-networkinterface-connectiontrackingspecification-tcpestablishedtimeout)" : {{Integer}},
  "[UdpStreamTimeout](#cfn-ec2-networkinterface-connectiontrackingspecification-udpstreamtimeout)" : {{Integer}},
  "[UdpTimeout](#cfn-ec2-networkinterface-connectiontrackingspecification-udptimeout)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-networkinterface-connectiontrackingspecification-syntax.yaml"></a>

```
  [TcpEstablishedTimeout](#cfn-ec2-networkinterface-connectiontrackingspecification-tcpestablishedtimeout): {{Integer}}
  [UdpStreamTimeout](#cfn-ec2-networkinterface-connectiontrackingspecification-udpstreamtimeout): {{Integer}}
  [UdpTimeout](#cfn-ec2-networkinterface-connectiontrackingspecification-udptimeout): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-networkinterface-connectiontrackingspecification-properties"></a>

`TcpEstablishedTimeout`  <a name="cfn-ec2-networkinterface-connectiontrackingspecification-tcpestablishedtimeout"></a>
Timeout (in seconds) for idle TCP connections in an established state. Min: 60 seconds. Max: 432000 seconds (5 days). Default: 350 seconds for Nitro v6 instance types (excluding P6e-GB200); 432000 seconds for all other instance types (including P6e-GB200). Recommended: Less than 432000 seconds.
*Required*: No
*Type*: Integer
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`UdpStreamTimeout`  <a name="cfn-ec2-networkinterface-connectiontrackingspecification-udpstreamtimeout"></a>
Timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction. Min: 60 seconds. Max: 180 seconds (3 minutes). Default: 180 seconds.
*Required*: No
*Type*: Integer
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`UdpTimeout`  <a name="cfn-ec2-networkinterface-connectiontrackingspecification-udptimeout"></a>
Timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction. Min: 30 seconds. Max: 60 seconds. Default: 30 seconds.
*Required*: No
*Type*: Integer
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
