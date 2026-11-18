---
source_url: https://docs.aws.amazon.com/route53globalresolver/1.0/userguide/security-monitoring.html
---

# Security monitoring capabilities in Amazon Route 53 Global Resolver
<a name="security-monitoring"></a>

Amazon Route 53 Global Resolver provides several security monitoring capabilities to help you identify and respond to potential threats:

DNS filtering alerts
When firewall rules are configured with ALERT actions, queries matching these rules are logged for security review while still being allowed through. This helps identify potential security issues without disrupting legitimate traffic.

Blocked query monitoring
Monitor blocked queries to understand attack patterns and validate that your security policies are working effectively. High numbers of blocked queries from specific sources may indicate targeted attacks.

Top domains reporting
Analyze the most frequently accessed and blocked domains to identify trends, optimize filtering rules, and detect anomalous behavior.

DDoS protection metrics
Amazon Route 53 Global Resolver includes built-in DDoS protection with top talker metrics and rate limiting. Monitor these metrics to understand traffic patterns and identify potential attacks.
