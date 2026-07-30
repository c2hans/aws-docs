---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-audioextractionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource AudioExtractionConfiguration
<a name="aws-properties-bedrock-datasource-audioextractionconfiguration"></a>

Configuration for audio extraction.

## Syntax
<a name="aws-properties-bedrock-datasource-audioextractionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-audioextractionconfiguration-syntax.json"></a>

```
{
  "[AudioExtractionStatus](#cfn-bedrock-datasource-audioextractionconfiguration-audioextractionstatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-audioextractionconfiguration-syntax.yaml"></a>

```
  [AudioExtractionStatus](#cfn-bedrock-datasource-audioextractionconfiguration-audioextractionstatus): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-audioextractionconfiguration-properties"></a>

`AudioExtractionStatus`  <a name="cfn-bedrock-datasource-audioextractionconfiguration-audioextractionstatus"></a>
Whether audio extraction is enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
