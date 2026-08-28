---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/special-conditions-TS-CMAF-manifests.html
---

# Special conditions for TS and CMAF manifests in MediaPackage
<a name="special-conditions-TS-CMAF-manifests"></a>

If you are using TS or CMAF manifests for MediaPackage, these special conditions apply.
+ For TS manifests, we strongly recommend that you use audio rendition groups to avoid removing the video streams that are multiplexed with the audio streams that are filtered out. For more information about rendition groups, see [AWS Elemental MediaPackage rendition groups reference](rendition-groups.md).
+ In TS and CMAF manifests, the audio sample rate is not signaled, so it's not easy to visually check the original or filtered manifests for this setting. To verify the audio sample rate, check the audio sample rate at the encoder level and output level.
+ In TS and CMAF manifests, the `BANDWIDTH` attribute for a variant associates the bandwidth of the audio track with the video track, whether it is multiplexed with the video track, or if it is an audio rendition track referenced by the video track. Therefore, you can't visually inspect the original and filtered manifests to confirm the `video_bitrate` filter has worked. To verify the filter, check the video bitrate at the encoder level and output level.
+ For TS and CMAF manifests, request parameters appended to bitrate playlists or segments result in an HTTP 400 error.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
