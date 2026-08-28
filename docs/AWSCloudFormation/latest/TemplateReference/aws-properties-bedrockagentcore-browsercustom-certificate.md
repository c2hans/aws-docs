---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-browsercustom-certificate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::BrowserCustom Certificate
<a name="aws-properties-bedrockagentcore-browsercustom-certificate"></a>

A certificate to install in the browser or code interpreter.

## Syntax
<a name="aws-properties-bedrockagentcore-browsercustom-certificate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-browsercustom-certificate-syntax.json"></a>

```
{
  "[CertificateLocation](#cfn-bedrockagentcore-browsercustom-certificate-certificatelocation)" : {{CertificateLocation}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-browsercustom-certificate-syntax.yaml"></a>

```
  [CertificateLocation](#cfn-bedrockagentcore-browsercustom-certificate-certificatelocation): {{
    CertificateLocation}}
```

## Properties
<a name="aws-properties-bedrockagentcore-browsercustom-certificate-properties"></a>

`CertificateLocation`  <a name="cfn-bedrockagentcore-browsercustom-certificate-certificatelocation"></a>
Property description not available.
*Required*: Yes
*Type*: [CertificateLocation](aws-properties-bedrockagentcore-browsercustom-certificatelocation.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
