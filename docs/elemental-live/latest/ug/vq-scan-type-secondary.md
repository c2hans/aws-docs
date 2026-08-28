---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/vq-scan-type-secondary.html
---

# Secondary fields for converting scan type
<a name="vq-scan-type-secondary"></a>

## Description
<a name="description-vq-scan-type-secondary"></a>

The scan type of the input can be converted to a different scan type: progressive, interlaced, hard telecine, or soft telecine. You can configure to leave the scan type as is or to convert from one incoming type (or a mix of incoming scan types) to another single type. Configuring for scan type conversion involves setting fields in specific ways.

**Force deinterlace **

The field applies only when the Deinterlacer Preprocessor is turned on. It deals with issues of badly tagged frames.
+ When the **Deinterlace Mode** is Adaptive, set **Force Mode** to Off.
+ When the **Deinterlace Mode** is Deinterlace, use **Force Mode** as follows:
  + **Off**: The processor does not convert frames that are tagged in metadata as "progressive." It only converts those that are tagged as some other type.
  + **On**: The processor converts every frame to "progressive" – even those that are already tagged as "progressive." Turn **Force ****Mode** on only if the input frames are incorrectly marked as "progressive." Do not turn otherwise; processing frames that are already tagged as "progressive" degrade video quality.
+ When the **Deinterlace Mode** is Inverse Telecine, use **Force Mode** as follows:
  +  Off: The processor monitors presence/absence of the hard telecine field repeat cadence and applies only to hard telecine to progressive conversion on frames that have a distinct cadence.
  + On: The processor still monitors for hard telecine cadence and adapts to cadence, but all frames are converted from hard telecine to progressive using the last detected cadence.

**Deinterlace algorithm **

The field applies only when the Deinterlacer Preprocessor is turned on and when the **Deinterlace Mode** is set to **Deinterlace** or **Adaptive**. Set it to the desired value:
+  Motion adaptive interpolation: Provides for better spatial quality (i.e. produces sharper images).
+ Motion adaptive blend: Provides for better temporal quality (i.e. produces smoother motion).
+ Low latency interpolation: Performs interpolated line-doubling to allow for lower latency applications.

## Location of fields
<a name="vq-scan-type-secondary-api"></a>

| Location of field on web interface | Location of tag in XML |
| --- | --- |
| Streams > Advanced >Preprocessors > Deinterlacer > Deinterlace Algorithm | stream\_assembly/video\_description/video\_preprocessors/deinterlacer/algorithm |
| Streams > Advanced >Preprocessors > Deinterlacer > Force Mode | stream\_assembly/video\_description/video\_preprocessors/deinterlacer/force |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
