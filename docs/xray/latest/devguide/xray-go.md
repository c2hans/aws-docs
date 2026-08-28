---
source_url: https://docs.aws.amazon.com/xray/latest/devguide/xray-go.html
---

# Working with Go
<a name="xray-go"></a>

 There are two ways to instrument your Go application to send traces to X-Ray:
+ [AWS Distro for OpenTelemetry Go](xray-go-opentel-sdk.md) – An AWS distribution that provides a set of open source libraries for sending correlated metrics and traces to multiple AWS monitoring solutions including Amazon CloudWatch, AWS X-Ray, and Amazon OpenSearch Service, via the [AWS Distro for OpenTelemetry Collector](https://aws-otel.github.io/docs/getting-started/collector).
+ [AWS X-Ray SDK for Go](xray-sdk-go.md) – A set of libraries for generating and sending traces to X-Ray via the [X-Ray daemon](xray-daemon.md).

 For more information, see [Choosing between the AWS Distro for OpenTelemetry and X-Ray SDKs](xray-instrumenting-your-app.md#xray-instrumenting-choosing).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
