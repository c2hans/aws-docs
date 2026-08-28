---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/register-endpoint.html
---

# Register a mobile device endpoint as an App Instance user for Amazon Chime SDK messaging
<a name="register-endpoint"></a>

To receive push notifications, app instance users must first use the [RegisterAppInstanceUserEndpoint](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_RegisterAppInstanceUserEndpoint.html) API to register a mobile device. They must register from a mobile app that has access to the device token for the device's operating system.

To ensure the app instance User has access to the Amazon Pinpoint application listed in the ARN, the user must have permission to call `mobiletargeting:GetApp` on the Amazon Pinpoint ARN. Otherwise, the Amazon Chime SDK throws a 403 Forbidden error when calling [RegisterAppInstanceUserEndpoint](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_RegisterAppInstanceUserEndpoint.html).

This example shows the policy needed to register an endpoint.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "PermissionToRegisterEndpoint",
            "Effect": "Allow",
            "Action": "chime:RegisterAppInstanceUserEndpoint",
            "Resource": "arn:aws:chime:{{us-east-1}}:{{123456789012}}:app-instance/{{app_instance_id}}/user/{{app_instance_user_id}}"
        },
        {
            "Sid": "PermissionToGetAppOnPinpoint",
            "Effect": "Allow",
            "Action": "mobiletargeting:GetApp",
            "Resource": "arn:aws:mobiletargeting:{{us-east-1}}:{{123456789012}}:apps/{{project_id}}"
        }
    ]
}
```

------

**To register an endpoint**
+ Use the Amazon Pinpoint ARN and your device token to call the [RegisterAppInstanceUserEndpoint](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_RegisterAppInstanceUserEndpoint.html) API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
