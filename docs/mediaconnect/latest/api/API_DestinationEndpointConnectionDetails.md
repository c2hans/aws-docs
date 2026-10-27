---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_DestinationEndpointConnectionDetails.html
---

# DestinationEndpointConnectionDetails
<a name="API_DestinationEndpointConnectionDetails"></a>

The connection details for a destination endpoint. After the destination endpoint connects to a source endpoint, MediaConnect populates these details to describe the connected source. This is a union type, so exactly one of its members is set, depending on the destination endpoint type.

## Contents
<a name="API_DestinationEndpointConnectionDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** routerInput **   <a name="mediaconnect-Type-DestinationEndpointConnectionDetails-routerInput"></a>
The connection details for a destination endpoint that represents a router input.
Type: [RouterInputDestinationEndpointConnectionDetails](API_RouterInputDestinationEndpointConnectionDetails.md) object
Required: No

 ** standard **   <a name="mediaconnect-Type-DestinationEndpointConnectionDetails-standard"></a>
The connection details for a standard destination endpoint.
Type: [StandardDestinationEndpointConnectionDetails](API_StandardDestinationEndpointConnectionDetails.md) object
Required: No

## See Also
<a name="API_DestinationEndpointConnectionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/DestinationEndpointConnectionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/DestinationEndpointConnectionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/DestinationEndpointConnectionDetails)
