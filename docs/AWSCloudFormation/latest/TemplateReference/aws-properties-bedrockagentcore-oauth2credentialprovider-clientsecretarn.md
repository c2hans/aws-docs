---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-clientsecretarn.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider ClientSecretArn
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-clientsecretarn"></a>

<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-clientsecretarn-description"></a>The `ClientSecretArn` property type specifies Property description not available. for an [AWS::BedrockAgentCore::OAuth2CredentialProvider](aws-resource-bedrockagentcore-oauth2credentialprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-clientsecretarn-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-clientsecretarn-syntax.json"></a>

```
{
  "[SecretArn](#cfn-bedrockagentcore-oauth2credentialprovider-clientsecretarn-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-clientsecretarn-syntax.yaml"></a>

```
  [SecretArn](#cfn-bedrockagentcore-oauth2credentialprovider-clientsecretarn-secretarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-clientsecretarn-properties"></a>

`SecretArn`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-clientsecretarn-secretarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov):secretsmanager:[A-Za-z0-9-]{1,64}:[0-9]{12}:secret:[a-zA-Z0-9-_/+=.@!]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
