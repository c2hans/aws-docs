---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-condition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule Condition
<a name="aws-properties-bedrockagentcore-gatewayrule-condition"></a>

A condition that determines when a gateway rule applies. Conditions can match on principals or request paths.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-condition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-condition-syntax.json"></a>

```
{
  "[MatchPaths](#cfn-bedrockagentcore-gatewayrule-condition-matchpaths)" : {{MatchPaths}},
  "[MatchPrincipals](#cfn-bedrockagentcore-gatewayrule-condition-matchprincipals)" : {{MatchPrincipals}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-condition-syntax.yaml"></a>

```
  [MatchPaths](#cfn-bedrockagentcore-gatewayrule-condition-matchpaths): {{
    MatchPaths}}
  [MatchPrincipals](#cfn-bedrockagentcore-gatewayrule-condition-matchprincipals): {{
    MatchPrincipals}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-condition-properties"></a>

`MatchPaths`  <a name="cfn-bedrockagentcore-gatewayrule-condition-matchpaths"></a>
A condition that matches on the request path.
*Required*: No
*Type*: [MatchPaths](aws-properties-bedrockagentcore-gatewayrule-matchpaths.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchPrincipals`  <a name="cfn-bedrockagentcore-gatewayrule-condition-matchprincipals"></a>
A condition that matches on the identity of the caller making the request.
*Required*: No
*Type*: [MatchPrincipals](aws-properties-bedrockagentcore-gatewayrule-matchprincipals.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
