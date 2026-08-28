---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/notification-center-setup.html
---

# Setting up notification rules
<a name="notification-center-setup"></a>

## Prerequisites
<a name="_prerequisites"></a>

 **For Slack notifications:**

1. Store your Slack webhook URL in AWS Secrets Manager.
**Note**
The secret must be in the **same AWS region** as the SDMA deployment. Cross-region secret access is not supported.

1. Grant the SDMA connector invocation Lambda permission to read the secret:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "secretsmanager:GetSecretValue",
         "Resource": "arn:aws:secretsmanager:<REGION>:<ACCOUNT_ID>:secret/<SECRET_NAME>"
       }
     ]
   }
   ```

 **For email notifications:**

Amazon SES must be configured in your AWS account with a verified sending identity. Recipients must have a verified email address in their Cognito user profile.

 **For in-app notifications:**

No additional setup required. The notification inbox is available automatically after deployment.

## Create a notification rule
<a name="_create-a-notification-rule"></a>

1. Create a connector with `"connectorType": "notification"` and `"direction": "publish"` at the library level. Specify the recipients, channel, and triggers in the `notificationConfig` block.

1. Associate the connector to one or more asset templates by adding its ID to the template’s `permittedConnectorIds` list.

1. The rule is now active. When an asset created from one of those templates fires a matching lifecycle event, SDMA delivers the notification.

Every delivery is recorded as a connector invocation — visible in the portal with status, timestamp, and result.

## Deliver to multiple channels
<a name="_deliver-to-multiple-channels"></a>

A notification rule targets exactly one channel. To deliver to multiple channels for the same event, create one rule per channel and associate all of them to the same template.

For example, to send both a Slack message and an in-app notification when an asset fails:

1. Create a `notification` connector with `"channels": [{"type": "slack", …​}]` and the desired trigger.

1. Create a second `notification` connector with `"channels": [{"type": "inApp"}]` and the same trigger.

1. Associate **both** connectors to the same asset template.

Each connector is dispatched independently — if the Slack delivery fails and retries, the in-app delivery is unaffected.

## Example: alert owners when an asset enters a failed state (Slack)
<a name="_example-alert-owners-when-an-asset-enters-a-failed-state-slack"></a>

```
{
  "connectorName": "Asset Failure Alerts — Slack",
  "connectorType": "notification",
  "direction": "publish",
  "enabled": true,
  "connectorConfig": {
    "notificationConfig": {
      "recipients": [
        {"role": "OWNER"}
      ],
      "channels": [
        {
          "type": "slack",
          "webhookUrlSecretArn": "arn:aws:secretsmanager:<REGION>:<ACCOUNT_ID>:secret/<SECRET_NAME>"
        }
      ],
      "messages": {
        "asset": ["Asset ${asset.assetName} entered ${asset.state} — ${eventName}"]
      }
    },
    "triggers": [
      {
        "resources": ["asset"],
        "events": ["stateChange"],
        "filter": {"stateFilter": ["ERROR", "FAILED"]},
        "steps": [{"stepType": "notification"}]
      }
    ]
  }
}
```

## Example: in-app notification when a new asset is created
<a name="_example-in-app-notification-when-a-new-asset-is-created"></a>

```
{
  "connectorName": "New Asset Alert — In-App",
  "connectorType": "notification",
  "direction": "publish",
  "enabled": true,
  "connectorConfig": {
    "notificationConfig": {
      "recipients": [
        {"role": "OWNER"},
        {"role": "MANAGER"}
      ],
      "channels": [
        {"type": "inApp"}
      ],
    },
    "triggers": [
      {
        "resources": ["asset"],
        "events": ["create"],
        "steps": [{"stepType": "notification"}]
      }
    ]
  }
}
```

## Example: multi-channel delivery (two rules, one template)
<a name="_example-multi-channel-delivery-two-rules-one-template"></a>

Create two connectors — one per channel — and associate both to the same template:

```
// Rule 1 — Slack
{
  "connectorName": "Failure Alert — Slack",
  "connectorType": "notification",
  "direction": "publish",
  "connectorConfig": {
    "notificationConfig": {
      "recipients": [{"role": "OWNER"}],
      "channels": [{"type": "slack", "webhookUrlSecretArn": "arn:aws:secretsmanager:<REGION>:<ACCOUNT_ID>:secret/<SLACK_SECRET>"}],
    },
    "triggers": [{"resources": ["asset"], "events": ["stateChange"], "filter": {"stateFilter": ["FAILED"]}, "steps": [{"stepType": "notification"}]}]
  }
}

// Rule 2 — In-app
{
  "connectorName": "Failure Alert — In-App",
  "connectorType": "notification",
  "direction": "publish",
  "connectorConfig": {
    "notificationConfig": {
      "recipients": [{"role": "OWNER"}],
      "channels": [{"type": "inApp"}],
    },
    "triggers": [{"resources": ["asset"], "events": ["stateChange"], "filter": {"stateFilter": ["FAILED"]}, "steps": [{"stepType": "notification"}]}]
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
