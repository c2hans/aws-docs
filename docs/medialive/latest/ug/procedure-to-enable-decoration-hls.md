---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/procedure-to-enable-decoration-hls.html
---

# Enabling decoration – HLS
<a name="procedure-to-enable-decoration-hls"></a>

In an HLS output group, manifest decoration is enabled at the output group level, which means that the manifests for all outputs in that group include instructions based on the SCTE 35 content.

**To enable decoration**

1. In the channel that you are creating, make sure that you have set the ad avail mode. See [Getting ready: Set the ad avail mode](getting-ready-set-the-ad-avail-mode.md).

1. In the navigation pane, find the desired HLS output group.

1. In **Ad Marker**, choose **Add ad markers**.

1. For **HLS ad markers**, select the type of ad marker. For information about the different types of markers, see [Sample manifests - HLS](sample-manifests-hls.md).

1. Repeat to add more types of markers, as desired.

The manifest for each output will include a separate set of tags for each type that you select.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
