---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-firewall-proxysettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::Firewall ProxySettings

The proxy settings of a proxy mode firewall: the ports and protocols on which the firewall's proxy listens for traffic, and optionally your own domain name and certificate.

## Syntax
<a name="aws-properties-networkfirewall-firewall-proxysettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-firewall-proxysettings-syntax.json"></a>

```json
{
  "[ListenerProperties](#cfn-networkfirewall-firewall-proxysettings-listenerproperties)" : {{[ ListenerProperty, ... ]}}
}
```

### YAML
<a name="aws-properties-networkfirewall-firewall-proxysettings-syntax.yaml"></a>

```yaml
  [ListenerProperties](#cfn-networkfirewall-firewall-proxysettings-listenerproperties): {{
    - ListenerProperty}}
```

## Properties
<a name="aws-properties-networkfirewall-firewall-proxysettings-properties"></a>

`ListenerProperties`  <a name="cfn-networkfirewall-firewall-proxysettings-listenerproperties"></a>
The listeners of the firewall's proxy. Specify at least one listener, and at most one HTTP listener and one HTTPS listener. Each listener needs a port from 1 to 65535, and the two listeners must use different ports.
If you don't specify listeners when you create the firewall, the firewall listens for HTTP on port 3128 and HTTPS on port 8443.
*Required*: No
*Type*: Array of [ListenerProperty](aws-properties-networkfirewall-firewall-listenerproperty.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
