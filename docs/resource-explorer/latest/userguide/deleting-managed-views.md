---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/userguide/deleting-managed-views.html
---

# Deleting managed views
<a name="deleting-managed-views"></a>

Managed views can only be deleted by the AWS service that manages them. Before the managing service can delete the view, you may need to perform service-specific tasks to remove a managed view from your account.

Resource Explorer managed views use the AWS Systems Manager `AWSManagedViewForSSM` unified console resource, which allows Systems Manager to access resource information indexed by Resource Explorer for your organization. If you want to delete the managed view, you must disable the unified console in Systems Manager. For instructions, see [Disabling the Systems Manager unified console](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-disable-integrated-console.html) in the *AWS Systems Manager User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
