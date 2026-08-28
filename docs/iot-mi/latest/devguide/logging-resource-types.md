---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/logging-resource-types.html
---

# Supported resource types
<a name="logging-resource-types"></a>

Each resource type corresponds to specific Managed Integrations workflows:

| Resource type | Workflows |
| --- | --- |
| managed-thing | Provisioning, commands, event processing |
| credential-locker | Credential locker operations |
| provisioning-profile | Provisioning profile operations |
| ota-task | OTA update tasks |
| account-association | Third-party discovery failures, OAuth callback failures, token refresh failures |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
