---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/third-party-firewalls.html
---

# Third-party firewalls on Amazon EC2
<a name="third-party-firewalls"></a>

 While AWS WAF is the recommended solution, many customers have third-party firewalls that they want to keep using when they move to the cloud. Many major firewall providers have AMI that can be used on EC2 instances. However, these EC2-based WAFs must be carefully architected to prevent them from becoming bottlenecks during DDoS attacks.

 For HTTP-based applications, AWS recommends that these firewalls are used as a secondary defense layer (fine-grained protections) behind AWS resources integrated with AWS WAF, which is configured with volumetric protection using rate-based rules and IP reputation rule groups to protect your firewall tier.
