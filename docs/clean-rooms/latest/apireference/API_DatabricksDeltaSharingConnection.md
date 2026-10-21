---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DatabricksDeltaSharingConnection.html
---

# DatabricksDeltaSharingConnection
<a name="API_DatabricksDeltaSharingConnection"></a>

Details about Delta Sharing Connector for Databricks

## Contents
<a name="API_DatabricksDeltaSharingConnection_Contents"></a>

 ** deltaShareEndpoint **   <a name="API-Type-DatabricksDeltaSharingConnection-deltaShareEndpoint"></a>
The base URL of a Delta Sharing server that hosts shared datasets.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1024.
Pattern: `https://(?:[a-zA-Z0-9.-]+\.cloud\.databricks\.com/api/2\.0/delta-sharing|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\.opensharing\.[a-z0-9-]+\.cloud\.databricks\.com/api/2\.0/opensharing)/metastores/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/recipients/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** shareName **   <a name="API-Type-DatabricksDeltaSharingConnection-shareName"></a>
Name of the Share used for OpenSharing (Delta Sharing) the Databricks Table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{M}\p{N}\p{Pc}\p{Pd}]+`
Required: Yes

## See Also
<a name="API_DatabricksDeltaSharingConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/DatabricksDeltaSharingConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/DatabricksDeltaSharingConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/DatabricksDeltaSharingConnection)
