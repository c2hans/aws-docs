---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-amazon-rds-db-instance-to-another-vpc-or-account.html
---

# Migrate an Amazon RDS DB instance to another VPC or account
<a name="migrate-an-amazon-rds-db-instance-to-another-vpc-or-account"></a>

*Dhrubajyoti Mukherjee, Amazon Web Services*

## Summary
<a name="migrate-an-amazon-rds-db-instance-to-another-vpc-or-account-summary"></a>

This pattern provides guidance for migrating an Amazon Relational Database Service (Amazon RDS) DB instance from one virtual private cloud (VPC) to another in the same AWS account, or from one AWS account to another AWS account.

This pattern is useful if you want to migrate your Amazon RDS DB instances to another VPC or account for separation or security reasons (for example, when you want to place your application stack and database in different VPCs).

Migrating a DB instance to another AWS account involves steps such as taking a manual snapshot, sharing it, and restoring the snapshot in the target account. This process can be time-consuming, depending on database changes and transaction rates. It also causes database downtime, so plan ahead for the migration. Consider a blue/green deployment strategy to minimize downtime. Alternatively, you can evaluate AWS Data Migration Service (AWS DMS) to minimize downtime for the change. However, this pattern doesn’t cover this option. To learn more, see the [AWS DMS documentation.](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)

## Prerequisites and limitations
<a name="migrate-an-amazon-rds-db-instance-to-another-vpc-or-account-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ AWS Identity and Access Management (IAM) permissions required for the VPC, subnets, and Amazon RDS console

**Limitations**
+ Changes to a VPC cause a database reboot, resulting in application outages. We recommend that you migrate during low peak times.
+ Limitations when migrating Amazon RDS to another VPC:
  + The DB instance you’re migrating must be a single instance with no standby. It must not be a member of a cluster.
  + Amazon RDS must not be in multiple Availability Zones.
  + Amazon RDS must not have any read replicas.
  + The subnet group created in the target VPC must have subnets from the Availability Zone where the source database is running.
+ Limitations when migrating Amazon RDS to another AWS account:
  + Sharing snapshots encrypted with the default service key for Amazon RDS isn‘t currently supported.

## Architecture
<a name="migrate-an-amazon-rds-db-instance-to-another-vpc-or-account-architecture"></a>

**Migrating to a VPC in the same AWS account**

The following diagram shows the workflow for migrating an Amazon RDS DB instance to a different VPC in the same AWS account.

![Workflow for migrating an Amazon RDS DB instance to a different VPC in the same AWS account](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/dabcee69-9cc6-47f9-9964-635e349caaaf/images/73e16544-6276-4f03-9ae2-42b8c7c20315.png)

The steps consist of the following. See the [Epics](#migrate-an-amazon-rds-db-instance-to-another-vpc-or-account-epics) section for detailed instructions.

1. Create a DB subnet group in the target VPC. A DB subnet group is a collection of subnets that you can use to specify a specific VPC when you create DB instances.

1. Configure the Amazon RDS DB instance in the source VPC to use the new DB subnet group.

1. Apply the changes to migrate the Amazon RDS DB to the target VPC.

**Migrating to a different AWS account**

The following diagram shows the workflow for migrating an Amazon RDS DB instance to a different AWS account.

![Workflow for migrating an Amazon RDS DB instance to a different AWS account](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/dabcee69-9cc6-47f9-9964-635e349caaaf/images/5536e69e-3965-4ca2-8a0b-2573659b5f8f.png)

The steps consist of the following. See the [Epics](#migrate-an-amazon-rds-db-instance-to-another-vpc-or-account-epics) section for detailed instructions.

1. Access the Amazon RDS DB instance in the source AWS account.

1. Create an Amazon RDS snapshot in the source AWS account.

1. Share the Amazon RDS snapshot with the target AWS account.

1. Access the Amazon RDS snapshot in the target AWS account.

1. Create an Amazon RDS DB instance in the target AWS account.

## Tools
<a name="migrate-an-amazon-rds-db-instance-to-another-vpc-or-account-tools"></a>

**AWS services**
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

## Best practices
<a name="migrate-an-amazon-rds-db-instance-to-another-vpc-or-account-best-practices"></a>
+ If database downtime is a concern when migrating an Amazon RDS DB instance to another account, we recommend that you use [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html). This service provides data replication, which causes less than five minutes of outage time.

## Epics
<a name="migrate-an-amazon-rds-db-instance-to-another-vpc-or-account-epics"></a>

### Migrate to a different VPC in the same AWS account
<a name="migrate-to-a-different-vpc-in-the-same-aws-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a new VPC. | On the [Amazon VPC console](https://console.aws.amazon.com/vpc/), create a new VPC and subnets with the desired properties and IP address ranges. For detailed instructions, see the [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html). | Administrator |
| Create a DB subnet group. | On the [Amazon RDS console](https://console.aws.amazon.com/rds/):1. Choose **Subnet groups**, **Create DB subnet group.**<br />2. Enter the subnet group name, description, and VPC ID.<br />3. Add the subnets that belong to the subnet group. Add subnets to cover at least two Availability Zones.<br />4. Choose **Create**.<br />For additional information, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.CreateDBSubnetGroup). | Administrator |
| Modify the Amazon RDS DB instance to use the new subnet group. | On the Amazon RDS console:1. In the navigation pane, choose **Databases**, and then choose the Amazon RDS DB instance to be migrated.<br />2. In the **Connectivity **section, choose the subnet group that’s associated with the target VPC.<br />3. In the **Schedule modifications** section, choose **Apply immediately**.<br />When the migration to the target VPC is complete, the target VPC's default security group is assigned to the Amazon RDS DB instance. You can configure a new security group for that VPC with the required inbound and outbound rules to your DB instance.<br />Alternatively, use the AWS Command Line Interface (AWS CLI) to perform the migration to the target VPC by explicitly providing the new VPC security group ID. For example:<pre>aws rds modify-db-instance \<br />    --db-instance-identifier testrds \<br />    --db-subnet-group-name new-vpc-subnet-group \<br />    --vpc-security-group-ids sg-idxxxx \<br />    --apply-immediately</pre> | Administrator |

### Migrate to a different AWS account
<a name="migrate-to-a-different-aws-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a new VPC and subnet group in the target AWS account. | 1. On the [Amazon VPC console](https://console.aws.amazon.com/vpc/), create a new VPC with the desired properties and IP address ranges. For detailed instructions, see the [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html).<br />2. Create subnets for the new VPC by following the instructions in the [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/create-subnets.html).<br />3. On the [Amazon RDS console](https://console.aws.amazon.com/rds/), create DB subnet groups. For instructions, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.CreateDBSubnetGroup). | Administrator |
| Share a manual snapshot of the database and share it with the target account. | 1. Take a manual snapshot of the source database by following the instructions in the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html).<br />2. Share the snapshot with the target AWS account by providing the target account ID. For instructions, see the [re:Post article](https://repost.aws/knowledge-center/rds-snapshots-share-account) about sharing DB snapshots with other accounts. | Administrator |
| Launch a new Amazon RDS DB instance. | Launch a new Amazon RDS DB instance from the shared snapshot in the target AWS account. For instructions, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RestoreFromSnapshot.html). | Administrator |

## Related resources
<a name="migrate-an-amazon-rds-db-instance-to-another-vpc-or-account-resources"></a>
+ [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
+ [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
+ [How do I change the VPC for an RDS DB instance?](https://aws.amazon.com/premiumsupport/knowledge-center/change-vpc-rds-db-instance/) (AWS re:Post article)
+ [How do I transfer ownership of Amazon RDS resources to a different AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/account-transfer-rds/) (AWS re:Post article)
+ [How do I share manual Amazon RDS DB snapshots or Aurora DB cluster snapshots with another AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/rds-snapshots-share-account/) (AWS re:Post article)
+ [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
