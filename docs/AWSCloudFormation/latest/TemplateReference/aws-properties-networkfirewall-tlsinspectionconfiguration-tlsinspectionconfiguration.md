---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::TLSInspectionConfiguration TLSInspectionConfiguration
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration"></a>

The object that defines a TLS inspection configuration. This defines the TLS inspection configuration.

AWS Network Firewall uses a TLS inspection configuration to decrypt traffic. Network Firewall re-encrypts the traffic before sending it to its destination.

To use a TLS inspection configuration, you add it to a new Network Firewall firewall policy, then you apply the firewall policy to a firewall. Network Firewall acts as a proxy service to decrypt and inspect the traffic traveling through your firewalls. You can reference a TLS inspection configuration from more than one firewall policy, and you can use a firewall policy in more than one firewall. For more information about using TLS inspection configurations, see [Inspecting SSL/TLS traffic with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html) in the *AWS Network Firewall Developer Guide*.

## Syntax
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration-syntax.json"></a>

```
{
  "[ServerCertificateConfigurations](#cfn-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration-servercertificateconfigurations)" : {{[ ServerCertificateConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration-syntax.yaml"></a>

```
  [ServerCertificateConfigurations](#cfn-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration-servercertificateconfigurations): {{
    - ServerCertificateConfiguration}}
```

## Properties
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration-properties"></a>

`ServerCertificateConfigurations`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration-servercertificateconfigurations"></a>
Lists the server certificate configurations that are associated with the TLS configuration.
*Required*: No
*Type*: Array of [ServerCertificateConfiguration](aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
