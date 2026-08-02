---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterOutputStreamDetails.html
---

# RouterOutputStreamDetails
<a name="API_RouterOutputStreamDetails"></a>

Information about the router output's stream, including connection state and destination details. The specific details provided vary based on the router output type.

## Contents
<a name="API_RouterOutputStreamDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** mediaConnectFlow **   <a name="mediaconnect-Type-RouterOutputStreamDetails-mediaConnectFlow"></a>
Configuration details for a MediaConnect flow when used as a router output destination.
Type: [MediaConnectFlowRouterOutputStreamDetails](API_MediaConnectFlowRouterOutputStreamDetails.md) object
Required: No

 ** mediaLiveInput **   <a name="mediaconnect-Type-RouterOutputStreamDetails-mediaLiveInput"></a>
Configuration details for a MediaLive input when used as a router output destination.
Type: [MediaLiveInputRouterOutputStreamDetails](API_MediaLiveInputRouterOutputStreamDetails.md) object
Required: No

 ** standard **   <a name="mediaconnect-Type-RouterOutputStreamDetails-standard"></a>
Configuration details for a standard router output stream type. Contains information about the destination IP address and connection state for basic output routing.
Type: [StandardRouterOutputStreamDetails](API_StandardRouterOutputStreamDetails.md) object
Required: No

## See Also
<a name="API_RouterOutputStreamDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterOutputStreamDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterOutputStreamDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterOutputStreamDetails)
