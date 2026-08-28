---
source_url: https://docs.aws.amazon.com/evs/latest/userguide/evs-env-ami-maintenance.html
---

# AMI maintenance
<a name="evs-env-ami-maintenance"></a>

Amazon EVS deploys ESX hosts with a custom EVS Amazon Machine Image (AMI). The AMI contains a custom vendor add-on containing the required packages for running ESX on Amazon EC2.

## Troubleshoot add host failure due to incompatible cluster image
<a name="troubleshoot-add-host-failure-cluster-image"></a>

When you add a host to your environment, the host has the latest available version of the EVS custom vendor add-on. If your environment uses hosts with an older add-on version, adding new hosts fails with an error that the new host is not compatible with your cluster image. For detailed steps to fix this issue, see [Add host failure due to incompatible cluster image](troubleshooting.md#troubleshoot-cluster-image).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic VMware Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query evs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
