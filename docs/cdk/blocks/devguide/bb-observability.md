---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/bb-observability.html
---

# Observability

This section covers AWS CDK Blocks for monitoring, logging, and tracing.

## Choosing an observability Block
<a name="_choosing_an_observability_block"></a>

| Block | Best for | Avoid when |
| --- | --- | --- |
|  `Metrics`  | Custom application metrics with dimensions for filtering and aggregation | You only need request-level tracing (use Tracer) |
|  `Logger`  | Structured JSON logging with log levels and request context | You need numeric aggregation or alerting (use Metrics) |
|  `Tracer`  | Request tracing in your backend code, latency analysis | You only need simple log output (use Logger) |
|  `Dashboard`  | A prebuilt view of compute health, logs, traces, and the metrics you choose | You need custom charts or interactive data exploration (use the CloudWatch console) |

## Metrics
<a name="bb-metrics"></a>

Custom application metrics. Emit named metric data points with dimensions for filtering and aggregation. Supports child emitters with merged dimensions for scoped metric contexts. Uses CloudWatch Embedded Metric Format to emit metrics.

Locally, Metrics writes to the console. On AWS, metrics flow to Amazon CloudWatch. Best for tracking business KPIs, API latencies, error rates, and custom application counters.

For more information, see [bb-metrics on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/bb-metrics).

## Logger
<a name="bb-logger"></a>

Structured JSON logging with levels and contextual metadata. Supports debug, info, warn, and error levels. Attach arbitrary metadata to log entries for filtering and analysis.

Locally, Logger writes to the console. On AWS, structured JSON flows to CloudWatch Logs. Each entry includes the X-Ray trace ID (`traceId`) when Lambda provides one. To tag entries with a request ID or other context, create a child logger with `log.child({ requestId })`. Best for application logging with searchable structured data.

For more information, see [bb-logger on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/bb-logger).

## Tracer
<a name="bb-tracer"></a>

Distributed request tracing. Wrap operations in traced segments to visualize request flow across your application. Add searchable annotations for debugging and add metadata for detailed inspection.

Locally, Tracer records traces to files in the `.bb-data/` directory for inspection. On AWS, it records segments in AWS X-Ray. Adding a `Tracer` turns on X-Ray active tracing for every compute Lambda function in the app, unless you set `enabled: false`. X-Ray bills per trace. Helper functions, such as database migrations, are not traced. Only Lambda functions are traced. API Gateway stage tracing is not turned on. Best for debugging latency issues and understanding request paths in production.

For more information, see [bb-tracer on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/bb-tracer).

## Dashboard
<a name="bb-dashboard"></a>

Auto-generated CloudWatch dashboard. It works without any other observability CDK Block: each compute in your app gets a health section and a logs section. A traces section appears when the app has an enabled `Tracer`. To chart your own metrics, pass a `Metrics` Block and list the metric names in `metricConfigs`. Dashboard does not create alarms.

Locally, Dashboard is not available; its route responds with a message directing you to deploy. On AWS, it provisions a CloudWatch Dashboard with those sections, and its route (`/aws-blocks/dashboard` by default) redirects to the dashboard in the CloudWatch console. Best for teams that want out-of-the-box monitoring without manual dashboard setup.

For more information, see [bb-dashboard on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/bb-dashboard).
