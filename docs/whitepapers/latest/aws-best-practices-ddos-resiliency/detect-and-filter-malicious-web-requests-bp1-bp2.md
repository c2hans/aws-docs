---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/detect-and-filter-malicious-web-requests-bp1-bp2.html
---

# Detect and filter malicious web requests (BP1, BP2)
<a name="detect-and-filter-malicious-web-requests-bp1-bp2"></a>

 When your application runs on AWS, you can use Amazon CloudFront (and its HTTP caching capability), AWS WAF, and Shield Advanced Automatic Application layer protection to help prevent unnecessary requests reach your origin during application layer DDoS attacks.

 This section outlines a defense-in-depth strategy to protect your origin infrastructure using two complementary approaches. First, AWS WAF acts as the primary defense layer by filtering and blocking malicious requests before they reach your architecture. Second, HTTP caching serves as an additional protective layer by reducing the load on your infrastructure behind CloudFront. By implementing both AWS WAF filtering and strategic HTTP caching, you create multiple layers of defense that significantly reduce the risk of malicious traffic impacting your origin servers while optimizing legitimate request handling.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
