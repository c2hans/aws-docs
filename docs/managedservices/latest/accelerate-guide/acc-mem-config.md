---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-config.html
---

# Accelerate Alarm Manager configuration profiles
<a name="acc-mem-config"></a>

When your account is onboarded to AMS Accelerate, two JSON documents, called configuration profiles, are deployed in your account with AWS AppConfig (see [What is AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html)). Both profile documents reside in the Alarm Manager application and in the AMS Accelerate infrastructure environment.

**Topics**
+ [Accelerate Configuration profile: monitoring](acc-mem-config-doc-format.md)
+ [Accelerate Configuration profile: pseudoparameter substitution](acc-mem-config-doc-sub.md)
+ [Accelerate alarm configuration examples](acc-mem-config-ex.md)
+ [Viewing your Accelerate Alarm Manager configuration](acc-mem-view-am.md)
+ [Changing the Accelerate alarm configuration](acc-mem-change-am.md)
+ [Modifying the Accelerate alarm default configuration](acc-mem-modify-default.md)
+ [Deploying Accelerate alarm configuration changes](acc-mem-deploy-change.md)
+ [Rolling back Accelerate alarm changes](acc-mem-rollback-am-change.md)
+ [Retaining Accelerate alarms](acc-mem-retain-alarm.md)
+ [Disabling the default Accelerate alarm configuration](acc-mem-disable-default-config.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
