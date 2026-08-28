---
source_url: https://docs.aws.amazon.com/rolesanywhere/latest/userguide/how-to-configure-custom-notification-settings.html
---

# Configuring custom notification threshold (console)
<a name="how-to-configure-custom-notification-settings"></a>

1. Sign in to [IAM Roles Anywhere console](https://console.aws.amazon.com/rolesanywhere/home).

1. Scroll to find trust anchor table and **choose the trust anchor** to apply custom notification settings.

1. Within trust anchor detail page scroll towards **Notification settings** section and choose **Manage settings**.

1.  **Customize threshold** for the [notification event](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/customize-notification-settings.html#notification-setting-event). IAM Roles Anywhere will start sending metrics/events/notifications when number of days until your X.509 certificate expires is less than or equal this threshold. See [IAM Roles Anywhere notification evaluation criteria]().

1. Choose **Save changes** to apply custom notification threshold.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Roles Anywhere. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rolesanywhere` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
