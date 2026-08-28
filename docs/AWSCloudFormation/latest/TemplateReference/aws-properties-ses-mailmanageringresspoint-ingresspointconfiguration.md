---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanageringresspoint-ingresspointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerIngressPoint IngressPointConfiguration
<a name="aws-properties-ses-mailmanageringresspoint-ingresspointconfiguration"></a>

The configuration of the ingress endpoint resource.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

## Syntax
<a name="aws-properties-ses-mailmanageringresspoint-ingresspointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanageringresspoint-ingresspointconfiguration-syntax.json"></a>

```
{
  "[SecretArn](#cfn-ses-mailmanageringresspoint-ingresspointconfiguration-secretarn)" : {{String}},
  "[SmtpPassword](#cfn-ses-mailmanageringresspoint-ingresspointconfiguration-smtppassword)" : {{String}},
  "[TlsAuthConfiguration](#cfn-ses-mailmanageringresspoint-ingresspointconfiguration-tlsauthconfiguration)" : {{TlsAuthConfiguration}}
}
```

### YAML
<a name="aws-properties-ses-mailmanageringresspoint-ingresspointconfiguration-syntax.yaml"></a>

```
  [SecretArn](#cfn-ses-mailmanageringresspoint-ingresspointconfiguration-secretarn): {{String}}
  [SmtpPassword](#cfn-ses-mailmanageringresspoint-ingresspointconfiguration-smtppassword): {{String}}
  [TlsAuthConfiguration](#cfn-ses-mailmanageringresspoint-ingresspointconfiguration-tlsauthconfiguration): {{
    TlsAuthConfiguration}}
```

## Properties
<a name="aws-properties-ses-mailmanageringresspoint-ingresspointconfiguration-properties"></a>

`SecretArn`  <a name="cfn-ses-mailmanageringresspoint-ingresspointconfiguration-secretarn"></a>
The SecretsManager::Secret ARN of the ingress endpoint resource.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc):secretsmanager:[a-z0-9-]+:\d{12}:secret:[a-zA-Z0-9/_+=,.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmtpPassword`  <a name="cfn-ses-mailmanageringresspoint-ingresspointconfiguration-smtppassword"></a>
The password of the ingress endpoint resource.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9!@#$%^&*()_+\-=\[\]{}|.,?]+$`
*Minimum*: `8`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TlsAuthConfiguration`  <a name="cfn-ses-mailmanageringresspoint-ingresspointconfiguration-tlsauthconfiguration"></a>
The mutual TLS authentication configuration of the ingress endpoint resource.
*Required*: No
*Type*: [TlsAuthConfiguration](aws-properties-ses-mailmanageringresspoint-tlsauthconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
