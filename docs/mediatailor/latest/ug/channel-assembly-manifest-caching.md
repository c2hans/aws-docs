---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-manifest-caching.html
---

# Manifest caching
<a name="channel-assembly-manifest-caching"></a>

MediaTailor periodically and opportunistically caches source playlists to improve channel assembly performance and reliability. Sometimes, the cached version becomes stale compared to the origin version at your source location. To force MediaTailor to refresh the cached version of the source, call [UpdateVodSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_UpdateVodSource.html). For example, use this call when the embedded paths change in your source. Make sure that you always keep an up-to-date version of the source available on your source location, even if you see few requests from MediaTailor.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
