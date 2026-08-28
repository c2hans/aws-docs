---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migration-guide-about.html
---

# About this guide
<a name="migration-guide-about"></a>

This guide describes how to upgrade a Conductor cluster consisting of AWS Elemental Conductor Live nodes and worker nodes (AWS Elemental Live and AWS Elemental Statmux). It describes how to perform an upgrade to a version in the range of 3.26.1 (2.26.1) to 3.26.5 (2.26.5) of the AWS Elemental software.

This special guide exists because an upgrade to a version in that range requires that you install the RHEL 9 version of the Linux operating system.

See [AWS Elemental Conductor Live Upgrade Guide](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/) if the following situations apply:
+ You are upgrading to a version earlier than 3.26.1.
+ You have migrated to a 3.26 version, and you now want to upgrade to a higher 3.26.x version to 3.27.x or higher.

**Note**
For assistance with your AWS Elemental appliances and software products, see the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
