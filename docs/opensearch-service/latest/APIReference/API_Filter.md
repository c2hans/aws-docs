---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

A filter used to limit results when describing inbound or outbound cross-cluster connections. You can specify multiple values per filter. A cross-cluster connection must match at least one of the specified values for it to be returned from an operation.

## Contents
<a name="API_Filter_Contents"></a>

 ** Name **   <a name="opensearchservice-Type-Filter-Name"></a>
The name of the filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9\-\_\.]+`
Required: No

 ** Values **   <a name="opensearchservice-Type-Filter-Values"></a>
One or more values for the filter.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9\-\_\.]+`
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
