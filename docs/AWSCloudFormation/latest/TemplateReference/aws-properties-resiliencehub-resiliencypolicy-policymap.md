---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehub-resiliencypolicy-policymap.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHub::ResiliencyPolicy PolicyMap
<a name="aws-properties-resiliencehub-resiliencypolicy-policymap"></a>

The type of resiliency policy to be created, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds.

## Syntax
<a name="aws-properties-resiliencehub-resiliencypolicy-policymap-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehub-resiliencypolicy-policymap-syntax.json"></a>

```
{
  "[AZ](#cfn-resiliencehub-resiliencypolicy-policymap-az)" : {{FailurePolicy}},
  "[Hardware](#cfn-resiliencehub-resiliencypolicy-policymap-hardware)" : {{FailurePolicy}},
  "[Region](#cfn-resiliencehub-resiliencypolicy-policymap-region)" : {{FailurePolicy}},
  "[Software](#cfn-resiliencehub-resiliencypolicy-policymap-software)" : {{FailurePolicy}}
}
```

### YAML
<a name="aws-properties-resiliencehub-resiliencypolicy-policymap-syntax.yaml"></a>

```
  [AZ](#cfn-resiliencehub-resiliencypolicy-policymap-az): {{
    FailurePolicy}}
  [Hardware](#cfn-resiliencehub-resiliencypolicy-policymap-hardware): {{
    FailurePolicy}}
  [Region](#cfn-resiliencehub-resiliencypolicy-policymap-region): {{
    FailurePolicy}}
  [Software](#cfn-resiliencehub-resiliencypolicy-policymap-software): {{
    FailurePolicy}}
```

## Properties
<a name="aws-properties-resiliencehub-resiliencypolicy-policymap-properties"></a>

`AZ`  <a name="cfn-resiliencehub-resiliencypolicy-policymap-az"></a>
Defines the RTO and RPO targets for Availability Zone disruption.
*Required*: Yes
*Type*: [FailurePolicy](aws-properties-resiliencehub-resiliencypolicy-failurepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Hardware`  <a name="cfn-resiliencehub-resiliencypolicy-policymap-hardware"></a>
Defines the RTO and RPO targets for hardware disruption.
*Required*: Yes
*Type*: [FailurePolicy](aws-properties-resiliencehub-resiliencypolicy-failurepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-resiliencehub-resiliencypolicy-policymap-region"></a>
Defines the RTO and RPO targets for Regional disruption.
*Required*: No
*Type*: [FailurePolicy](aws-properties-resiliencehub-resiliencypolicy-failurepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Software`  <a name="cfn-resiliencehub-resiliencypolicy-policymap-software"></a>
Defines the RTO and RPO targets for software disruption.
*Required*: Yes
*Type*: [FailurePolicy](aws-properties-resiliencehub-resiliencypolicy-failurepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
