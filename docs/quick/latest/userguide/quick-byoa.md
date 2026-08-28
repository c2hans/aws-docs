---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/quick-byoa.html
---

# Bring Your Own Amazon Q Business Index (BYOI)
<a name="quick-byoa"></a>

Amazon Quick enables you to use your existing Amazon Q Business indexes as data sources. You can leverage your enterprise data without having to recreate indexes. This capability, known as Bring Your Own Index (BYOI), lets you connect your Amazon Q Business indexes to Amazon Quick and use them alongside other data sources for comprehensive analytics and intelligent responses.

BYOI supports two implementation methods:

**IDC Implementation**
Uses IAM Identity Center for authentication. Requires both Amazon Q Business and Amazon Quick to authenticate through IAM Identity Center in the same AWS account and region.

**Non-IDC Implementation**
Supports multiple authentication methods including native identities, AWS Managed Microsoft AD, and IAM federation. All Amazon Quick users automatically receive access to connected Amazon Q Business indexes.

**Topics**
+ [Overview of Amazon Q Business indexes in Amazon Quick](qbiz-indexes-overview.md)
+ [Prerequisites](qbiz-indexes-prerequisites.md)
+ [Supported authentication methods](qbiz-indexes-supported-authentication.md)
+ [Setting up permissions](qbiz-indexes-permissions.md)
+ [Creating knowledge bases from Amazon Q Business indexes](qbiz-indexes-creating-datasets.md)
+ [Sharing Amazon Q Business index knowledge bases](qbiz-indexes-sharing.md)
+ [Using Amazon Q Business index knowledge bases](qbiz-indexes-using.md)
+ [Limitations](qbiz-indexes-limitations.md)
+ [Billing](qbiz-indexes-billing.md)
+ [Feature comparison](qbiz-indexes-feature-comparison.md)
+ [Troubleshooting](qbiz-indexes-troubleshooting.md)
+ [Security best practices](qbiz-indexes-security.md)
+ [User types and capabilities](qbiz-indexes-user-types.md)
+ [Common use cases](qbiz-indexes-use-cases.md)
+ [Interacting with your Amazon Q Business indexes](qbiz-indexes-chat-interaction.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
