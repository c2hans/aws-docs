---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-rhel-byol-systems-to-aws-license-included-instances-by-using-aws-mgn.html
---

# Migrate RHEL BYOL systems to AWS License-Included instances by using AWS MGN
<a name="migrate-rhel-byol-systems-to-aws-license-included-instances-by-using-aws-mgn"></a>

*Mike Kuznetsov, Amazon Web Services*

## Summary
<a name="migrate-rhel-byol-systems-to-aws-license-included-instances-by-using-aws-mgn-summary"></a>

When you migrate your workloads to AWS by using AWS Application Migration Service (AWS MGN), you might have to lift and shift (rehost) your Red Hat Enterprise Linux (RHEL) instances and change the license from the default Bring Your Own License (BYOL) model to an AWS License Included (LI) model during migration. AWS MGN supports a scalable approach that uses Amazon Machine Image (AMI) IDs. This pattern describes how to accomplish the license change on RHEL servers during the rehost migration at scale. It also explains how to change the license for a RHEL system that’s already running on Amazon Elastic Compute Cloud (Amazon EC2).

## Prerequisites and limitations
<a name="migrate-rhel-byol-systems-to-aws-license-included-instances-by-using-aws-mgn-prereqs"></a>

**Prerequisites **
+ Access to the target AWS account
+ AWS MGN initialized in the target AWS account and Region for the migration (not required if you have already migrated from your on-premises system to AWS)
+ A source RHEL server with a valid RHEL license

## Architecture
<a name="migrate-rhel-byol-systems-to-aws-license-included-instances-by-using-aws-mgn-architecture"></a>

This pattern covers two scenarios:
+ Migrating a system from on premises directly into an AWS LI instance by using AWS MGN. For this scenario, follow the instructions in the first epic (*Migrate to LI instance - option 1*) and third epic.
+ Changing the licensing model from BYOL to LI for a previously migrated RHEL system that’s already running on Amazon EC2. For this scenario, follow the instructions in the second epic (*Migrate to LI instance* - *option 2*) and third epic.

**Note**
The third epic involves reconfiguring the new RHEL instance to use the Red Hat Update Infrastructure (RHUI) servers provided by AWS. This process is the same for both scenarios.

## Tools
<a name="migrate-rhel-byol-systems-to-aws-license-included-instances-by-using-aws-mgn-tools"></a>

**AWS services**
+ [AWS Application Migration Service (AWS MGN)](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html) helps you rehost (lift and shift) applications to the AWS Cloud without change and with minimal downtime.

## Epics
<a name="migrate-rhel-byol-systems-to-aws-license-included-instances-by-using-aws-mgn-epics"></a>

### Migrate to LI instance - option 1 (for an on-premises RHEL system)
<a name="migrate-to-li-instance---option-1-for-an-on-premises-rhel-system"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Find the AMI ID of the RHEL AWS LI instance in the target Region. | Visit [AWS Marketplace](https://aws.amazon.com/marketplace) or use the [Amazon EC2 console](https://console.aws.amazon.com/ec2/) to find the RHEL AMI ID that matches the version of the RHEL source system (for example, RHEL-7.7), and write down the AMI ID. On the Amazon EC2 console, you can filter the AMIs by using one of the following search terms:+ Description = Provided by Red Hat, Inc.<br />+ AMI name = RHEL-7.7 | Cloud administrator |
| Configure AWS MGN launch settings.  | 1. On the [AWS MGN console](https://console.aws.amazon.com/mgn/home), add the source RHEL system: Install the AWS Replication Agent and add the source server by following the instructions in the [AWS MGN documentation](https://docs.aws.amazon.com/mgn/latest/ug/quick-start-guide-gs.html).<br />2. On the **Source servers** page, choose the source RHEL system, and then choose the **Launch settings** tab.<br />3. In the **General launch settings **section, choose **Edit**. To disable automatic selection and manually specify the target instance type, change **Instance type right sizing **to **None**, and then choose **Save settings**. This lets you use the instance type that you configure in your Amazon EC2 launch template. For more information, see the [AWS MGN documentation](https://docs.aws.amazon.com/mgn/latest/ug/right-sizing.html).<br />4. In the **EC2 Launch Template** section, choose **Modify**. In the **About modifying EC2 launch templates** dialog box, choose **Modify** again. This opens the Amazon EC2 console so you can change the template for this instance.<br />5. Review the key considerations in the [AWS MGN documentation](https://docs.aws.amazon.com/mgn/latest/ug/ec2-considerations-1.html#key-considerations).You can disregard the warning against choosing your own AMI.<br />6. On the [Amazon EC2 console](https://console.aws.amazon.com/ec2/), in the new launch template, modify the following:For **AMI**, specify the AMI ID you identified previously, or search for RHEL-*x* and specify the version you require (for example, RHEL-7.7).For **Instance type**, set the desired target instance type.Leave the following sections unchanged: **Key pair (login)**, **Network settings **(unless you want to specify a target subnet and security groups), **Storage**, **Resource tags** (unless you want to add or modify any tags).(Optional) In the **Advanced details** section, specify the IAM instance profile role, if needed for future management by AWS Systems Manager.<br />7. Choose **Create template version**, and then choose the link in the success message to view the launch template.<br />8. Choose **Actions**, **Set default version**. For **Template version**, select the latest version (version 2 for a new system), and then choose **Set as default version**.AWS MGN will now use this version of the launch template to launch test or cutover instances. For more information, see the [AWS MGN documentation](https://docs.aws.amazon.com/mgn/latest/ug/ec2-launch.html). | Cloud administrator |
| Validate settings. | 1. On the [AWS MGN console](https://console.aws.amazon.com/mgn/home), on the **Source servers** page, choose your source server, and then choose the **Launch settings** tab.<br />2. In the **EC2 Launch Template** section, verify that the **Instance type**, **Subnet**, and **Security groups** parameters are set correctly.This section doesn’t display the AMI ID you selected. To see the ID, you can open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/), **Launch Templates** view, and search for the template ID that’s shown in this section. | Cloud administrator |
| Launch the new LI instance. | 1. When the initial sync is complete, the **Migration lifecycle** column for the server on the AWS MGN console **Source servers** page changes to **Ready for testing***.* To launch the new test instance, choose your source server, open the **Test and cutover** menu, and then choose **Launch test instances**. Choose **View job details** to monitor the status of the launch job. For more information, see the [AWS MGN documentation](https://docs.aws.amazon.com/mgn/latest/ug/starting-test.html).<br />2. Wait for the launch job to complete, and then open the launched EC2 instance details page. Choose the **Details** tab and verify that the **Instance details** section contains the following:Platform details: "Red Hat Enterprise Linux"AMI name: The name of AMI you specified in the EC2 launch template<br />3. Cut over to the new LI instance by following the instructions in the [AWS MGN documentation](https://docs.aws.amazon.com/mgn/latest/ug/launch-cutover.html).<br />4. Reconfigure the new instance to use the AWS-provided RHUI servers by following the steps in the last epic. | Cloud administrator |

### Migrate to LI instance - option 2 (for a RHEL BYOL EC2 instance)
<a name="migrate-to-li-instance---option-2-for-a-rhel-byol-ec2-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate your RHEL BYOL EC2 instance to an AWS LI instance. | You can switch RHEL systems that you previously migrated to AWS as BYOL to AWS LI instances by moving their disks (Amazon Elastic Block Store volumes) and attaching them to a new LI instance. To make this switch, follow these steps:1. Launch a new target RHEL instance from a RHEL LI AMI. Make sure that the AMI you selected:Uses the same RHEL version as your current RHEL instance.Has the same boot-up process (BIOS or UEFI) as your current RHEL instance. For example, if the source server is BIOS-based, use the AWS Marketplace RHEL AMI that is also BIOS-based; for UEFI-based systems, choose the UEFI-based AMI.<br />2. Stop both instances: the new LI instance and the original source instance.<br />3. Detach all EBS volumes (including the root disk) from the new LI instance and delete them.<br />4. Detach all EBS volumes (including the root disk) from the old source instance and attach them to the new LI instance. Keep the same mapping of volumes to devices. (For example, the EBS volume that was previously attached to the `/dev/sda` drive must be attached as `/dev/sda` to the new instance.)<br />5. Delete the source (now diskless) instance.<br />6. Start the new LI instance. Log in to the instance and reconfigure it to use the AWS-provided RHUI servers by following the steps in the next epic. | Cloud administrator |

### Reconfigure RHEL OS to use AWS-provided RHUI – both options
<a name="reconfigure-rhel-os-to-use-aws-provided-rhui-ndash-both-options"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deregister the OS from the Red Hat subscription and license. | After migration and successful cutover, the RHEL system has to be removed from the Red Hat subscription to stop consuming the Red Hat license and avoid double billing.<br />To remove RHEL OS from the Red Hat subscription, follow the process described in the [Red Hat Subscription Management (RHSM) documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/installation_guide/chap-subscription-management-unregistering). Use the CLI command:  <pre>subscription-manager unregister</pre><br />You can also disable the subscription manager plugin to stop checking the status of the subscription on every **yum** call. To do this, edit the configuration file `/etc/yum/pluginconf.d/subscription-manager.conf` and change the parameter `enabled=1` to `enabled=0`. | Linux or system administrator |
| Replace the old update configuration (RHUI, Red Hat Satellite network, yum repositories) with the AWS-provided RHUI. | You must reconfigure the migrated RHEL system to use the AWS-provided RHUI servers. This gives you access to the RHUI servers within AWS Regions without requiring the external update infrastructure. The change involves the following process:1. Back up the existing **yum** configuration.<br />2. Remove the old RHUI (**yum** repositories) configuration and packages.<br />3. Add the new AWS-provided RHUI configuration and certificate packages. You have to retrieve these from another RHEL instance on AWS because these configuration packages are available only on AWS-provided RHUI servers.<br />Here are the detailed steps and commands:1. Back up the existing **yum** configuration and certificates by copying all `/etc/yum*` and `/etc/pki/*` folders to a backup location. For example:<pre>mkdir yum-backup<br />cp -ra /etc/yum* /etc/pki ./yum-backup<br />tar czf yum-backup.tgz ./yum-backup</pre><br />2. Remove the old RHUI configuration and packages:Find all installed RHUI packages:<pre> sudo rpm -qa | grep rhui</pre>Delete these packages:<pre> sudo yum remove $(rpm -qa | grep rhui)</pre>Remove the `/etc/yum/vars/releasever` file, if it exists.<br />3. Add the new AWS-provided RHUI and certificate packages. You must retrieve these from another RHEL instance on AWS. There are several ways to do this. For example, you can follow the instructions provided in the [Red Hat Knowledgebase article](https://access.redhat.com/solutions/5009491):Launch another RHEL (RHEL-EC2) instance from [AWS Marketplace](https://aws.amazon.com/marketplace).Download two packages from this instance: the latest RHUI client configuration package and the certificate authority (CA) certificates. For example, run this command from your desktop:<pre>ssh RHEL-EC2 "sudo yumdownloader ca-certificates rh-amazon-rhui-client"</pre>Copy the packages from the RHEL-EC2 instance to the new migrated system. For example:<pre>scp RHEL-EC2:rh-amazon-rhui-client\* RHEL-EC2:ca-certificates\* .<br />ssh <migrated-instance> "mkdir /tmp/amazon"<br />scp rh-amazon-rhui-client* ca-certificates* <migrated-instance>:/tmp/amazon</pre>Install the new RHUI and CA configuration packages on the migrated instance: <pre>ssh <migrated-instance> "sudo rpm -Uhv /tmp/amazon/*"</pre> | Linux or system administrator |
| Validate the configuration. | On the target migrated instance, verify that the new configuration is correct:<pre>sudo yum clean all <br />sudo yum repolist </pre> | Linux or system administrator |

## Related resources
<a name="migrate-rhel-byol-systems-to-aws-license-included-instances-by-using-aws-mgn-resources"></a>
+ [AWS Application Migration Service (AWS MGN) User Guide](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html)
+ [Get an AWS RHUI client package supporting IMDSv2](https://access.redhat.com/solutions/5009491) (Red Hat Knowledgebase article)
+ [Amazon EC2 launch templates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) (Amazon EC2 documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
