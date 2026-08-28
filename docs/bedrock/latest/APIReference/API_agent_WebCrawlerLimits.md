---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_WebCrawlerLimits.html
---

# WebCrawlerLimits
<a name="API_agent_WebCrawlerLimits"></a>

The rate limits for the URLs that you want to crawl. You should be authorized to crawl the URLs.

## Contents
<a name="API_agent_WebCrawlerLimits_Contents"></a>

 ** maxPages **   <a name="bedrock-Type-agent_WebCrawlerLimits-maxPages"></a>
 The max number of web pages crawled from your source URLs, up to 25,000 pages. If the web pages exceed this limit, the data source sync will fail and no web pages will be ingested.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** rateLimit **   <a name="bedrock-Type-agent_WebCrawlerLimits-rateLimit"></a>
The max rate at which pages are crawled, up to 300 per minute per host.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 300.
Required: No

## See Also
<a name="API_agent_WebCrawlerLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/WebCrawlerLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/WebCrawlerLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/WebCrawlerLimits)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
