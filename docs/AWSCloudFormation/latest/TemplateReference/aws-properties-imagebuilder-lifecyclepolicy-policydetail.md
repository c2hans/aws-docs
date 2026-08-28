---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-lifecyclepolicy-policydetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::LifecyclePolicy PolicyDetail
<a name="aws-properties-imagebuilder-lifecyclepolicy-policydetail"></a>

The configuration details for a lifecycle policy resource.

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
