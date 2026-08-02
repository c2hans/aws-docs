---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/vpc-to-vpc-connectivity.html
---

# VPC to VPC connectivity
<a name="vpc-to-vpc-connectivity"></a>

Customers can use two different VPC connectivity patterns to set up multi-VPC environments: *many to many*, or *hub and spoke*. In the many-to-many approach, the traffic between each VPC is managed individually between each VPC. In the hub-and-spoke model, all inter-VPC traffic flows through a central resource, which routes traffic based on established rules.
