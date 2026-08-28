---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/how-in-place-version-upgrades.html
---

# Use in-place version upgrades for Apache Flink
<a name="how-in-place-version-upgrades"></a>

With in-place version upgrades for Apache Flink, you retain application traceability against a single ARN across Apache Flink versions. This includes snapshots, logs, metrics, tags, Flink configurations, resource limit increases, VPCs, and more.

You can perform in-place version upgrades for Apache Flink to upgrade existing applications to a new Flink version in Amazon Managed Service for Apache Flink. To perform this task, you can use the AWS CLI, AWS CloudFormation, AWS SDK, or the AWS Management Console.

**Note**
You can't use in-place version upgrades for Apache Flink with Amazon Managed Service for Apache Flink Studio.

**Topics**
+ [Upgrade applications using in-place version upgrades for Apache Flink](upgrading-applications.md)
+ [Upgrade your application to a new Apache Flink version](upgrading-application-new-version.md)
+ [Roll back application upgrades](rollback.md)
+ [General best practices and recommendations for application upgrades](best-practices-recommendations.md)
+ [Precautions and known issues with application upgrades](precautions.md)
+ [Upgrading to Flink 2.2: Complete guide](flink-2-2-upgrade-guide.md)
+ [State compatibility guide for Flink 2.2 upgrades](state-compatibility.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
