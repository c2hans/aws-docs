---
source_url: https://docs.aws.amazon.com/blocks/latest/devguide/bb-configuration.html
---

# Configuration
<a name="bb-configuration"></a>

This section covers Blocks for application settings and secrets.

## AppSetting
<a name="bb-app-setting"></a>

A single configuration value or secret. Read and update values at runtime. Mark a setting as `secret: true` to store it as a SecureString. Values are typed and can be read in your API handlers without environment variable boilerplate.

Locally, AppSetting stores values in memory. On AWS, it provisions an SSM Parameter Store parameter (or SecureString for secrets). Best for API keys, feature flags, and any configuration that might change without a redeploy.

For more information, see [bb-app-setting on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-app-setting).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Blocks. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query blocks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
