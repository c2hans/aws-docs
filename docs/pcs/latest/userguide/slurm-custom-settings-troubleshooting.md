---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/slurm-custom-settings-troubleshooting.html
---

# Troubleshooting custom Slurm settings in AWS PCS
<a name="slurm-custom-settings-troubleshooting"></a>

If you encounter errors when creating or updating AWS PCS resources with Slurm custom settings, you can use logging to diagnose and resolve the issues.

## Troubleshooting incompatible Slurm custom settings
<a name="slurm-custom-settings-incompatible-error"></a>

**Problem:** You receive an error message similar to the following when performing cluster, compute node group, or queue operations:

```
{OPERATION} failed. The Slurm custom settings of the cluster might be incompatible. Check the settings and try again.
```

This error can occur with the following operations:
+ CreateCluster
+ CreateComputeNodeGroup
+ UpdateComputeNodeGroup
+ CreateQueue
+ UpdateQueue

**Solution:** Enable logging to understand the specific issue and troubleshoot the incompatible settings.

**To troubleshoot incompatible Slurm custom settings**

1. Create the cluster if it doesn't exist yet, or ensure your existing cluster is in a state where logging can be enabled.

1. Enable logging for your cluster. For detailed instructions, see [Logging and monitoring for AWS PCS](monitoring-overview.md).
**Note**
Logging can be enabled once the cluster is in creation.

1. Review the logs to identify the specific Slurm configuration issue causing the incompatibility.

1. Correct the incompatible custom settings based on the log information and retry the operation.

For information about supported Slurm custom settings, see:
+ [Custom Slurm settings for AWS PCS clusters](slurm-custom-settings-cluster.md)
+ [Custom Slurm settings for AWS PCS compute node groups](slurm-custom-settings-cng.md)
+ [Custom Slurm settings for AWS PCS queues](slurm-custom-settings-queue.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
