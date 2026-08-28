---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-certificatemanager-acmeendpoint-publiccertificateauthority.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CertificateManager::AcmeEndpoint PublicCertificateAuthority
<a name="aws-properties-certificatemanager-acmeendpoint-publiccertificateauthority"></a>

Configuration for a public certificate authority.

## Syntax
<a name="aws-properties-certificatemanager-acmeendpoint-publiccertificateauthority-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-certificatemanager-acmeendpoint-publiccertificateauthority-syntax.json"></a>

```
{
  "[AllowedKeyAlgorithms](#cfn-certificatemanager-acmeendpoint-publiccertificateauthority-allowedkeyalgorithms)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-certificatemanager-acmeendpoint-publiccertificateauthority-syntax.yaml"></a>

```
  [AllowedKeyAlgorithms](#cfn-certificatemanager-acmeendpoint-publiccertificateauthority-allowedkeyalgorithms): {{
    - String}}
```

## Properties
<a name="aws-properties-certificatemanager-acmeendpoint-publiccertificateauthority-properties"></a>

`AllowedKeyAlgorithms`  <a name="cfn-certificatemanager-acmeendpoint-publiccertificateauthority-allowedkeyalgorithms"></a>
The key algorithms allowed for certificates issued by this certificate authority.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
