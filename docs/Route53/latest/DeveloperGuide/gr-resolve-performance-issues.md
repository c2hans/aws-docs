---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-resolve-performance-issues.html
---

# Resolve DNS performance issues with Route 53 Global Resolver
<a name="gr-resolve-performance-issues"></a>

Route 53 Global Resolver is designed for optimal performance with global anycast architecture, but various factors can affect DNS resolution speed. Address slow DNS resolution and optimize query response times for better client device performance using Route 53 Global Resolver.

## Slow DNS resolution
<a name="gr-slow-dns-resolution"></a>

To diagnose and resolve slow DNS response times:

1. **Analyze query response times**
   + Use DNS query logs to identify queries with high response times
   + Compare response times across different domains and query types
   + Monitor response time trends over time

1. **Check for high query volumes**
   + Monitor CloudWatch metrics for query volume spikes
   + Identify client devices or DNS views generating excessive queries
   + Look for query patterns that might indicate misconfigurations

1. **Review cache performance**
   + Analyze cache hit rates for frequently queried domains
   + Review TTL settings for DNS records
   + Consider adjusting TTL values based on query patterns

1. **Verify optimal Region selection**
   + Ensure global resolver regions are close to client device locations
   + Monitor anycast routing to confirm queries reach the nearest Region
   + Consider adding regions if client devices are geographically distant

## Performance optimization strategies
<a name="gr-performance-optimization"></a>

Use these strategies to optimize DNS performance:

Cache optimization
+ Adjust TTL values based on query patterns and change frequency
+ Use longer TTLs for stable records, shorter TTLs for frequently changing records
+ Monitor cache hit rates and adjust TTLs accordingly

Region optimization
+ Deploy global resolver in regions closest to client device concentrations
+ Monitor query routing patterns and response times by region
+ Consider adding regions for better geographic coverage

Protocol optimization
+ Choose appropriate DNS protocols based on security and performance requirements
+ Consider DNS-over-HTTPS (DoH) for encrypted connections with caching benefits
+ Use DNS-over-TLS (DoT) for encrypted connections with lower overhead

Rule optimization
+ Review and optimize firewall rule priority and complexity
+ Place frequently matched rules higher in priority order
+ Simplify complex rule conditions where possible

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
