---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-operational-resilience/how-aws-maintains-operational-resilience-and-continuity-of-service.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# How AWS maintains operational resilience and continuity of service
<a name="how-aws-maintains-operational-resilience-and-continuity-of-service"></a>

 AWS builds to guard against outages and incidents, and accounts for them in the design of AWS services—so when disruptions do occur, their impact on customers and the continuity of services is as minimal as possible. To avoid single points of failure, AWS minimizes interconnectedness within our global infrastructure. AWS’s global infrastructure is geographically dispersed over five continents. At the time of publication, it's composed of 20 geographic Regions, which are composed of 61 [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) (AZs), which, in turn, are composed of data centers.

****
 You can take a virtual tour of an AWS data center here: [https://aws.amazon.com/compliance/data-center](https://aws.amazon.com/compliance/data-center).

The AZs, which are physically separated and independent from each other, are also built with highly redundant networking to withstand local disruptions. Regions are isolated from each other, meaning that a disruption in one Region does not result in contagion in other Regions. Compared to global financial institutions’ on-premises environments today, the locational diversity of AWS’s infrastructure greatly reduces geographic concentration risk. We are continuously adding new Regions and AZs, and you can view our most current global infrastructure map here: [https://aws.amazon.com/about-aws/global-infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

 At AWS, we employ compartmentalization throughout our infrastructure and services. We have multiple constructs that provide different levels of independent, redundant components. Starting at a high level, consider our AWS Regions. To minimize interconnectedness, AWS deploys a dedicated stack of infrastructure and services to each Region. Regions are autonomous and isolated from each other, even though we allow customers to replicate data and perform other operations across Regions. To allow these cross-Region capabilities, AWS takes enormous care to ensure that the dependencies and calling patterns between Regions are asynchronous and ring-fenced with safety mechanisms.

 For example, we have designed Amazon Simple Storage Service (Amazon S3) to allow customers to replicate data from one Region (for example, US-EAST-1) to another Region (for example, US-WEST-1), but at the same time, we have designed S3 to operate autonomously within each Region, so that an outage of S3 in US-EAST does not result in an S3 outage in US-WEST. The vast majority of services operate entirely within single Regions. The very few exceptions to this approach involve services that provide global delivery, such as Amazon Route 53 (an authoritative Domain Name System), whose data plane is designed for 100.000% availability. As discussed below, financial institutions and other customers can architect across both multiple Availability Zones and Regions.

 (This is as evidenced by the Amazon S3 service disruption of February 28, 2017, which occurred in the Northern Virginia (US-EAST-1) Region, but not in other Regions. See “Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region,” [https://aws.amazon.com/message/41926/](https://aws.amazon.com/message/41926/).)

 Availability Zones (AZs), which comprise a Region and are composed of multiple data centers, demonstrate further compartmentalization. Locating AZs within the same Region allows for data replication that provides redundancy without a substantial impact on latency—an important benefit for financial institutions and other customers who need low latency to run applications. At the same time, we make sure that AZs are independent in order to ensure services remain available in the event of major incidents. AZs have independent physical infrastructure and are distant from each other to mitigate the effects of fires, floods, and other events. Many AWS services run autonomously within AZs; this means that if one AZ within a single Region loses power or connectivity, the other AZs in the Region are unaffected, or in the case of a software error, the risk of that error propagating is limited. AZ independence allows AWS to build Regional services using multiple AZs that, in turn, provide high availability to and resiliency for our customers.

 In addition, AWS leverages another concept known as cell-based architecture. Cells are multiple instantiations of a service that are isolated from each other; these internal service structures are invisible to customers. In a cell-based architecture, resources and requests are partitioned into cells, which are capped in size. This design minimizes the chance that a disruption in one cell—for example, one subset of customers—would disrupt other cells. By reducing the blast radius of a given failure within a service based on cells, overall availability increases and continuity of service remains. A rough analogy is a set of watertight bulkheads on a ship: enough bulkheads, appropriately designed, can contain water in case the ship’s hull is breached and will allow the ship to remain afloat.

## Incident management
<a name="incident-management"></a>

 Although the likelihood of such incidents is very low, AWS is prepared to manage large-scale events that affect our infrastructure and services. AWS becomes aware of incidents or degradations in service based on continuous monitoring through metrics and alarms, high-severity tickets, customer reports, and the 24x7x365 service and technical support hotlines.

In case of a significant event, an on-call engineer convenes a call with problem resolvers to analyze the event to determine if additional resolvers should be engaged. A call leader drives the group of resolvers to find the approximate root cause to mitigate the event. The relevant resolvers will perform the necessary actions to address the event.

After addressing troubleshooting, repair procedures, and affected components, the call leader will assign follow-up documentation and actions and end the call engagement. The call leader will declare the recovery phase complete after the relevant fix activities have been addressed.

The post mortem and deep root cause analysis of the incident will be assigned to the relevant team. Post-mortems are convened after any significant operational issue, regardless of external impact, and Correction of Errors (COE) documents are composed such that the root cause is captured and preventative actions may be taken for the future. Implementation of the preventative measures is tracked during weekly operations meetings.
