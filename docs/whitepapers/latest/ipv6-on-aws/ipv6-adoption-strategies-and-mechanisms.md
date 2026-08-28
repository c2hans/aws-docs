---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/ipv6-adoption-strategies-and-mechanisms.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# IPv6 adoption strategies and mechanisms
<a name="ipv6-adoption-strategies-and-mechanisms"></a>

Working with customers, AWS observed the following two main drivers for IPv6 adoption.
+  Network Address Translation is no longer sufficient to work around exhaustion and poses significant challenges with overlapping IP addresses.
+  There are numerous organizational or regulatory mandates to adopt IPv6.

 Following is a summary of IPv6 adoption drivers:
+  **Mandated IPv6 endpoints** — Either mandated by a government policy or an industry regulator, and not necessarily tied to a particular use case.
+  **Interoperability with IPv6 networks** — The last years have seen a growing population of IPv6-only clients, and as a result so have the number of organizations wanting to cater to this user base. With the number of mobile IPv6-only users, many companies find they can’t afford to lose that section of their potential user base.
+  **Public IPv4 exhaustion** — As public IPv4 addresses become more scarce, allocating contiguous IP address ranges for public routing becomes more difficult and costly.
+  **Private IPv4 exhaustion** — As private IPv4 (RFC1918) addresses become exhausted and too fragmented within organizations’ private networks, IPv6-only networks offer opportunities to address additional nodes.

 At the time of this writing, global IPv6 adoption is primarily driven by the major internet providers, network device manufacturers, and organizations that need to grow their number of internet-reachable devices. Beyond these, rate of adoption is significantly slower. Reasons for this include the prevalence of NAT, and proxies used in combination with reusable private IPv4 address space (defined in RFC1918) which greatly reduces the number of unique internet-routable IP addresses. Also, the native lack of backwards compatibility between the two versions of IP protocol present barriers to adoption.

 Although your drivers will likely be similar to the needs of other organizations, each organization also has some unique requirements. Accordingly, best practices and design guidance in this paper are intended to offer guidance rather than a one-size-fits-all solution to IPv6 adoption. The design of your IPv6 network on AWS may differ from the examples provided in this document. However, this paper can help you make informed decisions as you embark to adopt IPv6.

 IPv6 adoption strategy depends on the driving force behind it. You may have an immediate goal such as addressing private IPv4 exhaustion, or the ability to provide IPv6 service endpoints as per government mandate, with the long-term goal of fully converting to an IPv6 only network. Following are the four main driving forces, and the corresponding adoption strategy:
+  **Private IPv4 exhaustion** — The goal is to provision new nodes and allocate routable IP addresses without IP overlap, and without the challenge of sourcing contiguous and usable IP addresses.

   **Adoption strategy** — Configure IPv6-only routing between dual stack network segments, to facilitate communication using the IPv6 stack. Provide IPv6 to IPv4 interoperability layer, such as dual-stack load balancers. You can configure IPv6-only subnets in your dual-stack Amazon VPCs, to accommodate for scale and growth, with NAT64 and DNS64 for backwards compatibility to IPv4-only parts of your network.
+  **Public IPv4 exhaustion** — The goal is to support IPv6-only clients connecting to your public endpoints. As an example, you may have an API endpoint for data upload from IoT devices which are connected to an IPv6-only network. The IoT devices have IPv6 addresses, and the network does not provide interoperability layer to IPv4. Other devices may operate in IPv4 networks.

   **Adoption strategy** — Create dual-stack VPCs and subnets. Configure AWS services such as load balancers and edge service in dual-stack mode with corresponding DNS record on the AWS Cloud. Optionally, provide separate endpoints for IPv4 and IPv6 in dedicated IPv4-only or IPv6-only deployments.
+  **Interoperability with IPv6-only networks** — The goal is to support connectivity to IPv6-only nodes from your IPv4-only network. This is a less frequent use case, because most endpoints operate in dual-stack mode and provide an interoperability layer.

   **Adoption strategy** — Create dual-stack VPCs and IPv6-only subnets as part of those VPCs. Use the AWS NAT Gateway with the integrated NAT64 capability, and DNS64 to maintain an interoperability layer. Full dual-stack adoption is often not practical, so providing backwards compatibility to IPv4 networks is required.
+  **Mandated IPv6 endpoints** — The goal is to support interoperability with IPv6-only nodes connecting to your services, and avoid building technical debt in new services. Have a plan and complete transition of older services which do not have a dedicated IPv6 or dual-stack capability.

   **Adoption strategy** — Create dual-stack VPCs and subnets. Configure AWS services such as load balancers and edge service in dual-stack model with corresponding DNS records on the AWS Cloud. Optionally, provide separate endpoints for IPv4 and IPv6 in dedicated IPv4-only and IPv6-only stacks.

 Your organization should be prepared to operate in heterogeneous mode for many years to come. For over 20 years, IPv6 coexisted side-by-side with IPv4, and it will continue to do so. The long-term goal is to be IPv6 everywhere and retire the IPv4 stack, but you don’t need to rush it. Instead, work backwards from your business requirements and act accordingly. If you are just starting with IPv6, small steps along with the power of the AWS Cloud will give you the needed confidence to transition more of your network to IPv6-only mode.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
