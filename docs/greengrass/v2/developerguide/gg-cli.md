---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/gg-cli.html
---

# Greengrass Command Line Interface
<a name="gg-cli"></a>

The Greengrass Command Line Interface (CLI) lets you interact with AWS IoT Greengrass Core on your device to locally develop components and debug issues. For example, you can use the Greengrass CLI to create a local deployment and restart a component on the core device.

Deploy the [Greengrass CLI component](greengrass-cli-component.md) (`aws.greengrass.Cli`) to install the Greengrass CLI on your core device.

**Important**
 <a name="local-dev-tools-production-environment-warning"></a>We recommend that you use this component in only development environments, not production environments. This component provides access to information and operations that you typically won't need in a production environment. Follow the principle of least privilege by deploying this component to only core devices where you need it.

**Topics**
+ [Install the Greengrass CLI](install-gg-cli.md)
+ [Greengrass CLI commands](gg-cli-reference.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
