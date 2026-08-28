---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-matchprincipals.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule MatchPrincipals
<a name="aws-properties-bedrockagentcore-gatewayrule-matchprincipals"></a>

A condition that matches requests based on the caller's identity.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-matchprincipals-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-matchprincipals-syntax.json"></a>

```
{
  "[AnyOf](#cfn-bedrockagentcore-gatewayrule-matchprincipals-anyof)" : {{[ MatchPrincipalEntry, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-matchprincipals-syntax.yaml"></a>

```
  [AnyOf](#cfn-bedrockagentcore-gatewayrule-matchprincipals-anyof): {{
    - MatchPrincipalEntry}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-matchprincipals-properties"></a>

`AnyOf`  <a name="cfn-bedrockagentcore-gatewayrule-matchprincipals-anyof"></a>
A list of principal entries. The condition is met if any of the entries match the caller's identity.
*Required*: Yes
*Type*: Array of [MatchPrincipalEntry](aws-properties-bedrockagentcore-gatewayrule-matchprincipalentry.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
