---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-9.1---identify-critical-performance-criteria-for-your-storage-workload..html
---

# Best practice 9.1 – Identify critical performance criteria for your storage workload
<a name="best-practice-9.1---identify-critical-performance-criteria-for-your-storage-workload."></a>

 In data analytics, throughput is often a constraining factor to enable your workloads to run effectively. Throughput is measured by the amount of information that has successfully moved through the network, compute, or storage layers. Improving throughput in each of these layers generally results in better query performance.

## Suggestion 9.1.1 – Use performance monitoring tools to determine if the analytics system performance is limited by compute, storage, or networking
<a name="suggestion-9.1.1---use-cloudwatch-metrics-or-self-managed-performance-monitoring-tools-to-determine-if-the-analytics-system-performance-is-limited-by-compute-storage-or-networking."></a>

 Use a metric collection and reporting system, such as Amazon CloudWatch, to analyze the performance characteristics of the analytics system. Evaluate the measured performance metrics relative to system reference documentation to characterize the system constraints for the workload as a percentage of maximum performance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
