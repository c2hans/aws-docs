---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Deltaintro.html
---

# Introduction to Delta Lake
<a name="Deltaintro"></a>

Delta Lake is an open-source project that helps implement modern data lake architectures commonly built on Amazon S3. Delta Lake offers the following capabilities:
+ Atomic, consistent, isolated, durable (ACID) transactions on Spark. Readers see a consistent view of the table during a Spark job.
+ Scalable metadata handling with distributed processing by Spark.
+ Combines streaming and batch uses cases with the same Delta table.
+ Automatic schema enforcement to avoid bad records during data ingestion.
+ Time travel with data versioning.
+ Supports merge, update, and delete operations for complex use cases like change data capture (CDC), streaming upserts, and more.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
