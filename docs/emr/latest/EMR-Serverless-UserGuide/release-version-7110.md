---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/release-version-7110.html
---

# EMR Serverless 7.11.0
<a name="release-version-7110"></a>

The following table lists the application versions available with EMR Serverless 7.11.0.

| Application | Version |
| --- | --- |
| Apache Spark | 3.5.6 |
| Apache Hive | 3.1.3 |
| Apache Tez | 0.10.2 |

**EMR Serverless 7.11.0 release notes**
+ **Maximum Job execution time** – The maximum value for `executionTimeoutMinutes` in `StartJobRun` action for BATCH jobs is 7 days from this release onwards. `executionTimeoutMinutes` can no longer be set to `0` i.e. no timeout, for batch job runs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
