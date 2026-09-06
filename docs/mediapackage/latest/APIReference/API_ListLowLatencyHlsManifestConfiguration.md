---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListLowLatencyHlsManifestConfiguration.html
---

# ListLowLatencyHlsManifestConfiguration
<a name="API_ListLowLatencyHlsManifestConfiguration"></a>

List the low-latency HTTP live streaming (HLS) manifest configuration.

## Contents
<a name="API_ListLowLatencyHlsManifestConfiguration_Contents"></a>

 ** ManifestName **   <a name="mediapackage-Type-ListLowLatencyHlsManifestConfiguration-ManifestName"></a>
A short short string that's appended to the endpoint URL. The manifest name creates a unique path to this endpoint. If you don't enter a value, MediaPackage uses the default manifest name, index. MediaPackage automatically inserts the format extension, such as .m3u8. You can't use the same manifest name if you use HLS manifest and low-latency HLS manifest. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** ChildManifestName **   <a name="mediapackage-Type-ListLowLatencyHlsManifestConfiguration-ChildManifestName"></a>
A short string that's appended to the endpoint URL. The child manifest name creates a unique path to this endpoint. If you don't enter a value, MediaPackage uses the default child manifest name, index\_1. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** Url **   <a name="mediapackage-Type-ListLowLatencyHlsManifestConfiguration-Url"></a>
The egress domain URL for stream delivery from MediaPackage.
Type: String
Required: No

## See Also
<a name="API_ListLowLatencyHlsManifestConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/ListLowLatencyHlsManifestConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/ListLowLatencyHlsManifestConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/ListLowLatencyHlsManifestConfiguration)
