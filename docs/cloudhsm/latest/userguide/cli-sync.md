---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cli-sync.html
---

# Synchronizing keys across cloned AWS CloudHSM clusters
<a name="cli-sync"></a>

Client-side and server-side synchronization are only for synchronizing keys within the *same* AWS CloudHSM cluster. If you copy a backup of a cluster to another region, use the [key replicate](cloudhsm_cli-key-replicate.md) command to replicate a key between two clusters. You might use cloned clusters for cross-region redundancy or to simplify your disaster recovery process. If you haven't installed CloudHSM CLI, see the instructions in [Getting started with AWS CloudHSM Command Line Interface (CLI)](cloudhsm_cli-getting-started.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
