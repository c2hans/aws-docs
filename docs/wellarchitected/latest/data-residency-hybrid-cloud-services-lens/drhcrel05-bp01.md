---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcrel05-bp01.html
---

# DRHCREL05-BP01 Provision spare compute capacity following an N\+M model
<a name="drhcrel05-bp01"></a>

 Provision spare compute capacity following an N\+M availability model, where N is the required capacity and M is the spare capacity to accommodate server failures. Use features like Amazon EC2 Auto Scaling groups, shared storage services, and AWS Elastic Disaster Recovery for reliable recovery.

 **Desired outcome:** Achieve high availability with sufficient spare capacity and seamless failover capabilities in hybrid environments while consistently meeting data residency requirements, even during hardware failures or maintenance events.

 **Benefits of establishing this best practice:** The N\+M model improves availability and resilience by providing buffer capacity to handle unexpected server failures or maintenance events, minimizing downtime and maintaining consistent performance while meeting data residency requirements.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-37"></a>

 Use placement groups with a spread strategy to improve reliability across hardware components. Prepare for network, instances, compute, racks or data centers, and Availability Zone or Region failure modes, and adopt highly-available design. Implement redundant network paths, and map application dependencies to understand the impact of disconnect events. Provide sufficient network redundancy to meet your application's availability requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
