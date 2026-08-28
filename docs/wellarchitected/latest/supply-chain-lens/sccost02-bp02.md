---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/sccost02-bp02.html
---

# SCCOST02-BP02 Query and retrieve data by partitions to save cost and improve performance
<a name="sccost02-bp02"></a>

 Optimize data access by using partitioned queries to enhance cost-efficiency and performance in supply chain systems.

 **Desired outcome:** Data access requirements are taken into consideration while defining data storage strategy.

 **Benefits of establishing this best practice:** Reduced cost, optimized performance, and better customer satisfaction

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-49"></a>

 Organize supply chain data by time, geography, or other relevant criteria to enhance storage efficiency and reduce retrieval costs.

 Implement data partitioning strategies to divide large volumes into manageable chunks based on specific characteristics like time or product ID, focusing query operations on relevant segments and reducing scanned data volume and associated costs.

### Implementation steps
<a name="implementation-steps-50"></a>

1.  Analyze supply chain data access patterns to identify optimal partitioning strategies based on time, geography, or product categories.

1.  Implement data partitioning in storage systems to organize data into logical segments that align with query patterns.

1.  Configure query engines to use partition pruning to scan only relevant data segments during retrieval operations.

1.  Use AWS Glue for automated data partitioning and Amazon S3's integrated compression options to further reduce costs.

1.  Implement partition management processes to maintain optimal partition sizes and help prevent partition proliferation.

1.  Monitor query performance and costs to continuously optimize partitioning strategies and data organization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
