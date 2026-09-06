---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-scraper-destination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Scraper Destination
<a name="aws-properties-aps-scraper-destination"></a>

Where to send the metrics from a scraper.

## Syntax
<a name="aws-properties-aps-scraper-destination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-scraper-destination-syntax.json"></a>

```
{
  "[AmpConfiguration](#cfn-aps-scraper-destination-ampconfiguration)" : {{AmpConfiguration}},
  "[CloudWatchConfiguration](#cfn-aps-scraper-destination-cloudwatchconfiguration)" : {{CloudWatchConfiguration}}
}
```

### YAML
<a name="aws-properties-aps-scraper-destination-syntax.yaml"></a>

```
  [AmpConfiguration](#cfn-aps-scraper-destination-ampconfiguration): {{
    AmpConfiguration}}
  [CloudWatchConfiguration](#cfn-aps-scraper-destination-cloudwatchconfiguration): {{
    CloudWatchConfiguration}}
```

## Properties
<a name="aws-properties-aps-scraper-destination-properties"></a>

`AmpConfiguration`  <a name="cfn-aps-scraper-destination-ampconfiguration"></a>
The Amazon Managed Service for Prometheus workspace to send metrics to.
*Required*: No
*Type*: [AmpConfiguration](aws-properties-aps-scraper-ampconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CloudWatchConfiguration`  <a name="cfn-aps-scraper-destination-cloudwatchconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [CloudWatchConfiguration](aws-properties-aps-scraper-cloudwatchconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
