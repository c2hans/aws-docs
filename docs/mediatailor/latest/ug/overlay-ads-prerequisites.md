---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/overlay-ads-prerequisites.html
---

# Prerequisites for using overlay ads with MediaTailor
<a name="overlay-ads-prerequisites"></a>

The following prerequisites apply when using overlay ads with MediaTailor:
+ The workflow must be live, not video on demand (VOD).
+ The Ad Decision Server (ADS) response must be configured to return only non-linear ads in the VAST response. MediaTailor ignores any linear ads for the purposes of ad stitching.
+ The manifest must use a SCTE-35 time signal message with segmentation type `id=0x38` to invoke the overlay-ad feature.
+ The streaming provider must have control of the client-device application and be integrated with the MediaTailor client-side tracking API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
