---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_NdiSourceMetadataInfo.html
---

# NdiSourceMetadataInfo
<a name="API_NdiSourceMetadataInfo"></a>

 Comprehensive information about the NDI® source that's associated with a flow. This includes the currently active NDI source, a list of all discovered NDI senders, metadata about the media streams, and any relevant status messages.

## Contents
<a name="API_NdiSourceMetadataInfo_Contents"></a>

 ** discoveredSources **   <a name="mediaconnect-Type-NdiSourceMetadataInfo-discoveredSources"></a>
 A list of the available upstream NDI senders aggregated from all of your configured discovery servers.
Type: Array of [NdiSourceInfo](API_NdiSourceInfo.md) objects
Required: Yes

 ** mediaInfo **   <a name="mediaconnect-Type-NdiSourceMetadataInfo-mediaInfo"></a>
 Detailed information about the media streams (video, audio, and so on) that are part of the active NDI source.
Type: [NdiMediaInfo](API_NdiMediaInfo.md) object
Required: Yes

 ** messages **   <a name="mediaconnect-Type-NdiSourceMetadataInfo-messages"></a>
 Any status messages or error codes related to the NDI source and its metadata.
Type: Array of [MessageDetail](API_MessageDetail.md) objects
Required: Yes

 ** activeSource **   <a name="mediaconnect-Type-NdiSourceMetadataInfo-activeSource"></a>
 The connected NDI sender that's currently sending source content to the flow's NDI source.
Type: [NdiSourceInfo](API_NdiSourceInfo.md) object
Required: No

## See Also
<a name="API_NdiSourceMetadataInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/NdiSourceMetadataInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/NdiSourceMetadataInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/NdiSourceMetadataInfo)
