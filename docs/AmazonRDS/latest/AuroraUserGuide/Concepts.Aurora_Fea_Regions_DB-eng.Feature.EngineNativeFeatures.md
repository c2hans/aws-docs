---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.EngineNativeFeatures.html
---

# Supported Regions and DB engines for Aurora engine-native features
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.EngineNativeFeatures"></a>

Aurora database engines also support additional features and functionality specifically for Aurora. Some engine-native features might have limited support or restricted privileges for a particular Aurora DB engine, version, or Region.

**Topics**
+ [Engine-native features for Aurora MySQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.EngineNativeFeatures.amy)
+ [Engine-native features for Aurora PostgreSQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.EngineNativeFeatures.apg)

## Engine-native features for Aurora MySQL
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.EngineNativeFeatures.amy"></a>

Following are the engine-native features for Aurora MySQL.
+ [Advanced Auditing](AuroraMySQL.Auditing.md)
+ [Backtrack](AuroraMySQL.Managing.Backtrack.md)
+ [Fault injection queries](AuroraMySQL.Managing.FaultInjectionQueries.md)
+ [In-cluster write forwarding](aurora-mysql-write-forwarding.md)
+ [Parallel query](aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-planning)

## Engine-native features for Aurora PostgreSQL
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.EngineNativeFeatures.apg"></a>

Following are the engine-native features for Aurora PostgreSQL.
+ [Babelfish](babelfish.md)
+ [Fault injection queries](AuroraPostgreSQL.Managing.FaultInjectionQueries.md)
+ [Query plan management](AuroraPostgreSQL.Optimize.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
