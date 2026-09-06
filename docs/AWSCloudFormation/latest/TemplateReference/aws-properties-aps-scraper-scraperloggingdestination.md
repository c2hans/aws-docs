---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-scraper-scraperloggingdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Scraper ScraperLoggingDestination
<a name="aws-properties-aps-scraper-scraperloggingdestination"></a>

The destination where scraper logs are sent.

## Syntax
<a name="aws-properties-aps-scraper-scraperloggingdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-scraper-scraperloggingdestination-syntax.json"></a>

```
{
  "[CloudWatchLogs](#cfn-aps-scraper-scraperloggingdestination-cloudwatchlogs)" : {{CloudWatchLogDestination}}
}
```

### YAML
<a name="aws-properties-aps-scraper-scraperloggingdestination-syntax.yaml"></a>

```
  [CloudWatchLogs](#cfn-aps-scraper-scraperloggingdestination-cloudwatchlogs): {{
    CloudWatchLogDestination}}
```

## Properties
<a name="aws-properties-aps-scraper-scraperloggingdestination-properties"></a>

`CloudWatchLogs`  <a name="cfn-aps-scraper-scraperloggingdestination-cloudwatchlogs"></a>
The CloudWatch Logs configuration for the scraper logging destination.
*Required*: No
*Type*: [CloudWatchLogDestination](aws-properties-aps-scraper-cloudwatchlogdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
