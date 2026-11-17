---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-bulky-oracle-databases/conclusion.html
---

# Conclusion
<a name="conclusion"></a>

In this guide, you learned how to minimize downtime by using Oracle cross-platform transportable tablespaces and RMAN incremental backups with Snowball Edge, AWS Direct Connect, and Amazon FSx for Lustre.

When migrating an Oracle database from on premises to AWS, consider the following variables:
+ The network bandwidth required by Direct Connect
+ The capacity of FSx for Lustre
+ The metadata size of the Oracle database
+ The incremental backup size

When you use the method in this guide to migrate a 100 TB Oracle database running on a Unix system to AWS, you can reduce downtime to around 10 hours.
