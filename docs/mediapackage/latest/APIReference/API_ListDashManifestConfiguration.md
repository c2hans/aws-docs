---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListDashManifestConfiguration.html
---

# ListDashManifestConfiguration
<a name="API_ListDashManifestConfiguration"></a>

List the DASH manifest configuration.

## Contents
<a name="API_ListDashManifestConfiguration_Contents"></a>

 ** ManifestName **   <a name="mediapackage-Type-ListDashManifestConfiguration-ManifestName"></a>
A short string that's appended to the endpoint URL. The manifest name creates a unique path to this endpoint. If you don't enter a value, MediaPackage uses the default manifest name, index.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** Url **   <a name="mediapackage-Type-ListDashManifestConfiguration-Url"></a>
The egress domain URL for stream delivery from MediaPackage.
Type: String
Required: No

## See Also
<a name="API_ListDashManifestConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/ListDashManifestConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/ListDashManifestConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/ListDashManifestConfiguration)
