---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-lifecyclepolicy-policydetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::LifecyclePolicy PolicyDetail
<a name="aws-properties-imagebuilder-lifecyclepolicy-policydetail"></a>

Defines one lifecycle policy rule: the action to take, the filter that determines which resources the rule applies to, and optional exclusion rules.

## Syntax
<a name="aws-properties-imagebuilder-lifecyclepolicy-policydetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-lifecyclepolicy-policydetail-syntax.json"></a>

```
{
  "[Action](#cfn-imagebuilder-lifecyclepolicy-policydetail-action)" : {{Action}},
  "[ExclusionRules](#cfn-imagebuilder-lifecyclepolicy-policydetail-exclusionrules)" : {{ExclusionRules}},
  "[Filter](#cfn-imagebuilder-lifecyclepolicy-policydetail-filter)" : {{Filter}}
}
```

### YAML
<a name="aws-properties-imagebuilder-lifecyclepolicy-policydetail-syntax.yaml"></a>

```
  [Action](#cfn-imagebuilder-lifecyclepolicy-policydetail-action): {{
    Action}}
  [ExclusionRules](#cfn-imagebuilder-lifecyclepolicy-policydetail-exclusionrules): {{
    ExclusionRules}}
  [Filter](#cfn-imagebuilder-lifecyclepolicy-policydetail-filter): {{
    Filter}}
```

## Properties
<a name="aws-properties-imagebuilder-lifecyclepolicy-policydetail-properties"></a>

`Action`  <a name="cfn-imagebuilder-lifecyclepolicy-policydetail-action"></a>
Configuration details for the policy action.
*Required*: Yes
*Type*: [Action](aws-properties-imagebuilder-lifecyclepolicy-action.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExclusionRules`  <a name="cfn-imagebuilder-lifecyclepolicy-policydetail-exclusionrules"></a>
Additional rules to specify resources that should be exempt from policy actions.
*Required*: No
*Type*: [ExclusionRules](aws-properties-imagebuilder-lifecyclepolicy-exclusionrules.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Filter`  <a name="cfn-imagebuilder-lifecyclepolicy-policydetail-filter"></a>
Specifies the resources that the lifecycle policy applies to.
*Required*: Yes
*Type*: [Filter](aws-properties-imagebuilder-lifecyclepolicy-filter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
