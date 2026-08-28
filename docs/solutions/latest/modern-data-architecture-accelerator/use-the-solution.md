---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/use-the-solution.html
---

# Use the solution
<a name="use-the-solution"></a>

This section explains how to use MDAA’s configuration capabilities to manage your data platform architecture.

## Using configuration files
<a name="use-config-files"></a>

MDAA is configured using YAML configuration files. The main CLI configuration file (typically 'mdaa.yaml') specifies:
+ Global settings
+ Domains
+ Environments
+ Modules to be deployed

Configuration layouts are flexible and can be:
+ Concentrated in a single MDAA config file
+ Spread across multiple config files by domain
+ Organized by line of business
+ Separated by environment

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Modern Data Architecture Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
