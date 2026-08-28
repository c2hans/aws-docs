---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/enable-manifest-decoration.html
---

# Enabling manifest decoration in the output
<a name="enable-manifest-decoration"></a>

You can choose to interpret SCTE 35 messages from the input sources in a MediaLive channel and insert corresponding instructions into the output manifest. This manifest decoratino is supported in the following types of MediaLive outputs:
+ HLS
+ Microsoft Smooth (the instructions are inserted in the sparse track).

MediaPackage outputs, which are a type of HLS output, are set up with manifest decoration enabled. You can't disable decoration in these outputs.

Manifest decoration is enabled at the output group level. If you enable the feature in a specific output group, all the outputs in that group have their manifests decorated.

To include manifest decoration in some outputs and not others, you must create two output groups of the specified type, for example, two HLS output groups.

**Topics**
+ [Enabling decoration – HLS](procedure-to-enable-decoration-hls.md)
+ [Enabling decoration – Microsoft Smooth](procedure-to-enable-decoration-ms-smooth.md)
+ [How SCTE 35 events are handled in manifests and sparse tracks](how-scte-35-events-are-handled-in-manifests.md)
+ [Sample manifests - HLS](sample-manifests-hls.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
