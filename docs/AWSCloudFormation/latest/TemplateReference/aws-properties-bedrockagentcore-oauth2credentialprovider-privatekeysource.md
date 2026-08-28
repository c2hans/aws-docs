---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-privatekeysource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider PrivateKeySource
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-privatekeysource"></a>

Contains the private key source configuration for a JWT client assertion.

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-privatekeysource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-privatekeysource-syntax.json"></a>

```
{
  "[KmsKeySource](#cfn-bedrockagentcore-oauth2credentialprovider-privatekeysource-kmskeysource)" : {{KmsKeySourceType}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-privatekeysource-syntax.yaml"></a>

```
  [KmsKeySource](#cfn-bedrockagentcore-oauth2credentialprovider-privatekeysource-kmskeysource): {{
    KmsKeySourceType}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-privatekeysource-properties"></a>

`KmsKeySource`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-privatekeysource-kmskeysource"></a>
The AWS KMS key source for the JWT client assertion.
*Required*: No
*Type*: [KmsKeySourceType](aws-properties-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
