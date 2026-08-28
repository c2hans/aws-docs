---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ResponseOutputItem.html
---

# ResponseOutputItem
<a name="API_ResponseOutputItem"></a>

The output item response.

## Contents
<a name="API_ResponseOutputItem_Contents"></a>

 ** ManifestName **   <a name="mediatailor-Type-ResponseOutputItem-ManifestName"></a>
The name of the manifest for the channel that will appear in the channel output's playback URL.
Type: String
Required: Yes

 ** PlaybackUrl **   <a name="mediatailor-Type-ResponseOutputItem-PlaybackUrl"></a>
The URL that your player uses for playback.
Type: String
Required: Yes

 ** SourceGroup **   <a name="mediatailor-Type-ResponseOutputItem-SourceGroup"></a>
A string used to associate a package configuration source group with a channel output.
Type: String
Required: Yes

 ** DashPlaylistSettings **   <a name="mediatailor-Type-ResponseOutputItem-DashPlaylistSettings"></a>
DASH manifest configuration settings.
Type: [DashPlaylistSettings](API_DashPlaylistSettings.md) object
Required: No

 ** DualStackPlaybackUrl **   <a name="mediatailor-Type-ResponseOutputItem-DualStackPlaybackUrl"></a>
The dual-stack (IPv4 and IPv6) URL that your player uses for playback.
Type: String
Required: No

 ** HlsPlaylistSettings **   <a name="mediatailor-Type-ResponseOutputItem-HlsPlaylistSettings"></a>
HLS manifest configuration settings.
Type: [HlsPlaylistSettings](API_HlsPlaylistSettings.md) object
Required: No

## See Also
<a name="API_ResponseOutputItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/ResponseOutputItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/ResponseOutputItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/ResponseOutputItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
