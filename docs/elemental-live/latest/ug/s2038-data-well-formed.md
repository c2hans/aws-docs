---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/s2038-data-well-formed.html
---

# Well-formed SMPTE 2038 source
<a name="s2038-data-well-formed"></a>

For Elemental Live to handle the ancillary data, the SMPTE 2038 must meet certain criteria:
+ The SMPTE 2038 packet must be present in every PMT.
+ The PID in which the SMPTE 2038 packet is located must not change in the stream. There is no support for changing the PID and sending a new PMT identifying that PID.
+ The stream should contain the SMPTE 2038 packet in only one PID. If it is present in more than one PID, there is no guarantee that Elemental Live will identify the PID that appears first. It could choose another PID, with results you do not intend.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
