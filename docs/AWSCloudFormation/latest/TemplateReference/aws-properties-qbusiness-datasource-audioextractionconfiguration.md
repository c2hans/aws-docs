---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-datasource-audioextractionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataSource AudioExtractionConfiguration
<a name="aws-properties-qbusiness-datasource-audioextractionconfiguration"></a>

Configuration settings for audio content extraction and processing.

## Syntax
<a name="aws-properties-qbusiness-datasource-audioextractionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-datasource-audioextractionconfiguration-syntax.json"></a>

```
{
  "[AudioExtractionStatus](#cfn-qbusiness-datasource-audioextractionconfiguration-audioextractionstatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-datasource-audioextractionconfiguration-syntax.yaml"></a>

```
  [AudioExtractionStatus](#cfn-qbusiness-datasource-audioextractionconfiguration-audioextractionstatus): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-datasource-audioextractionconfiguration-properties"></a>

`AudioExtractionStatus`  <a name="cfn-qbusiness-datasource-audioextractionconfiguration-audioextractionstatus"></a>
The status of audio extraction (ENABLED or DISABLED) for processing audio content from files.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
