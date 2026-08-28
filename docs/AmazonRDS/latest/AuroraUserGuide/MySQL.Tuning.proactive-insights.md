---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/MySQL.Tuning.proactive-insights.html
---

# Tuning Aurora MySQL with Amazon DevOps Guru proactive insights
<a name="MySQL.Tuning.proactive-insights"></a>

DevOps Guru proactive insights detect known problematic conditions on your Aurora MySQL DB clusters before they occur. DevOps Guru can do the following:
+ Prevent many common database issues by cross-checking your database configuration against common recommended settings.
+ Alert you to critical issues in your fleet that, if left unchecked, can lead to larger problems later.
+ Alert you to newly discovered problems.

Every proactive insight contains an analysis of the cause of the problem and recommendations for corrective actions.

**Topics**
+ [The InnoDB history list length increased significantly](proactive-insights.history-list.md)
+ [Database is creating temporary tables on disk](proactive-insights.temp-tables.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
