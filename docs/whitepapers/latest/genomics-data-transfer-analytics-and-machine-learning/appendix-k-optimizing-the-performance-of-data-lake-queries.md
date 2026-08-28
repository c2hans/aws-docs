---
source_url: https://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/appendix-k-optimizing-the-performance-of-data-lake-queries.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix K: Optimizing the performance of data lake queries
<a name="appendix-k-optimizing-the-performance-of-data-lake-queries"></a>

 For the solution implementation using tertiary analysis and data lakes, we optimized Amazon Athena performance based on the recommendations in [Top 10 Performance Tuning Tips for Amazon Athena](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/). We partitioned the variant data on the sample ID field, sorted each sample on location, and converted the data to Apache Parquet format. Partitioning in this way allows cohorts to be built optimally based on sample IDs. New samples can be ingested efficiently into the data lake without recomputing the data lake dataset. The annotation data sources are also written in Apache Parquet format to optimize for performance. If you need to query by location (chromosome, position, reference, alternate–CPRA), either create a sample ID to location ID lookup table in a database like Amazon DynamoDB or create a duplicate of the data partitioned on location.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
