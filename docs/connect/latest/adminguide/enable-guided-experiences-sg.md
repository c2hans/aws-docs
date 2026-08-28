---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/enable-guided-experiences-sg.html
---

# Enable step-by-step guides in Connect Customer
<a name="enable-guided-experiences-sg"></a>

The following steps allow you to provide your users with the ability to create guided experiences, and allow agents to interact with the experiences.

1. **Enable admins to create step-by-step guides**

   Assign managers and business analysts to the **Channels and flows - Views** security profile permission, as shown in the following image. This permission grants them the ability to configure step-by-step guides in flows.

   Since guides are created using flows, also assign the **Flows - Edit, Create** permissions so that they can create any type of flow.
![The Security profile permissions page, showing the flows and views permissions.](http://docs.aws.amazon.com/connect/latest/adminguide/images/sec-perms-admin-create-sq.png)

1. **Enable agents to view guides**

   Assign the **Agent Applications - Custom views** permission to agents. This enables them to see step-by-step guides in their agent workspace.
![The Security profile permissions page, the agent applications section, the custom views permission.](http://docs.aws.amazon.com/connect/latest/adminguide/images/sec-perms-agent-view-sq.png)

1. **Increase your service quota for concurrent active chats per instance**

   The workflows that agents interact with run as chat contacts in Connect Customer. We recommend that you increase your **concurrent active chats per instance** quota by the number of concurrent contacts you expect to have this feature enabled for.

   For more information about quotas, see [Connect Customer quotas](amazon-connect-service-limits.md#connect-quotas).
**Note**
Disconnect flow workflows count as their own contacts, so if you are setting both a `DefaultFlowID` and `DisconnectFlowID`, they will be counted as two active contacts.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
