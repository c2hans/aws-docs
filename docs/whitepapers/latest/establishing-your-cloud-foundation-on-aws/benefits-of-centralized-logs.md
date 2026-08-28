---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/benefits-of-centralized-logs.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Benefits of centralized logs
<a name="benefits-of-centralized-logs"></a>

As your environment grows and scales with your business needs, creating a single location to aggregate all the logs across your environment helps simplify the analysis and monitoring of the logs. Additionally, it makes it easier to access the environment logs, and controlling who is able to consume the logs. This allows you to create different dashboards and tools for your logging capabilities.

When your environment scales and distributes across multiple resources and isolated environments, there are some benefits that centralizing your logs in one place may bring to your environment.

## Create a single location for your logs
<a name="create-a-single-location-for-your-logs"></a>

Logs should be aggregated into a central location for long-term storage and centralized analysis. This enables you to monitor your environment centrally and simplifies your operations. It also creates a single source of truth across your resources, security, and operations logs. Additionally, it reduces the chance of logs being lost and ensures your environment is appropriately tracked continuously.

## Secure your logs
<a name="secure-your-logs"></a>

 When the logs in your environment are stored in a central location it is easier for you to establish comprehensive controls to protect your environment. Human access to your logs should be limited. Instead, read actions should be performed by different automated mechanism standardize access controls. We recommend you to have a monitoring mechanism in place that triggers an alarm when the log storage is access with write or admin permissions.

## Protect your logs with centralized controls
<a name="protect-your-logs-with-centralized-controls"></a>

All of your logs should be stored in the same isolated environment protected by centralized controls. Controls should be configured to protect your log storage environment using both preventative and detective controls.
+  **Preventive controls **enable you to prevent actions in the environment. Preventative controls can be used to restrict access and actions to log storage based on role, action type, service, or region.
+  **Detective controls **are implemented to actively monitor the environment. This allows you to create alerts based on unwanted or unexpected actions taken within the environment. Optionally, remediation actions can be invoked automatically mitigate the risks within the log storage environment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
