---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/elink-device-hd-uhd.html
---

# HD and UHD Link devices
<a name="elink-device-hd-uhd"></a>

There are two versions of the Link device. Each device can handle different usages, ingest different resolutions, and stream different formats.

- **AWS Elemental Link HD (Link HD)**
  - **Usage:** Connect to a MediaLive input
  - **Resolutions that the device is ingesting:** HD or lower
  - **Resolutions and codecs that the device produces:** The same resolution as the ingest, in HEVC

- **AWS Elemental Link UHD (Link UHD)**
  - **Usage:** Connect to a MediaLive input / **Resolutions that the device is ingesting:** UHD or lower / **Resolutions and codecs that the device produces:** The same resolution as the ingest, in HEVC
  - **Usage:** Connect to a MediaConnect flow / **Resolutions that the device is ingesting:** UHD or lower / **Resolutions and codecs that the device produces:** The same resolution as the ingest, in AVC or HEVC

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
