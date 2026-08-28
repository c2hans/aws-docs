---
source_url: https://docs.aws.amazon.com/cost-management/latest/userguide/manage-shared-access-managed-billing-views.html
---

# Understanding AWS managed billing views
<a name="manage-shared-access-managed-billing-views"></a>

AWS managed billing views are created when you map accounts to Billing Conductor billing groups or use billing transfer.

There are two types of AWS managed billing views: Billing group views, and billing transfer billing views.

**The two types of billing transfer billing views:**
+ My view - Shows the billing data that your bill transfer account is financially responsible for
+ Showback/chargeback view - Shows billing data configured for showback or chargeback purposes

AWS creates and manages these billing views, so you can't update or delete them directly. The** Cost Management Preferences **billing view tab currently shows only custom views, not AWS managed views.

To update an AWS managed view name, update the name of its associated resource (billing group or billing transfer). AWS managed views persist even if their associated resource is deleted or withdrawn.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
