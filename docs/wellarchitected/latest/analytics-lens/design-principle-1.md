---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/design-principle-1.html
---

# 1 – Monitor the health of the analytics application workload
<a name="design-principle-1"></a>

 **How do you measure the health of your analytics workload?** Data analytics workloads often involve multiple systems and process steps working in coordination. It is imperative that you monitor not only individual components but also the interaction of dependent processes to ensure a healthy data analytics workload.

|  **ID**  |  **Priority**  |  **Best practice**  |
| --- | --- | --- |
| ☐ BP 1.1  |  Required  |  Validate the data quality of source systems before transferring data for analytics.  |
| ☐ BP 1.2  |  Required  |  Monitor operational metrics of data processing jobs and the availability of source data. |

 For more details, refer to the following information:
+ AWS Big Data Blog: [Monitor data pipelines in a serverless data lake](https://aws.amazon.com/blogs/big-data/monitor-data-pipelines-in-a-serverless-data-lake/)
+  AWS Compute Blog: [Monitoring and troubleshooting serverless data analytics applications](https://aws.amazon.com/blogs/compute/monitoring-and-troubleshooting-serverless-data-analytics-applications/)
+  AWS Big Data Blog: [Building a serverless data quality and analysis framework with Deequ and AWS](https://aws.amazon.com/blogs/big-data/building-a-serverless-data-quality-and-analysis-framework-with-deequ-and-aws-glue/) [Glue](https://aws.amazon.com/blogs/big-data/building-a-serverless-data-quality-and-analysis-framework-with-deequ-and-aws-glue/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
