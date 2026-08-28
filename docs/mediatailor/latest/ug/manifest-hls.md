---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/manifest-hls.html
---

# Integrating an HLS source
<a name="manifest-hls"></a>

AWS Elemental MediaTailor supports `.m3u8` HLS manifests with an `EXT-X-VERSION` of `3` or higher for live streaming and video on demand (VOD). When MediaTailor encounters an ad break, it attempts ad insertion or replacement, based on the type of content. If there aren't enough ads to fill the duration, for the remainder of the ad break, MediaTailor displays the underlying content stream or the configured slate. For more information about HLS ad behavior based on content type, see [Understanding AWS Elemental MediaTailor ad insertion behavior](ad-behavior.md).

The following sections provide more information about how MediaTailor handles HLS manifests.

**Topics**
+ [HLS supported ad markers](hls-ad-markers.md)
+ [Enabling ad marker passthrough](ad-marker-passthrough.md)
+ [HLS manifest tag handling](manifest-hls-tags.md)
+ [HLS manifest examples](manifest-hls-example.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
