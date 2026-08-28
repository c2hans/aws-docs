---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/slurm-reboot-cancel.html
---

# Cancel a pending reboot in AWS PCS
<a name="slurm-reboot-cancel"></a>

Cancel a pending reboot to avoid unnecessary downtime when the issue has been resolved or when reboot is no longer needed.

## Prerequisites
<a name="slurm-reboot-cancel-prerequisites"></a>
+ Slurm Admin privileges
+ Node must have a pending reboot (showing "reboot issued" status)
+ Access to login node for command execution

## Procedure
<a name="slurm-reboot-cancel-procedure"></a>

1. Connect to the login node.

1. Verify the node has a pending reboot using `scontrol show node`.

   ```
   scontrol show node {{nodename}}
   ```

   Look for "reboot issued" in the node status.

1. Execute the cancel command.

   ```
   scontrol cancel_reboot {{nodename}}
   ```

1. Verify reboot cancellation and node status return to normal.

   ```
   scontrol show node {{nodename}}
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
