---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registry-approvalconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::Registry ApprovalConfiguration
<a name="aws-properties-agentregistry-registry-approvalconfiguration"></a>

Configuration for the registry's record approval workflow. It controls whether submitted records require manual review before becoming discoverable, or are automatically approved. When no auto-approval rules are configured, submitted records require manual review.

## Syntax
<a name="aws-properties-agentregistry-registry-approvalconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registry-approvalconfiguration-syntax.json"></a>

```
{
  "[AutoApprovalRules](#cfn-agentregistry-registry-approvalconfiguration-autoapprovalrules)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-agentregistry-registry-approvalconfiguration-syntax.yaml"></a>

```
  [AutoApprovalRules](#cfn-agentregistry-registry-approvalconfiguration-autoapprovalrules): {{
    - String}}
```

## Properties
<a name="aws-properties-agentregistry-registry-approvalconfiguration-properties"></a>

`AutoApprovalRules`  <a name="cfn-agentregistry-registry-approvalconfiguration-autoapprovalrules"></a>
The rules that determine which registry records are automatically approved on submission. When omitted or empty, submitted records require manual review. Currently, the only supported value is `APPROVE_ALL`, which automatically approves all submitted records.
*Required*: No
*Type*: Array of String
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
