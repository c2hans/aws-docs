---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-multi-cluster-config-run.html
---

# Configure the CloudHSM CLI for multi-cluster functionality
<a name="cloudhsm_cli-multi-cluster-config-run"></a>

To configure your CloudHSM CLI for multi-cluster functionality, follow these steps:

1. Identify the clusters you want to connect to.

1. Add these clusters to your CloudHSM CLI configuration using the [configure-cli](configure-sdk-5.md) subcommand `add-cluster` as described below.

1. Restart any CloudHSM CLI processes in order for the new configuration to take effect.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
