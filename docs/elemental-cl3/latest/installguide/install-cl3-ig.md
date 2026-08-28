---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/installguide/install-cl3-ig.html
---

# Installing Conductor Live on qualified hardware
<a name="install-cl3-ig"></a>

This section is for IT administrators who perform the first-time installation of AWS Elemental Conductor Live software on an appliance that is considered qualified hardware.

For information about hardware that AWS Elemental has qualified, contact your AWS Elemental Sales representative contact AWS Elemental Support through your company’s Private Space in [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter).

**Prerequisite Knowledge**
It is assumed that you know how to:
+ Log in to the Conductor Live appliance over SSH to work via the command line interface.
+ Use Windows Share (on a Windows computer), Samba (on a Mac workstation), or a utility such as scp (on a Linux workstation) to move files.
+ Access recently downloaded files on your workstation.

**Note**
In the following steps, we show how to install version 3.25.5. Modify your commands to specify the version that applies for you.

**Topics**
+ [Step A: Prepare the hardware and download files](install-cl3-ig-prep.md)
+ [Step B: Install (Kickstart) the operating system software](install-cl3-ig-install-ks.md)
+ [Step C: Install the Conductor Live software](install-cl3-ig-install-sw.md)
+ [Step D: Set up licenses](install-cl3-license.md)
+ [Step E: Complete cluster configuration](install-cl3-ig-complete.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
