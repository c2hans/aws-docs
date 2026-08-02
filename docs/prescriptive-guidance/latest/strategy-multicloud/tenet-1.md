---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud/tenet-1.html
---

# Tenet 1. Align multicloud goals with your strategy
<a name="tenet-1"></a>

Research by Gartner and industry trends show that organizations are increasingly adopting multicloud approaches to address specific business needs. The following scenarios demonstrate when a multicloud infrastructure can be strategically advantageous.

## Mergers and acquisitions
<a name="mergers"></a>

Mergers and acquisitions (M&A) create immediate decisions about cloud strategy. Although operating multiple clouds might increase costs and complexity, rapid consolidation can delay integration value and disrupt business operations. Your cloud decisions become central to realizing M&A benefits.

Integration planning should account for the complete technology landscape. Each workload requires evaluation within the context of your integration timeline and business priorities.

**Our guidance:**
+ Develop a business-driven consolidation strategy that balances immediate integration needs with long-term operational efficiency. Maintain multiple clouds initially in circumstances where hasty consolidation could disrupt critical business operations or delay M&A value realization.
+ Create clear workload placement criteria that align with your integration timeline. Prioritize revenue-generating applications and core business processes while accounting for technical dependencies and operational requirements.

## Desire to leverage long-term differentiated capabilities of another CSP
<a name="other-csp"></a>

The fear of missing out drives some companies to want a bit of every cloud. Workload placement decisions affect the entire organization—from engineering teams to finance to security operations.

Organizations therefore need to examine their reasoning for pursuing multiple clouds. Some argue that each workload should live on the cloud services provider (CSP) that best meets its needs. However, individual workload optimization must be balanced against the broader organizational impact. Each additional cloud provider risks increasing operational complexity, creating new talent requirements, and introducing security considerations that affect the entire technology organization.

**Our guidance:**
+ Follow an 80/20 approach: Select a primary provider for most workloads and consider additional providers only for specific, high-value use cases. This strategy maximizes efficiency and talent retention while reducing complexity.
+ Consider the total cost of operating across clouds. Include security tooling, governance products, financial management systems, and operational overhead in your analysis.
+ Evaluate each workload's dependencies and interactions. Workloads rarely operate in isolation; they share data, security controls, and operational processes.
+ Conduct thorough price-performance analysis across providers. Compare not just the direct costs but also the overhead of managing multiple environments.

## Multicloud at the holding company and primary cloud at the operating company or line of business
<a name="multiple-strategies"></a>

Private equity firms and holding companies face unique cloud strategy considerations. Their portfolio companies often maintain independent cloud strategies, frequently resulting from past M&A activity. This structure reduces the complexity that's typically associated with multicloud operations, because each business unit operates independently. However, this independence can limit opportunities to take advantage of enterprise-wide volume discounts and purchasing incentives.

The effectiveness of cloud strategy at the holding company level depends on the autonomy of portfolio companies and their individual technology needs. Although consolidation might create purchasing leverage, it might conflict with the independent operation model that's typical of holding companies and private equity portfolios.

**Our guidance:**
+ Understand CSP volume discount structures. Each provider offers mechanisms for adding or removing subsidiaries from enterprise agreements and spinning off business units into separate entities. These represent [two-way door decisions](https://aws.amazon.com/executive-insights/content/how-amazon-defines-and-operationalizes-a-day-1-culture/).
+ Plan cloud purchasing commitments carefully. Engage your CSP's account team early, or contact an AWS Partner with the [AWS Cloud Operations competency](https://aws.amazon.com/cloudops/partners/) for assistance.
+ Balance independence with efficiency. Consider shared services or purchasing agreements that benefit portfolio companies without constraining their operations.
+ Focus on business objectives first. Develop technology strategies that support your operating model rather than pursuing a multicloud strategy for its own sake.
+ Evaluate cloud strategies through the lens of portfolio management. Consider how cloud choices affect potential divestitures or future acquisitions.
