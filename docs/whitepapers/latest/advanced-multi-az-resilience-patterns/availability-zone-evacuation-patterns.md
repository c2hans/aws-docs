---
source_url: https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/availability-zone-evacuation-patterns.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Availability Zone evacuation patterns
<a name="availability-zone-evacuation-patterns"></a>

After detecting impact in a single Availability Zone, the next step is to evacuate that Availability Zone. There are two outcomes that evacuation needs to achieve.

First, you want to stop sending work to the impacted Availability Zone. This could mean different things in different architectures. In a request/response workload, this would mean stopping things like HTTP or gRPC requests coming from your customers being sent to the load balancer or other resources in the Availability Zone. In a batch processing or queue processing system, it could mean stopping compute resources from processing work in the impacted Availability Zone. You will also need to prevent resources in the unaffected Availability Zones from interacting with resources in the impacted Availability Zone, for example, an EC2 instance sending traffic to an [interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html) in the impacted Availability Zone or connecting to the primary instance of a database.

The second outcome is preventing new capacity from being provisioned in the impacted Availability Zone. This is important because new resources, like EC2 instances or containers, being provisioned in the affected Availability Zone are likely to see the same impact as existing resources. Additionally, because the first outcome prevents work from being sent to them, they cannot absorb the load they were provisioned to handle. This leads to increased load on the existing resources, which can ultimately lead to *brown out* or total unavailability of the workload. There are several auto scaling services available in AWS where this is applicable: [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/), [Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html), and [AWS Auto Scaling](https://aws.amazon.com/autoscaling/). Additionally, services like Amazon ECS, Amazon EKS, and [AWS Batch](https://aws.amazon.com/batch/) may schedule work on hosts across Availability Zones in a VPC as part of their normal operation.

**Topics**
+ [Availability Zone independence](availability-zone-independence.md)
+ [Control planes and data planes](control-planes-and-data-planes.md)
+ [Data plane-controlled evacuation](data-plane-controlled-evacuation.md)
+ [Control plane-controlled evacuation](control-plane-controlled-evacuation.md)
+ [Summary](evacuation-summary.md)
