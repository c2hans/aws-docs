---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterOutputSourceEndpointAssociatedResourceDetails.html
---

# RouterOutputSourceEndpointAssociatedResourceDetails
<a name="API_RouterOutputSourceEndpointAssociatedResourceDetails"></a>

The details of the router output that is associated with a source endpoint.

## Contents
<a name="API_RouterOutputSourceEndpointAssociatedResourceDetails_Contents"></a>

 ** maximumBitrate **   <a name="mediaconnect-Type-RouterOutputSourceEndpointAssociatedResourceDetails-maximumBitrate"></a>
The maximum bitrate of the router output, in bits per second.
Type: Long
Required: Yes

 ** messages **   <a name="mediaconnect-Type-RouterOutputSourceEndpointAssociatedResourceDetails-messages"></a>
The status messages for the router output.
Type: Array of [RouterOutputMessage](API_RouterOutputMessage.md) objects
Required: Yes

 ** name **   <a name="mediaconnect-Type-RouterOutputSourceEndpointAssociatedResourceDetails-name"></a>
The name of the router output.
Type: String
Required: Yes

 ** state **   <a name="mediaconnect-Type-RouterOutputSourceEndpointAssociatedResourceDetails-state"></a>
The state of the router output.
Type: String
Valid Values: `CREATING | STANDBY | STARTING | ACTIVE | STOPPING | DELETING | UPDATING | ERROR | RECOVERING | MIGRATING`
Required: Yes

## See Also
<a name="API_RouterOutputSourceEndpointAssociatedResourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterOutputSourceEndpointAssociatedResourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterOutputSourceEndpointAssociatedResourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterOutputSourceEndpointAssociatedResourceDetails)
