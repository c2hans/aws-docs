---
source_url: https://docs.aws.amazon.com/guidance/latest/automotive-data-platform-on-aws/customer-360.html
---

# Customer 360 Analytics
<a name="customer-360"></a>

The Customer 360 Analytics solution provides a comprehensive view of customer interactions, health metrics, and behavioral patterns across the entire customer lifecycle. By combining [Amazon Quick Suite](https://docs.aws.amazon.com/quicksuite/latest/userguide/) dashboards with Bedrock AI agents, this use case enables automotive companies to deliver personalized experiences, predict customer needs, and proactively address issues.

This chapter describes the architecture and design patterns for building a Customer 360 solution on top of the Automotive Data Platform. The v0.2 foundation deploy provides the governed data-product layer this pattern builds on — specifically the `customer_360`, `customer_interactions`, and `service_records` data products (see [Data products](data-products.md)). The analytics and AI layers described here represent a full implementation pattern informed by a reference deployment, but are not themselves provisioned by the `platform-foundation/` codebase today.

## What you’ll build
<a name="what-youll-build"></a>
+ Interactive dashboards with Quick Suite for visualizing customer sentiment and quality issues
+ Automated workflows with [Amazon Quick Automate](https://docs.aws.amazon.com/quicksuite/latest/userguide/using-amazon-quick-automate.html) for detecting critical issues
+ Approval processes with [Amazon Quick Flows](https://docs.aws.amazon.com/quicksuite/latest/userguide/using-amazon-quick-flows.html) for stakeholder notifications
+ AI-powered conversational analytics with Bedrock agents
+ Knowledge base with Aurora pgvector for semantic search

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for an Automotive Data Platform on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
