---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-manifest-last-updated.html
---

# Monitoring manifest update time in AWS Elemental MediaPackage
<a name="monitoring-manifest-last-updated"></a>

MediaPackage playback responses include the following custom headers that indicate when MediaPackage last modified the manifest in non-dynamic ad insertion workflows. These headers are helpful when troubleshooting issues related to stale manifests.

**X-Amzn-Mediapackage-Manifest-Last-Part**
This is only provided on requests for low-latency HLS manifests, and is the highest part sequence number in the manifest.

**X-MediaPackage-Manifest-Last-Sequence**
This is the highest segment sequence number in the manifest.
For HLS and CMAF, this is the highest segment number in the media playlist.
See the following section for [manifest example](#manifest-last-updated).

**X-MediaPackage-Manifest-Last-Updated**
The epoch timestamp in milliseconds when MediaPackage generates the segment referred to in `X-MediaPackage-Manifest-Last-Sequence`.

## HLS manifest example
<a name="manifest-last-updated"></a>

### HLS manifest
<a name="hls-examples"></a>

MediaPackage determines the `X-MediaPackage-Manifest-Last-Sequence` value from the last segment in the manifest. For example, in the following manifest `index_1_3.ts` is the highest segment sequence number, so the value of `X-MediaPackage-Manifest-Last-Sequence` is `3`. The value of `X-MediaPackage-Manifest-Last-Updated` corresponds to the epoch timestamp in milliseconds when MediaPackage generates the last segment in the manifest.

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:8
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:7.500,
index_1_0.ts?m=1583172400
#EXTINF:7.500,
index_1_1.ts?m=1583172400
#EXTINF:7.500,
index_1_2.ts?m=1583172400
#EXTINF:7.500,
index_1_3.ts?m=1583172400
#EXT-X-ENDLIST
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
