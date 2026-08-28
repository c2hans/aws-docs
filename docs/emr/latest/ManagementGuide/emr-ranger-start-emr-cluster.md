---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-start-emr-cluster.html
---

# Start an EMR cluster with Apache Ranger
<a name="emr-ranger-start-emr-cluster"></a>

Before you launch an Amazon EMR cluster with Apache Ranger, make sure each component meets the following minimum version requirement:
+ Amazon EMR 5.32.0 or later, or 6.3.0 or later. We recommend that you use the latest Amazon EMR release version.
+ Apache Ranger Admin server 2.x.

Complete the following steps.
+ Install Apache Ranger if you haven't already. For more information, see [Apache Ranger 0.5.0 installation](https://cwiki.apache.org/confluence/display/RANGER/Apache+Ranger+0.5.0+Installation).
+ Make sure there is network connectivity between your Amazon EMR cluster and the Apache Ranger Admin server. See [Set up a Ranger Admin server to integrate with Amazon EMR](emr-ranger-admin.md)
+ Create the necessary IAM Roles. See [IAM roles for native integration with Apache Ranger](emr-ranger-iam.md).
+ Create a EMR security configuration for Apache Ranger installation. See more information, see [Create the EMR security configuration](emr-ranger-security-config.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
