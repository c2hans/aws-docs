---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/cluster-secret-rotation-procedure.html
---

# Rotate a cluster secret in AWS PCS
<a name="cluster-secret-rotation-procedure"></a>

Rotate your cluster secret to comply with security requirements and address potential compromises. This process requires putting your cluster into maintenance mode.

## Prerequisites
<a name="cluster-secret-rotation-procedure-prerequisites"></a>
+ IAM role with `secretsmanager:RotateSecret` permission
+ Cluster in `ACTIVE` or `UPDATE_FAILED` state

## Procedure
<a name="cluster-secret-rotation-procedure-steps"></a>

1. Notify cluster users of the upcoming maintenance window.

1. Put the cluster into maintenance mode by scaling all compute node groups to 0 capacity.

   1. Use the UpdateComputeNodeGroup API to set both minInstanceCount and maxInstanceCount to 0 for all compute node groups.

   1. Wait until all nodes stop.

   1. Optional: Drain scheduler queues with Slurm commands before you terminate capacity for graceful job handling.

1. Initiate rotation through Secrets Manager.
   + **Console method**:

     1. Navigate to Secrets Manager, select your cluster secret, and choose **Rotate secret**.
   + **API method**:

     1. Use Secrets Manager `rotate-secret` API.

1. Monitor rotation progress.

   1. Track progress through CloudTrail events.

   1. Check `lastRotatedDate` through either the Secrets Manager console or the `secretsmanager:describeSecret` API.

   1. Wait for `RotationSucceeded` or `RotationFailed` CloudTrail event.

1. After successful rotation, restore cluster capacity.

   1. Use the UpdateComputeNodeGroup API to reset node groups to desired min/max capacity.

   1. For AWS PCS-managed login nodes: No additional action required.

   1. For BYO login nodes:

      1. Connect to login nodes.

      1. Update `/etc/slurm/slurm.key` with the new secret from Secrets Manager.

      1. Restart the Slurm Auth and Cred Kiosk Daemon (sackd).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
