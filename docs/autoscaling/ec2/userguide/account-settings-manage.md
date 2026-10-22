---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/account-settings-manage.html
---

# Manage account settings
<a name="account-settings-manage"></a>

You can view and change your account settings using the Amazon EC2 console or the AWS CLI. Account settings are specific to each AWS Region. For the available account settings, see [Available account setting](ec2-auto-scaling-account-settings.md#account-settings-available).

## View your account settings
<a name="account-settings-describe"></a>

You can view all the available account settings for your account, or a specified account setting.

**To view your account settings (console)**

1. Open the [Settings](https://console.aws.amazon.com/ec2/v2/home?#Settings:tab=autoscalingGroups) page of the Amazon EC2 console, and then choose the **Auto Scaling groups** tab.

1. On the navigation bar at the top of the screen, choose the AWS Region for the account settings that you want to view.

1. The **Launch before terminate** section shows whether the `launchBeforeTerminate` setting is **Enabled** or **Disabled**.

**To view all the account settings for your account (AWS CLI)**
Use the [describe-account-settings](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-account-settings.html) command. Omit the `--name` parameter to return all account settings.

```
aws autoscaling describe-account-settings
```

The following is example output.

```
{
    "Settings": [

        {
            "Name": "launchBeforeTerminate",
            "Value": "enabled",
            "EnforcementType": "none"
        }
    ]
}
```

**To view the specified account setting for your account (AWS CLI)**
Include the `--name` parameter to return the specified account setting.

```
aws autoscaling describe-account-settings \
    --name launchBeforeTerminate
```

## Change an account setting
<a name="account-settings-put"></a>

You can change an account setting at any time.

**To enable or disable a feature (console)**

1. Open the [Settings](https://console.aws.amazon.com/ec2/v2/home?#Settings:tab=autoscalingGroups) page of the Amazon EC2 console, and then choose the **Auto Scaling groups** tab.

1. On the navigation bar at the top of the screen, choose the AWS Region for the account setting that you want to change.

1. In the **Launch before terminate** section, choose **Manage**.

1. To enable the feature, select **Enable**. To disable the feature, clear **Enable**.

1. Choose **Update launch before terminate**.

**To enable or disable a feature (AWS CLI)**
Use the [put-account-setting](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/put-account-setting.html) command. Set the `--value` parameter to `enabled` or `disabled`.

```
aws autoscaling put-account-setting \
    --name launchBeforeTerminate \
    --value enabled
```
