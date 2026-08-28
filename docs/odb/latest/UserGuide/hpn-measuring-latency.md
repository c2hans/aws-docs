---
source_url: https://docs.aws.amazon.com/odb/latest/UserGuide/hpn-measuring-latency.html
---

# Measuring network latency
<a name="hpn-measuring-latency"></a>

To measure and validate network latency between your Amazon EC2 instances and Oracle Database@AWS databases, we recommend using **sockperf**, an open-source TCP-level latency measurement tool. sockperf provides complementary network metrics that help you:
+ Establish network performance baselines
+ Compare performance before and after infrastructure changes
+ Validate that sub-millisecond latency targets are being met

You can also use Oracle database performance tools such as [**Automatic Workload Repository (AWR)**](https://docs.oracle.com/en/engineered-systems/exadata-database-machine/sagug/awr.html), [**Active Session History (ASH)**](https://docs.oracle.com/en/database/oracle/oracle-database/26/tgdba/ash-report-ui.html), and [**SQL Trace**](https://docs.oracle.com/en/database/oracle/oracle-database/26/tgsql/performing-application-tracing.html#GUID-31EF2BD5-28DB-488F-A855-8DA324F6970B) for database-level performance analysis.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database at AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
