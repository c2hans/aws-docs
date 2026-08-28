---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentcredentialprovider-secretinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider SecretInfo
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-secretinfo"></a>

Information about a secret in AWS Secrets Manager.

## Syntax
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-secretinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-secretinfo-syntax.json"></a>

```
{
  "[SecretArn](#cfn-bedrockagentcore-paymentcredentialprovider-secretinfo-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-secretinfo-syntax.yaml"></a>

```
  [SecretArn](#cfn-bedrockagentcore-paymentcredentialprovider-secretinfo-secretarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-secretinfo-properties"></a>

`SecretArn`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-secretinfo-secretarn"></a>
The Amazon Resource Name (ARN) of the secret in AWS Secrets Manager.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b|aws-iso-e|aws-iso-f|aws-eusc):secretsmanager:[A-Za-z0-9-]{1,64}:[0-9]{12}:secret:[a-zA-Z0-9-_/+=.@!]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
