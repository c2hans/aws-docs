---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/notification-center-setup.html
---

# Setting Up Notification Rules

## Prerequisites
<a name="_prerequisites"></a>

 **For Slack and email notifications:**

Slack and email channels send through an IAM role in your account. The connector must define a `securityConfig` that assumes that role. The role name must start with `SpatialDataManagementContentPublisher-`, and its trust policy must allow the SDMA connector invocation role to assume it. If the role cannot be assumed, SDMA does not save the connector, and the error names the role to add to the trust policy. For more information, see [Security Configuration](connector-configuration.md#security-configuration).

 **For Slack notifications:**

1. Store your Slack webhook URL in AWS Secrets Manager.
**Note**
The secret must be in the **same AWS region** as the SDMA deployment. Cross-region secret access is not supported.

1. Allow the role that the connector assumes to read the secret:

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "secretsmanager:GetSecretValue",
         "Resource": "arn:aws:secretsmanager:<region>:<account-id>:secret:<secret-name>"
       }
     ]
   }
   ```

 **For email notifications:**

Amazon SES must be configured in your AWS account with a verified sending identity. Recipients must have a verified email address in their Cognito user profile.

Allow the role that the connector assumes to send email from the sending identity. In the following example, replace `<region>`, `<account-id>`, and `<sending-identity>` with your own values:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ses:SendEmail",
      "Resource": "arn:aws:ses:<region>:<account-id>:identity/<sending-identity>"
    }
  ]
}
```

If SES denies any address, the delivery fails, and the invocation shows as failed in the Portal.

 **For in-app notifications:**

No additional setup required. The notification inbox is available automatically after deployment.

## Create a Notification Rule
<a name="_create-a-notification-rule"></a>

1. Create a connector with `"connectorType": "notification"` and `"direction": "publish"` at the library level. Specify the recipients, channel, and triggers in the `notificationConfig` block.

1. Associate the connector to one or more asset templates by adding its ID to the template’s `permittedConnectorIds` list.

1. The rule is now active. When an asset created from one of those templates raises a matching lifecycle event, the recipients receive the notification.

Every delivery is recorded as a connector invocation — visible in the portal with status, timestamp, and result.

## Deliver to Multiple Channels
<a name="_deliver-to-multiple-channels"></a>

A notification rule targets exactly one channel. To deliver to multiple channels for the same event, create one rule per channel and associate all of them to the same template.

For example, to send both a Slack message and an in-app notification when an asset fails:

1. Create a `notification` connector with `"channels": [{"type": "slack", …​}]` and the desired trigger.

1. Create a second `notification` connector with `"channels": [{"type": "inApp"}]` and the same trigger.

1. Associate **both** connectors to the same asset template.

Each connector is dispatched independently — if the Slack delivery fails and retries, the in-app delivery is unaffected.

## Example – Alert Owners When an Asset Fails Quality Checks (Slack)
<a name="_example-alert-owners-when-an-asset-fails-quality-checks-slack"></a>

In the following example, replace `<account-id>`, `<region>`, and `<secret-name>` with your own values:

```json
{
  "connectorName": "Asset Failure Alerts — Slack",
  "connectorType": "notification",
  "direction": "publish",
  "enabled": true,
  "connectorConfig": {
    "securityConfig": {
      "type": "AssumeRole",
      "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentPublisher-Notifications"
    },
    "notificationConfig": {
      "recipients": [
        {"role": "OWNER"}
      ],
      "channels": [
        {
          "type": "slack",
          "webhookUrlSecretArn": "arn:aws:secretsmanager:<region>:<account-id>:secret:<secret-name>"
        }
      ],
      "messages": {
        "asset": ["Asset ${asset.assetName} failed QC — ${eventName}"]
      }
    },
    "triggers": [
      {
        "resources": ["asset"],
        "events": ["update"],
        "filter": {"asset": {"metadataAttributes": {"qcStatus": "failed"}}},
        "steps": [{"stepType": "notification"}]
      }
    ]
  }
}
```

## Example – In-App Notification When a New Asset Is Created
<a name="_example-in-app-notification-when-a-new-asset-is-created"></a>

```json
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
      ]
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

## Example – Email a Team Alias When a File Is Added
<a name="_example-email-a-team-alias-when-a-file-is-added"></a>

```json
{
  "connectorName": "New File Alert — Email",
  "connectorType": "notification",
  "direction": "publish",
  "enabled": true,
  "connectorConfig": {
    "securityConfig": {
      "type": "AssumeRole",
      "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentPublisher-Notifications"
    },
    "notificationConfig": {
      "recipients": [{"role": "OWNER"}],
      "channels": [
        {
          "type": "email",
          "senderEmail": "<verified-sender>",
          "emailAddresses": ["site-surveys@example.com"]
        }
      ]
    },
    "triggers": [
      {
        "resources": ["file"],
        "events": ["upload"],
        "steps": [{"stepType": "notification"}]
      }
    ]
  }
}
```

This rule emails the project owners and the alias. To email only the alias, add `"includeRecipientEmails": false` to the channel.

## Example – Multi-Channel Delivery (Two Rules, One Template)
<a name="_example-multi-channel-delivery-two-rules-one-template"></a>

Create two connectors — one per channel — and associate both to the same template:

```json
// Rule 1 — Slack
{
  "connectorName": "Failure Alert — Slack",
  "connectorType": "notification",
  "direction": "publish",
  "connectorConfig": {
    "securityConfig": {"type": "AssumeRole", "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentPublisher-Notifications"},
    "notificationConfig": {
      "recipients": [{"role": "OWNER"}],
      "channels": [{"type": "slack", "webhookUrlSecretArn": "arn:aws:secretsmanager:<region>:<account-id>:secret:<slack-secret>"}]
    },
    "triggers": [{"resources": ["asset"], "events": ["update"], "filter": {"asset": {"metadataAttributes": {"qcStatus": "failed"}}}, "steps": [{"stepType": "notification"}]}]
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
      "channels": [{"type": "inApp"}]
    },
    "triggers": [{"resources": ["asset"], "events": ["update"], "filter": {"asset": {"metadataAttributes": {"qcStatus": "failed"}}}, "steps": [{"stepType": "notification"}]}]
  }
}
```
