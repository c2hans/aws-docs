---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-gatewaypolicyengineconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway GatewayPolicyEngineConfiguration
<a name="aws-properties-bedrockagentcore-gateway-gatewaypolicyengineconfiguration"></a>

The configuration for a policy engine associated with a gateway. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with a gateway, the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies.

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-gatewaypolicyengineconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-gatewaypolicyengineconfiguration-syntax.json"></a>

```
{
  "[Arn](#cfn-bedrockagentcore-gateway-gatewaypolicyengineconfiguration-arn)" : {{String}},
  "[Mode](#cfn-bedrockagentcore-gateway-gatewaypolicyengineconfiguration-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-gatewaypolicyengineconfiguration-syntax.yaml"></a>

```
  [Arn](#cfn-bedrockagentcore-gateway-gatewaypolicyengineconfiguration-arn): {{String}}
  [Mode](#cfn-bedrockagentcore-gateway-gatewaypolicyengineconfiguration-mode): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-gatewaypolicyengineconfiguration-properties"></a>

`Arn`  <a name="cfn-bedrockagentcore-gateway-gatewaypolicyengineconfiguration-arn"></a>
The ARN of the policy engine. The policy engine contains Cedar policies that define fine-grained authorization rules specifying who can perform what actions on which resources as agents interact through the gateway.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:policy-engine\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9_]{10}$`
*Minimum*: `1`
*Maximum*: `170`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-bedrockagentcore-gateway-gatewaypolicyengineconfiguration-mode"></a>
The enforcement mode for the policy engine. Valid values include:
+ `LOG_ONLY` - The policy engine evaluates each action against your policies and adds traces on whether tool calls would be allowed or denied, but does not enforce the decision. Use this mode to test and validate policies before enabling enforcement.
+ `ENFORCE` - The policy engine evaluates actions against your policies and enforces decisions by allowing or denying agent operations. Test and validate policies in `LOG_ONLY` mode before enabling enforcement to avoid unintended denials or adversely affecting production traffic.
*Required*: Yes
*Type*: String
*Allowed values*: `LOG_ONLY | ENFORCE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
