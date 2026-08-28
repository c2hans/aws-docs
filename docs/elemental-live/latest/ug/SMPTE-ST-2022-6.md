---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/SMPTE-ST-2022-6.html
---

# Working with SMPTE 2022-6
<a name="SMPTE-ST-2022-6"></a>

Elemental Live supports sources that are compliant with the SMPTE 2022-6 standard. The Elemental Live implementation of SMPTE 2022-6 provides an effective way to handle uncompressed video content. SMPTE 2022-6 uses standard IP networking to receive content, which means it uses a cheaper and more readily available network infrastructure than the traditional SDI protocol.

Elemental Live supports redundant inputs using SMPTE 20227, and non-redundant inputs.

With SMPTE 2022-6, the video, audio, and ancillary data are muxed into one feed. Compare this design to SMPTE 2110, where the content is each in a separate essence.

To work with SMPTE ST 2022-6 in Elemental Live, see [Ingesting SMPTE 2022-6 content](input-2022-6.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
