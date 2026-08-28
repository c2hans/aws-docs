---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/dg/preserve-client-ip-address.html
---

# Preserve client IP addresses in AWS Global Accelerator
<a name="preserve-client-ip-address"></a>

Your options for preserving and accessing the client IP address for AWS Global Accelerator depend on the endpoints that you've set up with your accelerator. When client IP address preservation is enabled, the source IP address of the original client is preserved for packets that arrive at the load balancer.

Endpoints on custom routing accelerators always have the client IP address preserved. There are three types of endpoints for standard accelerators that can preserve the source IP address of the client in incoming packets: Application Load Balancers, Amazon EC2 instances, and Network Load Balancers with security groups. There are requirements and limitations for specific resources that you add as endpoint with client IP address preservation. For more information, see [Transition endpoints with client IP address preservation](about-endpoints.sipp.md).

Note that Global Accelerator does not support client IP address preservation for the following endpoint types:
+ Network Load Balancers without security groups
+ Elastic IP addresses

For details about endpoint requirements, see [Requirements for resources you add as accelerator endpoints](about-endpoints-caveats.md).

**Topics**
+ [Guidelines and restrictions](preserve-client-ip-address.how-to-enable-preservation.md)
+ [Requirements for client IP address preservation](about-endpoints.sipp-caveats.md)
+ [How the client IP address is preserved](preserve-client-ip-address.headers.md)
+ [Benefits of client IP address preservation](preserve-client-ip-address.benefits-of-preservation.md)
+ [Best practices for ENIs and security](best-practices-aga.md)
+ [Transition endpoints](about-endpoints.sipp.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
