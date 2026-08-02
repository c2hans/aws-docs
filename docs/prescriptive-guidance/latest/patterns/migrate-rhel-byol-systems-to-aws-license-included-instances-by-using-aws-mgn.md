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
| Find the AMI ID of the RHEL AWS LI instance in the target Region. | Visit [AWS Marketplace](https://aws.amazon.com/marketplace) or use the [Amazon EC2 console](https://console.aws.amazon.com/ec2/) to find the RHEL AMI ID that matches the version of the RHEL source system (for example, RHEL-7.7), and write down the AMI ID. On the Amazon EC2 console, you can filter the AMIs by using one of the following search terms:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-rhel-byol-systems-to-aws-license-included-instances-by-using-aws-mgn.html) | Cloud administrator |
| Configure AWS MGN launch settings.  | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-rhel-byol-systems-to-aws-license-included-instances-by-using-aws-mgn.html)AWS MGN will now use this version of the launch template to launch test or cutover instances. For more information, see the [AWS MGN documentation](https://docs.aws.amazon.com/mgn/latest/ug/ec2-launch.html). | Cloud administrator |
| Validate settings. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-rhel-byol-systems-to-aws-license-included-instances-by-using-aws-mgn.html) | Cloud administrator |
| Launch the new LI instance. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-rhel-byol-systems-to-aws-license-included-instances-by-using-aws-mgn.html) | Cloud administrator |

### Migrate to LI instance - option 2 (for a RHEL BYOL EC2 instance)
<a name="migrate-to-li-instance---option-2-for-a-rhel-byol-ec2-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate your RHEL BYOL EC2 instance to an AWS LI instance. | You can switch RHEL systems that you previously migrated to AWS as BYOL to AWS LI instances by moving their disks (Amazon Elastic Block Store volumes) and attaching them to a new LI instance. To make this switch, follow these steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-rhel-byol-systems-to-aws-license-included-instances-by-using-aws-mgn.html) | Cloud administrator |

### Reconfigure RHEL OS to use AWS-provided RHUI – both options
<a name="reconfigure-rhel-os-to-use-aws-provided-rhui-ndash-both-options"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deregister the OS from the Red Hat subscription and license. | After migration and successful cutover, the RHEL system has to be removed from the Red Hat subscription to stop consuming the Red Hat license and avoid double billing.<br />To remove RHEL OS from the Red Hat subscription, follow the process described in the [Red Hat Subscription Management (RHSM) documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/installation_guide/chap-subscription-management-unregistering). Use the CLI command:  <pre>subscription-manager unregister</pre><br />You can also disable the subscription manager plugin to stop checking the status of the subscription on every **yum** call. To do this, edit the configuration file `/etc/yum/pluginconf.d/subscription-manager.conf` and change the parameter `enabled=1` to `enabled=0`. | Linux or system administrator |
| Replace the old update configuration (RHUI, Red Hat Satellite network, yum repositories) with the AWS-provided RHUI. | You must reconfigure the migrated RHEL system to use the AWS-provided RHUI servers. This gives you access to the RHUI servers within AWS Regions without requiring the external update infrastructure. The change involves the following process:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-rhel-byol-systems-to-aws-license-included-instances-by-using-aws-mgn.html)<br />Here are the detailed steps and commands:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-rhel-byol-systems-to-aws-license-included-instances-by-using-aws-mgn.html) | Linux or system administrator |
| Validate the configuration. | On the target migrated instance, verify that the new configuration is correct:<pre>sudo yum clean all <br />sudo yum repolist </pre> | Linux or system administrator |

## Related resources
<a name="migrate-rhel-byol-systems-to-aws-license-included-instances-by-using-aws-mgn-resources"></a>
+ [AWS Application Migration Service (AWS MGN) User Guide](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html)
+ [Get an AWS RHUI client package supporting IMDSv2](https://access.redhat.com/solutions/5009491) (Red Hat Knowledgebase article)
+ [Amazon EC2 launch templates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) (Amazon EC2 documentation)
