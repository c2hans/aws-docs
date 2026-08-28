---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-operational-resilience/customers-can-achieve-and-test-resiliency-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Customers can achieve and test resiliency on AWS
<a name="customers-can-achieve-and-test-resiliency-on-aws"></a>

 AWS believes that financial institutions should ensure that they—and the critical economic functions they perform—are resilient to disruption and failure, whatever the cause. Prolonged outages or outright failures could cause loss of trust and confidence in affected financial institutions, in addition to causing direct financial losses due to failing to meet obligations.

 AWS builds—and encourages its customers to build—for failure to occur, at any time. Similarly, as the Bank of England recognizes, “We want firms to plan on the assumption that any part of their infrastructure could be impacted, whatever the reason.”

 In the design, building, and testing of their applications on AWS, customers are able to achieve their objectives for operational resilience. AWS offers the building blocks for any type of customer, from financial institutions to oil and gas companies to government agencies, to construct applications that can withstand large-scale events. In this section, we walk through how financial institution customers can build that type of resilient application on the AWS cloud.

## Starting with first principles
<a name="starting-with-first-principles"></a>

 AWS field teams, composed of technical managers, solution architects, and security experts, help financial institution customers build their applications according to customers’ design goals, security objectives, and other internal and regulatory requirements. As reflected in our shared responsibility model, customers remain responsible for deciding how to protect their data and systems in the AWS Cloud, but we offer workbooks, guidance documents, and on-site consulting to assist in the process. Before deploying a mission-critical application—whether on the AWS cloud or in another environment—significant financial institution customers will go through extensive development and testing.

We recommend that customers review the [Cloud Adoption Framework](https://aws.amazon.com/professional-services/CAF/) to develop efficient and effective adoption plans. See [Reliability Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html). For a customer who begins building an application on AWS with high availability and resiliency in mind, we recommend that they begin by answering some fundamental questions, including but not limited to:
+  What problems are you trying to solve?
+  What specific aspects of the application require specific levels of availability?
+  What is the amount of cumulative downtime that this workload can realistically accumulate in one year?
+  What is the actual impact of unavailability?

 Financial institutions and market utilities perform both critical and non-critical types of functions in the financial services sector. From deposit-taking to loan-processing, trade execution to securities settlement, financial entities across the world perform services whose continuity and resiliency are necessary to ensure the public’s trust and confidence in the financial system. At the industrywide level, for systemically important payment, clearing, settlement, and other types of applications, central banks and market regulators specify a discrete recovery time objective in the Principles for Financial Market Infrastructures (PFMI) standard: “The [business continuity] plan should incorporate the use of a secondary site and should be designed to ensure that critical information technology (IT) systems can resume operations within two hours following disruptive events. The plan should be designed to enable the FMI to complete settlement by the end of the day of the disruption, even in case of extreme circumstances.” (Key Consideration 17.6 of PFMI, available at [https://www.bis.org/cpmi/publ/d101a.pdf](https://www.bis.org/cpmi/publ/d101a.pdf).)

 Beyond the 2-hour RTO, financial regulatory agencies expect regulated entities to be able to meet RTOs and recovery point objectives (RPOs) according to the criticality of their applications, beginning with “Tier 1 application” as the most critical. For example, regulated entities may classify their RTO and RPOs in the following way:

 Table 1 — How regulated entities classify RTO and RPO

|   Resiliency requirement   |   Tier 1 app   |  Tier 2 app  |  Tier 3 app  |
| --- | --- | --- | --- |
|  Recovery Time Objective  |  2 Hours  |  < 8 Hours  |  24 Hours  |
|  Recovery Point Objective  |  < 30 seconds  |  < 4 Hours  |  24 Hours  |

 Although systemically important financial institutions may have upwards of 8,000 to 10,000 applications, they do not classify all applications according to the same criticality. For example, disruptions in an application for processing mortgage loan requests are undesirable, but a financial institution operating such an application may decide that it can tolerate an 8-hour RTO. Other types of important, but not necessarily systemically important, workloads include post-trade market analysis and customer-facing chatbots.

 While the majority of financial entities’ applications are non-critical from a systemic perspective, disruption of some Tier 1 applications would jeopardize not only the safety and soundness of the affected financial institution, but also other financial services entities and possibly the broader economy. For example, a settlement application may be a Tier 1 application and have an associated RTO of 30 minutes and an RPO of < 30 seconds. Such applications are the heart of financial markets and disruptions could cause operational, liquidity, and even credit risks to crystallize. For such applications, there is little to virtually no time for humans to make an active decision on how to recover from an outage or failover to a backup data center. Recovery would need to be automatic and triggered based on metrics and alarms.

 Customers can enable automatic recovery using a variety of AWS services, including [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) metrics [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html), and [AWS Lambda](https://aws.amazon.com/lambda/). See also the following AWS re:Invent presentation, “Disaster Recovery and Business Continuity for Financial Institutions,” for additional information on applicable AWS services and example architecture: [https://www.youtube.com/watch?v=Xa-xTwhP1UU](https://www.youtube.com/watch?v=Xa-xTwhP1UU).

 AWS provides guidance to customers on best practices for building highly available, resilient applications, including through the AWS Well-Architected Framework. See [https://aws.amazon.com/architecture/well-architected](https://aws.amazon.com/architecture/well-architected). For example, we recommend that the components comprising an application should be independent and isolated to provide redundancy. When changing components or configurations in an application, customers should make sure that they can roll back any changes to the application if it appears that the changes are not working. Monitoring and alarming should be used to track latency, error rates, and availability for each request, for all downstream dependencies, and for key operations. Data gathered through monitoring should allow for efficient diagnosis of problems. Best practices for distributed systems should be implemented to enable automated recovery. Recovery paths should be tested frequently—and most frequently for complex or critical recovery paths.

 A variety of AWS services support these practices; for examples, see the [Design your Workload to Withstand Component Failures](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-your-workload-to-withstand-component-failures.html) section of the Reliability Pillar whitepaper.

 For financial institutions, it can be difficult to practice these principles in traditional, on-premises environments, many of which reflect decades of consolidation with other entities and ad-hoc changes in their IT infrastructures. On the other hand, these principles are what drive the design of AWS’s global infrastructure and services and form the basis of our guidance to customers on how to achieve continuity of service. Financial institutions using AWS services can take advantage of AWS’s services to improve their resiliency, regardless of the state of their existing systems.

 For a comprehensive overview of our guidance to customers, see the AWS Well-Architected Framework [Reliability Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
