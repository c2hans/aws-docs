---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-firewall-proxysettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::Firewall ProxySettings
<a name="aws-properties-networkfirewall-firewall-proxysettings"></a>

The listener configuration for a proxy mode firewall. This specifies the ports and protocols on which the firewall's proxy listens for traffic.

## Syntax
<a name="aws-properties-networkfirewall-firewall-proxysettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-firewall-proxysettings-syntax.json"></a>

```
{
  "[ListenerProperties](#cfn-networkfirewall-firewall-proxysettings-listenerproperties)" : {{[ ListenerProperty, ... ]}}
}
```

### YAML
<a name="aws-properties-networkfirewall-firewall-proxysettings-syntax.yaml"></a>

```
  [ListenerProperties](#cfn-networkfirewall-firewall-proxysettings-listenerproperties): {{
    - ListenerProperty}}
```

## Properties
<a name="aws-properties-networkfirewall-firewall-proxysettings-properties"></a>

`ListenerProperties`  <a name="cfn-networkfirewall-firewall-proxysettings-listenerproperties"></a>
Listener properties for HTTP and HTTPS traffic.
*Required*: No
*Type*: Array of [ListenerProperty](aws-properties-networkfirewall-firewall-listenerproperty.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
