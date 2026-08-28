---
source_url: https://docs.aws.amazon.com/storagegateway/latest/vgw/SetParaVirtualization-common.html
---

# Configuring paravirtualization on a VMware host
<a name="SetParaVirtualization-common"></a>

The following procedure describes how to configure the VMware host platform for your Storage Gateway appliance to use paravirtual Internet Small Computer System Interface Protocol (iSCSI) controllers. Paravirtual iSCSI controllers are high performance storage controllers that can result in greater throughput and lower CPU use. These controllers are best suited for high performance storage environments. When you configure iSCSI controllers this way, the Storage Gateway virtual machine works with the host operating system to allow the gateway console to identify the virtual disks that you add to your virtual machine.

**Note**
You need to complete this step to avoid issues in identifying these disks when you configure them in the gateway console.

**To configure your VMware host platform to use paravirtualized controllers**

1. In the VMware vSphere client, right-click on the name of your gateway virtual machine in the navigation pane on the left side of the application window to open the context menu, and then choose **Edit Settings**.

1. In the **Virtual Machine Properties** dialog box, choose the **Hardware** tab.

1. On the **Hardware** tab, select **SCSI controller 0**, and then choose **Change Type**.

1. In the **Change SCSI Controller Type** dialog box, select the **VMware Paravirtual** SCSI controller type, and then choose **OK** to save the configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
