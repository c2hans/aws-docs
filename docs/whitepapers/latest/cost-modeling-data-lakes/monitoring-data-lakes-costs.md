---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cost-modeling-data-lakes/monitoring-data-lakes-costs.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Monitoring data lakes costs
<a name="monitoring-data-lakes-costs"></a>

 Once the data lake is built to provide its intended features, we recommend that you measure the cost and tie it back to business value it provides. This enables you to perform a return-on-investment analysis on your analytics portfolio. It also enables you to iterate and tune the resources for optimal cost based on cost optimization techniques discussed earlier in this whitepaper.

 To track the cost utilization for your analytic workloads, you need to define your cost allocation strategy. Cost-allocation tagging ensures that you tag your AWS resources with metadata key-value pairs that reflect the business unit the data lake pipeline was built for.

 Tags enable you to generate billing reports for the resources associated with a particular tag. This lets you to either do charge-back or return-on-investment analysis.

 Another strategy to track your costs is to use multiple AWS accounts and manage them using AWS Organizations. In this approach, every business unit owns their AWS account and provisions and manages their own resources. This lets them track all cost associated with that account for their data lake needs.

 By tracking costs and tying it back to your business value, you can complete your cost modeling for your first analytics workload. This process also lets you iterate and repeat the process again of deciding business use cases, defining KPI and building data lake features on top of your already built data lake foundation while monitoring the cost associated with it.
