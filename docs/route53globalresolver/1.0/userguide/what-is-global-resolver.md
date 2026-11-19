---
source_url: https://docs.aws.amazon.com/route53globalresolver/1.0/userguide/what-is-global-resolver.html
---

# What is Amazon Route 53 Global Resolver?

Amazon Route 53 Global Resolver is a DNS resolver reachable over the internet and over your private connections (managed through AWS Cloud WAN) that provides easy, secure, and reliable DNS resolution for authorized clients in your organization across remote locations, branch offices, and on-premises environments. You can resolve queries for domains hosted on Amazon Route 53 private hosted zones or public domains on the internet, while maintaining high availability through global anycast architecture. Amazon Route 53 Global Resolver helps you protect your clients from DNS-based data exfiltration attacks, by filtering queries to potentially malicious domains.

Amazon Route 53 Global Resolver uses anycast IP addresses that automatically route DNS queries to the AWS Region closest to your source query location for optimal latency and availability. You can select the regions where your global resolver should provide DNS resolution from for your authorized clients, configure different views for the clients for the resolution of private and public domains, filter malicious domains, and monitor DNS activity across your organization.

**Topics**
+ [Why Global Resolver](why-global-resolver.md)
+ [Why Amazon Route 53 Global Resolver?](#why-global-resolver)
+ [Concepts and terminology](concepts-terminology.md)
+ [How it works](how-it-works.md)
+ [Use cases](cloud-resolver-use-cases.md)
+ [Related services](related-services.md)
+ [Accessing Global Resolver](accessing-cloud-resolver.md)

## Why Amazon Route 53 Global Resolver?
<a name="why-global-resolver"></a>

Amazon Route 53 Global Resolver provides centralized DNS security and filtering for remote and hybrid clients and workloads across multiple locations. Regardless of the location of your workloads, applications, or users, Amazon Route 53 Global Resolver ensures consistent DNS protection without requiring complex on-premises infrastructure.

Key benefits for remote and hybrid environments:
+ **Simplified management** - Configure private and public domain resolution using a single solution instead of managing multiple on-premises DNS servers
+ **Unified DNS security** - Apply consistent filtering policies across all remote clients and hybrid workloads
+ **Scalable protection** - Automatically scales to handle DNS queries from growing remote workforces and cloud workloads
+ **Reduced infrastructure** - Minimizes the need for DNS security appliances at each remote location

To get started, see:
+ [Key concepts and components for Amazon Route 53 Global Resolver](concepts-terminology.md) - Core concepts for DNS security deployment
+ [How Amazon Route 53 Global Resolver works](how-it-works.md) - How Amazon Route 53 Global Resolver protects remote and hybrid environments
+ [Tutorial: Create your first Amazon Route 53 Global Resolver](getting-started.md) - Tutorial for your first DNS filtering setup
