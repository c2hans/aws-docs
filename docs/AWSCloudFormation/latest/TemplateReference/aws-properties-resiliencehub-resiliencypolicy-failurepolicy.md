---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehub-resiliencypolicy-failurepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHub::ResiliencyPolicy FailurePolicy
<a name="aws-properties-resiliencehub-resiliencypolicy-failurepolicy"></a>

Defines a failure policy.

## Syntax
<a name="aws-properties-resiliencehub-resiliencypolicy-failurepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehub-resiliencypolicy-failurepolicy-syntax.json"></a>

```
{
  "[RpoInSecs](#cfn-resiliencehub-resiliencypolicy-failurepolicy-rpoinsecs)" : {{Integer}},
  "[RtoInSecs](#cfn-resiliencehub-resiliencypolicy-failurepolicy-rtoinsecs)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-resiliencehub-resiliencypolicy-failurepolicy-syntax.yaml"></a>

```
  [RpoInSecs](#cfn-resiliencehub-resiliencypolicy-failurepolicy-rpoinsecs): {{Integer}}
  [RtoInSecs](#cfn-resiliencehub-resiliencypolicy-failurepolicy-rtoinsecs): {{Integer}}
```

## Properties
<a name="aws-properties-resiliencehub-resiliencypolicy-failurepolicy-properties"></a>

`RpoInSecs`  <a name="cfn-resiliencehub-resiliencypolicy-failurepolicy-rpoinsecs"></a>
Recovery Point Objective (RPO) in seconds.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RtoInSecs`  <a name="cfn-resiliencehub-resiliencypolicy-failurepolicy-rtoinsecs"></a>
Recovery Time Objective (RTO) in seconds.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
