---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-apikeycredentialprovider-apikeysecretarn.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::ApiKeyCredentialProvider ApiKeySecretArn
<a name="aws-properties-bedrockagentcore-apikeycredentialprovider-apikeysecretarn"></a>

<a name="aws-properties-bedrockagentcore-apikeycredentialprovider-apikeysecretarn-description"></a>The `ApiKeySecretArn` property type specifies Property description not available. for an [AWS::BedrockAgentCore::ApiKeyCredentialProvider](aws-resource-bedrockagentcore-apikeycredentialprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-apikeycredentialprovider-apikeysecretarn-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-apikeycredentialprovider-apikeysecretarn-syntax.json"></a>

```
{
  "[SecretArn](#cfn-bedrockagentcore-apikeycredentialprovider-apikeysecretarn-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-apikeycredentialprovider-apikeysecretarn-syntax.yaml"></a>

```
  [SecretArn](#cfn-bedrockagentcore-apikeycredentialprovider-apikeysecretarn-secretarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-apikeycredentialprovider-apikeysecretarn-properties"></a>

`SecretArn`  <a name="cfn-bedrockagentcore-apikeycredentialprovider-apikeysecretarn-secretarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov):secretsmanager:[A-Za-z0-9-]{1,64}:[0-9]{12}:secret:[a-zA-Z0-9-_/+=.@!]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
