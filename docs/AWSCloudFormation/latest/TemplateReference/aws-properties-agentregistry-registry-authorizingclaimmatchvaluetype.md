---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registry-authorizingclaimmatchvaluetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::Registry AuthorizingClaimMatchValueType
<a name="aws-properties-agentregistry-registry-authorizingclaimmatchvaluetype"></a>

The value and match operator used to authorize a claim during JSON Web Token (JWT) validation.

## Syntax
<a name="aws-properties-agentregistry-registry-authorizingclaimmatchvaluetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registry-authorizingclaimmatchvaluetype-syntax.json"></a>

```
{
  "[ClaimMatchOperator](#cfn-agentregistry-registry-authorizingclaimmatchvaluetype-claimmatchoperator)" : {{String}},
  "[ClaimMatchValue](#cfn-agentregistry-registry-authorizingclaimmatchvaluetype-claimmatchvalue)" : {{ClaimMatchValueType}}
}
```

### YAML
<a name="aws-properties-agentregistry-registry-authorizingclaimmatchvaluetype-syntax.yaml"></a>

```
  [ClaimMatchOperator](#cfn-agentregistry-registry-authorizingclaimmatchvaluetype-claimmatchoperator): {{String}}
  [ClaimMatchValue](#cfn-agentregistry-registry-authorizingclaimmatchvaluetype-claimmatchvalue): {{
    ClaimMatchValueType}}
```

## Properties
<a name="aws-properties-agentregistry-registry-authorizingclaimmatchvaluetype-properties"></a>

`ClaimMatchOperator`  <a name="cfn-agentregistry-registry-authorizingclaimmatchvaluetype-claimmatchoperator"></a>
The operator used to compare the claim value against the expected match value.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS | CONTAINS | CONTAINS_ANY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClaimMatchValue`  <a name="cfn-agentregistry-registry-authorizingclaimmatchvaluetype-claimmatchvalue"></a>
The expected value used to match the claim.
*Required*: Yes
*Type*: [ClaimMatchValueType](aws-properties-agentregistry-registry-claimmatchvaluetype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
