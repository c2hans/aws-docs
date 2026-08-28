---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/troubleshooting-v3-pc-cli-logs.html
---

# `pcluster` CLI logs
<a name="troubleshooting-v3-pc-cli-logs"></a>

The `pcluster` CLI writes logs of your commands to `pcluster.log.#` files in `/home/user/.parallelcluster/`.

For each command, the logs generally include the command with inputs, a copy of the CLI API version used to make the command, the response, and both info and error messages. For a create and build command, the logs also include the configuration file, configuration file validation operations, the CloudFormation template, and stack commands.

You can use these logs to verify errors, inputs, versions and `pcluster` CLI commands. They can also serve as a record of when commands were made.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
