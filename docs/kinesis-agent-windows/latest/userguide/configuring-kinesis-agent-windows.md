---
source_url: https://docs.aws.amazon.com/kinesis-agent-windows/latest/userguide/configuring-kinesis-agent-windows.html
---

# Configuring Amazon Kinesis Agent for Microsoft Windows
<a name="configuring-kinesis-agent-windows"></a>

Before starting Amazon Kinesis Agent for Microsoft Windows, you must create a configuration file and deploy it. The configuration file provides the necessary information to collect, transform, and stream data on Windows servers and desktop computers to various AWS services. Configuration files define sets of sources, sinks, and pipes that connect sources to sinks, along with optional transformations.

The Kinesis Agent for Windows configuration file is named `appsettings.json`. Deploy this file to `%PROGRAMFILES%\Amazon\AWSKinesisTap`.

**Topics**
+ [Basic Configuration Structure](basic-configuration-structure.md)
+ [Source Declarations](source-object-declarations.md)
+ [Sink Declarations](sink-object-declarations.md)
+ [Pipe Declarations](pipe-object-declarations.md)
+ [Configuring Automatic Updates](update-configuration-options.md)
+ [Kinesis Agent for Windows Configuration Examples](configuring-kaw-examples.md)
+ [Configuring Telemetrics](telemetrics-configuration-option.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Kinesis Agent for Windows. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis-agent-windows` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
