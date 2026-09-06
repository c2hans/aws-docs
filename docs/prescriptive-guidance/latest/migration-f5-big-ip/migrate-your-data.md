---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/migrate-your-data.html
---

# Migrating the data
<a name="migrate-your-data"></a>

All migrations must iterate on a configuration and build out the dependency tree. When using a single configuration file, this is all done for you. If you use the [TMSH API](https://clouddocs.f5.com/api/tmsh/), then you will have to iterate and build out the dependency tree. The following sections will outline the different options and configurations available when migrating an F5 BIG-IP workload.

**Topics**
+ [Migrating a full configuration](migration-at-a-glance.md)
+ [Migrating a partial configuration](migrate-partial-configuration.md)
+ [High-density deployments without Elastic IPs](high-density-deployments.md)
+ [Interconnecting your VPCs](interconnecting-vpcs.md)
+ [Connecting to your AWS infrastructure](considerations-existing-aws-infrastructure.md)
