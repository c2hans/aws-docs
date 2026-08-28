---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ce-anomalymonitor-resourcetag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CE::AnomalyMonitor ResourceTag
<a name="aws-properties-ce-anomalymonitor-resourcetag"></a>

The tag structure that contains a tag key and value.

**Note**
Tagging is supported only for the following Cost Explorer resource types: [`AnomalyMonitor`](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalyMonitor.html), [`AnomalySubscription`](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html), [`CostCategory`](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategory.html).

## Syntax
<a name="aws-properties-ce-anomalymonitor-resourcetag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ce-anomalymonitor-resourcetag-syntax.json"></a>

```
{
  "[Key](#cfn-ce-anomalymonitor-resourcetag-key)" : {{String}},
  "[Value](#cfn-ce-anomalymonitor-resourcetag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ce-anomalymonitor-resourcetag-syntax.yaml"></a>

```
  [Key](#cfn-ce-anomalymonitor-resourcetag-key): {{String}}
  [Value](#cfn-ce-anomalymonitor-resourcetag-value): {{String}}
```

## Properties
<a name="aws-properties-ce-anomalymonitor-resourcetag-properties"></a>

`Key`  <a name="cfn-ce-anomalymonitor-resourcetag-key"></a>
The key that's associated with the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:).*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-ce-anomalymonitor-resourcetag-value"></a>
The value that's associated with the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
