---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-firewallpolicy-flowtimeouts.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::FirewallPolicy FlowTimeouts
<a name="aws-properties-networkfirewall-firewallpolicy-flowtimeouts"></a>

Describes the amount of time that can pass without any traffic sent through the firewall before the firewall determines that the connection is idle and Network Firewall removes the flow entry from its flow table. When you update this value, existing connections will be treated according to your stream exception policy configuration.

## Syntax
<a name="aws-properties-networkfirewall-firewallpolicy-flowtimeouts-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-firewallpolicy-flowtimeouts-syntax.json"></a>

```
{
  "[TcpIdleTimeoutSeconds](#cfn-networkfirewall-firewallpolicy-flowtimeouts-tcpidletimeoutseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-networkfirewall-firewallpolicy-flowtimeouts-syntax.yaml"></a>

```
  [TcpIdleTimeoutSeconds](#cfn-networkfirewall-firewallpolicy-flowtimeouts-tcpidletimeoutseconds): {{Integer}}
```

## Properties
<a name="aws-properties-networkfirewall-firewallpolicy-flowtimeouts-properties"></a>

`TcpIdleTimeoutSeconds`  <a name="cfn-networkfirewall-firewallpolicy-flowtimeouts-tcpidletimeoutseconds"></a>
The number of seconds that can pass without any TCP traffic sent through the firewall before the firewall determines that the connection is idle. After the idle timeout passes, data packets are dropped, however, the next TCP SYN packet is considered a new flow and is processed by the firewall. Clients or targets can use TCP keepalive packets to reset the idle timeout.
You can define the `TcpIdleTimeoutSeconds` value to be between 60 and 6000 seconds. If no value is provided, it defaults to 350 seconds.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `6000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
