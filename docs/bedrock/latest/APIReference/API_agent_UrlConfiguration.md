---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UrlConfiguration.html
---

# UrlConfiguration
<a name="API_agent_UrlConfiguration"></a>

The configuration of web URLs that you want to crawl. You should be authorized to crawl the URLs.

## Contents
<a name="API_agent_UrlConfiguration_Contents"></a>

 ** seedUrls **   <a name="bedrock-Type-agent_UrlConfiguration-seedUrls"></a>
One or more seed or starting point URLs.
Type: Array of [SeedUrl](API_agent_SeedUrl.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## See Also
<a name="API_agent_UrlConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/UrlConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/UrlConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/UrlConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
