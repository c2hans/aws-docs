---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/aws-service-types.html
---

# AWS service types
<a name="aws-service-types"></a>

 AWS operates three different categories of services based on their fault isolation boundary: zonal, Regional, and global. This section will describe in more detail how these different types of services have been designed so that you can determine how failures within a service of a certain service type will impact your workload running on AWS. It also provides high level guidance on how to architect your workloads to use these services in a resilient way. For global services, this document also provides prescriptive guidance in [Appendix A - Partitional service guidance](appendix-a---partitional-service-guidance.md) and [Appendix B - Edge network global service guidance](appendix-b---edge-network-global-service-guidance.md) that can help you prevent impact to your workloads from control plane impairments in AWS services, helping you to safely take dependencies on global services while minimizing introducing single points of failure.

**Topics**
+ [Zonal services](zonal-services.md)
+ [Regional services](regional-services.md)
+ [Global services](global-services.md)
