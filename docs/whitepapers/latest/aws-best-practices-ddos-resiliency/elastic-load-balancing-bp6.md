---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/elastic-load-balancing-bp6.html
---

# Elastic Load Balancing (BP6)
<a name="elastic-load-balancing-bp6"></a>

 Large DDoS attacks can overwhelm the capacity of a single Amazon EC2 instance. With [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/), you can reduce the risk of overloading your application by distributing traffic across many backend instances. Elastic Load Balancing can scale automatically, allowing you to manage larger volumes when you have unanticipated extra traffic, for example, because flash crowds or DDoS attacks. For applications built within an Amazon VPC, there are different types of ELBs to consider, for example: Application Load Balancer (ALB) and Network Load Balancer (NLB).

## Best practices for web applications (HTTP/HTTPS)
<a name="best-practices-web-applications"></a>

 For web applications, you can use the [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) to route traffic based on content and accept only well-formed web requests, as shown in the following diagram. Application Load Balancer blocks many common DDoS attacks, such as SYN floods or UDP reflection attacks, protecting your application from the attack. Application Load Balancer automatically scales to absorb the additional traffic when these types of attacks are detected. Scaling activities due to infrastructure layer attacks are transparent for AWS customers and don't affect your bill.

![Application Load Balancers provide a flexible feature set for HTTP and HTTPS applications](http://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/images/alb-features.png)

 For more information about protecting web applications with Application Load Balancer, see [Getting Started with Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancer-getting-started.html).

## Best practices for TCP and UDP applications
<a name="best-practices-tcp-udp-applications"></a>

 For TCP, UDP, and TLS applications, you can use [Network Load Balancer](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/) to route traffic to targets (for example, Amazon EC2 instances) at ultra-low latency, as shown in the following diagram. Choose a network load balancer (NLB) when you need ultra-high performance, TLS offloading at scale, centralized certificate deployment, support UDP, and static IP address for your applications. One key consideration with Network Load Balancer is that any TCP or UDP traffic that reaches the load balancer on a valid listener will be routed to your targets, not absorbed, however this doesn't apply for TLS-listeners that terminate the TCP connection.

**Note**
 For NLB with TCP listeners, it's recommended to deploy these behind an AWS Global Accelerator to help protect again SYN floods. Global Accelerator has an inbuilt SYN proxy and connections made through the NLB are automatically tracked.

![Network load balancers provide high performance and a suite of support features](http://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/images/nlb-features.png)

 You can use Shield Advanced to configure DDoS protection for Elastic IP addresses. When an Elastic IP address is assigned per Availability Zone to the NLB, Shield Advanced will apply the relevant DDoS protections for the NLB traffic.

 For more information about protecting TCP and UDP applications with Network Load Balancer, see [Create a Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancer-getting-started.html).

**Note**
 Depending on the security group configuration of your Application Load Balancer, it requires the resource using the security to group to use connection tracking to track information about traffic, this can affect the load balancer's ability to process new connections, because the number of tracked connections is limited. A security group configuration that contains an ingress rule accepting traffic from any IP address (for example, `0.0.0.0/0` or `::/0`) but doesn't have a corresponding rule to allow the response traffic, causes the security group to use connection tracking information to allow the response traffic to be sent. In an event of an DDoS attack, the maximum number of tracked connections can be exhausted. To improve the DDoS resilience of your public-facing Application Load Balancer, ensure that the security group associated with your load balancer is configured to not use connection tracking (untracked connections), so the flow of traffic isn't subject to connection tracking limits.
 For this, configure your security group with a rule that allows inbound TCP traffic on your listener ports (for example, 80 and 443) from any IP address (0.0.0.0/0 or ::/0), and add a corresponding rule in the outbound direction allowing this resource to send the response traffic (allow outbound range for any IP address 0.0.0.0/0 or ::/0) for all ports (0-65535), so the response traffic is allowed based on the security group rule, and not on tracking information. With this configuration, Classic and Application Load Balancer aren't subject to exhaust connection tracking limits that might affect establishing new connections to its load balancer nodes and allows it to scale based on the increase in traffic in the event of a DDoS attack. More information about untracked connections can be found at: [Security group connection tracking: Untracked connections](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#untracked-connections).
 Avoiding security group connection tracking protects you on both paths. For DDoS traffic from allowed sources, untracked connections keep the connection tracking table from being exhausted. For DDoS traffic from sources the security group doesn't allow, the traffic is dropped at the security group, so it never creates connection tracking entries in the first place.
 For EC2 instances behind load balancers, configure security group rules to allow all traffic from the load balancer's security group on the target port. This creates untracked connections that don't consume connection tracking table entries, preventing table exhaustion during traffic surges or DDoS attacks.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
