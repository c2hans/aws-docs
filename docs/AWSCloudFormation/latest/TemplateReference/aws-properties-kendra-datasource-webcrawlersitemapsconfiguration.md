---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-webcrawlersitemapsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource WebCrawlerSiteMapsConfiguration
<a name="aws-properties-kendra-datasource-webcrawlersitemapsconfiguration"></a>

Provides the configuration information of the sitemap URLs to crawl.

 *When selecting websites to index, you must adhere to the [Amazon Acceptable Use Policy](https://aws.amazon.com/aup/) and all other Amazon terms. Remember that you must only use the Amazon Kendra web crawler to index your own webpages, or webpages that you have authorization to index.*

## Syntax
<a name="aws-properties-kendra-datasource-webcrawlersitemapsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-webcrawlersitemapsconfiguration-syntax.json"></a>

```
{
  "[SiteMaps](#cfn-kendra-datasource-webcrawlersitemapsconfiguration-sitemaps)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-webcrawlersitemapsconfiguration-syntax.yaml"></a>

```
  [SiteMaps](#cfn-kendra-datasource-webcrawlersitemapsconfiguration-sitemaps): {{
    - String}}
```

## Properties
<a name="aws-properties-kendra-datasource-webcrawlersitemapsconfiguration-properties"></a>

`SiteMaps`  <a name="cfn-kendra-datasource-webcrawlersitemapsconfiguration-sitemaps"></a>
The list of sitemap URLs of the websites you want to crawl.
The list can include a maximum of three sitemap URLs.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
