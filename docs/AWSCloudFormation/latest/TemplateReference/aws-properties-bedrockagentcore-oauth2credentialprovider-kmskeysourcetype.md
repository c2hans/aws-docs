---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider KmsKeySourceType
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype"></a>

Contains the AWS KMS key configuration for a JWT client assertion.

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype-syntax.json"></a>

```
{
  "[KmsKeyArn](#cfn-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype-syntax.yaml"></a>

```
  [KmsKeyArn](#cfn-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype-properties"></a>

`KmsKeyArn`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to sign the JWT client assertion. The key must be an asymmetric key with key usage SIGN\_VERIFY and a key spec compatible with the configured signing algorithm.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
