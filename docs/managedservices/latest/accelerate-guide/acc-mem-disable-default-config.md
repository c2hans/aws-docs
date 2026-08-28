---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-disable-default-config.html
---

# Disabling the default Accelerate alarm configuration
<a name="acc-mem-disable-default-config"></a>

AMS Accelerate provides the default configuration profile in your account based on the baseline alarms. However, this default configuration can be disabled by overriding any of the alarm definitions. You can disable a default configuration rule by overriding the **ConfigurationID** of the rule in your customization configuration profile and specifying the enabled field with a value of false.

For example, if the following configuration was present in the default configuration profile:

```
{
    "AWS::EC2::Instance": {
        "AMSManagedBlock1": {
            "Enabled": true,
            "Tag": {
                "Key": "ams:rt:ams-monitoring-policy",
                "Value": "ams-monitored"
            },
            "AlarmDefinition": {
                ...
            }
        }
    }
```

You could disable this tagging rule by including the following in your customization configuration profile:

```
{
    "AWS::EC2::Instance": {
        "AMSManagedBlock1": {
            "Enabled": false
        }
    }
}
```

To make these changes, the [CreateHostedConfigurationVersion](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateHostedConfigurationVersion.html) API must be called with the JSON profile document (see [Changing the Accelerate alarm configuration](acc-mem-change-am.md)) and subsequently must be deployed (see [Deploying Accelerate alarm configuration changes](acc-mem-deploy-change.md)). Note that when you create the new configuration version, you must also include any previously created custom alarms that you want in the JSON profile document.

**Important**
When AMS Accelerate updates the default configuration profile, it's not calibrated against your configured custom alarms, so review changes to the default alarms when you're overriding them in your customization configuration profile.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
