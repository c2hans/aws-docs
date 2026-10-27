---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SourceEndpointAssociatedResourceDetails.html
---

# SourceEndpointAssociatedResourceDetails
<a name="API_SourceEndpointAssociatedResourceDetails"></a>

The details of the resource that is associated with a source endpoint. This is a union type, so exactly one of its members is set, depending on the type of the source endpoint.

## Contents
<a name="API_SourceEndpointAssociatedResourceDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** routerOutput **   <a name="mediaconnect-Type-SourceEndpointAssociatedResourceDetails-routerOutput"></a>
The associated resource details for a source endpoint that represents a router output.
Type: [RouterOutputSourceEndpointAssociatedResourceDetails](API_RouterOutputSourceEndpointAssociatedResourceDetails.md) object
Required: No

 ** standard **   <a name="mediaconnect-Type-SourceEndpointAssociatedResourceDetails-standard"></a>
The associated resource details for a standard source endpoint.
Type: [StandardSourceEndpointAssociatedResourceDetails](API_StandardSourceEndpointAssociatedResourceDetails.md) object
Required: No

## See Also
<a name="API_SourceEndpointAssociatedResourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SourceEndpointAssociatedResourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SourceEndpointAssociatedResourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SourceEndpointAssociatedResourceDetails)
