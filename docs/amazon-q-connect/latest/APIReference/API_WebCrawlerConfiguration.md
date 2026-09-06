---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_WebCrawlerConfiguration.html
---

# WebCrawlerConfiguration
<a name="API_amazon-q-connect_WebCrawlerConfiguration"></a>

The configuration details for the web data source.

## Contents
<a name="API_amazon-q-connect_WebCrawlerConfiguration_Contents"></a>

 ** urlConfiguration **   <a name="connect-Type-amazon-q-connect_WebCrawlerConfiguration-urlConfiguration"></a>
The configuration of the URL/URLs for the web content that you want to crawl. You should be authorized to crawl the URLs.
Type: [UrlConfiguration](API_amazon-q-connect_UrlConfiguration.md) object
Required: Yes

 ** crawlerLimits **   <a name="connect-Type-amazon-q-connect_WebCrawlerConfiguration-crawlerLimits"></a>
The configuration of crawl limits for the web URLs.
Type: [WebCrawlerLimits](API_amazon-q-connect_WebCrawlerLimits.md) object
Required: No

 ** exclusionFilters **   <a name="connect-Type-amazon-q-connect_WebCrawlerConfiguration-exclusionFilters"></a>
A list of one or more exclusion regular expression patterns to exclude certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isn’t crawled.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** inclusionFilters **   <a name="connect-Type-amazon-q-connect_WebCrawlerConfiguration-inclusionFilters"></a>
A list of one or more inclusion regular expression patterns to include certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isn’t crawled.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** scope **   <a name="connect-Type-amazon-q-connect_WebCrawlerConfiguration-scope"></a>
The scope of what is crawled for your URLs. You can choose to crawl only web pages that belong to the same host or primary domain. For example, only web pages that contain the seed URL `https://docs.aws.amazon.com/bedrock/latest/userguide/` and no other domains. You can choose to include sub domains in addition to the host or primary domain. For example, web pages that contain `aws.amazon.com` can also include sub domain `docs.aws.amazon.com`.
Type: String
Valid Values: `HOST_ONLY | SUBDOMAINS`
Required: No

## See Also
<a name="API_amazon-q-connect_WebCrawlerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/WebCrawlerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/WebCrawlerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/WebCrawlerConfiguration)
