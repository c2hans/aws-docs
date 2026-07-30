---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-documentstandardgenerativefield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject DocumentStandardGenerativeField
<a name="aws-properties-bedrock-dataautomationproject-documentstandardgenerativefield"></a>

Settings for generating descriptions of documents.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-documentstandardgenerativefield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-documentstandardgenerativefield-syntax.json"></a>

```
{
  "[State](#cfn-bedrock-dataautomationproject-documentstandardgenerativefield-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-documentstandardgenerativefield-syntax.yaml"></a>

```
  [State](#cfn-bedrock-dataautomationproject-documentstandardgenerativefield-state): {{String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-documentstandardgenerativefield-properties"></a>

`State`  <a name="cfn-bedrock-dataautomationproject-documentstandardgenerativefield-state"></a>
Whether generating descriptions is enabled for documents.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
