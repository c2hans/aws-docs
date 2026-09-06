---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-datasource-videoextractionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataSource VideoExtractionConfiguration
<a name="aws-properties-qbusiness-datasource-videoextractionconfiguration"></a>

Configuration settings for video content extraction and processing.

## Syntax
<a name="aws-properties-qbusiness-datasource-videoextractionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-datasource-videoextractionconfiguration-syntax.json"></a>

```
{
  "[VideoExtractionStatus](#cfn-qbusiness-datasource-videoextractionconfiguration-videoextractionstatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-datasource-videoextractionconfiguration-syntax.yaml"></a>

```
  [VideoExtractionStatus](#cfn-qbusiness-datasource-videoextractionconfiguration-videoextractionstatus): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-datasource-videoextractionconfiguration-properties"></a>

`VideoExtractionStatus`  <a name="cfn-qbusiness-datasource-videoextractionconfiguration-videoextractionstatus"></a>
The status of video extraction (ENABLED or DISABLED) for processing video content from files.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
