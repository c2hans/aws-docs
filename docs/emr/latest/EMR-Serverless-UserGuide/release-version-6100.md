---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-6100.html
---

# EMR Serverless 6.10.0
<a name="release-version-6100"></a>

The following table lists the application versions available with EMR Serverless 6.10.0.

| Application | Version |
| --- | --- |
| Apache Spark | 3.3.1 |
| Apache Hive | 3.1.3 |
| Apache Tez | 0.10.2 |

**EMR Serverless 6.10.0 release notes**
+ For EMR Serverless applications with release 6.10.0 or higher, the default value for the `spark.dynamicAllocation.maxExecutors` property is `infinity`. Earlier releases default to `100`. For more information, refer to [Spark job properties](jobs-spark.md#spark-defaults).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
