---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-troubleshooting-queries-failed.html
---

# Queries are unexpectedly failing for Ranger integration with Amazon EMR
<a name="emr-ranger-troubleshooting-queries-failed"></a>

**Check Apache Ranger plugin logs (Apache Hive, EMR RecordServer, EMR SecretAgent, etc., logs)**

This section is common across all applications that integrate with the Ranger plugin, such as Apache Hive, EMR Record Server, and EMR SecretAgent.

**Common Error Messages**

| Error message | Cause |
| --- | --- |
| ERROR PolicyRefresher:272 - [] PolicyRefresher(serviceName=policy-repository): failed to find service. Will clean up local cache of policies (-1)  | This error messages means that the service name you provided in the EMR security configuration does not match a service policy repository in the Ranger Admin server. |

If within Ranger Admin server your AMAZON-EMR-SPARK service looks like the following, then you should enter **amazonemrspark** as the service name.

![Ranger Admin server showing AMAZON-EMR-SPARK troubleshooting.](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/ranger-amazon-emr-spark-troubleshooting.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
