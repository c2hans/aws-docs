---
source_url: https://docs.aws.amazon.com/marketplace/latest/buyerguide/management-access-with-apis.html
---

# Accessing the dashboard programmatically
<a name="management-access-with-apis"></a>

To create a **Procurement insights** dashboards programmatically, call the following API: [GetBuyerDashboard](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-reporting_GetBuyerDashboard.html).

**Important**
You must create the service-linked role listed in [Activating the dashboard](enabling-procurement-insights.md#integrate-dashboard) before you enable trusted access to the dashboard. Otherwise, the activation process fails.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
