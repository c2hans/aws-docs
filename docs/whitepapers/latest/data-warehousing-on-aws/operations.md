---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/operations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Operations
<a name="operations"></a>

 As a managed service, Amazon Redshift completely automates many operational tasks, including:
+  **Cluster Performance** — Amazon Redshift performs [Auto ANALYZE](https://docs.aws.amazon.com/redshift/latest/dg/r_ANALYZE.html) to maintain accurate table statistics. It also performs [Auto VACUUM](https://docs.aws.amazon.com/redshift/latest/dg/r_VACUUM_command.html) to ensure that the database storage is efficient and deleted data blocks are reclaimed.
+  **Cost Optimization** — Amazon Redshift enables you to pause and resume the clusters that need to be available only at a specific time, enabling you to suspend on-demand billing while the cluster is not being used. Pause and resume can also be automated using a schedule you define to match your operational needs. Cost controls can be defined on Amazon Redshift clusters to monitor and control your usage and associated cost for [Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum.html) and [Concurrency Scaling](https://docs.aws.amazon.com/redshift/latest/dg/concurrency-scaling.html) features.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
