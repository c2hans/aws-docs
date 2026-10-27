---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SourceEndpointConfiguration.html
---

# SourceEndpointConfiguration
<a name="API_SourceEndpointConfiguration"></a>

The configuration settings for a source endpoint. This is a union type, so exactly one of its members is set, depending on the type of the source endpoint.

## Contents
<a name="API_SourceEndpointConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** routerOutput **   <a name="mediaconnect-Type-SourceEndpointConfiguration-routerOutput"></a>
The configuration settings for a source endpoint that represents a router output.
Type: [RouterOutputSourceEndpointConfiguration](API_RouterOutputSourceEndpointConfiguration.md) object
Required: No

 ** standard **   <a name="mediaconnect-Type-SourceEndpointConfiguration-standard"></a>
The configuration settings for a standard source endpoint, which represents an external source.
Type: [StandardSourceEndpointConfiguration](API_StandardSourceEndpointConfiguration.md) object
Required: No

## See Also
<a name="API_SourceEndpointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SourceEndpointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SourceEndpointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SourceEndpointConfiguration)
