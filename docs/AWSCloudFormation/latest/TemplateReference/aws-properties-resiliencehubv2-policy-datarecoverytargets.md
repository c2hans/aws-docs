---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-policy-datarecoverytargets.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Policy DataRecoveryTargets
<a name="aws-properties-resiliencehubv2-policy-datarecoverytargets"></a>

Defines data recovery targets for a resilience policy.

## Syntax
<a name="aws-properties-resiliencehubv2-policy-datarecoverytargets-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-policy-datarecoverytargets-syntax.json"></a>

```
{
  "[TimeBetweenBackupsInMinutes](#cfn-resiliencehubv2-policy-datarecoverytargets-timebetweenbackupsinminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-policy-datarecoverytargets-syntax.yaml"></a>

```
  [TimeBetweenBackupsInMinutes](#cfn-resiliencehubv2-policy-datarecoverytargets-timebetweenbackupsinminutes): {{Integer}}
```

## Properties
<a name="aws-properties-resiliencehubv2-policy-datarecoverytargets-properties"></a>

`TimeBetweenBackupsInMinutes`  <a name="cfn-resiliencehubv2-policy-datarecoverytargets-timebetweenbackupsinminutes"></a>
The target time between backups, in minutes.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
