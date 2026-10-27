---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SourceEndpointConnectionDetails.html
---

# SourceEndpointConnectionDetails
<a name="API_SourceEndpointConnectionDetails"></a>

The connection details for a source endpoint. After the source endpoint connects to a destination endpoint, MediaConnect populates these details to describe the connected destination and how the source delivers content to it. This is a union type, so exactly one of its members is set, depending on the source endpoint type.

## Contents
<a name="API_SourceEndpointConnectionDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** routerOutput **   <a name="mediaconnect-Type-SourceEndpointConnectionDetails-routerOutput"></a>
The connection details for a source endpoint that represents a router output.
Type: [RouterOutputSourceEndpointConnectionDetails](API_RouterOutputSourceEndpointConnectionDetails.md) object
Required: No

 ** standard **   <a name="mediaconnect-Type-SourceEndpointConnectionDetails-standard"></a>
The connection details for a standard source endpoint.
Type: [StandardSourceEndpointConnectionDetails](API_StandardSourceEndpointConnectionDetails.md) object
Required: No

## See Also
<a name="API_SourceEndpointConnectionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SourceEndpointConnectionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SourceEndpointConnectionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SourceEndpointConnectionDetails)
