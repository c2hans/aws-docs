---
source_url: https://docs.aws.amazon.com/elemental-server/latest/installguide/install-vm-srvr-ig-install-vm.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Step B: Deploy the VM
<a name="install-vm-srvr-ig-install-vm"></a>

Perform these steps from your workstation.

1. Place the OVA image in a convenient location accessible to the VM host.

1. Start the VMware vSphere client and choose the option that lets you run the OVF Deploy wizard.

1. Complete the fields in the wizard. Pay special attention to the following settings:
   + For the *source*, enter the location where you saved the OVA file.
   + Ensure that the *hostname* that you assign to the VM guest is unique across all of your AWS Elemental products.
   + For *network settings*, such as DNS servers and eth configuration, leave the fields blank. You configure these settings later in the AWS Elemental Server installation and configuration process.

   When you finish and save your inputs, the OVA is installed, the guest is created, and the eth0 is configured as specified.

1. Before you proceed, take a snapshot of the VM as described in the VMware vSphere help text.

1. Repeat these steps to install the OVA on all of the VM instances.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
