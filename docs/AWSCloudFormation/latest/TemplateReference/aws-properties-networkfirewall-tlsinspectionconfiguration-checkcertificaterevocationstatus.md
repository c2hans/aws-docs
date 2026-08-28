---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::TLSInspectionConfiguration CheckCertificateRevocationStatus
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus"></a>

When enabled, Network Firewall checks if the server certificate presented by the server in the SSL/TLS connection has a revoked or unkown status. If the certificate has an unknown or revoked status, you must specify the actions that Network Firewall takes on outbound traffic. To check the certificate revocation status, you must also specify a `CertificateAuthorityArn` in [ServerCertificateConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkfirewall-servercertificateconfiguration.html).

## Syntax
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus-syntax.json"></a>

```
{
  "[RevokedStatusAction](#cfn-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus-revokedstatusaction)" : {{String}},
  "[UnknownStatusAction](#cfn-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus-unknownstatusaction)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus-syntax.yaml"></a>

```
  [RevokedStatusAction](#cfn-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus-revokedstatusaction): {{String}}
  [UnknownStatusAction](#cfn-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus-unknownstatusaction): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus-properties"></a>

`RevokedStatusAction`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus-revokedstatusaction"></a>
Configures how Network Firewall processes traffic when it determines that the certificate presented by the server in the SSL/TLS connection has a revoked status.
+ **PASS** - Allow the connection to continue, and pass subsequent packets to the stateful engine for inspection.
+ **DROP** - Network Firewall closes the connection and drops subsequent packets for that connection.
+ **REJECT** - Network Firewall sends a TCP reject packet back to your client. The service closes the connection and drops subsequent packets for that connection. `REJECT` is available only for TCP traffic.
*Required*: No
*Type*: String
*Allowed values*: `PASS | DROP | REJECT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnknownStatusAction`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus-unknownstatusaction"></a>
Configures how Network Firewall processes traffic when it determines that the certificate presented by the server in the SSL/TLS connection has an unknown status, or a status that cannot be determined for any other reason, including when the service is unable to connect to the OCSP and CRL endpoints for the certificate.
+ **PASS** - Allow the connection to continue, and pass subsequent packets to the stateful engine for inspection.
+ **DROP** - Network Firewall closes the connection and drops subsequent packets for that connection.
+ **REJECT** - Network Firewall sends a TCP reject packet back to your client. The service closes the connection and drops subsequent packets for that connection. `REJECT` is available only for TCP traffic.
*Required*: No
*Type*: String
*Allowed values*: `PASS | DROP | REJECT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
