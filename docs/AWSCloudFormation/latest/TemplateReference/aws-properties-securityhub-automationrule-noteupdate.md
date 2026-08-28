---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrule-noteupdate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRule NoteUpdate
<a name="aws-properties-securityhub-automationrule-noteupdate"></a>

The updated note.

## Syntax
<a name="aws-properties-securityhub-automationrule-noteupdate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrule-noteupdate-syntax.json"></a>

```
{
  "[Text](#cfn-securityhub-automationrule-noteupdate-text)" : {{String}},
  "[UpdatedBy](#cfn-securityhub-automationrule-noteupdate-updatedby)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrule-noteupdate-syntax.yaml"></a>

```
  [Text](#cfn-securityhub-automationrule-noteupdate-text): {{String}}
  [UpdatedBy](#cfn-securityhub-automationrule-noteupdate-updatedby): {{String}}
```

## Properties
<a name="aws-properties-securityhub-automationrule-noteupdate-properties"></a>

`Text`  <a name="cfn-securityhub-automationrule-noteupdate-text"></a>
The updated note text.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdatedBy`  <a name="cfn-securityhub-automationrule-noteupdate-updatedby"></a>
The principal that updated the note.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
