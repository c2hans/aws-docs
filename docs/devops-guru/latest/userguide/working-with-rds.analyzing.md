---
source_url: https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-rds.analyzing.html
---

# Analyzing anomalies in Amazon RDS
<a name="working-with-rds.analyzing"></a>

When DevOps Guru for RDS publishes a performance anomaly in the dashboard, you typically perform the following steps:

1. View the insight in the DevOps Guru dashboard. DevOps Guru for RDS reports both reactive and proactive insights.

   For more information, see [Viewing insights](working-with-rds.analyzing.insights.md).

1. View anomalies for **AWS/RDS** resources.

   For more information, see [Viewing reactive anomalies](working-with-rds.analyzing.metrics.md) and [Viewing proactive anomalies](working-with-rds.analyzing.proactive.metrics.md).

1. Respond to DevOps Guru for RDS recommendations.

   For more information, see [Responding to recommendations](working-with-rds.analyzing.recommend.md).

1. Monitor the health of your DB instances to make sure that resolved performance problems don't recur.

   For more information, see [Monitoring metrics in an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/MonitoringAurora.html) in the *Amazon Aurora User Guide* and [Monitoring metrics in an Amazon RDS instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Monitoring.html) in the *Amazon RDS User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
