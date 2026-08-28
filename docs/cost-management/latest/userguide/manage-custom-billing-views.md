---
source_url: https://docs.aws.amazon.com/cost-management/latest/userguide/manage-custom-billing-views.html
---

# Managing custom billing views
<a name="manage-custom-billing-views"></a>

As the creator of a custom billing view, you retain full control over the resource even after sharing it with other accounts. You can update the definition of a custom billing view to reflect changes in your organization. You can also manage which accounts can access a custom billing view, or you can delete a custom billing view, which immediately revokes access to all accounts. Accounts that have been given access to the view can’t modify the definition of the custom billing view. This ensures you retain full control over which accounts can access specific cost management data.

You can change the definition of an existing custom billing view at any time. Once edited, the updated custom billing view takes immediate effect. All accounts with access, including member accounts to which the custom billing view has been shared, will immediately see the cost management data based on the updated definition.

**Topics**
+ [Editing the filters of custom billing views](edit-filters-custom-billing-views.md)
+ [Editing the sources of custom billing views](edit-sources-custom-billing-views.md)
+ [Editing the tags of custom billing views](edit-tags-custom-billing-views.md)
+ [Deleting custom billing views](delete-custom-billing-views.md)
+ [Managing shared access to custom billing views in your organization](manage-shared-access-custom-billing-views.md)
+ [Understanding AWS managed billing views](manage-shared-access-managed-billing-views.md)
+ [Managing shared access to custom billing views outside of your organization](manage-external-shared-access-custom-billing-views.md)

You can control which accounts can access a custom billing view by modifying its associated resource share. Once you add an account to the resource share, the account gains access to the custom billing view. Once you remove an account from the resource share, the account loses access to the custom billing view.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
