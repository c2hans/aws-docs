---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-matchpaths.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule MatchPaths
<a name="aws-properties-bedrockagentcore-gatewayrule-matchpaths"></a>

A condition that matches requests based on the request path.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-matchpaths-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-matchpaths-syntax.json"></a>

```
{
  "[AnyOf](#cfn-bedrockagentcore-gatewayrule-matchpaths-anyof)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-matchpaths-syntax.yaml"></a>

```
  [AnyOf](#cfn-bedrockagentcore-gatewayrule-matchpaths-anyof): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-matchpaths-properties"></a>

`AnyOf`  <a name="cfn-bedrockagentcore-gatewayrule-matchpaths-anyof"></a>
A list of path patterns. The condition is met if the request path matches any of the patterns.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `512 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
