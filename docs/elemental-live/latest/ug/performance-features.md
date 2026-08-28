---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/performance-features.html
---

# Features that affect performance
<a name="performance-features"></a>

## Motion graphic overlays
<a name="performance-features-motion-gx"></a>

Motion graphic overlays in the video output can add up to 50% density, compared to an output without overlays.

For more information, see [Insert a motion graphic overlay in Elemental Live](motion-graphic-overlay.md).

## Color space conversions
<a name="performance-features-color-space"></a>

Color space conversions add compute complexity and require more CPU usage.

For more information, see [Working with color space](hdr-working-with.md).

## Noise reducer filters
<a name="performance-features-noise-reducer"></a>

Noise reducer filters add up to 10% density when compared to an output without noise reduction.

For more information, see [Noise reduction](vq-noise-reduction.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
