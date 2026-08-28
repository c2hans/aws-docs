---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-browsercustom-certificatelocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::BrowserCustom CertificateLocation
<a name="aws-properties-bedrockagentcore-browsercustom-certificatelocation"></a>

The location from which to retrieve a certificate.

## Syntax
<a name="aws-properties-bedrockagentcore-browsercustom-certificatelocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-browsercustom-certificatelocation-syntax.json"></a>

```
{
  "[SecretArn](#cfn-bedrockagentcore-browsercustom-certificatelocation-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-browsercustom-certificatelocation-syntax.yaml"></a>

```
  [SecretArn](#cfn-bedrockagentcore-browsercustom-certificatelocation-secretarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-browsercustom-certificatelocation-properties"></a>

`SecretArn`  <a name="cfn-bedrockagentcore-browsercustom-certificatelocation-secretarn"></a>
The AWS Secrets Manager location of the certificate.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws(?:-cn|-us-gov|-iso(?:-[bef])?)?):secretsmanager:[a-z0-9-]+:\d{12}:secret:[a-zA-Z0-9/_+=.@-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
