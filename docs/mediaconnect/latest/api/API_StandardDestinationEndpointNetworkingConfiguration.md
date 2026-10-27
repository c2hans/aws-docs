---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_StandardDestinationEndpointNetworkingConfiguration.html
---

# StandardDestinationEndpointNetworkingConfiguration
<a name="API_StandardDestinationEndpointNetworkingConfiguration"></a>

The networking configuration for a standard destination endpoint. This is a union type, so exactly one of its members is set: `public` for a publicly accessible endpoint, or `vpc` for an endpoint in a virtual private cloud (VPC).

## Contents
<a name="API_StandardDestinationEndpointNetworkingConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** public **   <a name="mediaconnect-Type-StandardDestinationEndpointNetworkingConfiguration-public"></a>
The configuration for a publicly accessible destination endpoint.
Type: [PublicDestinationEndpointNetworkingConfiguration](API_PublicDestinationEndpointNetworkingConfiguration.md) object
Required: No

 ** vpc **   <a name="mediaconnect-Type-StandardDestinationEndpointNetworkingConfiguration-vpc"></a>
The configuration for a destination endpoint in a virtual private cloud (VPC).
Type: [VpcDestinationEndpointNetworkingConfiguration](API_VpcDestinationEndpointNetworkingConfiguration.md) object
Required: No

## See Also
<a name="API_StandardDestinationEndpointNetworkingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/StandardDestinationEndpointNetworkingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/StandardDestinationEndpointNetworkingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/StandardDestinationEndpointNetworkingConfiguration)
