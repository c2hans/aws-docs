---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-staticroute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule StaticRoute
<a name="aws-properties-bedrockagentcore-gatewayrule-staticroute"></a>

A static route to a single gateway target.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-staticroute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-staticroute-syntax.json"></a>

```
{
  "[TargetName](#cfn-bedrockagentcore-gatewayrule-staticroute-targetname)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-staticroute-syntax.yaml"></a>

```
  [TargetName](#cfn-bedrockagentcore-gatewayrule-staticroute-targetname): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-staticroute-properties"></a>

`TargetName`  <a name="cfn-bedrockagentcore-gatewayrule-staticroute-targetname"></a>
The name of the target to route requests to.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
