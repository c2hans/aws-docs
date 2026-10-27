---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_DestinationEndpointAssociatedResourceDetails.html
---

# DestinationEndpointAssociatedResourceDetails
<a name="API_DestinationEndpointAssociatedResourceDetails"></a>

The details of the resource that is associated with a destination endpoint. This is a union type, so exactly one of its members is set, depending on the type of the destination endpoint.

## Contents
<a name="API_DestinationEndpointAssociatedResourceDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** routerInput **   <a name="mediaconnect-Type-DestinationEndpointAssociatedResourceDetails-routerInput"></a>
The associated resource details for a destination endpoint that represents a router input.
Type: [RouterInputDestinationEndpointAssociatedResourceDetails](API_RouterInputDestinationEndpointAssociatedResourceDetails.md) object
Required: No

 ** standard **   <a name="mediaconnect-Type-DestinationEndpointAssociatedResourceDetails-standard"></a>
The associated resource details for a standard destination endpoint.
Type: [StandardDestinationEndpointAssociatedResourceDetails](API_StandardDestinationEndpointAssociatedResourceDetails.md) object
Required: No

## See Also
<a name="API_DestinationEndpointAssociatedResourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/DestinationEndpointAssociatedResourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/DestinationEndpointAssociatedResourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/DestinationEndpointAssociatedResourceDetails)
