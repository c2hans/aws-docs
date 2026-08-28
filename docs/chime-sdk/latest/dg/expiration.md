---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/expiration.html
---

# Using ExpirationSettings in Amazon Chime SDK messaging
<a name="expiration"></a>

When you create an `AppInstanceUser` or a `Channel`, you can use `ExpirationSettings` to configure those resources for automatic deletion. `ExpirationSettings` helps reduce storage costs and prevent resource-limit-exceeded issues. For example, you can delete unused channels after 7 days, or delete an `AppInstanceUser` that was only invoked for testing purposes.

For an `AppInstanceUser`, you specify the expiration period based on user creation time. For a `Channel`, you specify the expiration period based on the channel's creation time, or last message time. The latter allows you use message activities to customize automatic deletion.

**Important**
Shortly after a resource expires, `ExpirationSettings` starts a background process to delete that resource. The process usually takes 6 hours, but that time can vary.
Expired `AppInstanceUsers` and `Channels` that haven’t yet been deleted still appear as valid and active. You can update or remove their expiration settings, and the system honors your changes.

**Topics**
+ [Configuring ExpirationSettings](#create-expiration)
+ [AWS CloudTrail events for expired resource deletion](#ct-events)

## Configuring ExpirationSettings
<a name="create-expiration"></a>

The following sections explain how to configure the `ExpirationSettings` of an `AppInstanceUser` or a `Channel`.

### Configuring ExpirationSettings when you create a resource
<a name="configure-on-create"></a>

You can configure `ExpirationSettings` when you run the [CreateAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateAppInstanceUser.html) or [CreateChannel](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannel.html) APIs. If you set the `ExpirationSettings` parameter, you must grant the following IAM permissions:
+ `chime:PutAppInstanceUserExpirationSettings` when creating an `AppInstanceUser`
+ `chime:PutChannelExpirationSettings` when creating a `Channel`.

The following example uses the AWS CLI to create an `AppInstanceUser` that expires after a day.

```
aws chime-sdk-identity create-app-instance-user \
--app-instance-arn "{{app_instance_arn}}" \
--app-instance-user-id "{{backend-worker}}" \
--name "{{backend-worker}}" \
--expiration-settings '{
            "ExpirationDays": {{1}},
            "ExpirationCriterion": "{{CREATED_TIMESTAMP}}"
        }'
```

The following example uses the AWS CLI to create a `Channel` that expires after a day after it last receives a message.

```
aws chime-sdk-messaging create-channel \
--chime-bearer "{{app_instance_user_arn}}" \
--app-instance-arn "{{app_instance_arn}}" \
--name "{{firstChannel}}" \
--expiration-settings '{
            "ExpirationDays": {{1}},
            "ExpirationCriterion": "{{LAST_MESSAGE_TIMESTAMP}}"
        }'
```

### Using Put APIs to configure ExpirationSettings
<a name="configure-on-put"></a>

You can also use the [PutAppInstanceUserExpirationSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_PutAppInstanceUserExpirationSettings.html) and [PutChannelExpirationSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PutChannelExpirationSettings.html) APIs to create, update, and delete `ExpirationSettings`.

The following example shows you to use the AWS CLI to update an `AppInstanceUser`'s `ExpirationSettings`.

```
aws chime-sdk-identity put-app-instance-user-expiration-settings \
--app-instance-user-arn "{{app_instance_user_arn}}" \
--expiration-settings '{
            "ExpirationDays": {{30}},
            "ExpirationCriterion": "{{CREATED_TIMESTAMP}}"
        }'
```

The following example shows you to use the AWS CLI to delete a channel's `ExpirationSettings`.

```
aws chime-sdk-messaging put-channel-expiration-settings \
--chime-bearer "{{app_instance_user_arn}}" \
--channel-arn "{{channel_arn}}"
```

## AWS CloudTrail events for expired resource deletion
<a name="ct-events"></a>

After the system deletes an expired resource, it sends an `ExpireAppInstanceUser` or `ExpireChannel` event to AWS CloudTrail. The type of event depends on the type of deleted asset.

The following example shows an `AppInstanceUser` event.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "accountId": "{{123456789012}}",
        "invokedBy": "chime.amazonaws.com"
    },
    "eventTime": "{{2023-03-15T00:00:00Z}}",
    "eventSource": "chime.amazonaws.com",
    "eventName": "ExpireAppInstanceUser",
    "awsRegion": "{{us-east-1}}",
    "sourceIPAddress": "chime.amazonaws.com",
    "userAgent": "chime.amazonaws.com",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "{{12345678-1234-1234-1234-123456789012}}",
    "readOnly": false,
    "resources": [
        {
            "accountId": "{{123456789012}}",
            "type": "AWS::Chime::AppInstanceUser",
            "ARN": "arn:aws:chime:{{us-east-1}}:{{123456789012}}:app-instance/{{app-instance-id}}/user/{{user-id}}"
        }
    ],
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "{{123456789012}}",
    "serviceEventDetails": {
        "reason": "AppInstanceUser deleted due to expiration settings."
    },
    "eventCategory": "Management"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
