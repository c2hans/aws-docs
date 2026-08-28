---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::TLSInspectionConfiguration ServerCertificateConfiguration
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration"></a>

Configures the AWS Certificate Manager certificates and scope that Network Firewall uses to decrypt and re-encrypt traffic using a [TLSInspectionConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkfirewall-tlsinspectionconfiguration.html). You can configure `ServerCertificates` for inbound SSL/TLS inspection, a `CertificateAuthorityArn` for outbound SSL/TLS inspection, or both. For information about working with certificates for TLS inspection, see [ Using SSL/TLS server certficiates with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-certificate-requirements.html) in the *AWS Network Firewall Developer Guide*.

**Note**
If a server certificate that's associated with your [TLSInspectionConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkfirewall-tlsinspectionconfiguration.html) is revoked, deleted, or expired it can result in client-side TLS errors.

## Syntax
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-syntax.json"></a>

```
{
  "[CertificateAuthorityArn](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-certificateauthorityarn)" : {{String}},
  "[CheckCertificateRevocationStatus](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-checkcertificaterevocationstatus)" : {{CheckCertificateRevocationStatus}},
  "[Scopes](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-scopes)" : {{[ ServerCertificateScope, ... ]}},
  "[ServerCertificates](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-servercertificates)" : {{[ ServerCertificate, ... ]}}
}
```

### YAML
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-syntax.yaml"></a>

```
  [CertificateAuthorityArn](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-certificateauthorityarn): {{String}}
  [CheckCertificateRevocationStatus](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-checkcertificaterevocationstatus): {{
    CheckCertificateRevocationStatus}}
  [Scopes](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-scopes): {{
    - ServerCertificateScope}}
  [ServerCertificates](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-servercertificates): {{
    - ServerCertificate}}
```

## Properties
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-properties"></a>

`CertificateAuthorityArn`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-certificateauthorityarn"></a>
The Amazon Resource Name (ARN) of the imported certificate authority (CA) certificate within AWS Certificate Manager (ACM) to use for outbound SSL/TLS inspection.
The following limitations apply:
+ You can use CA certificates that you imported into ACM, but you can't generate CA certificates with ACM.
+ You can't use certificates issued by AWS Private Certificate Authority.
For more information about configuring certificates for outbound inspection, see [Using SSL/TLS certificates with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-certificate-requirements.html) in the *AWS Network Firewall Developer Guide*.
For information about working with certificates in ACM, see [Importing certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *AWS Certificate Manager User Guide*.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws.*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CheckCertificateRevocationStatus`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-checkcertificaterevocationstatus"></a>
When enabled, Network Firewall checks if the server certificate presented by the server in the SSL/TLS connection has a revoked or unkown status. If the certificate has an unknown or revoked status, you must specify the actions that Network Firewall takes on outbound traffic. To check the certificate revocation status, you must also specify a `CertificateAuthorityArn` in [ServerCertificateConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkfirewall-servercertificateconfiguration.html).
*Required*: No
*Type*: [CheckCertificateRevocationStatus](aws-properties-networkfirewall-tlsinspectionconfiguration-checkcertificaterevocationstatus.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scopes`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-scopes"></a>
A list of scopes.
*Required*: No
*Type*: Array of [ServerCertificateScope](aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificatescope.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerCertificates`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration-servercertificates"></a>
The list of server certificates to use for inbound SSL/TLS inspection.
*Required*: No
*Type*: Array of [ServerCertificate](aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
