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
