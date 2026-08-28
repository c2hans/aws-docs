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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
