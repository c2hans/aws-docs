---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-dependency-discovery.html
---

# Dependency discovery
<a name="next-gen-dependency-discovery"></a>

Dependency discovery in the next generation of Resilience Hub automatically identifies all AWS services, internal endpoints, and third-party endpoints that your services depend on and assesses their location and frequency. It uses DNS query log analysis to surface dependencies you may not know about – including unexpected cross-region calls, critical third-party dependencies, and infrequently accessed services that could cause failures during incidents.

**Topics**
+ [How dependency discovery works](next-gen-how-discovery-works.md)
+ [Prerequisites for dependency discovery](next-gen-discovery-prerequisites.md)
+ [Enabling dependency discovery for a service](next-gen-enabling-discovery.md)
+ [Monitoring discovery status](next-gen-discovery-status.md)
+ [Viewing discovered dependencies](next-gen-viewing-dependencies.md)
+ [Classifying dependencies as hard or soft](next-gen-classifying-dependencies.md)
+ [Coverage and known limitations](next-gen-discovery-limitations.md)
+ [Troubleshooting dependency discovery](next-gen-troubleshooting-discovery.md)
+ [Pricing](next-gen-dependency-discovery-pricing.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
