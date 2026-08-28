---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/agent-accept-decline-ot.html
---

# Contact center agent ability to accept or decline overtime in Connect Customer
<a name="agent-accept-decline-ot"></a>

The following image shows pending Overtime requests in the agent calendars. Managers and agents can see overtime requests.

![The published schedule calendar tab, pending overtime requests.](http://docs.aws.amazon.com/connect/latest/adminguide/images/accept-decline-view-wfm.png)

Agents can accept or decline overtime in the Agent application schedule calendar.

## Required security profile permissions
<a name="req-sec-perms-accept-decline-ot"></a>

To accept or decline the request, an agent must have **Agent application schedule calendar - Edit** permissions in their security profile. This permission is shown in the following image of Agent Applications permissions on the security profiles page.

![Permissions in the agent application schedule calendar.](http://docs.aws.amazon.com/connect/latest/adminguide/images/SecurityProfile_cloudscape_staff_calendar.png)

## Accept and Decline overtime buttons for agents
<a name="buttons-for-agents-accept-decline-ot"></a>

The following image shows the Accept and Decline buttons on the agent application.

![The Accept and Decline buttons on the agent application.](http://docs.aws.amazon.com/connect/latest/adminguide/images/accept-decline-buttons-wfm.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
