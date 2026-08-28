---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::TLSInspectionConfiguration ServerCertificate
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificate"></a>

Any AWS Certificate Manager (ACM) Secure Sockets Layer/Transport Layer Security (SSL/TLS) server certificate that's associated with a [ServerCertificateConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificateconfiguration.html). Used in a [TLSInspectionConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkfirewall-tlsinspectionconfiguration.html) for inspection of inbound traffic to your firewall. You must request or import a SSL/TLS certificate into ACM for each domain Network Firewall needs to decrypt and inspect. AWS Network Firewall uses the SSL/TLS certificates to decrypt specified inbound SSL/TLS traffic going to your firewall. For information about working with certificates in AWS Certificate Manager, see [Request a public certificate ](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html) or [Importing certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *AWS Certificate Manager User Guide*.

## Syntax
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificate-syntax.json"></a>

```
{
  "[ResourceArn](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificate-resourcearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificate-syntax.yaml"></a>

```
  [ResourceArn](#cfn-networkfirewall-tlsinspectionconfiguration-servercertificate-resourcearn): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-tlsinspectionconfiguration-servercertificate-properties"></a>

`ResourceArn`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-servercertificate-resourcearn"></a>
The Amazon Resource Name (ARN) of the AWS Certificate Manager SSL/TLS server certificate that's used for inbound SSL/TLS inspection.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws.*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
