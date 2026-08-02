---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_FipsEndpoints.html
---

# FipsEndpoints
<a name="API_FipsEndpoints"></a>

FIPS-compliant endpoint URLs for an OpenSearch Serverless collection. These endpoints ensure all data transmission uses FIPS 140-3 validated cryptographic implementations, meeting federal security requirements for government workloads.

## Contents
<a name="API_FipsEndpoints_Contents"></a>

 ** collectionEndpoint **   <a name="opensearchserverless-Type-FipsEndpoints-collectionEndpoint"></a>
FIPS-compliant collection endpoint used to submit index, search, and data upload requests to an OpenSearch Serverless collection. This endpoint uses FIPS 140-3 validated cryptography and is required for federal government workloads.
Type: String
Required: No

 ** dashboardEndpoint **   <a name="opensearchserverless-Type-FipsEndpoints-dashboardEndpoint"></a>
FIPS-compliant endpoint used to access OpenSearch Dashboards. This endpoint uses FIPS 140-3 validated cryptography and is required for federal government workloads that need dashboard visualization capabilities.
Type: String
Required: No

## See Also
<a name="API_FipsEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/FipsEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/FipsEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/FipsEndpoints)
