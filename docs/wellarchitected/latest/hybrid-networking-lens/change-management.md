---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/change-management.html
---

# Change management
<a name="change-management"></a>

 Being aware of how change affects a system enables you to plan proactively, and monitoring enables you to quickly identify trends that could lead to capacity issues or SLA breaches.

| HNREL02: How do you prepare for scheduled maintenance events? |
| --- |
|   |

 Planned maintenance activities and scheduled events in hybrid networks span multiple components, technologies, and environments. Organizations must coordinate these activities carefully to minimize disruption while maintaining security and reliability. This includes managing maintenance windows, implementing temporary redundancy, and ensuring clear procedures for both planned changes and potential rollbacks.

| HNREL03: How do you monitor changing demands of your hybrid connectivity? |
| --- |
|   |

 Monitoring your dedicated connections and IPSec VPN connections is essential to ensure continuous availability, performance, and security of your hybrid network. By collecting and analyzing logs and metrics, you can quickly detect failures, bandwidth limitations, or security incidents. This proactive approach helps prevent outages, supports timely troubleshooting, and ensures your hybrid workloads remain resilient and compliant with organizational requirements.

**Topics**
+ [HNREL02-BP01 Monitor network service provider maintenance events](hnrel02-bp01.md)
+ [HNREL03-BP01 Monitor the bandwidth and scale the bandwidth as needed](hnrel03-bp01.md)
+ [HNREL03-BP02 Monitor logs and metrics for insights of hybrid networking resources](hnrel03-bp02.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
