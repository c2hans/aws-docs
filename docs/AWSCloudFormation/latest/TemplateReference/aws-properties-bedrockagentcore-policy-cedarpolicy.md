---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-policy-cedarpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Policy CedarPolicy
<a name="aws-properties-bedrockagentcore-policy-cedarpolicy"></a>

A Cedar policy statement within the AgentCore Policy system.

## Syntax
<a name="aws-properties-bedrockagentcore-policy-cedarpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-policy-cedarpolicy-syntax.json"></a>

```
{
  "[Statement](#cfn-bedrockagentcore-policy-cedarpolicy-statement)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-policy-cedarpolicy-syntax.yaml"></a>

```
  [Statement](#cfn-bedrockagentcore-policy-cedarpolicy-statement): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-policy-cedarpolicy-properties"></a>

`Statement`  <a name="cfn-bedrockagentcore-policy-cedarpolicy-statement"></a>
The Cedar policy statement that defines the authorization logic.
*Required*: Yes
*Type*: String
*Minimum*: `35`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
