---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-iamcredentialprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget IamCredentialProvider
<a name="aws-properties-bedrockagentcore-gatewaytarget-iamcredentialprovider"></a>

An IAM credential provider for gateway authentication. This structure contains the configuration for authenticating with the target endpoint using IAM credentials and SigV4 signing.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-iamcredentialprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-iamcredentialprovider-syntax.json"></a>

```
{
  "[Region](#cfn-bedrockagentcore-gatewaytarget-iamcredentialprovider-region)" : {{String}},
  "[Service](#cfn-bedrockagentcore-gatewaytarget-iamcredentialprovider-service)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-iamcredentialprovider-syntax.yaml"></a>

```
  [Region](#cfn-bedrockagentcore-gatewaytarget-iamcredentialprovider-region): {{String}}
  [Service](#cfn-bedrockagentcore-gatewaytarget-iamcredentialprovider-service): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-iamcredentialprovider-properties"></a>

`Region`  <a name="cfn-bedrockagentcore-gatewaytarget-iamcredentialprovider-region"></a>
The AWS Region used for SigV4 signing. If not specified, defaults to the gateway's Region.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Service`  <a name="cfn-bedrockagentcore-gatewaytarget-iamcredentialprovider-service"></a>
The target AWS service name used for SigV4 signing. This value identifies the service that the gateway authenticates with when making requests to the target endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
