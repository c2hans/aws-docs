---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registry-customclaimvalidationtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::Registry CustomClaimValidationType
<a name="aws-properties-agentregistry-registry-customclaimvalidationtype"></a>

A validation rule applied to a single claim of an inbound JSON Web Token (JWT).

## Syntax
<a name="aws-properties-agentregistry-registry-customclaimvalidationtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registry-customclaimvalidationtype-syntax.json"></a>

```
{
  "[AuthorizingClaimMatchValue](#cfn-agentregistry-registry-customclaimvalidationtype-authorizingclaimmatchvalue)" : {{AuthorizingClaimMatchValueType}},
  "[InboundTokenClaimName](#cfn-agentregistry-registry-customclaimvalidationtype-inboundtokenclaimname)" : {{String}},
  "[InboundTokenClaimValueType](#cfn-agentregistry-registry-customclaimvalidationtype-inboundtokenclaimvaluetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registry-customclaimvalidationtype-syntax.yaml"></a>

```
  [AuthorizingClaimMatchValue](#cfn-agentregistry-registry-customclaimvalidationtype-authorizingclaimmatchvalue): {{
    AuthorizingClaimMatchValueType}}
  [InboundTokenClaimName](#cfn-agentregistry-registry-customclaimvalidationtype-inboundtokenclaimname): {{String}}
  [InboundTokenClaimValueType](#cfn-agentregistry-registry-customclaimvalidationtype-inboundtokenclaimvaluetype): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registry-customclaimvalidationtype-properties"></a>

`AuthorizingClaimMatchValue`  <a name="cfn-agentregistry-registry-customclaimvalidationtype-authorizingclaimmatchvalue"></a>
The value and match operator used to authorize the claim.
*Required*: Yes
*Type*: [AuthorizingClaimMatchValueType](aws-properties-agentregistry-registry-authorizingclaimmatchvaluetype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InboundTokenClaimName`  <a name="cfn-agentregistry-registry-customclaimvalidationtype-inboundtokenclaimname"></a>
The name of the claim in the inbound JWT to validate.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9_.-:]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InboundTokenClaimValueType`  <a name="cfn-agentregistry-registry-customclaimvalidationtype-inboundtokenclaimvaluetype"></a>
The value type of the inbound token claim.
*Required*: Yes
*Type*: String
*Allowed values*: `STRING | STRING_ARRAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
