---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_VpcEndpoint.html
---

# VpcEndpoint
<a name="API_osis_VpcEndpoint"></a>

An OpenSearch Ingestion-managed VPC endpoint that will access one or more pipelines.

## Contents
<a name="API_osis_VpcEndpoint_Contents"></a>

 ** VpcEndpointId **   <a name="opensearchservice-Type-osis_VpcEndpoint-VpcEndpointId"></a>
The unique identifier of the endpoint.
Type: String
Required: No

 ** VpcId **   <a name="opensearchservice-Type-osis_VpcEndpoint-VpcId"></a>
The ID for your VPC. AWS PrivateLink generates this value when you create a VPC.
Type: String
Required: No

 ** VpcOptions **   <a name="opensearchservice-Type-osis_VpcEndpoint-VpcOptions"></a>
Information about the VPC, including associated subnets and security groups.
Type: [VpcOptions](API_osis_VpcOptions.md) object
Required: No

## See Also
<a name="API_osis_VpcEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/VpcEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/VpcEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/VpcEndpoint)
