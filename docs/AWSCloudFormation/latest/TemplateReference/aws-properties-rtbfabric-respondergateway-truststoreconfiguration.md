---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-respondergateway-truststoreconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::ResponderGateway TrustStoreConfiguration
<a name="aws-properties-rtbfabric-respondergateway-truststoreconfiguration"></a>

Describes the configuration of a trust store.

## Syntax
<a name="aws-properties-rtbfabric-respondergateway-truststoreconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-respondergateway-truststoreconfiguration-syntax.json"></a>

```
{
  "[CertificateAuthorityCertificates](#cfn-rtbfabric-respondergateway-truststoreconfiguration-certificateauthoritycertificates)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-rtbfabric-respondergateway-truststoreconfiguration-syntax.yaml"></a>

```
  [CertificateAuthorityCertificates](#cfn-rtbfabric-respondergateway-truststoreconfiguration-certificateauthoritycertificates): {{
    - String}}
```

## Properties
<a name="aws-properties-rtbfabric-respondergateway-truststoreconfiguration-properties"></a>

`CertificateAuthorityCertificates`  <a name="cfn-rtbfabric-respondergateway-truststoreconfiguration-certificateauthoritycertificates"></a>
The certificate authority certificate.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
