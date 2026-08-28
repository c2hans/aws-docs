---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-redshift.html
---

# Using Amazon Redshift integration for Apache Spark with Amazon EMR
<a name="emr-spark-redshift"></a>

With Amazon EMR release 6.4.0 and later, every release image includes a connector between [Apache Spark](https://aws.amazon.com/emr/features/spark/) and Amazon Redshift. With this connector, you can use Spark on Amazon EMR to process data stored in Amazon Redshift. For Amazon EMR releases 6.4.0 through 6.8.0, the integration is based on the [`spark-redshift` open-source connector](https://github.com/spark-redshift-community/spark-redshift#readme). For Amazon EMR releases 6.9.0 and later, the [Amazon Redshift integration for Apache Spark](https://docs.aws.amazon.com/redshift/latest/mgmt/spark-redshift-connector.html) has been migrated from the community version to a native integration.

**Topics**
+ [Launching a Spark application using the Amazon Redshift integration for Apache Spark](emr-spark-redshift-launch.md)
+ [Authenticating with Amazon Redshift integration for Apache Spark](emr-spark-redshift-auth.md)
+ [Reading and writing from and to Amazon Redshift](emr-spark-redshift-readwrite.md)
+ [Considerations and limitations when using the Spark connector](emr-spark-redshift-considerations.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
