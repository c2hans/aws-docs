---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateHlsManifestConfiguration.html
---

# CreateHlsManifestConfiguration
<a name="API_CreateHlsManifestConfiguration"></a>

Create an HTTP live streaming (HLS) manifest configuration.

## Contents
<a name="API_CreateHlsManifestConfiguration_Contents"></a>

 ** ManifestName **   <a name="mediapackage-Type-CreateHlsManifestConfiguration-ManifestName"></a>
A short short string that's appended to the endpoint URL. The manifest name creates a unique path to this endpoint. If you don't enter a value, MediaPackage uses the default manifest name, index. MediaPackage automatically inserts the format extension, such as .m3u8. You can't use the same manifest name if you use HLS manifest and low-latency HLS manifest. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** ChildManifestName **   <a name="mediapackage-Type-CreateHlsManifestConfiguration-ChildManifestName"></a>
A short string that's appended to the endpoint URL. The child manifest name creates a unique path to this endpoint. If you don't enter a value, MediaPackage uses the default manifest name, index, with an added suffix to distinguish it from the manifest name. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** FilterConfiguration **   <a name="mediapackage-Type-CreateHlsManifestConfiguration-FilterConfiguration"></a>
Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.
Type: [FilterConfiguration](API_FilterConfiguration.md) object
Required: No

 ** ManifestWindowSeconds **   <a name="mediapackage-Type-CreateHlsManifestConfiguration-ManifestWindowSeconds"></a>
The total duration (in seconds) of the manifest's content.
Type: Integer
Valid Range: Minimum value of 30.
Required: No

 ** ProgramDateTimeIntervalSeconds **   <a name="mediapackage-Type-CreateHlsManifestConfiguration-ProgramDateTimeIntervalSeconds"></a>
Inserts EXT-X-PROGRAM-DATE-TIME tags in the output manifest at the interval that you specify. If you don't enter an interval, EXT-X-PROGRAM-DATE-TIME tags aren't included in the manifest. The tags sync the stream to the wall clock so that viewers can seek to a specific time in the playback timeline on the player.
Irrespective of this parameter, if any ID3Timed metadata is in the HLS input, it is passed through to the HLS output.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1209600.
Required: No

 ** ScteHls **   <a name="mediapackage-Type-CreateHlsManifestConfiguration-ScteHls"></a>
The SCTE configuration.
Type: [ScteHls](API_ScteHls.md) object
Required: No

 ** StartTag **   <a name="mediapackage-Type-CreateHlsManifestConfiguration-StartTag"></a>
To insert an EXT-X-START tag in your HLS playlist, specify a StartTag configuration object with a valid TimeOffset. When you do, you can also optionally specify whether to include a PRECISE value in the EXT-X-START tag.
Type: [StartTag](API_StartTag.md) object
Required: No

 ** UriPathType **   <a name="mediapackage-Type-CreateHlsManifestConfiguration-UriPathType"></a>
The type of path to use in manifest URIs. `LEAF` uses leaf-relative paths (for example, `index_1.m3u8`). `ROOT` uses root-relative paths that include the full path from root (for example, `/out/v1/channel-group/channel/endpoint/index_1.m3u8`). If you don't specify a value, the default is `LEAF`.
Type: String
Valid Values: `LEAF | ROOT`
Required: No

 ** UrlEncodeChildManifest **   <a name="mediapackage-Type-CreateHlsManifestConfiguration-UrlEncodeChildManifest"></a>
When enabled, MediaPackage URL-encodes the query string for API requests for HLS child manifests to comply with AWS Signature Version 4 (SigV4) signature signing protocol. For more information, see [AWS Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in * AWS Identity and Access Management User Guide*.
Type: Boolean
Required: No

## See Also
<a name="API_CreateHlsManifestConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/CreateHlsManifestConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/CreateHlsManifestConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/CreateHlsManifestConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
