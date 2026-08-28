---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/sccost04-bp02.html
---

# SCCOST04-BP02 Implement a monitoring strategy for your cloud spend
<a name="sccost04-bp02"></a>

 Continually monitor and analyze usage patterns, network traffic, and associated costs to maintain optimal cost efficiency.

 **Desired outcome:** A continuous improvement approach which uses lowest cost service options from Cloud to optimize cost.

 **Benefits of establishing this best practice:** Reduced cost, optimized performance, and better customer satisfaction

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-55"></a>

 Define key cost metrics relevant to supply chain operations, such as data transmission costs, edge processing expenses, and cloud storage charges. Set budgets and alarms to Establish budget thresholds for each cost metric and configure alarms to notify when thresholds are approaching or exceeded, while regularly reviewing cost reports to identify anomalies, trends, or cost spikes that may require investigation or optimization.

### Implementation steps
<a name="implementation-steps-56"></a>

1.  Define key cost metrics relevant to supply chain operations, including data transmission, processing, and storage costs.

1.  Establish budget thresholds and configure automated alerts to notify when spending approaches or exceeds defined limits.

1.  Implement regular cost review processes to identify spending trends, anomalies, and optimization opportunities.

1.  Utilize AWS Trusted Advisor to receive recommendations for optimizing resource usage and reducing costs.

1.  Apply cost-effective data management practices including retention policies, archival strategies, and deletion of obsolete data.

1.  Track and optimize data transmission costs through techniques like data aggregation, compression, and prioritization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
