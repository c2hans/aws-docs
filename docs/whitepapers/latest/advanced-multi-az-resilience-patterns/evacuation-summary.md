---
source_url: https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/evacuation-summary.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Summary
<a name="evacuation-summary"></a>

The following table summarizes the pros and cons of the evacuation patterns described.

 *Table 5: Evacuation pattern pros and cons *

|  Approach  |  Pros  |  Cons  |
| --- | --- | --- |
|  Data plane-controlled evacuation  |  Relies only on data plane actions <br /> Quickly prevents work from being done in the impacted Availability Zone <br /> Flexible approach to a centralized view of Availability Zone health  |  Does not prevent capacity from being deployed in an impacted Availability Zone <br /> Not all workload types can use this approach easily  |
|  Control plane-controlled evacuation  |  Prevents new capacity from being deployed in the impacted Availability Zone <br /> Removes existing capacity from the impacted Availability Zone  |  Relies on each service’s control plane <br /> Requires code to be written for each service <br /> Has to be completed service by service <br /> Needs to be careful not to overwhelm capacity during the update  |

 You will likely use both approaches together as part of an Availability Zone evacuation plan. Start with the data plane-controlled evacuation actions that are more likely to succeed to quickly stop processing work in the impacted Availability Zone. Then, once the initial impact is mitigated, follow-up with the control plane-controlled evacuation actions, if you deem it necessary.
