---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/selecting-the-best-solution-for-your-organization.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Selecting the best solution for your organization
<a name="selecting-the-best-solution-for-your-organization"></a>

 There are various advantages and trade-offs with each of these solutions. Choosing the right solution for your organization depends on the specific requirements of each workload. You might choose to run different solutions in different VPCs to meet the needs of your specific workloads. The following table summarizes the criteria that you can use to evaluate what will work best for your organization. These include the complexity of the implementation, the management overhead, the availability of the solution, probability of hitting the PPS per network interface limit, and the cost of the solution.

* Table 5 – Solutions selection criteria *

|   |   **Route 53 Resolver**   |   **Secondary DNS in a VPC**   |   **Highly distributed forwarders**   |   **Zonal forwarders**   |
| --- | --- | --- | --- | --- |
|  Implementation complexity  |  Low  |  Medium  |  High  |  High  |
|  Management overhead  |  Low  |  Low  |  High  |  Medium  |
|  DNS <br /> Infrastructure resiliency  |  High  |  High  |  High  |  Medium  |
|  PPS limit breach  |  Low  |  Low  |  Low  |  Medium  |
|  Cost\*  |  Low  |  Low  |  High  |  Medium  |

 \* *Cost is a combination of the infrastructure and operational expense.*
