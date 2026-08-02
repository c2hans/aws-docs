---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPTroubleshooting.html
---

# Troubleshooting
<a name="CloudWatch-OTLPTroubleshooting"></a>

The following are the common troubleshooting scenarios and solutions for OTLP endpoint.

| Issue | Description | Solution |
| --- | --- | --- |
| Non-existing AWS credentials when launching OCB collector | Collector throws the following error when starting.<br />*Error: invalid configuration: extensions::sigv4auth: could not retrieve credential provider: failed to refresh cached credentials, no EC2 IMDS role found, operation error ec2imds: GetMetadata, request canceled, context deadline exceeded*. | Enter the correct credentials. |
| Invalid AWS credentials | Collector throws HTTP Status Code 403, Message=The security token included in the request is invalid., Details=[]“ when sending requests though OTLP endpoint. | Refresh the AWS credentials on the collector server. |
| Transactions Search disabled | Collector throws Message=The OTLP API is supported with CloudWatch Logs as a Trace Segment Destination. | Make sure Transaction Search is enabled in CloudWatch before using the OTLP endpoint for traces. For more information, see [Transaction Search](https://docs.aws.amazon.com//AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html). |
| Batching and timeout issues | Collector throws one of these issues:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPTroubleshooting.html) | Tune batching and timeout policies using [batchprocessor](https://github.com/open-telemetry/opentelemetry-collector/tree/main/processor/batchprocessor). |
| Retry issues | Transient network issues between the collector and OTLP endpoint.[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPTroubleshooting.html) | Tune retry policy using [exporter](https://github.com/open-telemetry/opentelemetry-collector/blob/main/exporter/exporterhelper/README.md). |
| Payload rejected | NA | Make sure the payload sent to the trace endpoint is within the limits and restrictions. For more information, see [Endpoint limits and restrictions](CloudWatch-OTLPEndpoint.md#CloudWatch-LimitsandRestrictions). |
| No auth header injected to outgoing export requests in ADOT | Generic 403 error, "Missing Authentication Token":<br />Example:<br />`ERROR:opentelemetry.exporter.otlp.proto.http.trace_exporter:Failed to export batch code: 403, reason: Missing Authentication Token` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPTroubleshooting.html)  |
| Logs or spans not appearing in CloudWatch log groups | No logs or spans are appearing in the expected CloudWatch log groups (aws/spans for spans and your specified custom log group for logs). | Make sure that the library to be instrumented is supported by auto-instrumentation. See supported libraries for [Java](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md), [Python](http://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/instrumentation/README.md), [JavaScript](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/packages/auto-instrumentations-node#supported-instrumentations) and [.NET](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/blob/main/docs/internal/instrumentation-libraries.md). |
