---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-connectiontrackingspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate ConnectionTrackingSpecification
<a name="aws-properties-ec2-launchtemplate-connectiontrackingspecification"></a>

A security group connection tracking specification that enables you to set the idle timeout for connection tracking on an Elastic network interface. For more information, see [Connection tracking timeouts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts) in the *Amazon EC2 User Guide*.

## Syntax
<a name="aws-properties-ec2-launchtemplate-connectiontrackingspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-connectiontrackingspecification-syntax.json"></a>

```
{
  "[TcpEstablishedTimeout](#cfn-ec2-launchtemplate-connectiontrackingspecification-tcpestablishedtimeout)" : {{Integer}},
  "[UdpStreamTimeout](#cfn-ec2-launchtemplate-connectiontrackingspecification-udpstreamtimeout)" : {{Integer}},
  "[UdpTimeout](#cfn-ec2-launchtemplate-connectiontrackingspecification-udptimeout)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-connectiontrackingspecification-syntax.yaml"></a>

```
  [TcpEstablishedTimeout](#cfn-ec2-launchtemplate-connectiontrackingspecification-tcpestablishedtimeout): {{Integer}}
  [UdpStreamTimeout](#cfn-ec2-launchtemplate-connectiontrackingspecification-udpstreamtimeout): {{Integer}}
  [UdpTimeout](#cfn-ec2-launchtemplate-connectiontrackingspecification-udptimeout): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-connectiontrackingspecification-properties"></a>

`TcpEstablishedTimeout`  <a name="cfn-ec2-launchtemplate-connectiontrackingspecification-tcpestablishedtimeout"></a>
Timeout (in seconds) for idle TCP connections in an established state. Min: 60 seconds. Max: 432000 seconds (5 days). Default: 350 seconds for Nitro v6 instance types (excluding P6e-GB200); 432000 seconds for all other instance types (including P6e-GB200). Recommended: Less than 432000 seconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UdpStreamTimeout`  <a name="cfn-ec2-launchtemplate-connectiontrackingspecification-udpstreamtimeout"></a>
Timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction. Min: 60 seconds. Max: 180 seconds (3 minutes). Default: 180 seconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UdpTimeout`  <a name="cfn-ec2-launchtemplate-connectiontrackingspecification-udptimeout"></a>
Timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction. Min: 30 seconds. Max: 60 seconds. Default: 30 seconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
