---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-tlscertificateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration TLSCertificateConfiguration
<a name="aws-properties-emrcontainers-securityconfiguration-tlscertificateconfiguration"></a>

Configurations related to the TLS certificate for the security configuration.

## Syntax
<a name="aws-properties-emrcontainers-securityconfiguration-tlscertificateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-securityconfiguration-tlscertificateconfiguration-syntax.json"></a>

```
{
  "[CertificateProviderType](#cfn-emrcontainers-securityconfiguration-tlscertificateconfiguration-certificateprovidertype)" : {{String}},
  "[PrivateKeySecretArn](#cfn-emrcontainers-securityconfiguration-tlscertificateconfiguration-privatekeysecretarn)" : {{String}},
  "[PublicKeySecretArn](#cfn-emrcontainers-securityconfiguration-tlscertificateconfiguration-publickeysecretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-securityconfiguration-tlscertificateconfiguration-syntax.yaml"></a>

```
  [CertificateProviderType](#cfn-emrcontainers-securityconfiguration-tlscertificateconfiguration-certificateprovidertype): {{String}}
  [PrivateKeySecretArn](#cfn-emrcontainers-securityconfiguration-tlscertificateconfiguration-privatekeysecretarn): {{String}}
  [PublicKeySecretArn](#cfn-emrcontainers-securityconfiguration-tlscertificateconfiguration-publickeysecretarn): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-securityconfiguration-tlscertificateconfiguration-properties"></a>

`CertificateProviderType`  <a name="cfn-emrcontainers-securityconfiguration-tlscertificateconfiguration-certificateprovidertype"></a>
The TLS certificate type. Acceptable values: `PEM` or `Custom`.
*Required*: No
*Type*: String
*Allowed values*: `PEM`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrivateKeySecretArn`  <a name="cfn-emrcontainers-securityconfiguration-tlscertificateconfiguration-privatekeysecretarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PublicKeySecretArn`  <a name="cfn-emrcontainers-securityconfiguration-tlscertificateconfiguration-publickeysecretarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
