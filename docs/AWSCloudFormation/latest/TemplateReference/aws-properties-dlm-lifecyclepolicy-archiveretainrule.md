---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-archiveretainrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy ArchiveRetainRule
<a name="aws-properties-dlm-lifecyclepolicy-archiveretainrule"></a>

**[Custom snapshot policies only]** Specifies information about the archive storage tier retention period.

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-archiveretainrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-archiveretainrule-syntax.json"></a>

```
{
  "[RetentionArchiveTier](#cfn-dlm-lifecyclepolicy-archiveretainrule-retentionarchivetier)" : {{RetentionArchiveTier}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-archiveretainrule-syntax.yaml"></a>

```
  [RetentionArchiveTier](#cfn-dlm-lifecyclepolicy-archiveretainrule-retentionarchivetier): {{
    RetentionArchiveTier}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-archiveretainrule-properties"></a>

`RetentionArchiveTier`  <a name="cfn-dlm-lifecyclepolicy-archiveretainrule-retentionarchivetier"></a>
Information about retention period in the Amazon EBS Snapshots Archive. For more information, see [Archive Amazon EBS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/snapshot-archive.html).
*Required*: Yes
*Type*: [RetentionArchiveTier](aws-properties-dlm-lifecyclepolicy-retentionarchivetier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
