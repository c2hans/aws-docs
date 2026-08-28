---
source_url: https://docs.aws.amazon.com/elemental-cf2/latest/migrationguide/migrate-topic-create-boot.html
---

# Create a boot USB drive
<a name="migrate-topic-create-boot"></a>

1. Obtain the RHEL 9 `.iso` file from [AWS Elemental Software Download page](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/softwaredownloads).

   Find the AWS Elemental product and version they are planning to use. The appropriate ISO file appears beside that version.

1. At your workstation, use a third-party utility (such as PowerISO or ISO2USB) to create a bootable USB drive from your `.iso` file. For help, see the knowledge base article [Creating Bootable Recovery (kickstart) Media](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-CentOS-Elemental-v2-0-Windows-and-Apple-OS-X).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor File. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cf2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
