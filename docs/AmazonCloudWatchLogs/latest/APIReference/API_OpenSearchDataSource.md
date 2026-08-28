---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_OpenSearchDataSource.html
---

# OpenSearchDataSource
<a name="API_OpenSearchDataSource"></a>

This structure contains information about the OpenSearch Service data source used for this integration. This data source was created as part of the integration setup. An OpenSearch Service data source defines the source and destination for OpenSearch Service queries. It includes the role required to execute queries and write to collections.

For more information about OpenSearch Service data sources , see [Creating OpenSearch Service data source integrations with Amazon S3.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3-creating.html)

## Contents
<a name="API_OpenSearchDataSource_Contents"></a>

 ** dataSourceName **   <a name="CWL-Type-OpenSearchDataSource-dataSourceName"></a>
The name of the OpenSearch Service data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** status **   <a name="CWL-Type-OpenSearchDataSource-status"></a>
This structure contains information about the status of this OpenSearch Service resource.
Type: [OpenSearchResourceStatus](API_OpenSearchResourceStatus.md) object
Required: No

## See Also
<a name="API_OpenSearchDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/OpenSearchDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/OpenSearchDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/OpenSearchDataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
