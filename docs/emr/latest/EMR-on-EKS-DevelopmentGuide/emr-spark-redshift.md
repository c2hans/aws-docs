---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-spark-redshift.html
---

# Using Amazon Redshift integration for Apache Spark on Amazon EMR on EKS
<a name="emr-spark-redshift"></a>

With Amazon EMR release 6.9.0 and later, every release image includes a connector between [Apache Spark](https://aws.amazon.com/emr/features/spark/) and Amazon Redshift. This way, you can use Spark on Amazon EMR on EKS to process data stored in Amazon Redshift. The integration is based on the [`spark-redshift` open-source connector](https://github.com/spark-redshift-community/spark-redshift#readme). For Amazon EMR on EKS, the [Amazon Redshift integration for Apache Spark](https://docs.aws.amazon.com/redshift/latest/mgmt/spark-redshift-connector.html) is included as a native integration.

**Topics**
+ [Launching a Spark application using the Amazon Redshift integration for Apache Spark](emr-spark-redshift-launch.md)
+ [Authenticating with the Amazon Redshift integration for Apache Spark](emr-spark-redshift-auth.md)
+ [Reading and writing from and to Amazon Redshift](emr-spark-redshift-readwrite.md)
+ [Considerations and limitations when using the Spark connector](emr-spark-redshift-considerations.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
