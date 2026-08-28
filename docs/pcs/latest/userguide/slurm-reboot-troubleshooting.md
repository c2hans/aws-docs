---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/slurm-reboot-troubleshooting.html
---

# Troubleshooting Slurm reboot issues in AWS PCS
<a name="slurm-reboot-troubleshooting"></a>

When you encounter node reboot problems, first check the node status using `scontrol show node {{nodename}}`. Then examine CloudWatch logs for both Slurm (slurmctld and slurmd) and system logs to identify potential errors.

For basic troubleshooting, verify network connectivity, check security group settings, and ensure all required services are running after the reboot. If problems persist after basic troubleshooting steps, contact AWS Support. When reaching out to support, provide relevant log excerpts, node status information, and a timeline of the reboot attempt to help expedite the resolution process.

## Additional resources
<a name="slurm-reboot-troubleshooting-additional-resources"></a>
+ For monitoring AWS PCS instances using CloudWatch, see [Monitoring AWS PCS instances using Amazon CloudWatch](https://docs.aws.amazon.com/pcs/latest/userguide/monitoring-cloudwatch_instances.html).
+ For general troubleshooting, see [Troubleshooting problems in AWS Parallel Computing Service](troubleshooting.md).
+ For Slurm documentation, see [Slurm Troubleshooting Guide](https://slurm.schedmd.com/troubleshoot.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
