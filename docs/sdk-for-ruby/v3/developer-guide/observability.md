---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/observability.html
---

# Configuring observability features in the AWS SDK for Ruby
<a name="observability"></a>

 Observability is the extent to which a system's current state can be inferred from the data it emits. The data emitted is commonly referred to as telemetry. The AWS SDK for Ruby can provide the traces as a telemetry signal. You can wire up a `TelemetryProvider` to collect and send telemetry data to an observability backend. The SDK currently supports OpenTelemetry (OTel) as a telemetry provider and OpenTelemetry has many ways to export your telemetry data, including using [AWS X-Ray](https://docs.aws.amazon.com/xray/?icmpid=docs_homepage_devtools) or [Amazon CloudWatch](https://docs.aws.amazon.com/cloudwatch/?icmpid=docs_homepage_mgmtgov). For more information on OpenTelemetry exporters for Ruby, see [Exporters](https://opentelemetry.io/docs/languages/ruby/exporters) on the OpenTelemetry website.

 By default, the SDK will not record or emit any telemetry data. This topic explains how to configure and emit telemetry output.

 Telemetry can be configured either for a specific service or globally. The SDK for Ruby supplies an OpenTelemetry provider. You can also define a custom telemetry provider of your choice.

## Configuring an `OTelProvider` for a service client
<a name="config-otel"></a>

The SDK for Ruby provides an OpenTelemetry provider called [`OTelProvider`](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Telemetry/OTelProvider.html). The following example configures telemetry export using OpenTelemetry for the Amazon Simple Storage Service service client. For this simple example, the `OTEL_TRACES_EXPORTER` environment variable from OpenTelemetry is used to export the traces to the console output when you run the code. To learn more about `OTEL_TRACES_EXPORTER`, see [Exporter Selection](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#exporter-selection) in the OpenTelemetry documentation.

```
require 'aws-sdk-s3'
require 'opentelemetry-sdk'
require 'opentelemetry-exporter-otlp'

ENV['OTEL_TRACES_EXPORTER'] ||= 'console'

OpenTelemetry::SDK.configure

otel_provider = Aws::Telemetry::OTelProvider.new
client = Aws::S3::Client.new(telemetry_provider: otel_provider)
client.list_buckets
```

The previous code example shows the steps to configuring trace output for a service client:

1. Require OpenTelemetry dependencies.

   1. [`opentelemetry-sdk`](https://rubygems.org/gems/opentelemetry-sdk) for using `Aws::Telemetry::OTelProvider`.

   1. [`opentelemetry-exporter-otlp`](https://rubygems.org/gems/opentelemetry-exporter-otlp) for exporting telemetry data.

1.  Call `OpenTelemetry::SDK.configure` to set up the OpenTelemetry SDK with their configuration defaults.

1.  Using SDK for Ruby's OpenTelemetry provider, create an instance of the `OTelProvider` to pass as a configuration option to the service client that you want to trace.

   ```
   otel_provider = Aws::Telemetry::OTelProvider.new
   client = Aws::S3::Client.new(telemetry_provider: otel_provider)
   ```

 Using these steps, any methods that are called on that service client will emit trace data.

An example of the trace output generated from the call to Amazon S3’s `list_buckets` method is as follows:

### Example OpenTelemetry trace output
<a name="otel-trace-output"></a>

```
#<struct OpenTelemetry::SDK::Trace::SpanData
 name="Handler.NetHttp",
 kind=:internal,
 status=#<OpenTelemetry::Trace::Status:0x000000011da17bd8 @code=1, @description="">,
 parent_span_id="\xBFb\xC9\xFD\xA6F!\xE1",
 total_recorded_attributes=7,
 total_recorded_events=0,
 total_recorded_links=0,
 start_timestamp=1736190567061767000,
 end_timestamp=1736190567317160000,
 attributes=
  {"http.method"=>"GET",
   "net.protocol.name"=>"http",
   "net.protocol.version"=>"1.1",
   "net.peer.name"=>"s3.amazonaws.com",
   "net.peer.port"=>"443",
   "http.status_code"=>"200",
   "aws.request_id"=>"22HSH7NQTYMB5NHQ"},
 links=nil,
 events=nil,
 resource=
  #<OpenTelemetry::SDK::Resources::Resource:0x000000011e0bf990
   @attributes=
    {"service.name"=>"unknown_service",
     "process.pid"=>37013,
     "process.command"=>"example.rb",
     "process.runtime.name"=>"ruby",
     "process.runtime.version"=>"3.3.0",
     "process.runtime.description"=>"ruby 3.3.0 (2023-12-25 revision 5124f9ac75) [arm64-darwin23]",
     "telemetry.sdk.name"=>"opentelemetry",
     "telemetry.sdk.language"=>"ruby",
     "telemetry.sdk.version"=>"1.6.0"}>,
 instrumentation_scope=#<struct OpenTelemetry::SDK::InstrumentationScope name="aws.s3.client", version="">,
 span_id="\xEF%\x9C\xB5\x8C\x04\xDB\x7F",
 trace_id=" \xE7\xF1\xF8\x9D\e\x16/\xAC\xE6\x1A\xAC%j\x81\xD8",
 trace_flags=#<OpenTelemetry::Trace::TraceFlags:0x000000011d994328 @flags=1>,
 tracestate=#<OpenTelemetry::Trace::Tracestate:0x000000011d990638 @hash={}>>
#<struct OpenTelemetry::SDK::Trace::SpanData
 name="S3.ListBuckets",
 kind=:client,
 status=#<OpenTelemetry::Trace::Status:0x000000011da17bd8 @code=1, @description="">,
 parent_span_id="\x00\x00\x00\x00\x00\x00\x00\x00",
 total_recorded_attributes=5,
 total_recorded_events=0,
 total_recorded_links=0,
 start_timestamp=1736190567054410000,
 end_timestamp=1736190567327916000,
 attributes={"rpc.system"=>"aws-api", "rpc.service"=>"S3", "rpc.method"=>"ListBuckets", "code.function"=>"list_buckets", "code.namespace"=>"Aws::Plugins::Telemetry"},
 links=nil,
 events=nil,
 resource=
  #<OpenTelemetry::SDK::Resources::Resource:0x000000011e0bf990
   @attributes=
    {"service.name"=>"unknown_service",
     "process.pid"=>37013,
     "process.command"=>"example.rb",
     "process.runtime.name"=>"ruby",
     "process.runtime.version"=>"3.3.0",
     "process.runtime.description"=>"ruby 3.3.0 (2023-12-25 revision 5124f9ac75) [arm64-darwin23]",
     "telemetry.sdk.name"=>"opentelemetry",
     "telemetry.sdk.language"=>"ruby",
     "telemetry.sdk.version"=>"1.6.0"}>,
 instrumentation_scope=#<struct OpenTelemetry::SDK::InstrumentationScope name="aws.s3.client", version="">,
 span_id="\xBFb\xC9\xFD\xA6F!\xE1",
 trace_id=" \xE7\xF1\xF8\x9D\e\x16/\xAC\xE6\x1A\xAC%j\x81\xD8",
 trace_flags=#<OpenTelemetry::Trace::TraceFlags:0x000000011d994328 @flags=1>,
 tracestate=#<OpenTelemetry::Trace::Tracestate:0x000000011d990638 @hash={}>>
```

The previous trace output has two spans of data. Each trace entry provides additional metadata about the event in one or more attributes.

## Configuring an `OTelProvider` for all service clients
<a name="otel-global"></a>

Instead of turning on telemetry for a specific service client like the previous section explained, you have the option to turn on telemetry globally.

To emit telemetry data for **all** AWS service clients, you can set the telemetry provider on the `Aws.config` prior to creating service clients.

```
otel_provider = Aws::Telemetry::OTelProvider.new
Aws.config[:telemetry_provider] = otel_provider
```

With this configuration, any service clients created afterwards will automatically emit telemetry. To learn more about using `Aws.config` to set global settings, see [`Aws.config`](setup-config.md#config).

## Configuring a custom telemetry provider
<a name="custom-telem"></a>

If you don't want to use OpenTelemetry as your telemetry provider, the AWS SDK for Ruby does support you implementing a custom provider. It might be helpful to use the [`OTelProvider` implementation](https://github.com/aws/aws-sdk-ruby/blob/version-3/gems/aws-sdk-core/lib/aws-sdk-core/telemetry/otel.rb) that is available in the AWS SDK for Ruby GitHub repository as an example. For additional context, refer to the notes in [`Module: Aws::Telemetry`](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Telemetry.html) in the *AWS SDK for Ruby API Reference*.

## Span Attributes
<a name="span-attributes"></a>

Traces are the output of telemetry. Traces consist of one or more spans. Spans have attributes that include additional metadata that is automatically included when appropriate for the method call. The following is a list of the attributes supported by the SDK for Ruby, where:
+ Attribute Name - the name used to label the data appearing in the trace.
+ Type - the data type of the value.
+ Description - a description of what the value represents.

|  |  |  |
| --- |--- |--- |
| Attribute Name | Type | Description |
| error | Boolean | True if the unit of work was unsuccessful. Otherwise, false. |
| exception.message | String | The exception or error message. |
| exception.stacktrace | String | A stacktrace as provided by the language runtime if available. |
| exception.type | String | The type (fully qualified name) of the exception or error. |
| rpc.system | String | The remote system identifier set to 'aws-api'. |
| rpc.method | String | The name of the operation being invoked. |
| rpc.service | String | The name of the remote service. |
| aws.request\_id | String | The AWS request ID returned in the response headers, per HTTP attempt. The latest request ID is used when possible. |
| code.function | String | The method or function name. |
| code.namespace | String | The namespace within which code.function is defined. |
| http.status\_code | Long | The HTTP response status code. |
| http.request\_content\_length | Long | The size of the request payload body in bytes. |
| http.response\_content\_length | Long | The size of the response payload body in bytes. |
| http.method | String | The HTTP request method. |
| net.protocol.name | String | The name of the application layer protocol. |
| net.protocol.version | String | The version of the application layer protocol (e.g. 1.0, 1.1, 2.0). |
| net.peer.name | String | The logical remote hostname. |
| net.peer.port | String | The logical remote port number. |

**Tip**
OpenTelemetry-Ruby has additional implementations that are integrated with SDK for Ruby's existing Telemetry support. For more information, see [OpenTelemetry AWS-SDK Instrumentation](https://github.com/open-telemetry/opentelemetry-ruby-contrib/tree/main/instrumentation/aws_sdk) in the `open-telemetry` GitHub repository.
