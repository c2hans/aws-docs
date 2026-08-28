---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-webcrawlerlimits.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource WebCrawlerLimits
<a name="aws-properties-bedrock-datasource-webcrawlerlimits"></a>

The rate limits for the URLs that you want to crawl. You should be authorized to crawl the URLs.

## Syntax
<a name="aws-properties-bedrock-datasource-webcrawlerlimits-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-webcrawlerlimits-syntax.json"></a>

```
{
  "[MaxPages](#cfn-bedrock-datasource-webcrawlerlimits-maxpages)" : {{Integer}},
  "[RateLimit](#cfn-bedrock-datasource-webcrawlerlimits-ratelimit)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-webcrawlerlimits-syntax.yaml"></a>

```
  [MaxPages](#cfn-bedrock-datasource-webcrawlerlimits-maxpages): {{Integer}}
  [RateLimit](#cfn-bedrock-datasource-webcrawlerlimits-ratelimit): {{Integer}}
```

## Properties
<a name="aws-properties-bedrock-datasource-webcrawlerlimits-properties"></a>

`MaxPages`  <a name="cfn-bedrock-datasource-webcrawlerlimits-maxpages"></a>
 The max number of web pages crawled from your source URLs, up to 25,000 pages. If the web pages exceed this limit, the data source sync will fail and no web pages will be ingested.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RateLimit`  <a name="cfn-bedrock-datasource-webcrawlerlimits-ratelimit"></a>
The max rate at which pages are crawled, up to 300 per minute per host.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
