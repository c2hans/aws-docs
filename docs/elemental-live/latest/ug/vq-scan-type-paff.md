---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/vq-scan-type-paff.html
---

# Adaptive field frame controls
<a name="vq-scan-type-paff"></a>

## Description
<a name="description-vq-scan-type"></a>

The following are the settings and internal algorithms tied to the scan type:
+
+ **Picture Adaptive Field Frame (PAFF)**: This setting is automatically enabled on GPU-enabled versions of Elemental Live and automatically disabled on CPU-only versions.
+ **Macroblock Adaptive Field Frame (MBAFF)**: This setting is automatically enabled on CPU-only versions of Elemental Live and automatically disabled on GPU-enabled versions.
+ **Force Field Pictures**: This field appears only if the codec is H.264 and only affects GPU-enabled versions of Elemental Live.
  + **Enabled**: All outputs are forced to use PAFF field picture encoding.
  + **Disabled**: Elemental Live switches between PAFF and MBAFF, depending on the content.

## Recommendations
<a name="vq-scan-type-recommendations"></a>
+ **Force Field Pictures **results in a significant reduction in quality so it should only be used if required for compatibility with specific decoders or playback devices.

## Location of fields
<a name="vq-scan-type-api"></a>

| Location of field on web interface | Location of tag in XML |
| --- | --- |
| Streams – Video > Advanced > Force Field Pictures | stream\_assembly/video\_description/{{codec}}/force\_field\_pictures<br />where {{codec}} is:<br />**h264\_settings** |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
