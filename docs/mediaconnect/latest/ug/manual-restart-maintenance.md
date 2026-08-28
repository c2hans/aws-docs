---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/manual-restart-maintenance.html
---

# Manually restarting resources for maintenance
<a name="manual-restart-maintenance"></a>

You can manually restart a router I/O or a flow at any time to apply pending maintenance updates immediately, rather than waiting for the next scheduled maintenance window. This is useful when you want to control exactly when the maintenance occurs.

**Router I/O behavior**
Manually restarting a router I/O applies any pending updates and resets the maintenance countdown. During the restart, the I/O enters the **Migrating** state, which causes an interruption to the stream. After the restart completes, the I/O returns to the Active state. For the full restart procedure, see [Restarting a router I/O in MediaConnect](restarting-router-io.md).

**Flow behavior**
Manually restarting a flow applies any pending updates. The flow's maintenance status changes to **Canceled** because you performed the restart outside the scheduled window. For detailed procedures on stopping and starting flows, see [Managing flows in MediaConnect](flows.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
