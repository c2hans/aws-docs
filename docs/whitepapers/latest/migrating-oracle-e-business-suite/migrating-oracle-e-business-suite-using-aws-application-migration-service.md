---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/migrating-oracle-e-business-suite-using-aws-application-migration-service.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migrating Oracle E-Business Suite using AWS Transform MGN
<a name="migrating-oracle-e-business-suite-using-aws-application-migration-service"></a>

 [AWS Transform MGN](https://aws.amazon.com/application-migration-service/) (AWS MGN) is a migration and replication tool available from AWS which can be used for migrating the applications as well as for setting up DR environments on AWS. It works by migrating or replicating the blocks of storage devices from source to target. Because it operates at the block level, it can migrate various workloads, including enterprise resource planning (ERP) applications from virtual machines (VMs), cloud, or physical data center. AWS MGN supports migration from any OS to AWS. Following is an architecture showing various components of AWS MGN and how they work together to migrate workloads on AWS.

![Reference architecture diagram showing AWS MGN migration/disaster recovery](http://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/images/aws-mgn-migration-dr.jpg)

 The AWS MGN orchestration engine automatically launches a fully operational Oracle E-Business Suite environment in the target AWS Region, enabling a recovery time objective (RTO) of minutes. The AWS MGN automated machine conversion process takes approximately 30 seconds, and ensures that OS machines replicated from physical, virtual, and cloud-based infrastructure will natively boot and run transparently in AWS, by automatically handling all hypervisor and OS configuration changes, boot process changes, and OS activation and installation of target infrastructure guest agents.

 Major steps involved in migrating Oracle E-Business Suite environment using AWS MGN are as follows:

1.  Identify the list of servers to be migrated by name, and break down the list to migration waves.

1.  Install the AWS MGN software agents on the selected servers to initiate replication and confirm replication progress within the AWS MGN console.

1.  Assess source Oracle E-Business Suite network to plan the network creation in the target infrastructure.

1.  Create the target network within the target infrastructure of choice.

1.  Once server replication is complete, create test target machines using the AWS MGN dashboard and confirm that they are functioning and accessible.

1.  Upon confirmation of the successful target machines launch, engage with the business/application owners for Oracle E-Business Suite acceptance tests. If corrections are required, modify the target blueprints accordingly and repeat this step. If the acceptance tests are completed successfully, proceed to cutover.

1.  Cutover procedure:

   1.  Schedule a migration cutover window.

   1.  Prevent user connectivity to the source Oracle E-Business Suite environment.

   1.  Create a final version of the target machines.

   1.  Confirm Oracle E-Business Suite application readiness.

   1.  Redirect user traffic to the new target machines.

   1.  Stop the AWS MGN replication on the source servers that were cutover, and decommission them.

**Notes:**
+  For the database tier, use of Oracle native tools outlined in this document is recommended rather than AWS MGN.
+  If you’re using Oracle ASM or Oracle ASM Filter Driver, refer to [Can Application Migration Service replicate Oracle ASM?](https://docs.aws.amazon.com/mgn/latest/ug/Replication-Related-FAQ.html#Can-Replicate-Oracle-ASM) in the [Application Migration Service whitepaper](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html).
+  If you are using Oracle ASM, note the EC2 volume limits by EC2 instance family at [Linux-specific volume limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html#linux-specific-volume-limits).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
