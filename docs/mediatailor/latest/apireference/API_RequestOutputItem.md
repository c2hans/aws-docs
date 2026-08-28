---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_RequestOutputItem.html
---

# RequestOutputItem
<a name="API_RequestOutputItem"></a>

The output configuration for this channel.

## Contents
<a name="API_RequestOutputItem_Contents"></a>

 ** ManifestName **   <a name="mediatailor-Type-RequestOutputItem-ManifestName"></a>
The name of the manifest for the channel. The name appears in the `PlaybackUrl`.
Type: String
Required: Yes

 ** SourceGroup **   <a name="mediatailor-Type-RequestOutputItem-SourceGroup"></a>
A string used to match which `HttpPackageConfiguration` is used for each `VodSource`.
Type: String
Required: Yes

 ** DashPlaylistSettings **   <a name="mediatailor-Type-RequestOutputItem-DashPlaylistSettings"></a>
DASH manifest configuration parameters.
Type: [DashPlaylistSettings](API_DashPlaylistSettings.md) object
Required: No

 ** HlsPlaylistSettings **   <a name="mediatailor-Type-RequestOutputItem-HlsPlaylistSettings"></a>
HLS playlist configuration parameters.
Type: [HlsPlaylistSettings](API_HlsPlaylistSettings.md) object
Required: No

## See Also
<a name="API_RequestOutputItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/RequestOutputItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/RequestOutputItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/RequestOutputItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
