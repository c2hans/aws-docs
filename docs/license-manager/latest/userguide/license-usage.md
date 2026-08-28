---
source_url: https://docs.aws.amazon.com/license-manager/latest/userguide/license-usage.html
---

# Seller issued license usage in License Manager
<a name="license-usage"></a>

License Manager allows you to centrally track licenses across multiple Regions, by maintaining a count of all the checked out entitlements. License Manager also tracks the identity of the user and the underlying resource identifier, if available, associated with each check out, along with when it was checked out. You can track this time-series data through CloudWatch Events.

Licenses may be in one of the following states:
+ **Created** – The license is created.
+ **Updated** – The license is updated.
+ **Deactivated** – The license is deactivated.
+ **Deleted** – The license is deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
