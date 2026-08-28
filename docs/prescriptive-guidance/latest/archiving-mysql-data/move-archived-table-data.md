---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/move-archived-table-data.html
---

# Moving archived table data to Amazon S3
<a name="move-archived-table-data"></a>

Amazon Simple Storage Service (Amazon S3) is the natural target for archived data. It provides 99.999999999 percent durability, and it's less expensive than database storage.

Furthermore, Amazon S3 has built-in storage classes that are priced based on the retrieval pattern. You have the option of transitioning the offloaded S3 objects into a lower-priced storage tier based on the data's retrieval frequency. For more information about storage classes and pricing, see the [Amazon S3 documentation](https://aws.amazon.com/s3/storage-classes/).

For applications that use fleets of MySQL instances, offloading into Amazon S3 would mean saving money on data that meets the following criteria:
+ Must be archived from the database to increase efficiency
+ Isn't required immediately, or is sparingly needed for any business process
+ Must be retained for a long term because of audit requirements

You can archive MySQL data in the following ways:
+ Export data from a live Amazon Aurora DB cluster
+ Export data by using `SELECT INTO OUTFILE S3`
+ Export data by using AWS Glue

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
