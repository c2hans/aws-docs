---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_StandardSourceEndpointNetworkingConfiguration.html
---

# StandardSourceEndpointNetworkingConfiguration
<a name="API_StandardSourceEndpointNetworkingConfiguration"></a>

The networking configuration for a standard source endpoint. This is a union type, so exactly one of its members is set: `public` for a publicly accessible endpoint, or `vpc` for an endpoint in a virtual private cloud (VPC).

## Contents
<a name="API_StandardSourceEndpointNetworkingConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** public **   <a name="mediaconnect-Type-StandardSourceEndpointNetworkingConfiguration-public"></a>
The configuration for a publicly accessible source endpoint.
Type: [PublicSourceEndpointNetworkingConfiguration](API_PublicSourceEndpointNetworkingConfiguration.md) object
Required: No

 ** vpc **   <a name="mediaconnect-Type-StandardSourceEndpointNetworkingConfiguration-vpc"></a>
The configuration for a source endpoint in a virtual private cloud (VPC).
Type: [VpcSourceEndpointNetworkingConfiguration](API_VpcSourceEndpointNetworkingConfiguration.md) object
Required: No

## See Also
<a name="API_StandardSourceEndpointNetworkingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/StandardSourceEndpointNetworkingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/StandardSourceEndpointNetworkingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/StandardSourceEndpointNetworkingConfiguration)
