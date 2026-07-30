---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessskillgitauth.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessSkillGitAuth
<a name="aws-properties-bedrockagentcore-harness-harnessskillgitauth"></a>

Authentication configuration for accessing a private git repository.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessskillgitauth-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessskillgitauth-syntax.json"></a>

```
{
  "[CredentialArn](#cfn-bedrockagentcore-harness-harnessskillgitauth-credentialarn)" : {{String}},
  "[Username](#cfn-bedrockagentcore-harness-harnessskillgitauth-username)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessskillgitauth-syntax.yaml"></a>

```
  [CredentialArn](#cfn-bedrockagentcore-harness-harnessskillgitauth-credentialarn): {{String}}
  [Username](#cfn-bedrockagentcore-harness-harnessskillgitauth-username): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessskillgitauth-properties"></a>

`CredentialArn`  <a name="cfn-bedrockagentcore-harness-harnessskillgitauth-credentialarn"></a>
The ARN of the credential in AgentCore Identity containing the password or personal access token.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-bedrockagentcore-harness-harnessskillgitauth-username"></a>
Username for authentication. Defaults to 'oauth2' if not specified.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
