---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-migrating.html
---

# Migrating from AWS Resilience Hub
<a name="next-gen-migrating"></a>

If you're an existing AWS Resilience Hub (v1) customer, this guide helps you understand what changes with the next generation of Resilience Hub and how to migrate your applications. The following table summarizes key changes between the two versions.

| Area | AWS Resilience Hub v1 | Next generation Resilience Hub |
| --- | --- | --- |
| Core primitive | Application | System \+ Services |
| Assessment engine | Static rule-based checks | GenAI-powered failure mode analysis |
| Dependency visibility | None | Dependency discovery |
| Multi-account | Limited | Full AWS Organizations integration |
| Policies | Single RTO/RPO policy per application | Modular, composable policies (DR \+ Availability \+ Data recovery) |
| Testing | AWS FIS experiment templates (manual setup) | Recommended resilience tests (pre-configured, auto-targeted, pass/fail) |
| API version | /v1 | /v2 |

**Topics**
+ [What changes with Next generation Resilience Hub](next-gen-what-changes.md)
+ [Concept mapping: AWS Resilience Hub v1 to Next generation Resilience Hub](next-gen-concept-mapping.md)
+ [Step-by-step migration guide](next-gen-migration-guide.md)
+ [Pricing transition](next-gen-billing-transition.md)
+ [Known limitations during migration](next-gen-migration-limitations.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
