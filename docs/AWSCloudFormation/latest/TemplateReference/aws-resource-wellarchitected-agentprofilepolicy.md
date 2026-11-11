---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wellarchitected-agentprofilepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WellArchitected::AgentProfilePolicy
<a name="aws-resource-wellarchitected-agentprofilepolicy"></a>

**Note**
AWS Well-Architected Agent is in preview release and is subject to change.

Attaches or replaces a resource-based policy on an Agent Profile. The policy controls cross-account access to the profile and its child resources such as recommendations, goals, and contexts. Only the profile owner can call this operation. The policy must be valid IAM JSON with Allow-only statements and no negation condition operators.

## Syntax
<a name="aws-resource-wellarchitected-agentprofilepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wellarchitected-agentprofilepolicy-syntax.json"></a>

```
{
  "Type" : "AWS::WellArchitected::AgentProfilePolicy",
  "Properties" : {
      "[Policy](#cfn-wellarchitected-agentprofilepolicy-policy)" : {{String}},
      "[ProfileArn](#cfn-wellarchitected-agentprofilepolicy-profilearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-wellarchitected-agentprofilepolicy-syntax.yaml"></a>

```
Type: AWS::WellArchitected::AgentProfilePolicy
Properties:
  [Policy](#cfn-wellarchitected-agentprofilepolicy-policy): {{String}}
  [ProfileArn](#cfn-wellarchitected-agentprofilepolicy-profilearn): {{String}}
```

## Properties
<a name="aws-resource-wellarchitected-agentprofilepolicy-properties"></a>

`Policy`  <a name="cfn-wellarchitected-agentprofilepolicy-policy"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `51200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProfileArn`  <a name="cfn-wellarchitected-agentprofilepolicy-profilearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:[0-9]{12}:agent-profile/[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-wellarchitected-agentprofilepolicy-return-values"></a>

### Ref
<a name="aws-resource-wellarchitected-agentprofilepolicy-return-values-ref"></a>
