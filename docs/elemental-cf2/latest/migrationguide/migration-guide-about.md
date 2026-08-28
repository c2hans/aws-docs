---
source_url: https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migration-guide-about.html
---

# About this guide
<a name="migration-guide-about"></a>

This guide describes how to upgrade or downgrade a Conductor cluster consisting of AWS Elemental Conductor File nodes and AWS Elemental Server worker nodes. It describes how to perform an upgrade to version 2.18 or higher of the AWS Elemental software, and how to downgrade to a version below 2.18.

This special guide exists because this software upgrade requires that you install the RHEL 9 version of the Linux operating system. A software downgrade requires that you re-install RHEL 7 or CentOS 7.

After you have migrated to a 2.18 version, you don't need to read this guide to perform further upgrades. Instead, read the regular upgrade guide.

**Important**
We strongly recommend that you test the entire migration procedure in your lab. This strategy lets you test the migration process itself, and test the entire workflow on the new software.

**Note**
For assistance with your AWS Elemental appliances and software products, see the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor File. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cf2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
