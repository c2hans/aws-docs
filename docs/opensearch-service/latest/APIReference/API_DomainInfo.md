---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DomainInfo.html
---

# DomainInfo
<a name="API_DomainInfo"></a>

Information about an OpenSearch Service domain.

## Contents
<a name="API_DomainInfo_Contents"></a>

 ** DomainName **   <a name="opensearchservice-Type-DomainInfo-DomainName"></a>
Name of the domain.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: No

 ** EngineType **   <a name="opensearchservice-Type-DomainInfo-EngineType"></a>
The type of search engine that the domain is running.`OpenSearch` for an OpenSearch engine, or `Elasticsearch` for a legacy Elasticsearch OSS engine.
Type: String
Valid Values: `OpenSearch | Elasticsearch`
Required: No

## See Also
<a name="API_DomainInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DomainInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DomainInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DomainInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
