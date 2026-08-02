---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/create-app-instance.html
---

# Creating an AppInstance for Amazon Chime SDK messaging
<a name="create-app-instance"></a>

To use Amazon Chime SDK messaging, you must first create an Amazon Chime SDK `AppInstance` in your AWS account.

**Topics**
+ [Building an AppInstance](#app-instance-steps)
+ [Creating an AppInstanceUser](#create-app-instance-user)

## Building an AppInstance
<a name="app-instance-steps"></a>

**To create an `AppInstance` for messaging**

1. In the CLI, run `aws chime-sdk-identity create-app-instance --name {{NameOfAppInstance}}.`

1. In the create response, make note of the `AppInstanceArn`. `arn:aws:chime:{{region}}: {{aws_account_id}}:app-instance/{{app_instance_id}}`.

## Creating an AppInstanceUser
<a name="create-app-instance-user"></a>

Once you create an `AppInstance`, you create an `AppInstanceUser` in that `AppInstance`. You typically do this when a user first registers or logs in to your app. You can also create an `AppInstanceUser` that acts on behalf of your back-end services.

The following example shows how to create a back-end `AppInstanceUser`:

```
aws chime-sdk-identity create-app-instance-user \
    --app-instance-arn "{{app_instance_arn}}" \
    --app-instance-user-id "back-end-worker" \
    --name "back-end-worker"
```

In the create response, note the `AppInstanceUserArn`. It takes this form: `arn:aws:chime:{{region}}: {{aws_account_id}}:app-instance/{{app_instance_id}}/user/{{app_instance_user_id}}`. In this example, `app_instance_user_id` is "back-end-worker."

**Note**
As a best practice, when creating an `AppInstanceUser` for a client application, have the `AppInstanceUserId` match an existing unique ID for that user, such as the `sub` of an identity provider. The name is an optional placeholder that is attached to some API entities, such as a message sender. It allows you to control the display name of a user in one place, rather then needing to look it up from `AppInstanceUser` ARN, which is also attached as the sender of a message.
