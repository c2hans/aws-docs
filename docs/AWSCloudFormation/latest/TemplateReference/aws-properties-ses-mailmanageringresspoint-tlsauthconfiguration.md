---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanageringresspoint-tlsauthconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerIngressPoint TlsAuthConfiguration
<a name="aws-properties-ses-mailmanageringresspoint-tlsauthconfiguration"></a>

The mutual TLS authentication configuration for an ingress endpoint.

## Syntax
<a name="aws-properties-ses-mailmanageringresspoint-tlsauthconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanageringresspoint-tlsauthconfiguration-syntax.json"></a>

```
{
  "[TrustStore](#cfn-ses-mailmanageringresspoint-tlsauthconfiguration-truststore)" : {{TrustStore}}
}
```

### YAML
<a name="aws-properties-ses-mailmanageringresspoint-tlsauthconfiguration-syntax.yaml"></a>

```
  [TrustStore](#cfn-ses-mailmanageringresspoint-tlsauthconfiguration-truststore): {{
    TrustStore}}
```

## Properties
<a name="aws-properties-ses-mailmanageringresspoint-tlsauthconfiguration-properties"></a>

`TrustStore`  <a name="cfn-ses-mailmanageringresspoint-tlsauthconfiguration-truststore"></a>
The trust store configuration for mutual TLS authentication.
*Required*: Yes
*Type*: [TrustStore](aws-properties-ses-mailmanageringresspoint-truststore.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
