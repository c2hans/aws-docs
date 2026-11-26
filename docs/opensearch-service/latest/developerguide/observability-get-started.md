---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-get-started.html
---

# Get started

You create an observability stack from the Amazon OpenSearch Service console. The console prepares an AWS CloudFormation stack with the template and parameters filled in, and you confirm it in the CloudFormation console.

## Prerequisites
<a name="obs-stack-create-prereqs"></a>
+ Permissions to create CloudFormation stacks and the resources listed in [What an observability stack creates](observability.md#observability-stack-creates), including IAM roles.
+ The IAM role that you are signed in with becomes the administrator of the stack's OpenSearch UI application and its data.

## Creation methods
<a name="obs-stack-create-options"></a>

Easy create
You enter only a name. The stack uses recommended settings: an Amazon OpenSearch Serverless collection for storage and a workspace that is ready to use.

Standard create
You also choose the storage backend. For more information, see [Choose a storage backend](#obs-stack-create-backend).

Both methods include the demo workload unless you clear its check box.

The create page lists every resource that will be created, by name, and the settings that will be used, before you create anything.

## Choose a storage backend
<a name="obs-stack-create-backend"></a>

The storage backend holds the logs and traces of your stack. Easy create uses an Amazon OpenSearch Serverless collection. With Standard create, you choose between a collection and an OpenSearch Service domain. The domain uses the engine that is optimized for log analytics in AWS Regions where that engine is available, and the general purpose engine in other AWS Regions. You can't change the backend after the stack is created.

The following table compares what the stack creates for each backend.

| Setting | Amazon OpenSearch Serverless collection | OpenSearch Service domain optimized for log analytics | OpenSearch Service domain on the general purpose engine |
| --- | --- | --- | --- |
| Capacity | Scales between 0 and 16 OpenSearch Compute Units (OCUs), and scales down when the stack is idle | One `om2.large.search` data node with 100 GiB of storage | One `r7g.large.search` data node with 100 GiB of storage |
| Trace index | `otel-v1-apm-span*` | `otel-v2-apm-span*` | `otel-v1-apm-span*` |
| Log and trace retention | 30 days by default | Not set by the stack | Not set by the stack |
| Alert monitors | Monitors for the demo workload | A cluster health monitor, and monitors for the demo workload except `OTel Demo - Payment Failures` | A cluster health monitor, and monitors for the demo workload |

For more information about each backend, see the following topics:
+ [Amazon OpenSearch Serverless](serverless.md)
+ [Creating and managing Amazon OpenSearch Service domains](createupdatedomains.md)
+ [Optimized for log analytics](optimized-log-analytics.md), which includes the AWS Regions where the engine is available

For the alert monitors, see [Alert monitors that a stack creates](obs-stack-use.md#obs-stack-use-alerts).

## Create a stack
<a name="obs-stack-create-procedure"></a>

**To create an observability stack**

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the navigation pane, under **Observability stack**, choose **Get started**, and then choose **Create observability stack**.

1. Enter a name for the stack. The name must be 3–17 characters, use only lowercase letters, numbers, and hyphens, start with a letter, and end with a letter or number. Resource names are derived from it.

1. Keep **Easy create**, or choose **Standard create** and select the backend.

1. Choose **Create in CloudFormation**. The CloudFormation console opens in a new tab with the template and parameters filled in.

1. In the CloudFormation console, acknowledge that CloudFormation will create IAM resources, and then choose **Create stack**. Keep the stack name that is filled in, so that the stack appears in your list of observability stacks.

1. Return to the Amazon OpenSearch Service console. The page shows the progress of each resource. Creation typically takes 15–30 minutes, and you can leave the page while it runs.

When the stack is created, open its workspace in OpenSearch UI from the stack's page. You sign in with your AWS account. If you deployed the demo workload, sample data starts to appear within a few minutes. To find your way around the workspace, see [Use and manage your observability stack](obs-stack-use.md).

## Send data to your observability stack
<a name="obs-stack-send-data"></a>

Each observability stack has one OpenTelemetry Protocol (OTLP) endpoint, provided by its Amazon OpenSearch Ingestion pipeline. The pipeline sends logs and traces to the stack's storage and metrics to its Prometheus workspace. You don't configure the pipeline yourself.

### Find the endpoint
<a name="obs-stack-send-data-endpoint"></a>

The OTLP endpoint is shown on the stack's page in the Amazon OpenSearch Service console, where you can copy it. It is also the `OSISEndpoint` output of the CloudFormation stack.

The endpoint has the following form:

```
https://{{pipeline-endpoint}}.{{region}}.osis.amazonaws.com
```

The pipeline accepts each signal on its own path. The paths include the name that you gave the stack, without the `obs-` prefix that the pipeline's own name has:

| Signal | Path |
| --- | --- |
| Logs | `/{{stack-name}}-ingest/v1/logs` |
| Traces | `/{{stack-name}}-ingest/v1/traces` |
| Metrics | `/{{stack-name}}-ingest/v1/metrics` |

### Permissions
<a name="obs-stack-send-data-permissions"></a>

Requests to the endpoint must be signed with AWS Signature Version 4 for the `osis` service. The IAM principal that sends data needs the `osis:Ingest` permission on the stack's pipeline. The pipeline's Amazon Resource Name (ARN) is the `OSISPipelineArn` output of the CloudFormation stack.

The following JSON policy example grants the `osis:Ingest` permission on a stack's pipeline. Replace the placeholder values with your own.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "osis:Ingest",
      "Resource": "arn:aws:osis:{{region}}:{{account-id}}:pipeline/obs-{{stack-name}}-ingest"
    }
  ]
}
```
+ {{region}} – The AWS Region of the stack, for example `us-east-1`.
+ {{account-id}} – Your AWS account ID.
+ {{stack-name}} – The name that you gave the observability stack.

### Send a test request
<a name="obs-stack-send-data-test"></a>

To check the endpoint and your permissions before you configure a collector, send one log record. The following example uses awscurl to send an OTLP log record in JSON. To get awscurl, see [awscurl](https://github.com/okigan/awscurl) on the GitHub website. Replace the placeholder values with your own.

```curl
awscurl --service osis --region {{region}} \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"resourceLogs":[{"resource":{"attributes":[{"key":"service.name","value":{"stringValue":"test"}}]},"scopeLogs":[{"logRecords":[{"timeUnixNano":"{{time-in-nanoseconds}}","severityText":"INFO","body":{"stringValue":"test log"}}]}]}]}' \
    {{otlp-endpoint}}/{{stack-name}}-ingest/v1/logs
```

You should see a `200 OK` response with an empty JSON object:

```json
{}
```

A `403` response means that the principal doesn't have the `osis:Ingest` permission on the pipeline, or that the request wasn't signed for the `osis` service.

### Configure an OpenTelemetry Collector
<a name="obs-stack-send-data-collector"></a>

The following YAML configuration example shows the parts of an OpenTelemetry Collector configuration that export to a stack. It uses the `sigv4auth` extension and the `otlphttp` exporter, which are included in the OpenTelemetry Collector Contrib distribution. Replace the placeholder values with your own.

```yaml
extensions:
  sigv4auth:
    region: "{{region}}"
    service: "osis"

exporters:
  otlphttp/logs:
    logs_endpoint: {{otlp-endpoint}}/{{stack-name}}-ingest/v1/logs
    auth: { authenticator: sigv4auth }
    compression: none
  otlphttp/traces:
    traces_endpoint: {{otlp-endpoint}}/{{stack-name}}-ingest/v1/traces
    auth: { authenticator: sigv4auth }
    compression: none
  otlphttp/metrics:
    metrics_endpoint: {{otlp-endpoint}}/{{stack-name}}-ingest/v1/metrics
    auth: { authenticator: sigv4auth }
    compression: none

service:
  extensions: [sigv4auth]
  pipelines:
    logs:    { receivers: [otlp], exporters: [otlphttp/logs] }
    traces:  { receivers: [otlp], exporters: [otlphttp/traces] }
    metrics: { receivers: [otlp], exporters: [otlphttp/metrics] }
```
+ {{region}} – The AWS Region of the stack, for example `us-east-1`.
+ {{otlp-endpoint}} – The stack's OTLP endpoint, including `https://`.
+ {{stack-name}} – The name that you gave the observability stack.

A new pipeline can take several minutes after it becomes active before its endpoint accepts data. Keep the exporter's retry enabled so that data sent during that time isn't dropped.

For how to instrument your applications and for other ways to send telemetry, see [Ingesting application telemetry](observability-ingestion.md). To send traces from AI agents, see [AI observability](observability-ai.md).

### Check that data is arriving
<a name="obs-stack-send-data-verify"></a>

Open the stack's workspace in OpenSearch UI and view your logs and traces. For more information, see [Discover Logs](observability-analyze-logs.md) and [Discover Traces](observability-analyze-traces.md). If you deployed the demo workload, its sample data appears alongside yours.

## Learn more
<a name="observability-get-started-learn-more"></a>

Use the following resources to learn more about sending telemetry data:
+ [OpenTelemetry instrumentation guides (per-language)](https://observability.opensearch.org/docs/send-data/applications/)
+ [Infrastructure monitoring (AWS, Docker, Kubernetes, Prometheus)](https://observability.opensearch.org/docs/send-data/infrastructure/)
+ [OTel Collector configuration](https://observability.opensearch.org/docs/send-data/opentelemetry/collector/)
+ [Data pipeline and batching](https://observability.opensearch.org/docs/send-data/data-pipeline/)
+ [Overview of Amazon OpenSearch Ingestion](ingestion.md) in this guide
