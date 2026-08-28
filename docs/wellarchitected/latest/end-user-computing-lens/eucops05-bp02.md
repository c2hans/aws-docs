---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops05-bp02.html
---

# EUCOPS05-BP02 Store and regularly analyze log files to detect anomalous activity and behaviors
<a name="eucops05-bp02"></a>

 Maintaining a central store of log data and performance metrics is frequently a mandatory requirement if specific compliance standards need to be maintained. Even in the absence of compliance requirements, maintaining a central store of data facilitates a better understanding of service scaling, performance, and security enables analysis, which improves root cause analysis and drives incremental service improvement.

 Review the available data sources that provide key insight into the usage of your EUC environment.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-6"></a>

 Extracting performance data and log files from both WorkSpaces and WorkSpaces Applications and storing it centrally is essential if you need to adhere to specific industry compliance standards or if you want to perform retrospective analysis of data for troubleshooting purposes, root cause analysis, or predicting service scalability and requirements.

 Amazon CloudWatch can be used to capture specific metrics and store the data longer term in Amazon S3. Amazon Kinesis agents can also be installed on WorkSpaces or WorkSpaces Applications instances to propagate system logs in real time to a centralized location. For more detail, see [Using Amazon Kinesis Agents to Store AppStream Event Logs](https://aws.amazon.com/blogs/desktop-and-application-streaming/using-kinesis-agent-for-microsoft-windows-to-store-appstream-2-0-windows-event-logs/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
