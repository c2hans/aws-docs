---
source_url: https://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/appendix-l-optimizing-the-cost-of-data-lake-queries.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix L: Optimizing the cost of data lake queries
<a name="appendix-l-optimizing-the-cost-of-data-lake-queries"></a>

 The biggest challenge with cost optimizing a data lake in Amazon Simple Storage Service (Amazon S3) is understanding the data lake access patterns to lifecycle the data and optimize for cost. With data lakes, the access patterns are often irregular, making it difficult to capture a common set of access patterns and lifecycle the data. Amazon S3 Intelligent-Tiering solves this problem.

 For a small monitoring and automation fee, S3 Intelligent-Tiering monitors access patterns and moves objects that have not been accessed for 30 consecutive days to the Infrequent Access tier. If the data is accessed later, it is automatically moved back to the frequent access tier. Enabling S3 Intelligent-Tiering is an easy way to cost optimize your data lake.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
