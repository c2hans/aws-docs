---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-elb-envoy-proxy.html
---

# Routing traffic to an Elastic Load Balancing for Envoy proxy

Elastic Load Balancing for Envoy runs your Envoy configuration on a proxy that AWS manages. The proxy serves as the single point of contact for your clients. For more information, see [What is Elastic Load Balancing for Envoy?](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/what-is.html) in the *Elastic Load Balancing for Envoy User Guide*.

To route domain traffic to a proxy, use Amazon Route 53 to create an [alias record](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html) that points to the DNS name of your proxy.

**Note**
Route 53 doesn't charge for alias queries to Elastic Load Balancing for Envoy proxies or other AWS resources.

## Prerequisites
<a name="routing-to-elb-envoy-proxy-prereqs"></a>

To get started, you need the following:
+ An Elastic Load Balancing for Envoy proxy. To get the DNS name of the proxy, open the Amazon EC2 console, choose **Proxies** in the navigation pane, and then choose the proxy name to open its details page. You can also get the DNS name from the `dnsName` field that the `GetProxy` or `ListProxies` API operation returns.
+ A registered domain name. You can use Route 53 as your domain registrar, or you can use a different registrar.
+ Route 53 as the DNS service for the domain. If you register your domain name by using Route 53, we automatically configure Route 53 as the DNS service for the domain.

  For information about using Route 53 as the DNS service provider for your domain, see [Making Amazon Route 53 the DNS service for an existing domain](MigratingDNS.md).

## Configuring Amazon Route 53 to route traffic to an Elastic Load Balancing for Envoy proxy
<a name="routing-to-elb-envoy-proxy-configuring"></a>

To configure Amazon Route 53 to route traffic to an Elastic Load Balancing for Envoy proxy, perform the following procedure.<a name="routing-to-elb-envoy-proxy-procedure"></a>

**To route traffic to an Elastic Load Balancing for Envoy proxy**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Hosted zones**.

1. Choose the name of the hosted zone that has the domain name that you want to use to route traffic to your proxy.

1. Choose **Create record**.

1. Specify the following values:
**Routing policy**
Choose the applicable routing policy. For more information, see [Choosing a routing policy](routing-policy.md).
**Record name**
Enter the domain or subdomain name that you want to use to route traffic to your proxy. The default value is the name of the hosted zone.
For example, if the name of the hosted zone is example.com and you want to use acme.example.com to route traffic to your proxy, enter **acme**.
**Alias**
If you are using the **Quick create** record creation method, turn on **Alias**.
**Value/Route traffic to**
Choose **Alias to ELB for Envoy proxy**, then choose the Region that the proxy is in. Enter the DNS name of the proxy, for example, `my-proxy-1234567890.elb-proxy.us-east-1.on.aws`.
The console doesn't list your proxies, so you need to enter the DNS name. Only Regions that support this alias target are available. If the DNS name isn't for a proxy in the Region that you chose, the console displays an error.
**Record type**
Choose **A – IPv4 address** or **AAAA – IPv6 address**, depending on the IP addressing configuration of your proxy.
**Evaluate target health**
If you want Route 53 to route traffic based on the health of your resources, choose **Yes**. For more information about checking the health of your resources, see [Creating Amazon Route 53 health checks](dns-failover.md).

1. Choose **Create records**.

   Changes generally propagate to all Route 53 servers within 60 seconds. When propagation is done, you'll be able to route traffic to your proxy by using the name of the alias record that you created in this procedure.
