---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-dns-resolution-for-hybrid-networks-in-a-single-account-aws-environment.html
---

# Set up DNS resolution for hybrid networks in a single-account AWS environment
<a name="set-up-dns-resolution-for-hybrid-networks-in-a-single-account-aws-environment"></a>

*Abdullahi Olaoye, Amazon Web Services*

## Summary
<a name="set-up-dns-resolution-for-hybrid-networks-in-a-single-account-aws-environment-summary"></a>

This pattern describes how to set up a fully hybrid Domain Name System (DNS) architecture that enables end-to-end DNS resolution of on-premise resources, AWS resources, and internet DNS queries, without administrative overhead. The pattern describes how to set up Amazon Route 53 Resolver forwarding rules that determine where a DNS query that originates from AWS should be sent, based on the domain name. DNS queries for on-premises resources are forwarded to on-premises DNS resolvers. DNS queries for AWS resources and internet DNS queries are resolved by Route 53 Resolver.

This pattern covers hybrid DNS resolution in an AWS single-account environment. For information about setting up outbound DNS queries in an AWS multi-account environment, see the pattern [Set up DNS resolution for hybrid networks in a multi-account AWS environment](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-dns-resolution-for-hybrid-networks-in-a-multi-account-aws-environment.html).

## Prerequisites and limitations
<a name="set-up-dns-resolution-for-hybrid-networks-in-a-single-account-aws-environment-prereqs"></a>

**Prerequisites **
+ An AWS account
+ A virtual private cloud (VPC) in your AWS account
+ A network connection between the on-premises environment and your VPC, through AWS Virtual Private Network (AWS VPN) or AWS Direct Connect
+ IP addresses of your on-premises DNS resolvers (reachable from your VPC)
+ Domain/subdomain name to forward to on-premises resolvers (for example, onprem.mydc.com)
+ Domain/subdomain name for the AWS private hosted zone (for example, myvpc.cloud.com)

## Architecture
<a name="set-up-dns-resolution-for-hybrid-networks-in-a-single-account-aws-environment-architecture"></a>

**Target technology stack  **
+ Amazon Route 53 private hosted zone
+ Amazon Route 53 Resolver
+ Amazon VPC
+ AWS VPN or Direct Connect

**Target architecture**

![Workflow of Hybrid DNS resolution in an AWS single-account environment using Route 53 Resolver.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/120dedc8-cc6c-4aa7-be11-c70a7ee80642/images/7b75f534-1adc-4a39-86d6-5c4596ff7b6a.png)

## Tools
<a name="set-up-dns-resolution-for-hybrid-networks-in-a-single-account-aws-environment-tools"></a>
+ [Amazon Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-getting-started.html) makes hybrid cloud easier for enterprise customers by enabling seamless DNS query resolution across your entire hybrid cloud. You can create DNS endpoints and conditional forwarding rules to resolve DNS namespaces between your on-premises data center and your VPCs.
+ [Amazon Route 53 private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html) is a container that holds information about how you want Route 53 to respond to DNS queries for a domain and its subdomains within one or more VPCs that you create with the Amazon VPC service.

## Epics
<a name="set-up-dns-resolution-for-hybrid-networks-in-a-single-account-aws-environment-epics"></a>

### Configure a private hosted zone
<a name="configure-a-private-hosted-zone"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a Route 53 private hosted zone for an AWS reserved domain name such as myvpc.cloud.com. | This zone holds the DNS records for AWS resources that should be resolved from the on-premises environment. For instructions, see [Creating a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-creating.html) in the Route 53 documentation. | Network admin, System admin |
| Associate the private hosted zone with your VPC. | To enable resources in your VPC to resolve DNS records in this private hosted zone, you must associate your VPC with the hosted zone. For instructions, see [Creating a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-creating.html) in the Route 53 documentation. | Network admin, System admin |

### Set up Route 53 Resolver endpoints
<a name="set-up-route-53-resolver-endpoints"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an inbound endpoint. | Route 53 Resolver uses the inbound endpoint to receive DNS queries from on-premises DNS resolvers. For instructions, see [Forwarding inbound DNS queries to your VPCs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html) in the Route 53 documentation. Make a note of the inbound endpoint IP address. | Network admin, System admin |
| Create an outbound endpoint. | Route 53 Resolver uses the outbound endpoint to send DNS queries to on-premises DNS resolvers. For instructions, see [Forwarding outbound DNS queries to your network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html) in the Route 53 documentation. Make a note of the output endpoint ID. | Network admin, System admin |

### Set up a forwarding rule and associate it with your VPC
<a name="set-up-a-forwarding-rule-and-associate-it-with-your-vpc"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a forwarding rule for the on-premises domain. | This rule will instruct Route 53 Resolver to forward any DNS queries for on-premises domains (such as onprem.mydc.com) to on-premises DNS resolvers. To create this rule, you will need the IP addresses of the on-premises DNS resolvers and the outbound endpoint ID for Route 53 Resolver. For instructions, see [Managing forwarding rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-rules-managing.html) in the Route 53 documentation. | Network admin, System admin |
| Associate the forwarding rule with your VPC. | For the forwarding rule to take effect, you must associate the rule with your VPC. Route 53 Resolver then takes the rule into consideration when resolving a domain. For instructions, see [Managing forwarding rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-rules-managing.html) in the Route 53 documentation. | Network admin, System admin |

### Configure on-premises DNS resolvers
<a name="configure-on-premises-dns-resolvers"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure conditional forwarding in the on-premise DNS resolvers.  | For DNS queries to be sent to the Route 53 private hosted zone from the on-premises environment, you must configure conditional forwarding in the on-premises DNS resolvers. This instructs the DNS resolvers to forward all DNS queries for the AWS domain (for example, for myvpc.cloud.com) to the inbound endpoint IP address for Route 53 Resolver. | Network admin, System admin |

### Test end-to-end DNS resolution
<a name="test-end-to-end-dns-resolution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test DNS resolution from AWS to the on-premises environment. | From a server in the VPC, perform a DNS query for an on-premises domain (such as server1.onprem.mydc.com). | Network admin, System admin |
| Test DNS resolution from the on-premises environment to AWS. | From an on-premises server, perform DNS resolution for an AWS domain (such as server1.myvpc.cloud.com). | Network admin, System admin |

## Related resources
<a name="set-up-dns-resolution-for-hybrid-networks-in-a-single-account-aws-environment-resources"></a>
+ [Centralized DNS management of hybrid cloud with Amazon Route 53 and AWS Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/centralized-dns-management-of-hybrid-cloud-with-amazon-route-53-and-aws-transit-gateway/) (AWS Networking & Content Delivery blog)
+ [Simplify DNS management in a multi-account environment with Route 53 Resolver](https://aws.amazon.com/blogs/security/simplify-dns-management-in-a-multiaccount-environment-with-route-53-resolver/) (AWS Security blog)
+ [Working with private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html) (Route 53 documentation)
+ [Getting started with Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-getting-started.html) (Route 53 documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
