---
source_url: https://docs.aws.amazon.com/app2container/latest/UserGuide/configuration.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Configuring your application
<a name="configuration"></a>

Containerizing your application and creating pipelines with App2Container requires configuration throughout the process. This section of the guide describes the configuration files that are created by **app2container** commands, the fields that they contain, and which fields are configurable. App2Container commands primarily generate JSON configuration files, using standard JSON notation. Field details for the files included here indicate where there are specific requirements for the values.

App2Container also generates YAML format CloudFormation templates when you run the **generate app-deployment** command. However, those are not covered in this section, as their content is dictated by the target container management environment, such as Amazon ECS, Amazon EKS, or AWS App Runner. For more information about how App2Container works with these services, see [Product and service integrations for AWS App2Container](a2c-integrations.md).

Creating IAM resources is also covered separately, under the Security section. For more information and instructions about how to set up IAM resources for App2Container, see [Identity and access management in App2Container](iam-a2c.md).

You can consolidate your containerization workload by configuring connections to your application servers to run containerization workflows remotely, using App2Container remote commands from your worker machine. Prior to running remote commands, you must configure the connections that the worker machine uses for its target application servers. For more information on configuring connections, see the [remote configure](cmd-remote-configure.md) command reference page.

**Topics**
+ [Manage secrets](manage-secrets.md)
+ [Configure containers](config-containers.md)
+ [Configure deployment](config-deployment.md)
+ [Configure pipelines](config-pipeline.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App2Container. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app2container` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
