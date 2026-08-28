---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ConnectionProperties.html
---

# ConnectionProperties
<a name="API_ConnectionProperties"></a>

The connection properties of an outbound connection.

## Contents
<a name="API_ConnectionProperties_Contents"></a>

 ** CrossClusterSearch **   <a name="opensearchservice-Type-ConnectionProperties-CrossClusterSearch"></a>
The connection properties for cross cluster search.
Type: [CrossClusterSearchConnectionProperties](API_CrossClusterSearchConnectionProperties.md) object
Required: No

 ** Endpoint **   <a name="opensearchservice-Type-ConnectionProperties-Endpoint"></a>
The endpoint of the remote domain. Applicable for VPC\_ENDPOINT connection mode.
Type: String
Pattern: `^[A-Za-z0-9\-\.]+$`
Required: No

## See Also
<a name="API_ConnectionProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ConnectionProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ConnectionProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ConnectionProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
