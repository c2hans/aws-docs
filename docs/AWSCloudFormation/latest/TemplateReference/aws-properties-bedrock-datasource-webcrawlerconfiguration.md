---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-webcrawlerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource WebCrawlerConfiguration
<a name="aws-properties-bedrock-datasource-webcrawlerconfiguration"></a>

The configuration of web URLs that you want to crawl. You should be authorized to crawl the URLs.

## Syntax
<a name="aws-properties-bedrock-datasource-webcrawlerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-webcrawlerconfiguration-syntax.json"></a>

```
{
  "[CrawlerLimits](#cfn-bedrock-datasource-webcrawlerconfiguration-crawlerlimits)" : {{WebCrawlerLimits}},
  "[ExclusionFilters](#cfn-bedrock-datasource-webcrawlerconfiguration-exclusionfilters)" : {{[ String, ... ]}},
  "[InclusionFilters](#cfn-bedrock-datasource-webcrawlerconfiguration-inclusionfilters)" : {{[ String, ... ]}},
  "[Scope](#cfn-bedrock-datasource-webcrawlerconfiguration-scope)" : {{String}},
  "[UserAgent](#cfn-bedrock-datasource-webcrawlerconfiguration-useragent)" : {{String}},
  "[UserAgentHeader](#cfn-bedrock-datasource-webcrawlerconfiguration-useragentheader)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-webcrawlerconfiguration-syntax.yaml"></a>

```
  [CrawlerLimits](#cfn-bedrock-datasource-webcrawlerconfiguration-crawlerlimits): {{
    WebCrawlerLimits}}
  [ExclusionFilters](#cfn-bedrock-datasource-webcrawlerconfiguration-exclusionfilters): {{
    - String}}
  [InclusionFilters](#cfn-bedrock-datasource-webcrawlerconfiguration-inclusionfilters): {{
    - String}}
  [Scope](#cfn-bedrock-datasource-webcrawlerconfiguration-scope): {{String}}
  [UserAgent](#cfn-bedrock-datasource-webcrawlerconfiguration-useragent): {{String}}
  [UserAgentHeader](#cfn-bedrock-datasource-webcrawlerconfiguration-useragentheader): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-webcrawlerconfiguration-properties"></a>

`CrawlerLimits`  <a name="cfn-bedrock-datasource-webcrawlerconfiguration-crawlerlimits"></a>
The configuration of crawl limits for the web URLs.
*Required*: No
*Type*: [WebCrawlerLimits](aws-properties-bedrock-datasource-webcrawlerlimits.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExclusionFilters`  <a name="cfn-bedrock-datasource-webcrawlerconfiguration-exclusionfilters"></a>
A list of one or more exclusion regular expression patterns to exclude certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isn’t crawled.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1000 | 25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InclusionFilters`  <a name="cfn-bedrock-datasource-webcrawlerconfiguration-inclusionfilters"></a>
A list of one or more inclusion regular expression patterns to include certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isn’t crawled.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1000 | 25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scope`  <a name="cfn-bedrock-datasource-webcrawlerconfiguration-scope"></a>
The scope of what is crawled for your URLs.
You can choose to crawl only web pages that belong to the same host or primary domain. For example, only web pages that contain the seed URL "https://docs.aws.amazon.com/bedrock/latest/userguide/" and no other domains. You can choose to include sub domains in addition to the host or primary domain. For example, web pages that contain "aws.amazon.com" can also include sub domain "docs.aws.amazon.com".
*Required*: No
*Type*: String
*Allowed values*: `HOST_ONLY | SUBDOMAINS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserAgent`  <a name="cfn-bedrock-datasource-webcrawlerconfiguration-useragent"></a>
Returns the user agent suffix for your web crawler.
*Required*: No
*Type*: String
*Minimum*: `15`
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserAgentHeader`  <a name="cfn-bedrock-datasource-webcrawlerconfiguration-useragentheader"></a>
A string used for identifying the crawler or bot when it accesses a web server. The user agent header value consists of the `bedrockbot`, UUID, and a user agent suffix for your crawler (if one is provided). By default, it is set to `bedrockbot_UUID`. You can optionally append a custom suffix to `bedrockbot_UUID` to allowlist a specific user agent permitted to access your source URLs.
*Required*: No
*Type*: String
*Minimum*: `61`
*Maximum*: `86`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
