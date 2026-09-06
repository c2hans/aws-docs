---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ETSI-NFVO-compliant-orchestration-in-kubernetes/service-provider-requirements.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Service provider requirements
<a name="service-provider-requirements"></a>

 With the mobile traffic increasing almost 10% quarter by quarter ([Ericsson Mobility Report](https://www.ericsson.com/en/reports-and-papers/mobility-report/dataforecasts/mobile-traffic-update)) and technology evolving at a fast pace, service providers are under pressure from multiple dimensions. Some of the challenges are as follows:
+  **Cost savings (TCO) and productivity** — The increase in traffic corresponds to higher bandwidth and processing capacity requirements. With proliferation of unlimited plans, this increase might not necessarily translate to new revenues. Therefore, it is imperative to lower the cost of operations and to enable new enterprise use cases by avoiding complex interactions between functions. Avoiding duplication of functionalities and tying it with custom logics increases the cost of deployment and operations. It’s important to think of truly cloud-native, Kubernetes-savvy orchestrators with abstractions that avoid duplication and overlap of functionalities. Intent-driven and not procedure-driven coordination between different functions also increases staff productivity.
+  **Agility** — Since the traffic demand fluctuates, CSPs are thinking of ways to elastically scale to provide the required capacity. This requires a versatile network orchestrator that can stand up, take down, scale-out, or scale-in both network functions and infrastructure. Infrastructure cost should be optimized, with baseline infrastructure being negotiated as a long-term contract, while the fluctuating demand is addressed by a pay-as-you go model. Cloud cost models are beneficial in this role if the network orchestrator supports fluctuating and agile operation.
+  **Assurance and Resilience** — With more and more safety- and business-critical services relying on connected infrastructure, it is important that the connectivity service meets SLAs. When failures happen, an intelligent orchestration system should provide automated self-healing while keeping customer experience within desired SLA bounds.

 To achieve the preceding business goals, it’s important that customers design their orchestration and automation architecture with the goals in mind. To achieve these goals, orchestrator implementation itself should take advantage of the latest cloud-native and serverless implementation best practices. These features enable the orchestration solution to be resilient and agile, and allow the solution to take advantage of the latest infrastructure and CNF functionalities. It also makes the orchestrator itself to evolve rapidly as the requirements changes.

 In the following section, we outline one such possible implementation in the context of day-to-day operations of the network that achieves the desired agility, assurance, and resilience goals while also being cost-effective
