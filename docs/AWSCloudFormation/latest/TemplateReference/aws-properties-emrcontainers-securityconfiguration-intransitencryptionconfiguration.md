---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-intransitencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration InTransitEncryptionConfiguration
<a name="aws-properties-emrcontainers-securityconfiguration-intransitencryptionconfiguration"></a>

Configurations related to in-transit encryption for the security configuration.

## Syntax
<a name="aws-properties-emrcontainers-securityconfiguration-intransitencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-securityconfiguration-intransitencryptionconfiguration-syntax.json"></a>

```
{
  "[TLSCertificateConfiguration](#cfn-emrcontainers-securityconfiguration-intransitencryptionconfiguration-tlscertificateconfiguration)" : {{TLSCertificateConfiguration}}
}
```

### YAML
<a name="aws-properties-emrcontainers-securityconfiguration-intransitencryptionconfiguration-syntax.yaml"></a>

```
  [TLSCertificateConfiguration](#cfn-emrcontainers-securityconfiguration-intransitencryptionconfiguration-tlscertificateconfiguration): {{
    TLSCertificateConfiguration}}
```

## Properties
<a name="aws-properties-emrcontainers-securityconfiguration-intransitencryptionconfiguration-properties"></a>

`TLSCertificateConfiguration`  <a name="cfn-emrcontainers-securityconfiguration-intransitencryptionconfiguration-tlscertificateconfiguration"></a>
TLS certificate-related configuration input for the security configuration.
*Required*: No
*Type*: [TLSCertificateConfiguration](aws-properties-emrcontainers-securityconfiguration-tlscertificateconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
