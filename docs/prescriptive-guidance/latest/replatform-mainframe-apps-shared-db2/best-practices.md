---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-mainframe-apps-shared-db2/best-practices.html
---

# Best practices
<a name="best-practices"></a>

This section outlines a set of best practices for addressing key challenges in replatforming mainframe workloads to cloud environments while keeping the database on Db2 for z/OS.

## Network latency
<a name="latency"></a>

To accurately predict the latency impact of separating the application from the Db2 database during a replatforming effort, we recommend that you conduct a thorough evaluation of the number of Db2 calls for both transactions and batch processes. This evaluation should be done by using trace data and should include the following steps:
+ **Collect trace data**: Gather detailed traces of representative transactions and batch jobs, and make sure that the traces capture all Db2 interactions, including entries and exits.
+ **Analyze the trace data**: Count the number of Db2 entries and exits for each transaction and batch job, and calculate the average number of Db2 interactions per transaction and batch process.
+ **Measure current response times**: Check if Db2 access is aligned with your application's service-level agreement (SLA).
+ **Estimate network latency**: Determine the expected network latency between the replatformed application and the Db2 database. Consider factors such as physical distance, network infrastructure, and potential bottlenecks.
+ **Calculate potential impact**: For each transaction and batch process, multiply the number of Db2 entries and exits by the estimated network latency. Add this calculated time to the current response times to predict the new total processing time.
+ **Assess the results**: Evaluate whether the predicted latency increase is acceptable for your business requirements and identify any transactions or processes that might require optimization or redesign to mitigate latency issues.
+ **Consider mitigation strategies**: Explore options such as connection pooling, caching, or batch data retrieval to reduce the number of individual Db2 interactions. Evaluate the possibility of moving frequently accessed data closer to the application tier.

By following these steps, you'll be able to make data-driven decisions about the feasibility of your replatforming strategy and identify any potential performance issues before they impact your production environment. This approach will help ensure a smooth transition while maintaining acceptable performance levels for your database-dependent applications.

## Security
<a name="security"></a>
+ **Secure your application build**: Use a private subnet in the virtual private cloud (VPC) to run AWS CodeBuild to help ensure isolation and enhanced security. Implement a Db2 trusted context from the CodeBuild subnet CIDR for secure database access during the build process.
+ **Secure your runtime environment**: Use a Db2 trusted context from the runtime subnet CIDR for secure database connections.
+ **Manage database credentials securely:** Implement a regular credential rotation schedule to minimize the risk of unauthorized access. Store Db2 credentials securely in AWS Secrets Manager.
+ **Establish network security**: Implement strong network segmentation and firewall rules to protect both build and runtime environments. Use the correct combination of AWS Direct Connect and AWS Site-to-Site VPN to achieve the necessary level of security.
+ **Enforce encryption**: Enforce encryption for data in transit between your application and Db2 for z/OS.

## Application governance
<a name="governance"></a>
+ **Establish a source of truth: **Establish the new software configuration management (SCM)—for example, GitHub—as the single source of truth for the migrated application code. This ensures consistency and eliminates version discrepancies between the cloud and mainframe environments during the transition period.
+ **Update the change management process: **Update the change management process to consider code modifications in this new, dual-environment paradigm. This process should include:
  + Clear approval workflows for code changes.
  + Mandatory code reviews before merging code into the main branch.
  + Synchronized deployment procedures to ensure that both environments receive updates simultaneously.
  + Rollback mechanisms in case of issues in either environment.

## Elasticity
<a name="elasticity"></a>

The elasticity of cloud computing introduces a paradigm shift that significantly alters the mainframe cost structure and resource management. Unlike the traditional mainframe environment, which has fixed capacity and peak-based pricing models, cloud platforms offer dynamic scalability and a pay-as-you-go approach that can potentially lead to substantial cost savings and improved operational efficiency.

In a cloud environment, organizations can scale their computing resources up or down in real time based on actual demand, which eliminates the need for overprovisioning to accommodate peak loads. This elasticity allows businesses to pay only for the resources they consume instead of investing in expensive hardware and software licenses to handle occasional spikes in usage.

For details on how pricing works on AWS, see [AWS Pricing](https://aws.amazon.com/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
