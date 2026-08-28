---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/using-elb-listenerconfig-quickref.html
---

# Listener configurations for Classic Load Balancers
<a name="using-elb-listenerconfig-quickref"></a>

The following table describes possible configurations for HTTP and HTTPS listeners for a Classic Load Balancer.

| Use case | Front-end protocol | Front-end options | Back-end protocol | Back-end options | Notes |
| --- | --- | --- | --- | --- | --- |
| Basic HTTP load balancer | HTTP | NA | HTTP | NA |  +  Supports the [X-Forwarded headers](x-forwarded-headers.md#x-forwarded-for)   |
| Secure website or application using Elastic Load Balancing to offload SSL decryption | HTTPS | [SSL negotiation](elb-ssl-security-policy.md) | HTTP | NA |  +  Supports the [X-Forwarded headers](x-forwarded-headers.md#x-forwarded-for) <br />+  Requires an [SSL certificate](ssl-server-cert.md) deployed on the load balancer   |
| Secure website or application using end-to-end encryption | HTTPS | [SSL negotiation](elb-ssl-security-policy.md) | HTTPS | Back-end authentication |  +  Supports the [X-Forwarded headers](x-forwarded-headers.md#x-forwarded-for) <br />+  Requires [SSL certificates](ssl-server-cert.md) deployed on the load balancer and the registered instances   |

The following table describes possible configurations for TCP and SSL listeners for a Classic Load Balancer.

| Use case | Front-end protocol | Front-end options | Back-end protocol | Back-end options | Notes |
| --- | --- | --- | --- | --- | --- |
| Basic TCP load balancer | TCP | NA | TCP | NA |  +  Supports the [proxy protocol header](enable-proxy-protocol.md)   |
| Secure website or application using Elastic Load Balancing to offload SSL decryption | SSL | [SSL negotiation](elb-ssl-security-policy.md) | TCP | NA |  +  Requires an [SSL certificate](ssl-server-cert.md) deployed on the load balancer <br />+  Supports the [proxy protocol header](enable-proxy-protocol.md)   |
| Secure website or application using end-to-end encryption with Elastic Load Balancing | SSL | [SSL negotiation](elb-ssl-security-policy.md) | SSL | Back-end authentication |  +  Requires [SSL certificates](ssl-server-cert.md) deployed on the load balancer and the registered instances <br />+  Does not insert SNI headers on back-end SSL connections <br />+  Does not support the proxy protocol header   |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
