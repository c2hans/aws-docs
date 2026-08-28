---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ConfluenceDataSourceConfiguration.html
---

# ConfluenceDataSourceConfiguration
<a name="API_agent_ConfluenceDataSourceConfiguration"></a>

The configuration information to connect to Confluence as your data source for self-managed knowledge bases.

## Contents
<a name="API_agent_ConfluenceDataSourceConfiguration_Contents"></a>

 ** sourceConfiguration **   <a name="bedrock-Type-agent_ConfluenceDataSourceConfiguration-sourceConfiguration"></a>
The endpoint information to connect to your Confluence data source.
Type: [ConfluenceSourceConfiguration](API_agent_ConfluenceSourceConfiguration.md) object
Required: Yes

 ** crawlerConfiguration **   <a name="bedrock-Type-agent_ConfluenceDataSourceConfiguration-crawlerConfiguration"></a>
The configuration of the Confluence content. For example, configuring specific types of Confluence content.
Type: [ConfluenceCrawlerConfiguration](API_agent_ConfluenceCrawlerConfiguration.md) object
Required: No

## See Also
<a name="API_agent_ConfluenceDataSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ConfluenceDataSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ConfluenceDataSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ConfluenceDataSourceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
