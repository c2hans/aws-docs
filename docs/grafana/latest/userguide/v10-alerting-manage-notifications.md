---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/v10-alerting-manage-notifications.html
---

# Customize notifications
<a name="v10-alerting-manage-notifications"></a>

****
This documentation topic is designed for Grafana workspaces that support **Grafana version 10.x**.
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

Customize your notifications with notifications templates.

You can use notification templates to change the title, message, and format of the message in your notifications.

Notification templates are not tied to specific contact point integrations, such as Amazon SNS or Slack. However, you can choose to create separate notification templates for different contact point integrations.

You can use notification templates to:
+ Add, remove, or re-order information in the notification including the summary, description, labels and annotations, values, and links
+ Format text in bold and italic, and add or remove line breaks

You cannot use notification templates to:
+ Change the design of notifications in instant messaging services such as Slack and Microsoft Teams

**Topics**
+ [Using Go’s templating language](v10-alerting-notifications-go-templating.md)
+ [Create notification templates](v10-alerting-create-templates.md)
+ [Using notification templates](#v10-alerting-use-notification-templates)
+ [Template reference](v10-alerting-template-reference.md)

## Using notification templates
<a name="v10-alerting-use-notification-templates"></a>

Use templates in contact points to customize your notifications.

**To use a template when creating a contact point**

1. From the **Alerting** menu, choose the **Contact points** tab to see a list of existing contact points.

1. Choose **New**. Alternately, you can edit an existing contact point by choosing the **Edit** icon.

1. Enter the templates you wish to use in a field, such as **Message** or **Subject**. To enter a template, use the form `{{ template "{{template_name}}" . }}`, replacing {{template\_name}} with the name of the template you want to use.

1. Choose **Save contact point**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
