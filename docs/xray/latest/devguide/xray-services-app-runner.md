---
source_url: https://docs.aws.amazon.com/xray/latest/devguide/xray-services-app-runner.html
---

# AWS App Runner and X-Ray
<a name="xray-services-app-runner"></a>

 AWS App Runner is an AWS service that provides a fast, simple, and cost-effective way to deploy from source code or a container image directly to a scalable and secure web application in the AWS Cloud. You don't need to learn new technologies, decide which compute service to use, or know how to provision and configure AWS resources. See [What is AWS App Runner](https://docs.aws.amazon.com/apprunner/latest/dg/what-is-apprunner.html) for more information.

 AWS App Runner sends traces to X-Ray by integrating with the [AWS Distro for OpenTelemetry](xray-services-adot.md) (ADOT). Use ADOT SDKs to collect trace data for your containerized applications, and use X-Ray to analyze and gain insights into your instrumented application. For more information, see [Tracing for your App Runner application with X-Ray](https://docs.aws.amazon.com/apprunner/latest/dg/monitor-xray.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
