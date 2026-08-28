---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/how-maintenance-works.html
---

# How maintenance works
<a name="how-maintenance-works"></a>

For router I/Os, MediaConnect automatically schedules maintenance every 60–66 days after the I/O is started. You configure a preferred day and start hour, and MediaConnect applies updates to the I/O within that two-hour window.

For flows, MediaConnect assigns a "Required by" date when updates are available. You configure a preferred day and start hour, and MediaConnect restarts the flow within that two-hour window.

**What happens during maintenance**
The impact of maintenance depends on the resource type:

Router outputs
The output enters the **Migrating** state. During this process, there is an interruption to that output's stream only. After the maintenance completes, the output returns to the **Active** state.

Router inputs
The input enters the **Migrating** state. During this process, there is an interruption to all outputs currently routed to receive from that input. After the maintenance completes, the input returns to the **Active** state.

Flows
During maintenance, there is an interruption to all outputs on the flow.

**If maintenance does not complete**
The rescheduling behavior depends on the resource type:

Flows
If MediaConnect is unable to perform maintenance at the scheduled time, the service reschedules maintenance to the following week's maintenance window.

Router I/Os
If maintenance does not complete within the scheduled window, MediaConnect reschedules it to the next maintenance period.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
