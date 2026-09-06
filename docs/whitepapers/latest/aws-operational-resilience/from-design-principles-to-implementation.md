---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-operational-resilience/from-design-principles-to-implementation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# From design principles to implementation
<a name="from-design-principles-to-implementation"></a>

 Customers have to make many decisions: where to place their content, where to run their applications, and how to achieve higher levels of availability and resiliency. For example, a financial institution can choose to run its mobile banking application in a single AWS Region to take advantage of multiple AZs.

![Example of Multi-AZ Design](http://docs.aws.amazon.com/whitepapers/latest/aws-operational-resilience/images/multi-az-design.png)

 *Figure 1: Example of Multi-AZ Design*

Let’s take the example of a deployment across two AZs to illustrate how AZ independence provides resiliency. As shown in Figure 1, the customer deploys its mobile banking application so that its architecture is stable and consistent across AZs; for example, the workload in each AZ has sufficient capacity as well as stable infrastructure, configurations, and policies that keep both AZs up to date. Elastic Load Balancing routes traffic only to healthy instances and data layer replication allows for fast failover in case a database instance fails in one AZ, thus minimizing downtime for the financial institution’s mobile banking customers.

 Compared to AWS’s infrastructure and services, traditional, on-premises environments present several obstacles for achieving operational resilience. For example, let’s assume a significant event shuts down a financial institution’s primary, on-premises data center. The financial institution also has a secondary data center in addition to its primary data center. The capacity of the secondary data center is able to handle only a proportion of the overall workload that would otherwise operate at the primary data center (for example, 11,000 servers at the secondary center instead of 12,000 servers at the primary center; network capacity increased 300% at the primary center in the last 4 years, but only 250% at the secondary center) and errors in replication mean that the secondary center’s data has not been updated in 36 hours. Furthermore, macroeconomic factors have driven transaction volume higher at the primary data center by 15% over the past 6 months. As a result, the financial institution may find that its secondary data center cannot process current transaction volume within a given time period per its internal and regulatory requirements.

 By using AWS services, the financial institution would have been able to increase its capacity at frequent intervals to support increasing transaction volumes, as well as track and manage changes to maintain all of its deployments with the same, up-to-date capacity and architecture. In addition, customers can maintain additional “cold” infrastructure and backups on AWS that can activate if necessary—at much lower cost than procuring their own physical infrastructure. This is not a hypothetical issue—key regulatory requirements highlight the need for regulated entities to account for capacity needs in adverse scenarios.

 (See, for example, U.S. Securities and Exchange Commission (SEC), Regulation Systems Compliance and Integrity, 17 C.F.R. § 240, 242 & 249; see also adopting release: [https://www.sec.gov/rules/final/2014/34-73639.pdf](https://www.sec.gov/rules/final/2014/34-73639.pdf). See also FFIEC, Business Continuity Planning, IT Examination Handbook (February 2015), available at [https://ithandbook.ffiec.gov/media/274725/ffiec\_itbooklet\_businesscontinuityplanning.pdf](https://ithandbook.ffiec.gov/media/274725/ffiec_itbooklet_businesscontinuityplanning.pdf).)

 On AWS, customers can also deploy workloads across AZs located in multiple Regions (Figure 2) to achieve both AZ redundancy and Region redundancy. Customers that have regulatory or other requirements to store data in multiple Regions or to achieve even greater availability can use a multi-Region design. In a multi-Region set-up, the customer will need to perform additional engineering to minimize data loss and ensure consistent data between Regions. A routing component monitors the health of the customer’s application as well as dependencies. This routing layer will also handle automatic failovers, changing the destination when a location is unhealthy and temporarily stopping data replication. Traffic will go only to healthy Regions.

 AWS improves operational resilience compared to traditional, on-premises environments not only for failover, but also for returning to full resiliency. For the financial institution with a secondary data center, it may have to perform data backup and restoration over several days. Many traditional environments do not feature bidirectional replication, resulting in current data at the backup site and “outdated” data in the primary site that makes fast failback difficult to achieve. On AWS, the financial institution is not “stuck” as it would be in a traditional environment—it can fail forward by quickly launching its workload in another location. The key point is that AWS’s global infrastructure and services offer financial institutions the capacity and performance to meet aggressive resiliency objectives.

 To achieve assurance about the resiliency of their applications, we recommend that financial institution customers perform continuous performance, load, and failure testing; extensively use logging, metrics, and alarms; maintain runbooks for reporting and performance tracking; and validate their architecture through realistic, full-scale tests known as “game day” exercises. Per the regulatory requirements in their jurisdictions, financial institutions may provide evidence of such tests, runbooks, and exercises to their financial regulatory authorities.

![Example of multi-Region desig](http://docs.aws.amazon.com/whitepapers/latest/aws-operational-resilience/images/multi-region-design.png)

 *Figure 2: Example of multi-Region design*
