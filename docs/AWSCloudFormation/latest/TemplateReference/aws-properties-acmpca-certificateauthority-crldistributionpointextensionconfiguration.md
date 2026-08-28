---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-acmpca-certificateauthority-crldistributionpointextensionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ACMPCA::CertificateAuthority CrlDistributionPointExtensionConfiguration
<a name="aws-properties-acmpca-certificateauthority-crldistributionpointextensionconfiguration"></a>

Contains configuration information for the default behavior of the CRL Distribution Point (CDP) extension in certificates issued by your CA. This extension contains a link to download the CRL, so you can check whether a certificate has been revoked. To choose whether you want this extension omitted or not in certificates issued by your CA, you can set the **OmitExtension** parameter.

## Syntax
<a name="aws-properties-acmpca-certificateauthority-crldistributionpointextensionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-acmpca-certificateauthority-crldistributionpointextensionconfiguration-syntax.json"></a>

```
{
  "[OmitExtension](#cfn-acmpca-certificateauthority-crldistributionpointextensionconfiguration-omitextension)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-acmpca-certificateauthority-crldistributionpointextensionconfiguration-syntax.yaml"></a>

```
  [OmitExtension](#cfn-acmpca-certificateauthority-crldistributionpointextensionconfiguration-omitextension): {{Boolean}}
```

## Properties
<a name="aws-properties-acmpca-certificateauthority-crldistributionpointextensionconfiguration-properties"></a>

`OmitExtension`  <a name="cfn-acmpca-certificateauthority-crldistributionpointextensionconfiguration-omitextension"></a>
Configures whether the CRL Distribution Point extension should be populated with the default URL to the CRL. If set to `true`, then the CDP extension will not be present in any certificates issued by that CA unless otherwise specified through CSR or API passthrough.
Only set this if you have another way to distribute the CRL Distribution Points for certificates issued by your CA, such as the Matter Distributed Compliance Ledger.
This configuration cannot be enabled with a custom CNAME set.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
