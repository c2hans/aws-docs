---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-archiverule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy ArchiveRule
<a name="aws-properties-dlm-lifecyclepolicy-archiverule"></a>

**[Custom snapshot policies only]** Specifies a snapshot archiving rule for a schedule.

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-archiverule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-archiverule-syntax.json"></a>

```
{
  "[RetainRule](#cfn-dlm-lifecyclepolicy-archiverule-retainrule)" : {{ArchiveRetainRule}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-archiverule-syntax.yaml"></a>

```
  [RetainRule](#cfn-dlm-lifecyclepolicy-archiverule-retainrule): {{
    ArchiveRetainRule}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-archiverule-properties"></a>

`RetainRule`  <a name="cfn-dlm-lifecyclepolicy-archiverule-retainrule"></a>
Information about the retention period for the snapshot archiving rule.
*Required*: Yes
*Type*: [ArchiveRetainRule](aws-properties-dlm-lifecyclepolicy-archiveretainrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
