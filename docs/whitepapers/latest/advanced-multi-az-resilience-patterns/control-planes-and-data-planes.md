---
source_url: https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/control-planes-and-data-planes.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Control planes and data planes
<a name="control-planes-and-data-planes"></a>

 Before we get to the actual patterns you can use to perform an Availability Zone evacuation, we need to discuss the concepts of control planes and data planes. AWS makes a distinction between control planes and data planes in our services. Control planes are the machinery involved in making changes to a system—adding resources, deleting resources, modifying resources—and getting those changes propagated to wherever they need to go to take effect, such as updating a network configuration for an ALB or creating an AWS Lambda function.

 Data planes are the primary function of those resources, things such as the running EC2 instance, or getting items from or putting items into an Amazon DynamoDB table. For a more detailed discussion of control planes and data planes, refer to [Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones) and [AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/aws-infrastructure.html#control-planes-and-data-planes).

 For the purposes of this document, consider that control planes tend to have more moving parts and dependencies than data planes. This makes it statistically more likely that the control plane becomes impaired compared to the data plane. This is especially relevant for services that provide AZI, such as Amazon EC2 and EBS, because parts of those services have control planes that are also zonally independent and can be impacted during a single-AZ event.

 While control plane actions can be used to perform AZ evacuation, based on the previous information, they may have a lower probability of success, especially during a failure event. To increase the probability of successfully mitigating impact, you can use two different patterns. The first pattern relies only on data plane actions to initially mitigate impact by preventing work from being routed to or stop work from being done in the impacted Availability Zone. Then, the second pattern can be attempted to update the configuration of resources with control plane actions to both prevent capacity from being provisioned in the impacted Availability Zone as well as stop inter-Availability Zone communication with that Availability Zone.

 The recovery patterns discussed in this section are *big red buttons*. They are the mechanisms you use to take large-scale action, quickly, akin to pulling an [Andon cord on an assembly line](https://en.wikipedia.org/wiki/Andon_(manufacturing)). They assume that the workloads have already attempted strategies such as [retry with exponential backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) in their code to overcome transient errors. This means that when isolated Availability Zone impact is detected, its effects on availability or latency are severe enough to require evacuating the Availability Zone to effectively mitigate.
