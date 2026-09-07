---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/configure-notifications.html
---

# Configure notifications
<a name="configure-notifications"></a>

In addition to the solution-managed Amazon SNS topics described in [Example SNS notifications](example-sns-notifications.md), you can create notification configurations from the Web UI. Each configuration controls which events are delivered, where they are delivered, and what each message contains. The solution stores configurations in the admin account and applies them to findings and remediations aggregated to that account and Region.

**Web UI required**
You create and manage notification configurations from the Web UI. You must enable the Web UI (deploy the Web UI components when you launch or update the admin stack) to create and manage notification configurations.

## Notification channels
<a name="notification-channels"></a>

Each notification configuration delivers events through one or more channels. The solution supports the following channel types:

| Channel | Description |
| --- | --- |
| Email | Sends email to the recipients you select. Recipients can be chosen by role (primary account contact, security contact, operations contact, account operators) or entered as custom email addresses. Custom email recipients must confirm their subscription before they receive messages. |
| Slack | Posts messages to a Slack channel. Requires the Slack channel ID and an AWS Secrets Manager secret holding the Slack credentials. |
| JIRA | Creates a JIRA issue. Requires the JIRA instance URL, project key, issue type, and a Secrets Manager secret holding the JIRA credentials. |
| ServiceNow | Creates a record in a ServiceNow table. Requires the ServiceNow instance URL, table name, and a Secrets Manager secret holding the ServiceNow API key. |
| Amazon SNS | Publishes to an Amazon SNS topic in the admin account and Region. |

**Important**
The solution reads credentials for the Slack, JIRA, and ServiceNow channels from AWS Secrets Manager. The secret name must start with `asr/notifications/` (for example, `arn:aws:secretsmanager:us-east-1:111111111111:secret:asr/notifications/servicenow-creds`). The instance URL for the JIRA and ServiceNow channels must use HTTPS.

## Create a notification configuration
<a name="create-a-notification-configuration"></a>

1. Open the Web UI and go to the **Notifications** page.

1. Choose **Create notification configuration**.
![Create notification configuration.](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/create-notification-configuration-popup.png)

1.  **Basic information** – Enter a configuration name and choose the notification type:

   1.  **Finding** – Notify when new findings are detected.

   1.  **Remediation** – Notify when remediations are executed.

1.  **Delivery channels** – Select one or more channels and provide their configuration. At least one channel must be enabled.
![Notification delivery channels.](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/create-notification-delivery-channels-popup.png)

1. (Optional) **Filters** – Narrow the events the configuration matches by severity, remediation status (remediation type only), control IDs, or resource filters. Leaving a filter set to **All** applies no restriction on that dimension.
![Notification filters.](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/create-notification-notification-filter-popup.png)

1. (Optional) **Batching** – Enable a batch window to group multiple events into a single notification. The batch window duration must be within these ranges: 5–60 minutes, 1–24 hours, 1–365 days.
![Notification batching.](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/create-notification-notification-batching-popup.png)

1.  **Content options** – Choose what each message includes. See [Notification content options](#notification-content-options).
![Notification content options.](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/create-notification-notification-content-popup.png)

1. Choose **Submit**.

## Notification content options
<a name="notification-content-options"></a>

Content options control what each notification message includes. The following options each add a link or snippet to the message:

| Option | Description |
| --- | --- |
|  `includeManualRemediationLink`  | Adds a link to the finding’s page in the Web UI, where an operator can run the remediation manually. |
|  `includeEnableAutomationLink`  | Adds a link to the Web UI page for enabling fully-automated remediation for the control. |
|  `includeIaCSnippet`  | Adds an infrastructure-as-code snippet for the remediation in the formats you select (CloudFormation YAML, CloudFormation JSON, Terraform, or CDK). Applies to remediation-type notifications. |
|  `includeRemediationDeadline`  | Adds a remediation due-by date to each notification for a matching finding. Applies to finding-type notifications. When enabled, set `remediationDeadlineDays` (1–90). See [Remediation deadlines and deadline enforcement](#remediation-deadlines). |

**Links require the Web UI**
The `includeManualRemediationLink` and `includeEnableAutomationLink` options add links to Web UI pages. The Web UI must be enabled for these links to resolve. If the Web UI is not deployed, do not enable these options.

## Remediation deadlines and deadline enforcement
<a name="remediation-deadlines"></a>

A finding-type notification configuration can attach a remediation deadline to each finding it matches, and — optionally — enforce that deadline by automatically remediating overdue findings.

### Remediation deadlines
<a name="plain-remediation-deadlines"></a>

Enable the `includeRemediationDeadline` content option on a finding-type configuration and set `remediationDeadlineDays` to a value from 1 to 90. For each finding the configuration matches, the solution computes a remediation due-by date (the finding’s creation time plus the configured number of days) and includes it in the notification.

By themselves, deadlines are **informational**. The due-by date appears in the notification, but nothing happens when it passes — the solution does not act on an overdue finding unless you also enable enforcement.

### Deadline enforcement
<a name="deadline-enforcement"></a>

**Warning**
When you enable the `enforceDeadline` option on a finding-type configuration, remediation deadlines stop being advisory and become **enforcing**. The solution automatically triggers the Orchestrator to remediate any overdue, unresolved finding that matches the configuration — **with no human intervention**. This applies whether or not the finding’s control has automated remediation enabled. Enable enforcement only for configurations whose matching findings you are comfortable having the solution remediate automatically.

**24-hour minimum grace period**
The solution never remediates a finding less than **24 hours** after it becomes eligible for enforcement — even for a pre-existing backlog whose creation-time deadline is already in the past. This 24-hour floor is fixed and non-configurable, and is separate from (and additional to) the 1–90 day `remediationDeadlineDays` range.
As a result, turning on enforcement for an existing backlog does **not** trigger a mass remediation the instant you enable it. Every matching finding gets at least 24 hours of notice before the solution can remediate it.

#### Prerequisites and scope
<a name="deadline-enforcement-prerequisites"></a>
+  **Finding-type only.** Enforcement is supported only on finding-type notification configurations, not remediation-type configurations.
+  **Deadline required.** The configuration must have `includeRemediationDeadline` enabled and `remediationDeadlineDays` set to a value from 1 to 90.
+  **Web UI required.** Notification configurations are created and managed from the Web UI, so the Web UI must be deployed.
+  **Config-boundary scope.** Enforcement applies to findings that match the configuration’s control, severity, and resource filters — the notification-config boundary, not the control boundary. It does not depend on whether the matching control has automated remediation enabled. In practice, only findings that were not already auto-remediated ever reach enforcement.

## ServiceNow custom field mappings
<a name="servicenow-custom-field-mappings"></a>

Custom field mappings let you add key-value pairs to the ServiceNow record created for a finding. The value can include template variables that the solution substitutes from the finding at send time. The key is the ServiceNow column name on the target table.

The following template variables are supported in the value:
+  `${FINDING_ID}`
+  `${CONTROL_ID}`
+  `${SEVERITY}`
+  `${ACCOUNT_ID}`
+  `${REGION}`
+  `${RESOURCE_ARN}`
+  `${CONFIG_NAME}`

The solution enforces the following constraints on custom field mappings:
+ Up to 20 mappings per channel.
+ Key length up to 64 characters; resolved value length up to 256 characters.
+ Do not use the following solution-managed fields as keys: `short_description`, `description`, `urgency`, `impact`, `work_notes`.

**Important**
The solution writes finding data to ServiceNow as-is and does not HTML-encode or sanitize the values it sends. Map custom fields only to standard data fields (for example, plain String fields). Do **not** map them to:
HTML fields or journal/journal-input fields, which can render HTML, or
Script fields (`script`, `script_plain`), which can be evaluated by server-side code.
A plain String field displays values as text. HTML and journal fields can render markup. Finding data, such as a resource identifier, might contain characters that your ServiceNow instance renders as markup. Whether stored values are rendered or escaped is governed by your ServiceNow instance’s security hardening settings (for example, HTML escaping and the HTML sanitizer), which you own and should keep enabled. Prefer customer-defined custom columns (typically prefixed `u_` or `x_`) over out-of-box fields, and confirm the target field type before mapping.

For more information about ServiceNow security hardening, see the following resources:
+  [ServiceNow input validation (instance security hardening)](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/administer/security/reference/input-validation-instance-security-hardening.html)
+  [Render journal field entries as HTML (default High Security escaping behavior)](https://docs.servicenow.com/bundle/paris-governance-risk-compliance/page/administer/field-administration/task/render-journal-field-entries-as-html.html)
