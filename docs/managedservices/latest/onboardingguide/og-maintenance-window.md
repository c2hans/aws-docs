---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/og-maintenance-window.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Maintenance Window
<a name="og-maintenance-window"></a>

You will want to create a maintenance window that considers different application needs, different AWS Regions, and different stress periods. Your maintenance window is when AMS will apply patching. Here are some guidelines:
+ To limit the impact on users, plan your maintenance window according to the AWS Region where your environments are deployed.
+ Schedule a window outside of regular business hours and when the least traffic is expected on production servers.
+ Typically, infrastructure stacks require monthly updates.
+ Schedule a maintenance window for at least 300 minutes. Operating system patching takes 60-90 minutes, infrastructure stack patching takes 180-300 minutes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
