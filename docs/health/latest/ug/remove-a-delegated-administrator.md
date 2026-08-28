---
source_url: https://docs.aws.amazon.com/health/latest/ug/remove-a-delegated-administrator.html
---

# Removing a delegated administrator from your organizational view
<a name="remove-a-delegated-administrator"></a>

To remove access for a delegated administrator, call the [DeregisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.html) API operation.

From your organization's management account, call the following AWS CLI command to remove a member account as delegated administrator. In the following example command, replace **ACCOUNT\_ID** with the member account ID that you want to remove.

```
aws organizations deregister-delegated-administrator --account-id ACCOUNT_ID --service-principal  health.amazonaws.com
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query health` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
