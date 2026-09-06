---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DirectQueryDataSource.html
---

# DirectQueryDataSource
<a name="API_DirectQueryDataSource"></a>

 The configuration details for a data source that can be directly queried.

## Contents
<a name="API_DirectQueryDataSource_Contents"></a>

 ** DataSourceArn **   <a name="opensearchservice-Type-DirectQueryDataSource-DataSourceArn"></a>
 The unique, system-generated identifier that represents the data source.
Type: String
Required: No

 ** DataSourceName **   <a name="opensearchservice-Type-DirectQueryDataSource-DataSourceName"></a>
 A unique, user-defined label to identify the data source within your OpenSearch Service environment.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 80.
Pattern: `[a-z][a-z0-9_]+`
Required: No

 ** DataSourceType **   <a name="opensearchservice-Type-DirectQueryDataSource-DataSourceType"></a>
 The supported AWS service that is used as the source for direct queries in OpenSearch Service.
Type: [DirectQueryDataSourceType](API_DirectQueryDataSourceType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** Description **   <a name="opensearchservice-Type-DirectQueryDataSource-Description"></a>
 A description that provides additional context and details about the data source.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^([a-zA-Z0-9_])*[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`
Required: No

 ** OpenSearchArns **   <a name="opensearchservice-Type-DirectQueryDataSource-OpenSearchArns"></a>
 A list of Amazon Resource Names (ARNs) for the OpenSearch collections that are associated with the direct query data source.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** TagList **   <a name="opensearchservice-Type-DirectQueryDataSource-TagList"></a>
 A list of tags attached to a direct query data source.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_DirectQueryDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DirectQueryDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DirectQueryDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DirectQueryDataSource)
