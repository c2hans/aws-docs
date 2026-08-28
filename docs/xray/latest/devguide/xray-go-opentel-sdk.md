---
source_url: https://docs.aws.amazon.com/xray/latest/devguide/xray-go-opentel-sdk.html
---

# AWS Distro for OpenTelemetry Go
<a name="xray-go-opentel-sdk"></a>

**Note**
X-Ray SDK/Daemon Maintenance Notice – On February 25th, 2026, the AWS X-Ray SDKs/Daemon will enter maintenance mode, where AWS will limit X-Ray SDK and Daemon releases to address security issues only. For more information on the support timeline, see [X-Ray SDK and Daemon Support timeline](xray-sdk-daemon-timeline.md). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation ](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-migration.html).

With the AWS Distro for OpenTelemetry Go, you can instrument your applications once and send correlated metrics and traces to multiple AWS monitoring solutions including Amazon CloudWatch, AWS X-Ray, and Amazon OpenSearch Service. Using X-Ray with AWS Distro for OpenTelemetry requires two components: an *OpenTelemetry SDK* enabled for use with X-Ray, and the *AWS Distro for OpenTelemetry Collector* enabled for use with X-Ray.

To get started, see the [AWS Distro for OpenTelemetry Go documentation](https://aws-otel.github.io/docs/getting-started/go-sdk).

For more information about using the AWS Distro for OpenTelemetry with AWS X-Ray and other AWS services, see [AWS Distro for OpenTelemetry](https://aws-otel.github.io/) or the [AWS Distro for OpenTelemetry Documentation](https://aws-otel.github.io/docs/introduction).

For more information about language support and usage, see [AWS Observability on GitHub](https://github.com/aws-observability).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
