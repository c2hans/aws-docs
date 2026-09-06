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
