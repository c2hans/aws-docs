---
source_url: https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/how_to_use_metrics.html
---

# How to use Amazon File Cache metrics
<a name="how_to_use_metrics"></a>

The metrics reported by Amazon File Cache provide information that you can analyze in different ways. The following list shows some common uses for the metrics. These are suggestions to get you started, not a comprehensive list.

| How Do I Determine... | Relevant Metrics |
| --- | --- |
| My cache's throughput? | SUM(DataReadBytes \+ DataWriteBytes)/Period (in seconds) |
| My cache's IOPS? | Total IOPS = SUM(DataReadOperations \+ DataWriteOperations \+ MetadataOperations)/Period (in seconds) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
