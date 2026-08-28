---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/dolby-metadata-output-dolby-digital-codec.html
---

# Output with the Dolby Digital codec
<a name="dolby-metadata-output-dolby-digital-codec"></a>

| Named metadata parameters | Category | Field | API tag (at stream\_assembly\\audio\_description\\ac3\_settings) | Default |
| --- | --- | --- | --- | --- |
| Dialogue Level | D | Dialnorm<br />  | dialnorm | Not set |
| Channel Mode | D | Coding Mode | coding\_mode | 2/0 |
| LFE Channel | D | Coding Mode<br />Coding Mode set to “3/2mode with LFE” means LFE is enabled. All other options mean LFE is disabled. |   | Disabled |
| Bitstream Mode | D | Bitstream Mode | bitstream\_mode | Complete Main |
| Line Mode Compression | D | No user control |   | Film Std. |
| RF Mode Compression | D | No user control |   | Film Std. |
| RF Overmodulation Protection | D | No user control |   |   |
| Center Downmix Level | D | No user control |   | -3dB |
| Surround Downmix Level | D | No user control |   | Not indicated |
| Dolby Surround Mode | D | No user control |   | Disabled |
| Audio Production Information | D | No user control |   | 0 (does not exist) |
| Mix Level | D | No user control |   | Not set |
| Room Type | D | No user control |   | Not set |
| Copyright Bit | D | No user control |   | 0 |
| Original Bitstream | D | No user control |   | 0 |
| Preferred Stereo Downmix | D | No user control |   | Not indicated |
| Lt/Rt Center Downmix Level | D | No user control |   | -3.0 dB |
| Lt/Rt Surround Downmix Level | D | No user control |   | -3.0 dB |
| Lo/Ro Center Downmix Level | D | No user control |   | -3.0 dB |
| Lo/Ro Surround Downmix Level | D | No user control |   | -3.0 dB |
| Dolby Surround EX Mode | D | No user control |   | Disabled |
| A/D Converter Type | D | No user control |   | 0 (standard) |
| DC Filter | EC | No user control |   | Enabled |
| LFE Lowpass Filter | EC | When Coding Mode is 3/2, LFE Filter checkbox appears at the far right. | lfe\_filter | Disabled |
| Surround 3 dB Attenuation | EC | No user control |   | Enabled |
| Surround Phase Shift | EC | No user control |   | Disabled |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
