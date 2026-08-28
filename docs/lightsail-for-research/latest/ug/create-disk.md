---
source_url: https://docs.aws.amazon.com/lightsail-for-research/latest/ug/create-disk.html
---

# Create a storage disk in the Lightsail for Research console
<a name="create-disk"></a>

Complete the following steps to create a disk for your Lightsail for Research virtual computer.

1. Sign in to the [Lightsail for Research console](https://lfr.console.aws.amazon.com/ls/research).

1. Choose **Storage** in the navigation pane.

1. Choose **Create disk**.

1. Enter a name for your disk. Valid characters include alphanumeric characters, numbers, periods, hyphens, and underscores.

   Disk names must also meet the following requirements:
   + Be unique within each AWS Region in your Lightsail for Research account.
   + Contain 2–255 characters.
   + Start and end with an alphanumeric character or number.

1. Choose an AWS Region for your disk.

   The disk must be in the same Region as the virtual computer that you will attach it to.

1. Choose your disk size in GB.

1. Continue to the [Attach a disk](attach-disk.md) section for information about attach disks to your virtual computer.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail for Research. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail-for-research` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
