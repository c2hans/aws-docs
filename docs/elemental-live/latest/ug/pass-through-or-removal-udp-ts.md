---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/pass-through-or-removal-udp-ts.html
---

# UDP/TS procedure
<a name="pass-through-or-removal-udp-ts"></a>

Passthrough is enabled or disabled individually for each output, which means it can be applied differently for different outputs in the same group.

**To enable passthrough**

1. In the Profile or Event screen, go to the Output Groups section at the bottom of the screen and display the tab for UDP/TS Output Group.

1. In the output where you want to pass through SCTE-35 messages, open the PID Control section. Complete the following fields:
   + SCTE-35: Click to select.
   + SCTE-35 PID: Enter the ID of the PID where you want the SCTE-35 messages to go.

**Result**
All SCTE-35 messages from the input are included in the data stream of the relevant output.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
