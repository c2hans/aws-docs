---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/migrate.html
---

# Migrating your workload
<a name="migrate"></a>

To migrate your workload to AWS, you use CloudEndure's web-based console to configure your source and target environments and to set up your replication servers. In this phase, you also install the CloudEndure Agent on your source machines, and specify a Blueprint for creating and configuring your target machine With these components and configurations in place, replication from the source environment to the lightweight staging area can begin.

## Define replication settings for AWS
<a name="replication-settings"></a>

To replicate data into or within the target environment, CloudEndure uses replication server(s) to provide a lightweight replication staging area on AWS. These servers are automatically launched into the subnet you created previously in the [Configure your source and target network](prepare.md#network) section.

The CloudEndure User Console address (console.cloudendure.com) is used for all cloud and on-premises platforms, except for specific cases.

In the CloudEndure User Console, you use the **Replication Settings** tab to define your source and target environments, and to configure the default replication servers in the staging area of the target infrastructure. For step-by-step instructions, see [Defining Replication Settings for AWS](https://docs.cloudendure.com/#Defining_Your_Replication_Settings/Defining_Replication_Settings_for_AWS/Defining_Replication_Settings_for_AWS.htm) in the CloudEndure documentation.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/images/guide-img/bbb5871c-6fdf-4a96-872d-e22410dc477d/images/2d7f9629-ddc7-469d-b9d9-89e546cae265.png)

## Install CloudEndure Agent on source machines
<a name="agent"></a>

After you've prepared your environment and configured your replication settings, you can install CloudEndure Agent on the machines in your source environment. The Agent replicates your applications and data in the staging area on AWS. Follow these steps:

1. In the CloudEndure User Console, choose **Machines**, **Machine Actions**, **Add Machines**.

1. Locate the Installation Token that was provided for you when your CloudEndure account was activated. (To locate your tokens, choose **Help**, **How to Add Machines** in the CloudEndure User Console.)

1. Download the Agent installer file to each source machine, and then use the command provided in the **How to Add Machines** pane to run the installer on each source machine.

 For more information, see [Installing the CloudEndure Agents](https://docs.cloudendure.com/#Installing_the_CloudEndure_Agents/Installing_the_CloudEndure_Agents.htm%3FTocPath%3DNavigation%7CInstalling%2520the%2520CloudEndure%2520Agents%7C_____0) in the CloudEndure documentation.

When the Agent is installed, the source machine appears in the CloudEndure User Console, in the **Machines** tab, and the machine undergoes initial data replication (Initial Sync).

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/images/guide-img/bbb5871c-6fdf-4a96-872d-e22410dc477d/images/0d0552d7-925b-4d90-823d-154b9faa5a3d.png)

Use the **Machines** dashboard to monitor the Initial Sync process, which includes these steps:

1. Creating firewall rules.

1. Creating the replication server.

1. Booting the replication server.

1. Resolving the CloudEndure Service Manager address in the replication server.

1. Authenticating the replication server with the CloudEndure Service Manager.

1. Downloading the CloudEndure replication software to the replication server.

1. Creating staging disks.

1. Attaching the staging disks to the replication server.

1. Pairing the CloudEndure Agent with the replication server.

1. Establishing communication between the CloudEndure Agent and the replication server.

When the Initial Sync is complete, the **Machines** dashboard shows the final status as **Continuous Data Replication**. This indicates that all changes in the source server are being synchronized with the CloudEndure replication server.

For more information, see [Monitoring Your Solution](https://docs.cloudendure.com/#Monitoring_Your_Solution/Monitoring_Your_Solution.htm) in the CloudEndure documentation.

## Configure the target system Blueprint
<a name="blueprint"></a>

A Blueprint provides a set of instructions for creating and launching a target machine for a specified source machine. To configure a source machine's Blueprint, choose the machine name from the **Machines** dashboard to access the **Machine Details** pane, and choose the **Blueprint** tab from the menu on the right.

Enter the following values in the **Blueprint** tab and then choose **Save Blueprint**.

|
|
| Key | Value |
| --- |--- |
| Machine Type | t3.medium |
| Launch Type | On Demand |
| Subnet | *Target subnet* |
| Security Groups | *Target security group* |
| Private IP | Create New |
| Public IP (ephemeral): | No |
| Disks | SSD |

For more information about these settings, see [Configuring the Target Machine Blueprint](https://docs.cloudendure.com/Content/Configuring_and_Running_Disaster_Recovery/Configuring_the_Target_Machine_Blueprint/Configuring_the_Target_Machine_Blueprint.htm) in the CloudEndure documentation.
