---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/anti-patterns.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Anti-Patterns
<a name="anti-patterns"></a>

 Amazon Redshift is not ideally suited for the following usage patterns:
+  **OLTP** – Amazon Redshift is designed for data warehousing workloads delivering extremely fast and inexpensive analytic capabilities. If you require a fast transactional system, you might want to choose a relational database system such as [Amazon Aurora](https://aws.amazon.com/rds/aurora/) or [Amazon RDS](https://aws.amazon.com/rds/), or a NoSQL database such as [Amazon DynamoDB](https://aws.amazon.com/dynamodb/).
+  **Unstructured data** – Data in Amazon Redshift must be structured by a defined schema. Amazon Redshift doesn’t support an arbitrary schema structure for each row. If your data is unstructured, you can perform ETL on Amazon EMR to get the data ready for loading into Amazon Redshift. For JSON data, you can store key value pairs and use the [native JSON functions](https://docs.aws.amazon.com/redshift/latest/dg/json-functions.html) in your queries.
+  **BLOB data** – If you plan to store binary large object (BLOB) files such as digital video, images, or music, you might want to store the data in S3 and reference its location in Amazon Redshift. In this scenario, Amazon Redshift keeps track of metadata (such as item name, size, date created, owner, location, and so on) about your binary objects, but the large objects themselves are stored in S3.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
