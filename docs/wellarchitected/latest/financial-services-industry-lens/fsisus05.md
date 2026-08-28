---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus05.html
---

# FSISUS05: How do you define, review, and optimize network access patterns for sustainability?
<a name="fsisus05"></a>

 Assess and optimize network access patterns for sustainability. Pay attention to redundant layers and redirects or patterns generating excessive and unnecessary data movement.

## FSISUS05-BP01 Analyze network access patterns to identify the places that your customers are connecting from
<a name="fsisus05-bp01"></a>

 **Prescriptive guidance**

 Remove redundant layers and redirects, use pagination and local caching mechanisms to reduce data movement, and consider separating workloads that serve different users.

## FSISUS05-BP02 Avoid common architectural misconfigurations
<a name="fsisus05-bp02"></a>

 In financial services organizations, it's common to hairpin large amounts of traffic through on- premises networks, have largely redundant layers of control using trusted private networks, and sometimes include untrusted public traffic.

 A simple example of this is using [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/) where performance is often degraded as FSI organizations insist that all inbound and outbound traffic originates from their network.

 Another common mistake is to serve both OLAP and OLTP workloads from the same database or cluster, which normally span two or more completely different geographic locations. Both patterns generate excessive and unnecessary data movement.

### Prescriptive guidance
<a name="prescriptive-guidance-13"></a>

 Identify poor architectural choices and risky configurations as good candidates for remediation.

 Assess your workflows from the perspective of varying demand over time, so select scalable AWS services over fixed ones.

 Do not underestimate your network requirements, especially for peak loads. Provide sufficient failover resources to support your operations in case of partial outages.

 Optimize generative AI inference patterns to minimize data transfer and network overhead.

 Implement edge inference for generative AI models where appropriate to reduce network traffic.

 Use efficient prompt engineering to reduce token lengths and network utilization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
