---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterInputDestinationEndpointAssociatedResourceDetails.html
---

# RouterInputDestinationEndpointAssociatedResourceDetails
<a name="API_RouterInputDestinationEndpointAssociatedResourceDetails"></a>

The details of the router input that is associated with a destination endpoint.

## Contents
<a name="API_RouterInputDestinationEndpointAssociatedResourceDetails_Contents"></a>

 ** maximumBitrate **   <a name="mediaconnect-Type-RouterInputDestinationEndpointAssociatedResourceDetails-maximumBitrate"></a>
The maximum bitrate of the router input, in bits per second.
Type: Long
Required: Yes

 ** messages **   <a name="mediaconnect-Type-RouterInputDestinationEndpointAssociatedResourceDetails-messages"></a>
The status messages for the router input.
Type: Array of [RouterInputMessage](API_RouterInputMessage.md) objects
Required: Yes

 ** name **   <a name="mediaconnect-Type-RouterInputDestinationEndpointAssociatedResourceDetails-name"></a>
The name of the router input.
Type: String
Required: Yes

 ** state **   <a name="mediaconnect-Type-RouterInputDestinationEndpointAssociatedResourceDetails-state"></a>
The state of the router input.
Type: String
Valid Values: `CREATING | STANDBY | STARTING | ACTIVE | STOPPING | DELETING | UPDATING | ERROR | RECOVERING | MIGRATING`
Required: Yes

## See Also
<a name="API_RouterInputDestinationEndpointAssociatedResourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterInputDestinationEndpointAssociatedResourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterInputDestinationEndpointAssociatedResourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterInputDestinationEndpointAssociatedResourceDetails)
