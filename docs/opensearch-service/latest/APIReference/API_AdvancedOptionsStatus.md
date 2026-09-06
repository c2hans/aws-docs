---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AdvancedOptionsStatus.html
---

# AdvancedOptionsStatus
<a name="API_AdvancedOptionsStatus"></a>

Status of the advanced options for the specified domain. The following options are available:
+  `"rest.action.multi.allow_explicit_index": "true" | "false"` - Note the use of a string rather than a boolean. Specifies whether explicit references to indexes are allowed inside the body of HTTP requests. If you want to configure access policies for domain sub-resources, such as specific indexes and domain APIs, you must disable this property. Default is true.
+  `"indices.fielddata.cache.size": "80" ` - Note the use of a string rather than a boolean. Specifies the percentage of heap space allocated to field data. Default is unbounded.
+  `"indices.query.bool.max_clause_count": "1024"` - Note the use of a string rather than a boolean. Specifies the maximum number of clauses allowed in a Lucene boolean query. Default is 1,024. Queries with more than the permitted number of clauses result in a `TooManyClauses` error.
+  `"override_main_response_version": "true" | "false"` - Note the use of a string rather than a boolean. Specifies whether the domain reports its version as 7.10 to allow Elasticsearch OSS clients and plugins to continue working with it. Default is false when creating a domain and true when upgrading a domain.

For more information, see [Advanced cluster parameters](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options).

## Contents
<a name="API_AdvancedOptionsStatus_Contents"></a>

 ** Options **   <a name="opensearchservice-Type-AdvancedOptionsStatus-Options"></a>
The status of advanced options for the specified domain.
Type: String to string map
Required: Yes

 ** Status **   <a name="opensearchservice-Type-AdvancedOptionsStatus-Status"></a>
The status of advanced options for the specified domain.
Type: [OptionStatus](API_OptionStatus.md) object
Required: Yes

## See Also
<a name="API_AdvancedOptionsStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AdvancedOptionsStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AdvancedOptionsStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AdvancedOptionsStatus)
