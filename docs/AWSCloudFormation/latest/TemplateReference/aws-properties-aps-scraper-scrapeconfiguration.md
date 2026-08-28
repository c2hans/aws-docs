---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-scraper-scrapeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Scraper ScrapeConfiguration
<a name="aws-properties-aps-scraper-scrapeconfiguration"></a>

A scrape configuration for a scraper, base 64 encoded. For more information, see [Scraper configuration](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-configuration) in the *Amazon Managed Service for Prometheus User Guide*.

## Syntax
<a name="aws-properties-aps-scraper-scrapeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-scraper-scrapeconfiguration-syntax.json"></a>

```
{
  "[ConfigurationBlob](#cfn-aps-scraper-scrapeconfiguration-configurationblob)" : {{String}}
}
```

### YAML
<a name="aws-properties-aps-scraper-scrapeconfiguration-syntax.yaml"></a>

```
  [ConfigurationBlob](#cfn-aps-scraper-scrapeconfiguration-configurationblob): {{String}}
```

## Properties
<a name="aws-properties-aps-scraper-scrapeconfiguration-properties"></a>

`ConfigurationBlob`  <a name="cfn-aps-scraper-scrapeconfiguration-configurationblob"></a>
The base 64 encoded scrape configuration file.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
