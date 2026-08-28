---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/descale-configurations.html
---

# Descaling your configurations
<a name="descale-configurations"></a>

"Descale" means moving an F5 BIG-IP configuration to a lower or more cost-efficient configuration, based on the features or metrics required after your initial discovery findings. You must carefully evaluate all these options because they will impact the architecture and the number of instances required.

The following diagram helps you assess if descaling is appropriate for your needs and requirements.

![Process flow for descaling a configuration.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/images/guide-img/migration-f5-big-ip/images/F5-descale.png)

The migration will also create new considerations in the following areas.
+ **Network topology** – AWS does not currently support `802.1q `tagged VLANs, so the number of instance interfaces (minus one for management) present a limit to the number of networks that an instance can support. If you require a specific topology, you need to evaluate it compared to the different instances that F5 supports in the AWS Cloud.
+ **SSL performance** – F5 appliances and chassis have an SSL performance that exceeds what can be accomplished on `x86`. You must evaluate the aggregate and per-virtual server SSL requirements.
+ **Network performance** – You must evaluate the aggregate, outbound, and internal network characteristics. AWS instance types have different network characteristics (low, medium, high, up to X, or dedicated) that must be considered. There are also limits to how much traffic a single instance can send outbound or across a direct connection.
+ **VIP density** – If you have a larger number of virtual IP addresses (VIPs), you must consider the instance limit to the number of VIPs that can be mapped to the network interfaces.
+ **Concurrent connection** – There are flow limits to the maximum number of connections that the instances can support.
+ **Session state** – Different applications use different types of persistence. Stateful and stateless applications will change the methods used to shared state, and this can impact scale for in/out operations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
