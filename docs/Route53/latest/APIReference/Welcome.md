---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

## Amazon Route 53
<a name="Welcome_Amazon_Route_53"></a>

Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. Route 53 performs four main functions:
+  **Domain registration** – Route 53 lets you register domain names such as example.com.
+  **Domain Name System (DNS) service** – Route 53 translates friendly domain names into IP addresses using a global network of authoritative DNS servers, and provides DNS resolution within your VPCs for private hosted zones.
+  **Health checking** – Route 53 sends automated requests over the internet to your application to verify that it's reachable, available, and functional.
+  **Resolver** – Route 53 Resolver lets you forward DNS queries from a VPC that you created using Amazon VPC to DNS resolvers in your network, and from your network to resolvers in your VPC.

You can use the API to create and manage the following resources:

Public and Private Hosted Zones
A *public hosted zone* is a container that holds information about how you want to route traffic on the internet for a domain, such as example.com, and its subdomains.
A *private hosted zone* is a container that holds information about how you want to route traffic for a domain and its subdomains within one or more VPCs that you created with the Amazon VPC service.

Reusable Delegation Sets
By default, each hosted zone that you create gets a different set of four name servers—a different delegation set. If you create a lot of hosted zones, maintaining different delegation sets can be difficult and time consuming. Route 53 lets you create a delegation set that you can reuse with multiple hosted zones.

Resource Record Sets
After you create a hosted zone for your domain, such as example.com, you create resource record sets to tell the Domain Name System (DNS) how to route traffic for that domain.

Traffic Policies and Traffic Policy Instances
You can create complex routing configurations, known as traffic policies, that use weighted, latency, failover, and geolocation resource record sets. You can then associate a traffic policy with a domain name or subdomain name, such as www.example.com, by creating a traffic policy instance. When users submit DNS queries for the domain or subdomain, Route 53 responds based on the traffic policy that you used to create the traffic policy instance.

Health Checks
Route 53 health checks monitor the health and performance of your web applications, web servers, and other resources. At regular intervals that you specify, Route 53 submits automated requests over the internet to your application, server, or other resource to verify that it's reachable, available, and functional.

Domain Registrations
When you want to get a new domain name, such as example.com, you can register it with Route 53. You can also transfer the registration for existing domains from other registrars to Route 53.

DNS–DNSSEC
You can protect your domain from DNS spoofing or a man-in-the-middle attack, by configuring Domain Name System Security Extensions (DNSSEC).

Query Logs
You can configure Route 53 to log information about the DNS queries that Route 53 receives, such as the domain or subdomain that was requested, the date and time of the request, and the DNS record type (such as A or AAAA).
You can also configure Route 53 Resolver to log information about the DNS queries that originate in Amazon VPCs.

Outbound and Inbound Endpoints, and Rules
You can configure Route 53 Resolver to forward DNS queries from your VPC to your network or vice versa. DNS queries pass through an outbound endpoint on their way from a VPC to your network, and they pass through an inbound endpoint on their way from your network to a VPC. For outbound queries, rules let you specify the domain names that you want to forward to your network and the IP addresses of the DNS resolvers in your network.

Tags
A tag is a label that you assign to an AWS resource. Each tag consists of a key and a value, both of which you define. You can use tags for a variety of purposes; one common use is to categorize and track your Route 53 costs.

Profiles
A *profile* is a named container that groups DNS configurations—such as private hosted zone associations, Resolver rules, and DNS Firewall rule groups—into a single reusable unit. You can associate a profile with multiple VPCs and share it across AWS accounts so that each VPC inherits the same DNS settings without requiring individual configuration.

DNS Firewall
A *DNS Firewall rule group* is an ordered collection of rules that each pair a domain list with an action—allow, block, or alert. You associate rule groups with your VPCs to filter outbound DNS queries made by VPC resources, preventing connections to known-malicious domains or restricting access to only approved domains.

You can also use the Route 53 API to get the current limit on Route 53 objects that you can create, such as hosted zones and health checks.

For information about Route 53 concepts and about how to use the Route 53 console, see the [Amazon Route 53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/).

## Amazon Route 53 domain registration
<a name="Welcome_Amazon_Route_53_Domains"></a>

Amazon Route 53 API actions let you register domain names and perform related operations.

## Amazon Route 53 Global Resolver
<a name="Welcome_Amazon_Route_53_Global_Resolver"></a>

Amazon Route 53 Global Resolver is a global, internet-accessible DNS resolver that enables customers to resolve and forward traffic for both public and private domains while ensuring security and authenticity of queries over the internet. Route 53 Global Resolver supports DNS-over-port 53 (Do53), DNS-over-TLS (DoT), and DNS-over-HTTPS (DoH) protocols through global anycast IP addresses.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Route 53 Profiles
<a name="Welcome_Route_53_Profiles"></a>

 With Amazon Route 53 Profiles you can share Route 53 configurations with VPCs and AWS accounts

## Amazon Route 53 Resolver
<a name="Welcome_Amazon_Route_53_Resolver"></a>

When you create a VPC using Amazon VPC, you automatically get DNS resolution within the VPC from Route 53 Resolver. By default, Resolver answers DNS queries for VPC domain names such as domain names for EC2 instances or Elastic Load Balancing load balancers. Resolver performs recursive lookups against public name servers for all other domain names.

You can also configure DNS resolution between your VPC and your network over a Direct Connect or VPN connection:

 **Forward DNS queries from resolvers on your network to Route 53 Resolver**

DNS resolvers on your network can forward DNS queries to Resolver in a specified VPC. This allows your DNS resolvers to easily resolve domain names for AWS resources such as EC2 instances or records in a Route 53 private hosted zone. For more information, see [How DNS Resolvers on Your Network Forward DNS Queries to Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html#resolver-overview-forward-network-to-vpc) in the *Amazon Route 53 Developer Guide*.

 **Conditionally forward queries from a VPC to resolvers on your network**

You can configure Resolver to forward queries that it receives from EC2 instances in your VPCs to DNS resolvers on your network. To forward selected queries, you create Resolver rules that specify the domain names for the DNS queries that you want to forward (such as example.com), and the IP addresses of the DNS resolvers on your network that you want to forward the queries to. If a query matches multiple rules (example.com, acme.example.com), Resolver chooses the rule with the most specific match (acme.example.com) and forwards the query to the IP addresses that you specified in that rule. For more information, see [How Route 53 Resolver Forwards DNS Queries from Your VPCs to Your Network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html#resolver-overview-forward-vpc-to-network) in the *Amazon Route 53 Developer Guide*.

Like Amazon VPC, Resolver is Regional. In each Region where you have VPCs, you can choose whether to forward queries from your VPCs to your network (outbound queries), from your network to your VPCs (inbound queries), or both.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
