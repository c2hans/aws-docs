---
source_url: https://docs.aws.amazon.com/elemental-server/latest/ug/vq-scan-type.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Encoding – Scan Type
<a name="vq-scan-type"></a>

## Description
<a name="description-vq-scan-type"></a>

The scan type of content can affect the video quality. The following are the settings and internal algorithms tied to the scan type:
+  The encoding controls that deal with scan type are dealt with in [Image Processing – Scan Type – Key Controls](vq-scan-type-key.md).
+ **Picture Adaptive Field Frame (PAFF)**: This control is automatically enabled on Graphics Processing Unit (GPU)-enabled versions of the software and automatically disabled on Central Processing Unit (CPU)-only versions.
+ **Macroblock Adaptive Field Frame (MBAFF)**: This control is automatically enabled on CPU-only versions of the software and automatically disabled on GPU-enabled versions.
+ **Force Field Pictures**: This field appears only if the codec is H.264 and only affects GPU-enabled versions of the software.
  + **Enabled**: All outputs are forced to use PAFF field picture encoding.
  + **Disabled**: The encoder switches between PAFF and MBAFF, depending on the content.

## Recommendations
<a name="vq-scan-type-recommendations"></a>
+ **Force Field Pictures **results in a significant reduction in quality so it should only be used if required for compatibility with specific decoders or playback devices.

## Location of Fields
<a name="vq-scan-type-api"></a>

| Location of Field on Web Interface | Location of Tag in XML |
| --- | --- |
| Streams – Video > Advanced > Force Field Pictures | stream\_assembly/video\_description/{{codec}}/force\_field\_pictures<br />where {{codec}} is:<br />**h264\_settings** |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
