---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_DestinationEndpointConfiguration.html
---

# DestinationEndpointConfiguration
<a name="API_DestinationEndpointConfiguration"></a>

The configuration settings for a destination endpoint. This is a union type, so exactly one of its members is set, depending on the type of the destination endpoint.

## Contents
<a name="API_DestinationEndpointConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** routerInput **   <a name="mediaconnect-Type-DestinationEndpointConfiguration-routerInput"></a>
The configuration settings for a destination endpoint that represents a router input.
Type: [RouterInputDestinationEndpointConfiguration](API_RouterInputDestinationEndpointConfiguration.md) object
Required: No

 ** standard **   <a name="mediaconnect-Type-DestinationEndpointConfiguration-standard"></a>
The configuration settings for a standard destination endpoint, which represents an external destination.
Type: [StandardDestinationEndpointConfiguration](API_StandardDestinationEndpointConfiguration.md) object
Required: No

## See Also
<a name="API_DestinationEndpointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/DestinationEndpointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/DestinationEndpointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/DestinationEndpointConfiguration)
