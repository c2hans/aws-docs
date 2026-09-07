---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/restart-the-aws-replication-agent-automatically-without-disabling-selinux-after-rebooting-a-rhel-source-server.html
---

# Automatically restart the AWS Replication Agent after a RHEL reboot without disabling SELinux
<a name="restart-the-aws-replication-agent-automatically-without-disabling-selinux-after-rebooting-a-rhel-source-server"></a>

*Anil Kunapareddy, Amazon Web Services*

## Summary
<a name="restart-the-aws-replication-agent-automatically-without-disabling-selinux-after-rebooting-a-rhel-source-server-summary"></a>

AWS Transform MGN helps simplify, expedite, and automate the migration of Red Hat Enterprise Linux (RHEL) workloads to the Amazon Web Services (AWS) Cloud. To add source servers to MGN, you install the [AWS Replication Agent](https://docs.aws.amazon.com/mgn/latest/ug/agent-installation.html) on the servers.

MGN provides real-time, asynchronous, block-level replication. This means that you can continue normal IT operations during the entire replication process. These IT operations might require that you reboot or restart your RHEL source server during the migration. If this happens, the AWS Replication Agent will not restart automatically, and your data replication will stop. Typically, you can set Security-Enhanced Linux (SELinux) to **disabled** or **permissive** mode to automatically restart the AWS Replication Agent. However, your organization’s security policies might prohibit disabling SELinux, and you might also have to [relabel your files](https://access.redhat.com/solutions/3176).

This pattern describes how to automatically restart the AWS Replication Agent without turning off SELinux when your RHEL source server reboots or restarts during a migration.

## Prerequisites and limitations
<a name="restart-the-aws-replication-agent-automatically-without-disabling-selinux-after-rebooting-a-rhel-source-server-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ An on-premises RHEL workload that you want to migrate to the AWS Cloud.
+ MGN initialized from the MGN console. Initialization is required only the first time you use this service. For instructions, see the [MGN documentation](https://docs.aws.amazon.com/mgn/latest/ug/mandatory-setup.html).
+ An existing [AWS Identity and Access Management (IAM) policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) for MGN. For more information, see the [MGN documentation](https://docs.aws.amazon.com/mgn/latest/ug/mgn-policies.html).

**Versions**
+ RHEL version 7 or later

## Architecture
<a name="restart-the-aws-replication-agent-automatically-without-disabling-selinux-after-rebooting-a-rhel-source-server-architecture"></a>

The following image shows the architecture for this approach.

![Automatically restarting the AWS Replication Agent after a RHEL reboot](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/3257dc61-bdc0-439e-b008-c0a62dd223ef/images/cf064194-1a34-4bb7-bd0b-b36db2c67b9d.png)

## Tools
<a name="restart-the-aws-replication-agent-automatically-without-disabling-selinux-after-rebooting-a-rhel-source-server-tools"></a>

*AWS services*
+ [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html) is a highly automated lift-and-shift (rehost) solution that simplifies, expedites, and reduces the cost of migrating applications to AWS.

*Linux commands*

The following table provides a list of Linux commands that you run on your RHEL source server. These are also described in the epics and stories for this pattern.

|
|
| **Command** | **Description** |
| --- |--- |
| `#systemctl –version` | Identifies the system version |
| `#systemctl list-units --type=service` | Lists all active services that are available on the RHEL server |
| `#systemctl list-units --type=service \| grep running` | Lists all services that are currently running on the RHEL server |
| `#systemctl list-units --type=service \| grep failed` | Lists all services that failed to load after the RHEL server rebooted or restarted |
| `#restorecon -Rv /etc/rc.d/init.d/aws-replication-service` | Changes the context to `aws-replication-service` |
| `#yum install policycoreutils*` | Installs the policy core utilities that are required for the operation of the SELinux system |
| `#ausearch -c "insmod" --raw \| audit2allow -M my-modprobe` | Searches the audit log and creates a module for policies |
| `#semodule -i my-modprobe.pp` | Activates the policy |
| `#cat my-modprobe.te` | Displays the contents of the `my-modprobe.te` file |
| `#semodule -l \| grep my-modprobe` | Checks whether the policy has been loaded to the SELinux module |

## Epics
<a name="restart-the-aws-replication-agent-automatically-without-disabling-selinux-after-rebooting-a-rhel-source-server-epics"></a>

### Install the AWS Replication Agent and reboot the RHEL source server
<a name="install-the-aws-replication-agent-and-reboot-the-rhel-source-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Generate AWS temporary credentials. | The [temporary credentials](https://docs.aws.amazon.com/mgn/latest/ug/credentials.html) provided by MGN use a similar mechanism to the one used by [AWS Identity and Access Management Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html).<br />To create temporary credentials, you need to:1. [Create a new IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) with the `AWSApplicationMigrationAgentInstallationPolicy` policy.<br />2. [Request temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html) through AWS Security Token Service (AWS STS) by using the [AssumeRole API](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html).<br />You can generate temporary credentials by using the AWS Command Line Interface (AWS CLI). For an example, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html#examples). | Migration engineer |
| Install the AWS Replication Agent. | 1. Sign in to the AWS Management Console and open the [AWS Transform MGN console](https://console.aws.amazon.com/mgn/home).<br />2. Configure replication settings by following the instructions in the [MGN documentation](https://docs.aws.amazon.com/mgn/latest/ug/template-vs-server.html).<br />3. Install the AWS Replication Agent by following the instructions in the [MGN documentation](https://docs.aws.amazon.com/mgn/latest/ug/agent-installation-instructions.html).<br />4. On the **Source Servers** page, choose the RHEL source server, and then choose **Replication** to start the initial replication. For more information, see the [MGN documentation](https://docs.aws.amazon.com/mgn/latest/ug/interracting.html). | Migration engineer |
| Check data replication status. | Wait until the replication is complete, and then check the **Data replication status** on the Migration dashboard. It should be in the **Healthy **state. | Migration engineer |
| Restart or reboot the RHEL source server. | Restart or reboot the RHEL source server. Notice the **Data replication status** displays as **Stalled **on the [Migration dashboard](https://docs.aws.amazon.com/mgn/latest/ug/migration-dashboard.html). | Migration engineer |

### Check the AWS Replication Agent status on the RHEL source server
<a name="check-the-aws-replication-agent-status-on-the-rhel-source-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify the system version. | Open the command line interface for your RHEL source server and run the following command to identify the system version:<br />`#systemctl –version` | Migration engineer |
| List all active services. | To list all active services available on the RHEL server, run the following command:<br />`#systemctl list-units --type=service` | Migration engineer |
| List all running services. | To list all services that are currently running on the RHEL server, use the following command:<br />`#systemctl list-units --type=service \| grep running` | Migration engineer |
| List all services that failed to load. | To list all services that failed to load after the RHEL server rebooted or restarted, run the command:<br />`#systemctl list-units --type=service \| grep failed` | Migration engineer |

### Create and run the SELinux module
<a name="create-and-run-the-selinux-module"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Change the security context. | In the command line interface for your RHEL source server, run the following command to change the security context to the AWS replication service:<br />`#restorecon -Rv /etc/rc.d/init.d/aws-replication-service` | Migration engineer |
| Install core utilities. | To install the core utilities required for the operation of the SELinux system and its policies, run the following command:<br />`#yum install policycoreutils*` | Migration engineer |
| Search the audit log and create a module for policies. | Run the following command:<br />`#ausearch -c "insmod" --raw \| audit2allow -M my-modprobe` | Migration engineer |
| Display the contents of the `my-modprobe-te` file. | The `my-modprobe.te` file is generated by the **audit2allow **command. It includes the SELinux domains, policy source directory, and subdirectories, and it specifies the access vector rules and transitions associated with the domains. To display the contents of the file, run the following command:<br />`#cat my modprobe.te` | Migration engineer |
| Activate the policy. | To insert the module and make the policy package active, run the following command:<br />`#semodule -i my-modprobe.pp` | Migration engineer |
| Check whether the module has been loaded. | Run the following command:<br />`#semodule -l \| grep my-modprobe`<br />After the SELinux module is loaded, you no longer have to set SELinux to **disabled** or **permissive** mode during your migration. | Migration engineer |
| Reboot or restart the RHEL source server and verify the data replication status. | Open the AWS Transform MGN console, navigate to **Data replication progress**, and then reboot or restart your RHEL source server. Data replication should now resume automatically after the RHEL source server reboots. | Migration engineer |

## Related resources
<a name="restart-the-aws-replication-agent-automatically-without-disabling-selinux-after-rebooting-a-rhel-source-server-resources"></a>
+ [MGN documentation](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html)
+ [MGN policies](https://docs.aws.amazon.com/mgn/latest/ug/mgn-policies.html)
+ [Technical training materials](https://docs.aws.amazon.com/mgn/latest/ug/mgn-training.html)
+ [Troubleshooting AWS Replication Agent issues](https://docs.aws.amazon.com/mgn/latest/ug/Troubleshooting-Agent-Issues.html)
