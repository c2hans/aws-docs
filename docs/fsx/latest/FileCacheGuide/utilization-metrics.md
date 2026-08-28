---
source_url: https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/utilization-metrics.html
---

# Cache utilization metrics
<a name="utilization-metrics"></a>

The following metrics report cache-level storage information. These metrics take one dimension (`FileCacheId`) and are published into the `AWS/FSx` namespace in CloudWatch.

| Metric | Description |
| --- | --- |
| `FreeDataStorageCapacity` | The amount of available data storage capacity.<br />The `Sum` statistic is the total number of bytes available in the cache The `Minimum` statistic is the total number bytes available in the fullest disk. The `Maximum` statistic is the total number of bytes available in the disk with the most remaining available storage. The `Average` statistic is the average number of bytes available per disk. The `SampleCount` statistic is the number of disks.<br />Units:+  Bytes for `Sum`, `Minimum`, `Maximum`. <br />+  Count for `SampleCount`. <br />Valid statistics: `Sum`, `Minimum`, `Maximum`, `Average`, `SampleCount`. |
| `FreeMetadataStorageCapacity` | The amount of available metadata storage capacity.<br />The `Sum` statistic is the total number of bytes of metadata storage available in the cache. The `Minimum` statistic is the total number of bytes available in the fullest metadata target (MDT) disk. The `Maximum` statistic is the total number of bytes available in the MDT disk with the most remaining storage. The `Average` statistic is the average number of bytes available per MDT disk. The `SampleCount` statistic is the number of MDT disks.<br />Units:+  Bytes for `Sum`, `Minimum`, `Maximum`, `Average`. <br />+  Count for `SampleCount`. <br />Valid statistics: `Sum`, `Minimum`, `Maximum`, `Average`, `SampleCount`. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
