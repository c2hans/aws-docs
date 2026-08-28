---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-resourcepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::ResourcePolicy
<a name="aws-resource-bedrockagentcore-resourcepolicy"></a>

Specifies a resource-based policy for an Amazon Bedrock AgentCore resource. A resource policy grants cross-account or service-level access to a specific AgentCore resource such as a Runtime or Gateway.

**Note**
This feature is currently available only for AgentCore Runtime and Gateway.

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-resourcepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-resourcepolicy-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::ResourcePolicy",
  "Properties" : {
      "[Policy](#cfn-bedrockagentcore-resourcepolicy-policy)" : {{String}},
      "[ResourceArn](#cfn-bedrockagentcore-resourcepolicy-resourcearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-resourcepolicy-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::ResourcePolicy
Properties:
  [Policy](#cfn-bedrockagentcore-resourcepolicy-policy): {{String}}
  [ResourceArn](#cfn-bedrockagentcore-resourcepolicy-resourcearn): {{String}}
```

## Properties
<a name="aws-resource-bedrockagentcore-resourcepolicy-properties"></a>

`Policy`  <a name="cfn-bedrockagentcore-resourcepolicy-policy"></a>
The resource policy to create or update.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `20480`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceArn`  <a name="cfn-bedrockagentcore-resourcepolicy-resourcearn"></a>
The Amazon Resource Name (ARN) of the resource for which to create or update the resource policy.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-]+:bedrock-agentcore:[a-z0-9-]*:[0-9]{12}:.+$`
*Minimum*: `20`
*Maximum*: `1011`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-bedrockagentcore-resourcepolicy-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-resourcepolicy-return-values-ref"></a>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
