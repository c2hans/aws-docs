---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/drain-fleet-instance.html
---

# Drain a Fleet Instance
<a name="drain-fleet-instance"></a>

Draining an instance means instructing the fleet to stop accepting new user sessions while allowing existing sessions to continue until users naturally disconnect. Once all sessions have ended, the instance is automatically reclaimed and replaced with a fresh instance running the latest image.

This approach lets you:
+ **Apply image updates without disrupting users** — existing sessions run to completion, while new sessions are routed to other instances.
+ **Manage maximum instance lifetime** — by periodically draining older instances, you ensure that no instance runs indefinitely without being refreshed.
+ **Maintain fleet hygiene proactively** — rather than waiting for a full fleet restart, you can cycle individual instances on a rolling basis.

**Note**
Draining an instance does not disconnect or terminate active user sessions. Users already connected will not be affected.

**Important**
Once an instance is placed in Drain Mode, this action cannot be reversed. The instance will continue to drain until all active sessions have ended and it is reclaimed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
