---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DataSourceDetails.html
---

# DataSourceDetails
<a name="API_DataSourceDetails"></a>

Details about a direct-query data source.

## Contents
<a name="API_DataSourceDetails_Contents"></a>

 ** DataSourceType **   <a name="opensearchservice-Type-DataSourceDetails-DataSourceType"></a>
The type of data source.
Type: [DataSourceType](API_DataSourceType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** Description **   <a name="opensearchservice-Type-DataSourceDetails-Description"></a>
A description of the data source.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^([a-zA-Z0-9_])*[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`
Required: No

 ** Name **   <a name="opensearchservice-Type-DataSourceDetails-Name"></a>
The name of the data source.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 80.
Pattern: `[a-z][a-z0-9_]+`
Required: No

 ** Status **   <a name="opensearchservice-Type-DataSourceDetails-Status"></a>
The status of the data source.
Type: String
Valid Values: `ACTIVE | DISABLED`
Required: No

## See Also
<a name="API_DataSourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DataSourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DataSourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DataSourceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
