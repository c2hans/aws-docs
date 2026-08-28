---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost05-bp01.html
---

# ADVCOST05-BP01 Use cost efficient data types and configurations for collaborative data environments
<a name="advcost05-bp01"></a>

 Use efficient storage formats and streamlined query configurations to reduce unnecessary data scanning, duplication, and transfer costs in collaborative analytics environments.

## Implementation guidance
<a name="imp-guidance-advcost05-bp01"></a>
+  Use parquet or columnar formats with partitioning and compress datasets.
+  Use standard SQL for lightweight or well-partitioned datasets.
+  Avoid unnecessary cross-joins or full table scans.
+  Use same-Region AWS Clean Rooms collaborations to minimize inter-Region transfer costs.

## Key AWS services
<a name="key-aws-services-51"></a>
+  AWS Clean Rooms

## Resources
<a name="resources-73"></a>
+  [Data formats for AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/data-formats.html)
+  [Data Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-10.4---partition-your-data-to-avoid-unnecessary-file-reads.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
