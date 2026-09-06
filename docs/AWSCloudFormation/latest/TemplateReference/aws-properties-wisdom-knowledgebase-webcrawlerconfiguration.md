---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-webcrawlerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase WebCrawlerConfiguration
<a name="aws-properties-wisdom-knowledgebase-webcrawlerconfiguration"></a>

The configuration details for the web data source.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-webcrawlerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-webcrawlerconfiguration-syntax.json"></a>

```
{
  "[CrawlerLimits](#cfn-wisdom-knowledgebase-webcrawlerconfiguration-crawlerlimits)" : {{CrawlerLimits}},
  "[ExclusionFilters](#cfn-wisdom-knowledgebase-webcrawlerconfiguration-exclusionfilters)" : {{[ String, ... ]}},
  "[InclusionFilters](#cfn-wisdom-knowledgebase-webcrawlerconfiguration-inclusionfilters)" : {{[ String, ... ]}},
  "[Scope](#cfn-wisdom-knowledgebase-webcrawlerconfiguration-scope)" : {{String}},
  "[UrlConfiguration](#cfn-wisdom-knowledgebase-webcrawlerconfiguration-urlconfiguration)" : {{UrlConfiguration}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-webcrawlerconfiguration-syntax.yaml"></a>

```
  [CrawlerLimits](#cfn-wisdom-knowledgebase-webcrawlerconfiguration-crawlerlimits): {{
    CrawlerLimits}}
  [ExclusionFilters](#cfn-wisdom-knowledgebase-webcrawlerconfiguration-exclusionfilters): {{
    - String}}
  [InclusionFilters](#cfn-wisdom-knowledgebase-webcrawlerconfiguration-inclusionfilters): {{
    - String}}
  [Scope](#cfn-wisdom-knowledgebase-webcrawlerconfiguration-scope): {{String}}
  [UrlConfiguration](#cfn-wisdom-knowledgebase-webcrawlerconfiguration-urlconfiguration): {{
    UrlConfiguration}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-webcrawlerconfiguration-properties"></a>

`CrawlerLimits`  <a name="cfn-wisdom-knowledgebase-webcrawlerconfiguration-crawlerlimits"></a>
The configuration of crawl limits for the web URLs.
*Required*: No
*Type*: [CrawlerLimits](aws-properties-wisdom-knowledgebase-crawlerlimits.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExclusionFilters`  <a name="cfn-wisdom-knowledgebase-webcrawlerconfiguration-exclusionfilters"></a>
A list of one or more exclusion regular expression patterns to exclude certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isn’t crawled.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InclusionFilters`  <a name="cfn-wisdom-knowledgebase-webcrawlerconfiguration-inclusionfilters"></a>
A list of one or more inclusion regular expression patterns to include certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isn’t crawled.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Scope`  <a name="cfn-wisdom-knowledgebase-webcrawlerconfiguration-scope"></a>
The scope of what is crawled for your URLs. You can choose to crawl only web pages that belong to the same host or primary domain. For example, only web pages that contain the seed URL `https://docs.aws.amazon.com/bedrock/latest/userguide/` and no other domains. You can choose to include sub domains in addition to the host or primary domain. For example, web pages that contain `aws.amazon.com` can also include sub domain `docs.aws.amazon.com`.
*Required*: No
*Type*: String
*Allowed values*: `HOST_ONLY | SUBDOMAINS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UrlConfiguration`  <a name="cfn-wisdom-knowledgebase-webcrawlerconfiguration-urlconfiguration"></a>
The configuration of the URL/URLs for the web content that you want to crawl. You should be authorized to crawl the URLs.
*Required*: Yes
*Type*: [UrlConfiguration](aws-properties-wisdom-knowledgebase-urlconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
