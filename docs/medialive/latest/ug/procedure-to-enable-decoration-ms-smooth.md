---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/procedure-to-enable-decoration-ms-smooth.html
---

# Enabling decoration – Microsoft Smooth
<a name="procedure-to-enable-decoration-ms-smooth"></a>

In a Microsoft Smooth output group, if you enable manifest decoration, instructions are inserted in the sparse track.

Manifest decoration is enabled at the output group level, which means that the sparse tracks for all outputs in that group will include instructions based on the SCTE 35 content.

**To enable decoration**

1. In the channel that you are creating, make sure that you have set the ad avail mode. See [Getting ready: Set the ad avail mode](getting-ready-set-the-ad-avail-mode.md).

1. In the navigation pane, find the desired Microsoft Smooth output group.

1. For **Sparse track**, for **Sparse track type**, choose **SCTE\_35**.

1. Complete **Acquisition point ID**, only if encryption is enabled on the output. Enter the address of the certificate.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
