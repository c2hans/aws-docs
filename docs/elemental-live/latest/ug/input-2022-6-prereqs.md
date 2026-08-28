---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/input-2022-6-prereqs.html
---

# Appliance hardware requirements
<a name="input-2022-6-prereqs"></a>

A SMPTE 2022-6 input requires an Elemental Live appliance with a high-speed network interface card (NIC). Therefore, to set up a SMPTE 2022-6 input, you must create the event on one of the following appliances.

| Appliance | Network interface card (NIC) |
| --- | --- |
| L800 series Elemental Live appliance | 25 GbE NIC |
| A bare-metal appliance | 25 GbE Mellanox NIC. You must make sure that the NIC is licensed for use with the RiverMax SDK. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
