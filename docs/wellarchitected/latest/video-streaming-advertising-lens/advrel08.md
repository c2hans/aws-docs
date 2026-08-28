---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel08.html
---

# Privacy
<a name="advrel08"></a>

| ADVREL08: How do you verify privacy while building reliable collaborations between multiple parties in your system? |
| --- |
|   |

 Privacy-enhanced collaboration systems (such systems allow multiple parties to work together on advertising campaigns and data analysis while protecting individual user privacy and sensitive business data) require high reliability to maintain secure and consistent data sharing between parties while verifying data integrity and availability. Implementing reliable practices involves designing resilient architectures, maintaining data consistency, and verifying robust recovery mechanisms while preserving privacy. This includes redundancy in critical components, proper error handling, and maintaining service availability across different Regions.

**Topics**
+ [ADVREL08-BP01 Design resilient architectures with privacy-preserving fault tolerance](advrel08-bp01.md)
+ [ADVREL08-BP02 Maintain data consistency and availability across collaboration workflows](advrel08-bp02.md)
+ [ADVREL08-BP03 Implement secure and privacy-preserving recovery mechanisms for collaboration workloads](advrel08-bp03.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
