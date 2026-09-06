---
source_url: https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/fault-tolerance-and-fault-isolation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Fault tolerance and fault isolation
<a name="fault-tolerance-and-fault-isolation"></a>

 These are two important concepts when we think about availability. Fault tolerance is the ability to [withstand subsystem failure](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-your-workload-to-withstand-component-failures.html) and maintain availability (doing the right thing within an established SLA). To implement fault tolerance, workloads use spare (or redundant) subsystems. When one of the subsystems in a redundant set fails, another picks up its work, typically almost seamlessly. In this case, spares are truly spare capacity; they are available to assume 100% of the work from the failed subsystem. With true spares, multiple subsystem failures are required to produce an adverse impact on the workload.

 Fault isolation minimizes the scope of impact when a failure does occur. This is typically implemented with modularization. Workloads are broken down into small subsystems that fail independently and can be repaired in isolation. The failure of a module [does not propagate beyond the module](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-interactions-in-a-distributed-system-to-mitigate-or-withstand-failures.html). This idea spans both vertically, across differently functionality in a workload, and horizontally, across multiple subsystems that provide the same functionality. These modules act as fault containers that limit the scope of impact during an event.

 The architectural patterns of control planes, data planes, and static stability directly support implementing fault tolerance and fault isolation. The Amazon Builders’ Library article [Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones) provides good definitions for these terms and how they apply to building resilient, highly available workloads. This whitepaper uses these patterns in the section [Designing highly available distributed systems on AWS,](designing-highly-available-distributed-systems-on-aws.md#designing-highly-available-distributed-systems-on-aws.title) and we also summarize their definitions here.
+  **Control plane** – The part of the workload involved in making changes: adding resources, deleting resources, modifying resources, and propagating those changes to where they are needed. Control planes are typically more complex and have more moving parts than data planes, and are thus statistically more likely to fail and have lower availabilities.
+  **Data plane** – The part of the workload that provides the day-to-day business functionality. Data planes tend to be simpler and operate at higher volumes than control planes, leading to higher availabilities.
+  **Static stability** – The ability of a workload to continue correct operation despite dependency impairments. One method of implementation is to remove control plane dependencies from data planes. Another method is to loosely couple workload dependencies. Perhaps the workload doesn’t see any updated information (such as new things, deleted things, or modified things) that its dependency was supposed to have delivered. However, everything it was doing before the dependency became impaired continues to work.

 When we think about impairment of a workload, there are two high-level approaches we can consider for recovery. The first method is to respond to that impairment after it happens, perhaps using AWS Auto Scaling to add new capacity. The second method is to prepare for those impairments before they happen, maybe by overprovisioning a workload’s infrastructure so that it can continue to operate correctly without needing additional resources.

 A statically stable system uses the latter approach. It pre-provisions spare capacity to be available during failure. This method avoids creating a dependency on a control plane in the workload’s recovery path to provision new capacity to recover from the failure. Additionally, provisioning new capacity for various resources takes time. While waiting for new capacity your workload can be overloaded by existing demand and experience further degradation, leading to “brown-out” or complete availability loss. However, you should also consider the cost implications of utilizing pre-provisioned capacity against your availability goals.

 Static stability provides the next two rules for high availability workloads.

**Rule 7**
 Don’t take dependencies on control planes in your data plane, especially during recovery.

**Rule 8**
 Loosely couple dependencies so your workload can operate correctly despite dependency impairment, where possible.
