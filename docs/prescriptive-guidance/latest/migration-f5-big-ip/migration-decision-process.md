---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/migration-decision-process.html
---

# Deciding what to migrate
<a name="migration-decision-process"></a>

When you migrate, you have to decide which workloads are essential; which workloads are "nice to have" but not essential; and which workloads are not necessary and can be [retired once the migration is complete.](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-retiring-applications/welcome.html)

A significant part of your decision-making process will involve individual requirements that you have for automation, API, tooling, and other processes. You will also need to consider your organization's functional and performance requirements.

For example, you might have used shared hardware platforms in an existing data center with user partitions. However, your migration might require that services run on systems that are not as widely shared due to performance limitations of moving from hardware-accelerated solutions. For instance, Secure Sockets Layer (SSL) transactions per second (TPS) could require that a certain service does not run on a shared system.

After you identify and document which applications will migrate and their requirements, you need to prepare your source systems by using the following best practices.
+ Run the same version of F5 TMOS that you will run in the AWS Cloud. [Version 14.1](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/releasenotes/product/relnote-bigip-14-1-0.html) or later is recommended, but [version 13.1](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/releasenotes/product/relnote-bigip-ve-13-1-0.html) or later can also be used. Although you can migrate version [12.1.x](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/releasenotes/product/relnote-bigip-12-1-5.html), you might encounter security, automation, and maintainability issues.
+ Have valid backups of all configurations from each device. Since the Univention Corporate Server (UCS) backup contains attributes and objects that are specific to the data center (such as IP addresses, nodes, or pool members), F5 recommends that you create a shell command file (SCF) to edit and merge the configurations.
+ Have backups of all relevant security certificates, and consider changing from RSA to ECC encryption for better performance.
+ Have detailed performance metrics at the virtual server level for scaling and capacity planning.
+ Have an [F5 Global Server Load Balancing (GSLB)](https://www.f5.com/solutions/use-cases/global-server-load-balancing-gslb) solution for the cutover from the data center to the AWS Cloud.
+ Understand the impact of migrating from a hardware appliance model to a software and virtualized model in terms of performance, scalability, and high availability.
+ Have defined requirements of what will be migrated to the AWS Cloud, and be aware of the following considerations.
  + Know that any migration to the AWS Cloud requires decisions about whether entire or partial configurations will be migrated. Typically, one partial move at a time is more efficient.
  + Understand which routes and IP addresses will change.
  + Identify which SNAT pools should be replaced with F5 SNAT Automap.

You should also consider consulting [AWS Partners](https://partners.amazonaws.com/partners/001E000000Rl12PIAR/F5%20Networks) or the F5 Professional Services team. This will help ensure a high probability of a successful migration.
