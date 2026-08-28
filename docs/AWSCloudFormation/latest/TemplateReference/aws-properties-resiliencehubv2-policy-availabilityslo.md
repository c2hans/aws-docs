---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-policy-availabilityslo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Policy AvailabilitySlo
<a name="aws-properties-resiliencehubv2-policy-availabilityslo"></a>

Defines the availability service level objective (SLO) for a resilience policy.

## Syntax
<a name="aws-properties-resiliencehubv2-policy-availabilityslo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-policy-availabilityslo-syntax.json"></a>

```
{
  "[Target](#cfn-resiliencehubv2-policy-availabilityslo-target)" : {{Number}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-policy-availabilityslo-syntax.yaml"></a>

```
  [Target](#cfn-resiliencehubv2-policy-availabilityslo-target): {{Number}}
```

## Properties
<a name="aws-properties-resiliencehubv2-policy-availabilityslo-properties"></a>

`Target`  <a name="cfn-resiliencehubv2-policy-availabilityslo-target"></a>
The target availability percentage, expressed as a value between 0 and 100.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
