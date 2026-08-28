---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/qbiz-indexes-limitations.html
---

# Limitations
<a name="qbiz-indexes-limitations"></a>

**Note**
In an IDC implementation, when a Amazon Q Business knowledge base is first created in Amazon Quick, access to the knowledge base is automatically granted to users with access to the selected Amazon Q Business index. For additional users to have access to a knowledge base, the admin must configure user access in both the Amazon Q Business console and Amazon Quick knowledge base permissions pages.

When using Amazon Q Business indexes in Amazon Quick, be aware of the following limitations:

## General Limitations
<a name="general-limitations"></a>
+ Amazon Q Business index knowledge bases cannot be changed like other knowledge bases in Amazon Quick.
+ Amazon Q Business index knowledge bases only support the docs types supported by Amazon Q Business.
+ QApps, Actions, and Amazon Q Business chat guardrails are not included in the BYOI capability.
+ Amazon Q Business indexes must be in the same AWS account and region as Amazon Quick.

## IDC Implementation Limitations
<a name="idc-implementation-limitations"></a>
+ Both Amazon Quick and Amazon Q Business must use the same instance of IAM Identity Center.

## Index Quotas
<a name="index-quotas"></a>
+ You can connect up to two Amazon Q Business indexes per Region to Amazon Quick in the current release.
+ This quota cannot be increased.
+ Once indexes are selected and saved in a Amazon Quick instance, they cannot be directly unselected.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
