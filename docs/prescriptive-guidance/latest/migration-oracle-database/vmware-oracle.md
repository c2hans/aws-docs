---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/vmware-oracle.html
---

# VMware Cloud on AWS for Oracle
<a name="vmware-oracle"></a>

VMware Cloud on AWS is an integrated cloud offering jointly developed by AWS and VMware. When you migrate Oracle Database to VMware Cloud on AWS, you have full control of the database and operating system-level access, as with Amazon EC2. You can run advanced architectures like Oracle Real Application Cluster (RAC) and Oracle RAC extended clusters (across different Availability Zones) in VMware Cloud on AWS. You can choose from a number of migration methods and tools based on your needs and your existing system.

For online migrations, VMware technologies like VMware Hybrid Cloud Extension (VMware HCX) and HCX vMotion help you migrate VM workloads from on-premises VMware clusters to VMware Cloud on AWS. For offline migrations of Oracle workloads, you can use Oracle RMAN, [AWS Snowball](https://aws.amazon.com/snowball/), [AWS Storage Gateway](https://aws.amazon.com/storagegateway/), or VMware HCX.

## When to choose VMware Cloud on AWS
<a name="vmware-oracle-choosing"></a>

VMware Cloud on AWS is a good option for your Oracle database when:
+ Your Oracle databases are already running in an on-premises data center in vSphere virtualized environments.
+ You need to run Oracle RAC in the cloud.
+ You have a large number of databases and you need fast migration (for example, only a few hours) to the cloud without requiring any additional work from the migration team.

For more information, see the blog posts [How to Migrate Oracle Workloads to VMware Cloud on AWS](https://aws.amazon.com/blogs/apn/how-to-migrate-oracle-workloads-to-vmware-cloud-on-aws/) and [Best Practices for Virtualizing Oracle RAC with VMware Cloud on AWS](https://aws.amazon.com/blogs/apn/virtualizing-oracle-rac-with-vmware-cloud-on-aws/) on the AWS Partner Network (APN) blog.
