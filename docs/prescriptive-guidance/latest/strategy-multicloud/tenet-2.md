---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud/tenet-2.html
---

# Tenet 2. Be mindful of multicloud misconceptions
<a name="tenet-2"></a>

When you're developing your multicloud strategy, avoid the common misconceptions that are discussed in the following sections.

## Everyone is adopting multicloud strategies
<a name="misconception-global-adoption"></a>

Advisory firms and media companies paint a complex picture of multicloud adoption. Research shows broad interest in multicloud approaches, but spending patterns often tell a different story. In practice, many enterprises maintain either single cloud environments or clear primary/secondary CSP relationships. This disconnect highlights the importance of looking beyond headlines and focusing instead on the specific needs of your organization.

**Our guidance:**
+ Make cloud decisions based on your specific business requirements instead of following industry trends. Focus on measurable costs and risks for your organization.
+ Examine multicloud use cases within your industry context. Cloud strategies that work for consumer technology companies might not translate to financial services, manufacturing, or gaming environments.
+ Consider data gravity as a primary factor in workload placement decisions. The location and movement of data often determine the most effective cloud architecture.
+ Look beyond adoption statistics to understand spending patterns. High reported multicloud adoption rates often mask actual spending patterns.
+ Evaluate technical constraints before committing to a multicloud environment. Some workloads perform best when their components remain within a single cloud environment.

## Multicloud reduces the risk of vendor lock-in
<a name="misconception-vendor-lockin"></a>

Vendor flexibility is a legitimate consideration in cloud strategy development. Organizations value the ability to adapt their technology choices as business needs evolve. This concern reflects prior experiences with traditional IT investments that created binding, long-term commitments. Cloud services offer different dynamics around provider flexibility. AWS provides open source compatible services and data portability options that reduce technical barriers to migration. However, the trade-off between flexibility and operational efficiency remains important. Organizations must weigh the business value of maintaining provider options against the technical advantages of deeply integrating with specialized services from a primary provider.

Some customers attempt to avoid lock-in by engineering cloud-agnostic solutions that use containers. This approach often restricts them to basic compute and storage services, and bypasses the advantages of advanced cloud capabilities. Our experience shows that this strategy adds considerable complexity due to the increased development time and resources required, compared with using native services.

**Our guidance:**
+ Consider the full cost of cloud-agnostic architectures. The additional engineering overhead might not justify portability benefits.
+ Use cloud-native capabilities for maximum value. Basic compute and storage services alone often sacrifice significant advantages in security, scalability, and innovation.
+ Plan cloud strategies based on business requirements. When a multicloud implementation adds clear value, such as the ability to serve users on multiple platforms, the additional engineering investment becomes worthwhile.
+ Evaluate realistic exit scenarios and costs. Compare the likelihood and expense of changing providers against the benefits of using the complete set of AWS services.
+ Build on the open source foundations of AWS. AWS managed services such as [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/) give you both flexibility and operational excellence, and support the database engines you are using today.
+ Leverage the comprehensive migration tools provided by AWS. We help you move workloads in any direction and provide free data egress if you leave AWS to use other providers. For more information, see the AWS blog post [Free data transfer out to internet when moving out of AWS](https://aws.amazon.com/blogs/aws/free-data-transfer-out-to-internet-when-moving-out-of-aws/).

## Multicloud improves availability and resilience
<a name="misconception-availability"></a>

The belief in seamless workload switching between cloud providers during outages drives some organizations toward multicloud strategies. This mindset creates an oversimplified view of cloud infrastructure resilience that ignores fundamental technical realities.

Based on years of experience working with multicloud customers on AWS, we've seen that maintaining full workload portability between providers often creates substantial complexity without delivering all the expected benefits. Data-intensive applications face insurmountable challenges due to data gravity constraints. In fact, in our view, it is nearly impossible for organizations to successfully implement a truly seamless multicloud failover for data-heavy workloads.

Lydia Leong, Distinguished VP Analyst at Gartner, reinforces this perspective in a [social media post](https://twitter.com/cloudpundit/status/1448713618321723400): "Multicloud failover is complex and costly to the point of nearly almost always being impractical, and it's not an especially effective way to address cloud resilience risks." The inherent differentiation between providers in networking, storage, databases, machine learning, and security makes true portability nearly impossible. Spreading workloads across providers might increase risk, because a failure in either environment could trigger an outage across all enviornments.

**Our guidance:**
+ Focus on mastering AWS capabilities for individual workloads instead of pursuing complex multicloud architectures.
+ Build resilience through AWS Regions and Availability Zones instead of attempting cross-provider failover. For a technical deep dive into how AWS can automatically fail over workloads between physical data centers, see the AWS blog post, [Zonal autoshift – Automatically shift your traffic away from Availability Zones when we detect potential issues](https://aws.amazon.com/blogs/aws/zonal-autoshift-automatically-shift-your-traffic-away-from-availability-zones-when-we-detect-potential-issues/).
+ Migrate workloads strategically to AWS, and focus on one application at a time to maximize success.

## Multicloud provides better pricing
<a name="multicloud-provides-better-pricing"></a>

Price competitiveness might be the weakest argument of all for multicloud environments. Organizations' experiences with complicated, expensive software or data center contracts that lock them into multi-year agreements have made them wary when procuring IT services. Traditional procurement approaches have not adapted to pay-as-you-go purchasing, volume discounts, or the reality of price competition in the cloud. (As of January 2025, AWS has reduced prices 151 times since its inception.)

The biggest single driver of cost reduction is a well-managed and optimized cloud environment. A company sees better cost optimization by working primarily with a provider whose services offer price-performance advantages (such as compute instances that are based on custom-designed chips such as [AWS Graviton](https://aws.amazon.com/pm/ec2-graviton/)) and has superior cloud financial management solutions. According to a [2022 Hackett Group study](https://pages.awscloud.com/rs/112-TZM-766/images/hackett-group-the-business-value-of-migration-to-aws-012022.pdf) of more than 1,000 organizations, infrastructure spending as a percentage of total IT spending was 20% lower for AWS customers compared with multicloud organizations.

Our experience has shown that companies do not anticipate the added cost and complexity of operating in multiple clouds, nor do they appropriately weigh this cost against the perceived gain in a head-to-head sourcing engagement.

**Our guidance:**
+ Build your cost optimization strategy on the [AWS Well-Architected Framework Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/). There are five design principles:
  + **Implement cloud financial management:** To achieve financial success and accelerate business value realization in the cloud, you must invest in cloud financial management. Your organization must dedicate the necessary time and resources for building capability in this new domain of technology and usage management. As with your security or operations capability, you need to grow capabilities through knowledge building, programs, resources, and processes to help become a cost-efficient organization.
  + **Adopt a consumption model:** Pay only for the computing resources you consume, and increase or decrease usage depending on business requirements. For example, development and test environments are typically used only for eight hours a day during the work week. You can stop these resources when they're not in use for a potential cost savings of 75% (40 hours versus 168 hours).
  + **Measure overall efficiency:** Measure the business output of your workload and the costs that are associated with delivery. Use this data to understand the gains you make from increasing output, increasing functionality, and reducing cost.
  + **Stop spending money on undifferentiated heavy lifting:** CSPs do the heavy lifting of data center operations such as racking, stacking, and powering servers. They also remove the operational burden of managing operating systems and applications by using managed services. This allows you to focus on your customers and business projects instead of IT infrastructure.
  + **Analyze and attribute expenditure:** The cloud makes it easier to accurately identify the cost and usage of workloads, which then allows transparent attribution of IT costs to revenue streams and individual workload owners. This helps measure return on investment (ROI) and gives workload owners an opportunity to optimize their resources and reduce costs.
+ Given the financial overhead of operating across different providers, we guide customers to invest heavily in automation and cost optimization tooling. Each CSP offers extensive native tools in this area, such as the [AWS Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html). Most native tools provide excellent capabilities for customers in their cloud environment. However, to understand spend across multiple CSPs, you can choose from a rich set of ISV and software as a service (SaaS) products that extend these capabilities to provide a single experience for cost optimization.
+ Diluting purchasing power through a *spend equity* strategy doesn't generate business value. It can undermine potential volume discounts and potentially undermines technical design. The most efficient way to consume cloud services is by using a primary provider for the bulk of your operations and using other CSPs only where it adds business value.
