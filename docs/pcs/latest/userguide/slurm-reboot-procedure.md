---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/slurm-reboot-procedure.html
---

# Reboot a compute node using Slurm in AWS PCS
<a name="slurm-reboot-procedure"></a>

Use Slurm's native reboot command to resolve performance issues, clear resource problems, or recover from degraded states without loss of EC2 instance capacity.

## Prerequisites
<a name="slurm-reboot-procedure-prerequisites"></a>
+ Slurm Admin privileges (root user access)
+ Access to a login node in the AWS PCS cluster

## Procedure
<a name="slurm-reboot-procedure-steps"></a>

1. Connect to a login node through the EC2 console.

   1. In the EC2 console, choose **Instances**.

   1. Select your login node instance.

   1. Choose **Connect**.

1. Identify the target compute node name using `sinfo` or `scontrol show node`.

   ```
   sinfo
   # or
   scontrol show node
   ```

1. Execute the reboot command using one of these options:
**Warning**
Don't use `nextstate=DOWN` with the `scontrol reboot` command. This parameter marks the node as unhealthy and triggers instance replacement.
   + Basic reboot (waits for node to become idle):

     ```
     scontrol reboot {{nodename}}
     ```
   + Immediate reboot (drains node and reboots when jobs complete):

     ```
     scontrol reboot ASAP {{nodename}}
     ```
   + Reboot with reason:

     ```
     scontrol reboot ASAP reason="troubleshooting" {{nodename}}
     ```
   + Reboot with resume state:

     ```
     scontrol reboot ASAP nextstate=RESUME {{nodename}}
     ```

1. Monitor reboot progress using `scontrol show node`.

   ```
   scontrol show node {{nodename}}
   ```

1. Verify the node returns to service after reboot completion.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
