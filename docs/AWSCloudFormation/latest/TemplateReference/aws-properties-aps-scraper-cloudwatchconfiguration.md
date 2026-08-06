---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-scraper-cloudwatchconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Scraper CloudWatchConfiguration
<a name="aws-properties-aps-scraper-cloudwatchconfiguration"></a>

<a name="aws-properties-aps-scraper-cloudwatchconfiguration-description"></a>The `CloudWatchConfiguration` property type specifies Property description not available. for an [AWS::APS::Scraper](aws-resource-aps-scraper.md).

## Syntax
<a name="aws-properties-aps-scraper-cloudwatchconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-scraper-cloudwatchconfiguration-syntax.json"></a>

```
{
  "[DatasetArn](#cfn-aps-scraper-cloudwatchconfiguration-datasetarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-aps-scraper-cloudwatchconfiguration-syntax.yaml"></a>

```
  [DatasetArn](#cfn-aps-scraper-cloudwatchconfiguration-datasetarn): {{String}}
```

## Properties
<a name="aws-properties-aps-scraper-cloudwatchconfiguration-properties"></a>

`DatasetArn`  <a name="cfn-aps-scraper-cloudwatchconfiguration-datasetarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z]*:cloudwatch:[-a-z0-9]+:[0-9]{12}:dataset\/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
