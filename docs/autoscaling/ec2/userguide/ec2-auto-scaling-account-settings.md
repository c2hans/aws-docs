---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-account-settings.html
---

# Amazon EC2 Auto Scaling account settings
<a name="ec2-auto-scaling-account-settings"></a>

Use account settings to control whether certain Amazon EC2 Auto Scaling features are enabled (turned on) for your AWS account. Each account setting has a name and a value of `enabled` or `disabled`.

**Note**
Each account setting applies to your entire account within a single AWS Region. Configure a setting in every Region where you want it to take effect.

**Topics**
+ [Available account setting](#account-settings-available)
+ [Manage account settings](account-settings-manage.md)

## Available account setting
<a name="account-settings-available"></a>

Amazon EC2 Auto Scaling provides the following account setting.

**`launchBeforeTerminate`**
Controls whether Amazon EC2 Auto Scaling launches a replacement instance before terminating the instance it replaces. This applies to groups that don't define an instance maintenance policy or set instance refresh preferences. For more information, see [Launch replacement instances before terminating old ones](ec2-auto-scaling-launch-before-terminate-account-setting.md).
+ Valid values: `enabled` \| `disabled`
