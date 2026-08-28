---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel01-bp02.html
---

# ADVREL01-BP02 Architect your system with appropriate recovery objectives
<a name="advrel01-bp02"></a>

 Avoid over- or under-architecting your services by [working backwards](https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes) from your services' recovery objectives, striking a balance with adjacent pillars such as cost optimization and operational excellence. KPIs established in the operational excellence pillar should inform approaches to reliability.

## Implementation guidance
<a name="implementation-guidance-16"></a>

 Identify critical parts of the architecture and individually confirm their reliability and recovery point and time objectives (RPO and RTO). For example, with real-time bidding (RTB), delivery services have increased RPO and RTO requirements as compared to creative services. On close inspection, certain architectures also have variable availability and recovery requirements, operating on a spectrum from multiple layers of redundancy to entirely non-redundant. Advertising customers accept ranges from milliseconds to hours as appropriate recovery. For example, enrichment and auction layers often have the most stringent requirements, while analytics or as necessary reporting can see reduced requirements.

## Key AWS services
<a name="key-aws-services-3"></a>
+  [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/)

## Resources
<a name="resources-11"></a>
+  [Establishing RPO and RTO Targets for Cloud Applications](https:\aws.amazon.com\blogs\mt\establishing-rpo-and-rto-targets-for-cloud-applications)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
