---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-configure-load-balancer.html
---

# Configure your Classic Load Balancer
<a name="elb-configure-load-balancer"></a>

After you create a Classic Load Balancer, you can change its configuration. For example, you can update the load balancer attributes, subnets, and security groups.Load balancer attributes

[Connection draining](config-conn-drain.md)
If enabled, the load balancer allows existing requests to complete before the load balancer shifts traffic away from a deregistered or unhealthy instance.

[Cross-zone load balancing](enable-disable-crosszone-lb.md)
If enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.

[Desync migitation mode](config-desync-mitigation-mode.md)
Determines how the load balancer handles requests that might pose a security risk to your application. The possible values are `monitor`, `defensive`, and `strictest`. The default is `defensive`.

[Idle timeout](config-idle-timeout.md)
If enabled, the load balancer allows the connections to remain idle (no data is sent over the connection) for the specified duration. The default is 60 seconds.

[Sticky sessions](elb-sticky-sessions.md)
Classic Load Balancers support both duration-based and application-based session stickiness.Load balancer details

[Security groups](elb-vpc-security-groups.md)
The security groups for your load balancer must allow traffic on the listener and health check ports.

[Subnets](elb-manage-subnets.md)
You can expand the ability of your load balancer to additional subnets.

[Proxy protocol](enable-proxy-protocol.md)
If enabled, we add a header with connection information that is sent to the instance.

[Tags](add-remove-tags.md)
You can add tags to categorize your load balancres.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
