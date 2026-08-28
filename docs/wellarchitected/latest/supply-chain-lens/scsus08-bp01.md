---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsus08-bp01.html
---

# SCSUS08-BP01 Collect usage data to feed advanced analysis and ML models to better predict future resources needs
<a name="scsus08-bp01"></a>

 Consider improving your ability to predict AWS Cloud resources required for your supply chain and sustainability-related workloads to prefer on-demand over always-on. Base this data on forecasts, seasonality, and peaks and valleys analysis to efficiently turn resources on and off accordingly or scaling resources up and down and horizontally.

 **Desired outcome**: Achieve dynamic scalability and resource efficiency by using historical usage data to predict and optimize resource needs.

 **Benefits of establishing this best practice:** Improves operational agility, reduces downtime, and minimizes unnecessary resource usage.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-64"></a>

 Consider collecting data about resource usage over the past years to design and prefer on-demand over always-on, with the main goal of optimizing resources scaling, uptime and downtime, availability, and replication based on your business needs.

 Gain visibility of required resources through ML-based predictions, using built-in features of AWS System Manager, Instance Scheduler on AWS, and signals from Amazon CloudWatch, while using managed databases like Amazon RDS, and [containers orchestration](https://aws.amazon.com/containers/) running on AWS towards serverless architectures.

### Implementation steps
<a name="implementation-steps-65"></a>

1.  Collect and analyze historical resource usage data to identify patterns and optimization opportunities for on-demand resource allocation.

1.  Implement machine learning-based prediction models to forecast future resource needs based on business patterns and seasonality.

1.  Deploy AWS Systems Manager and Instance Scheduler to automate resource scheduling based on predicted demand patterns.

1.  Configure Amazon CloudWatch monitoring to provide real-time signals for dynamic resource scaling decisions.

1.  Migrate appropriate workloads to managed databases and serverless architectures to optimize resource utilization.

1.  Establish continuous monitoring and optimization processes to refine on-demand resource strategies over time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
