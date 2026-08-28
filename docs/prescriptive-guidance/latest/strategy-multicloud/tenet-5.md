---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud/tenet-5.html
---

# Tenet 5. Have a longer-term integration strategy
<a name="tenet-5"></a>

Be careful when you move large volumes of data between applications in different clouds, especially if your compute resources and applications are deployed in one CSP, and your data storage resources are deployed in another. Such a situation can add complexity and latency that might offset perceived benefits. We speak with many customers who have a data lake on one cloud but want to perform machine learning (ML) or analytics with tools from another CSP. Deciding where to place workloads in a multicloud environment is one of the most crucial—and often most challenging—decisions organizations face. We recommend that you evaluate each workload placement decision through three critical dimensions: technical requirements, business needs, and provider strengths.

Start technical evaluations by mapping each workload's essential characteristics: computing power, data operations, response time needs, and growth requirements. Applications naturally perform best when they're located near their data. Moving applications away from their data sources creates unnecessary technical hurdles and slows performance.

Business decisions must account for provider pricing, data residency requirements, and vendor contracts. Each workload placement affects the entire organization's operations, security, and productivity. Looking at workloads in isolation leads to suboptimal decisions.

**Our guidance:**
+ Implement bulk data transfer between clouds instead of real-time access. Schedule periodic data refresh by using efficient bulk operations instead of using constant API calls between clouds. This approach reduces costs, improves reliability, and maintains consistent performance. For example, export summarized daily sales data instead of querying individual transactions across clouds.
+ Consider data gravity when designing workload placement. Keep applications close to their primary data sources to maintain performance and to reduce costs. ML models, analytics engines, and transaction processing systems all benefit from direct access to their data. Moving these workloads away from their data creates unnecessary network latency and complexity.
+ Evaluate workload decisions within the context of your complete cloud strategy instead of reviewing them in isolation. Consider how each placement choice affects operational processes, security controls, and team capabilities across your organization. A decision that seems optimal for a single workload might complicate monitoring or increase security risks when viewed holistically.
+ Define clear data ownership and governance policies that specify where different types of data can reside. Create a data classification framework that drives consistent decisions about data placement across cloud providers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
