---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-splitterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject SplitterConfiguration
<a name="aws-properties-bedrock-dataautomationproject-splitterconfiguration"></a>

Document splitter settings. If a document is too large to be processed in one pass, the document splitter splits it into smaller documents.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-splitterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-splitterconfiguration-syntax.json"></a>

```
{
  "[State](#cfn-bedrock-dataautomationproject-splitterconfiguration-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-splitterconfiguration-syntax.yaml"></a>

```
  [State](#cfn-bedrock-dataautomationproject-splitterconfiguration-state): {{String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-splitterconfiguration-properties"></a>

`State`  <a name="cfn-bedrock-dataautomationproject-splitterconfiguration-state"></a>
Whether document splitter is enabled for a project.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
