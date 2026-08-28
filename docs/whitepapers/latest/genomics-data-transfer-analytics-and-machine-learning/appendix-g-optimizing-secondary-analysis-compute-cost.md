---
source_url: https://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/appendix-g-optimizing-secondary-analysis-compute-cost.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix G: Optimizing secondary analysis compute cost
<a name="appendix-g-optimizing-secondary-analysis-compute-cost"></a>

 To optimize compute cost, first consider the resource requirements for a given tool that runs in your secondary analysis workflow. There are a variety of tools available to help with Amazon Elastic Compute Cloud (Amazon EC2) instance right-sizing for a given workload in AWS. The basic idea is to gather sufficient data about your tool performance over a period of time to capture the workload and business peak resource utilization. For more information about EC2 instance right sizing, see [Identifying Opportunities to Right Size](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-right-sizing/identifying-opportunities-to-right-size.html) in the *Right Sizing: Provisioning Instances to Match Workloads* whitepaper.

 By setting the instance type attribute in your AWS Batch compute environment to optimal, AWS Batch will dynamically provision the optimal quantity and type of compute resources (for example, CPU or memory optimized instances) based on the volume and specific resource requirements of the batch jobs submitted. You can also specify a specific set of instance types that are optimal for your given tools. Also, if a Spot Instances type is unavailable, AWS Batch can use another instance type defined for that job. Keep in mind that AWS Batch can pick large instance types and schedule a number of jobs on that same instance, so it is not limited to one tool for one instance. It can be cost-effective to bin pack jobs on a larger instance than placing one job in one instance with the lowest cost.

 AWS Batch has built-in failover support from Spot Instances compute environments to an On-Demand compute environment, allowing organizations to take advantage of lower compute cost on Spot Instances when it’s available. If you specify the maximum price when configuring your AWS Batch compute environment that is using Spot Instances, AWS Batch will only schedule jobs in that compute environment when Spot Instance pricing is below your maximum price (as a percent of the On-Demand price). For more information about AWS Batch compute environment, see [Creating a Compute Environment](https://docs.aws.amazon.com/batch/latest/userguide/create-compute-environment.html) in the *AWS Batch User Guide*. If you choose to set up a queue with two compute environments—Spot Instances and On-Demand Instances—jobs will be submitted to the On-Demand queue when the Spot Instances price is above the maximum price or if Spot instances are not available. By default, the maximum price is 100% of EC2 On-Demand prices.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
