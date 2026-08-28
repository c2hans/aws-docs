---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-quotashare-quotasharepreemptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::QuotaShare QuotaSharePreemptionConfiguration
<a name="aws-properties-batch-quotashare-quotasharepreemptionconfiguration"></a>

Specifies the preemption behavior for jobs in a quota share.

## Syntax
<a name="aws-properties-batch-quotashare-quotasharepreemptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-quotashare-quotasharepreemptionconfiguration-syntax.json"></a>

```
{
  "[InSharePreemption](#cfn-batch-quotashare-quotasharepreemptionconfiguration-insharepreemption)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-quotashare-quotasharepreemptionconfiguration-syntax.yaml"></a>

```
  [InSharePreemption](#cfn-batch-quotashare-quotasharepreemptionconfiguration-insharepreemption): {{String}}
```

## Properties
<a name="aws-properties-batch-quotashare-quotasharepreemptionconfiguration-properties"></a>

`InSharePreemption`  <a name="cfn-batch-quotashare-quotasharepreemptionconfiguration-insharepreemption"></a>
Specifies whether jobs within a quota share can be preempted by another, higher priority job in the same quota share.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
