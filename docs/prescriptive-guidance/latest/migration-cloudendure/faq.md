---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions about using CloudEndure Migration to migrate your workloads. For additional information, see the [FAQ](https://docs.cloudendure.com/Content/FAQ/FAQ/FAQ.htm) on the CloudEndure website.

**Q.** Can I use my existing Windows licensing with CloudEndure Migration?

**A. **You have a variety of options for using new and existing Microsoft software licenses on the AWS Cloud.
+ You can purchase Amazon EC2 or Amazon Relational Database Service (Amazon RDS) license-included instances to get new, fully compliant Windows Server and SQL Server licenses from AWS.
+ You can use your existing licenses on AWS with Amazon EC2 Dedicated Hosts, Amazon EC2 Dedicated Instances, or EC2 instances with default tenancy by using [Microsoft License Mobility through Software Assurance](https://aws.amazon.com/windows/resources/licensemobility/). Whether you want to purchase new Microsoft licenses, or utilize existing ones, you can rely on AWS to run your Microsoft software.

CloudEndure converts Microsoft Windows licenses to AWS Windows licenses and activates them by using Microsoft Key Management Service. If license activation fails, follow the [instructions on the AWS support website](https://aws.amazon.com/premiumsupport/knowledge-center/windows-activation-fails/)  to resolve the issue.

**Q.**  Can I use my existing Linux licenses with CloudEndure Migration?

**A. **When you migrate your Linux machines to AWS with CloudEndure Migration, you must supply your own Linux OS licenses (BYOL). That is, AWS will not assign its own Linux OS licenses automatically.

**Q. **What is the required bandwidth for TCP port 1500 to replicate data?

**A. **The required bandwidth for transferring the replicated data over TCP port 1500 should be based on the write speed of the participating source machines. The minimum bandwidth is the sum of the average write speed of all replicated source machines.

For example, if you are replicating two source machines that have write speeds of 5 megabytes per second (MBps) and 7 MBps, the recommended bandwidth should be at least 12 MBps.

**Q. **Can I change the default disk type to SSD instead of Provisioned SSD in the Blueprint for the target instance?

**A. **You can change the default disk type, but this affects the first boot time of the target machine. The target machine will boot much more slowly the first time on AWS. Sometimes, this process is so slow that some Windows processes will time out and network drivers won't be activated during bootup time.

**Q.** How can I route replication traffic when I have multiple leased lines in the source? Is there configuration setting I can use in CloudEndure? **A.** CloudEndure uses standard routing. If you configure the router to push the data to the IP addresses to the staging area over the second link, this is what it'll do.

**Q.** What compression mechanism does CloudEndure use during replication? **A.** CloudEndure uses [Lempel-Ziv-Welch (LZW) compression](https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/) during transit, which results in 60-70% compression, depending on the type of data.

**Q.** What does the CloudEndure machine conversion server do?

**A.** The machine conversion server runs in the target infrastructure and converts the disks to boot. Specifically, this server makes bootloader changes, injects hypervisor drivers, and installs cloud tools. The CloudEndure machine conversion process typically takes less than a minute.

**Q.** What are the differences between conversion servers and replication servers?

**A.** Here's a list of similarities and differences between the two server types:
+ Replication servers run on Linux, and conversion servers (for Windows machines) run on Windows.
+ When CloudEndure launches replication servers, it automatically places Windows conversion servers in the same subnet as the replication servers.
+ Both conversion and replication servers have public IPs.
+ Conversion servers use the same security groups as replication servers.
+ The conversion server must be able to access the CloudEndure Service Manager.
+ The conversion server machines, just like replication servers, are managed automatically by CloudEndure. Any attempt to disrupt their automated functionality will result in failed conversions.

**Q. **Which AWS Regions does CloudEndure use for production and disaster recovery?

**A.**  CloudEndure uses US East (N. Virginia) for production and US West (N. California) for disaster recovery. Data is copied from the production Region to the disaster recovery Region over a private AWS network.

**Q. **What is the effect of having a dedicated replication server?

**A.** The dedicated replication instance makes full use of available bandwidth to accelerate replication.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
