---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/conclusion.html
---

# Conclusion
<a name="conclusion"></a>

Large migrations present different challenges when compared to smaller migrations. This is mostly due to the complexities introduced by the scale. For example, installing an agent onto a single server is fairly straightforward and will take approximately 5 minutes. However, if you have 5,000 servers in scope for your migration, this will take approximately 416 hours and will present the following challenges:
+ It's likely that there are multiple operating systems that require different processes.
+ It's possible that there are different credentials for different groups of servers.
+ There might be separate Microsoft Active Directory domains to manage due to previous mergers and acquisitions.
+ Effective processes and tools are required to orchestrate the agent installation for each wave and then track and report the progress.

This strategy outlines large migration best practices based on AWS Professional Services experiences helping a wide range of customers. This includes people, process, and technology perspectives. If you want to start or are in the process of migrating to AWS, consultants at AWS Professional Services would be happy to assist you. Contact your AWS representative to start the conversation.

For next steps, we recommend that you review the AWS Prescriptive Guidance series designed to help you plan and complete a large migration to the AWS Cloud. For the complete series, see [Large migrations to the AWS Cloud](https://aws.amazon.com/prescriptive-guidance/large-migrations/).
