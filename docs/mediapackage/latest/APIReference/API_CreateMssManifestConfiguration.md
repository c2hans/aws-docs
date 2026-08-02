---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateMssManifestConfiguration.html
---

# CreateMssManifestConfiguration
<a name="API_CreateMssManifestConfiguration"></a>

Configuration parameters for creating a Microsoft Smooth Streaming (MSS) manifest. MSS is a streaming media format developed by Microsoft that delivers adaptive bitrate streaming content to compatible players and devices.

## Contents
<a name="API_CreateMssManifestConfiguration_Contents"></a>

 ** ManifestName **   <a name="mediapackage-Type-CreateMssManifestConfiguration-ManifestName"></a>
A short string that's appended to the endpoint URL to create a unique path to this MSS manifest. The manifest name must be unique within the origin endpoint and can contain letters, numbers, hyphens, and underscores.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** FilterConfiguration **   <a name="mediapackage-Type-CreateMssManifestConfiguration-FilterConfiguration"></a>
Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.
Type: [FilterConfiguration](API_FilterConfiguration.md) object
Required: No

 ** ManifestLayout **   <a name="mediapackage-Type-CreateMssManifestConfiguration-ManifestLayout"></a>
Determines the layout format of the MSS manifest. This controls how the manifest is structured and presented to client players, affecting compatibility with different MSS-compatible devices and applications.
Type: String
Valid Values: `FULL | COMPACT`
Required: No

 ** ManifestWindowSeconds **   <a name="mediapackage-Type-CreateMssManifestConfiguration-ManifestWindowSeconds"></a>
The total duration (in seconds) of the manifest window. This determines how much content is available in the manifest at any given time. The manifest window slides forward as new segments become available, maintaining a consistent duration of content. The minimum value is 30 seconds.
Type: Integer
Valid Range: Minimum value of 30.
Required: No

## See Also
<a name="API_CreateMssManifestConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/CreateMssManifestConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/CreateMssManifestConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/CreateMssManifestConfiguration)
