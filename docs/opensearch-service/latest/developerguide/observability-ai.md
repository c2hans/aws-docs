---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-ai.html
---

# AI observability

AI observability in OpenSearch provides end-to-end tooling for monitoring, debugging, and optimizing AI agent and large language model (LLM) workflows. Built on GenAI semantic conventions and natively integrated with OpenTelemetry (OTel), it gives you full visibility into how your AI applications behave in production.

AI observability includes the following capabilities:
+ **Agent tracing** – Capture hierarchical execution traces across agent orchestration steps, LLM calls, tool invocations, and retrieval operations.
+ **Agent evaluations** – Score agent runs offline with test suites and online on production traces, compare agent versions, and open the trace behind each result. For more information, see [Agent evaluations](observability-ai-evaluations.md).
+ **GenAI semantic conventions** – Use standardized OTel attributes such as `gen_ai.system`, `gen_ai.request.model`, and `gen_ai.usage.input_tokens` to describe AI-specific telemetry.
+ **Auto-instrumentation** – Automatically capture traces from popular AI frameworks and providers, including OpenAI, Anthropic, Amazon Bedrock, LangChain, and more than 20 additional libraries.
+ **PPL querying** – Query and aggregate trace data using Piped Processing Language (PPL) directly from OpenSearch UI.

## Architecture
<a name="observability-ai-architecture"></a>

Your agent produces traces and agent logs with any OpenTelemetry GenAI instrumentation, such as the built-in instrumentation of Strands Agents, or with the `@observe` decorator of the OpenSearch GenAI SDK. Your evaluation code produces evaluation results with the SDK. The SDK sends all three signals over OTLP, signed with SigV4, to an OpenSearch Ingestion pipeline. The pipeline writes each signal to its own index in an OpenSearch Service domain or an OpenSearch Serverless collection:
+ Spans go to `otel-v1-apm-span*` (`otel-v2-apm-span*` for an observability stack on a domain with the engine optimized for log analytics).
+ Agent logs go to `logs-otel-v1*`.
+ Evaluation results, which are log events named `gen_ai.evaluation.result`, go to `otel-v1-genai-evaluation*`.

OpenSearch UI reads these indexes. The Agent Traces pages show the traces with their logs, and the Evaluations pages show the evaluation results with a link to the trace that each result judged. The Logs pages show the agent logs on their own, so you can search them without opening a trace. The following diagram shows the agent and evaluation code sending these signals to the pipeline, the pipeline writing them to the three indexes, and OpenSearch UI reading them.

![Architecture diagram. Inside the OpenSearch GenAI SDK, your agent, instrumented with any OpenTelemetry GenAI instrumentation, sends OTLP traces and logs, and your evaluation code sends OTLP evaluation results, signed with SigV4, to an OpenSearch Ingestion pipeline. The pipeline writes spans to otel-v1-apm-span*, agent logs to logs-otel-v1*, and evaluation results to otel-v1-genai-evaluation*, in an OpenSearch Service domain or an OpenSearch Serverless collection. OpenSearch UI reads all three indexes for its Agent Traces, Evaluations, and Logs pages.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/ai-observability/ai-observability-architecture.png)

In the diagram, the OpenSearch GenAI SDK contains your agent and your evaluation code. The agent sends traces and logs, and the evaluation code sends evaluation results, to the OpenSearch Ingestion pipeline. The pipeline connects to three indexes inside the OpenSearch Service domain or OpenSearch Serverless collection: `otel-v1-apm-span*` for spans, `logs-otel-v1*` for agent logs, and `otel-v1-genai-evaluation*` for evaluation results. The domain or collection connects to OpenSearch UI, where the Agent Traces, Evaluations, and Logs pages read the data.

## Getting started
<a name="observability-ai-getting-started"></a>

This section walks you through instrumenting an AI agent, sending traces to Amazon OpenSearch Service, and viewing them in OpenSearch UI.

Agent tracing works with spans that follow the OpenTelemetry [semantic conventions for generative AI spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md). You don't need the OpenSearch GenAI SDK to send traces. You can instrument your agent with any of the following:
+ An agent framework with built-in OpenTelemetry instrumentation that follows these conventions, such as Strands Agents.
+ The OpenInference or OpenLLMetry (Traceloop) instrumentation libraries. The `otel_traces` processor in your pipeline maps their attributes to `gen_ai.*` attributes.
+ The OpenSearch GenAI SDK, which also signs requests to the pipeline with SigV4.

OpenSearch Ingestion accepts only SigV4-signed requests. If you don't use the SDK, send your traces through an OpenTelemetry Collector with the `sigv4auth` extension. For more information, see [Using an OpenSearch Ingestion pipeline with OpenTelemetry Collector](configure-client-otel.md). The following procedures use the SDK.

### To install the SDK
<a name="observability-ai-install-sdk"></a>

Install the OpenSearch GenAI SDK and the OpenTelemetry instrumentation package for your LLM provider. The following example installs the Python SDK with the OpenAI instrumentation.

```bash
pip install "opensearch-genai-observability-sdk-py>=0.3.0" opentelemetry-instrumentation-openai-v2
```

For TypeScript, install `@opensearch-project/genai-observability-sdk-ts` instead.

### To instrument your agent code
<a name="observability-ai-instrument"></a>

The OpenSearch GenAI SDK is built on OpenTelemetry and the GenAI semantic conventions. It works in three parts:
+ `register()` sets up the trace and log exporters, signs them with SigV4 for OpenSearch Ingestion, and turns on every installed OpenTelemetry instrumentation package, so LLM calls are traced without code changes.
+ The `@observe` decorator records your agent and tool functions as `invoke_agent` and `execute_tool` spans.
+ `enrich()` adds GenAI attributes, such as the model and the agent version, to the current span.

The following Python code example traces an agent and its tool. Replace the placeholder values with your own.

```python
from opensearch_genai_observability_sdk_py import Op, enrich, observe, register

register(
    service_name="travel-assistant",
    traces_endpoint="https://{{pipeline-endpoint}}/{{traces-path}}",
    logs_endpoint="https://{{pipeline-endpoint}}/{{logs-path}}",
    sigv4={"service": "osis", "region": "{{region}}"},
)

# weather_api() and call_llm() are your own tool and LLM code.
@observe(op=Op.EXECUTE_TOOL)
def get_weather(city: str) -> str:
    return weather_api(city)

@observe(name="Travel Assistant", op=Op.INVOKE_AGENT)
def run_agent(prompt: str) -> str:
    enrich(model="gpt-4o", provider="openai", agent_version="1.0.0")
    weather = get_weather("Paris")
    return call_llm(prompt, weather)  # traced by the OpenAI instrumentation
```

The SDK works with any agent framework, such as Strands Agents, LangGraph, CrewAI, the OpenAI Agents SDK, and Amazon Bedrock Agents. The same SDK also records evaluation results next to the traces. For more information, see [Agent evaluations](observability-ai-evaluations.md). For a runnable example for each framework, see [Framework integrations](https://observability.opensearch.org/docs/send-data/ai-agents/integrations/) in the OpenSearch observability stack documentation.

**Note**
When you send traces to Amazon OpenSearch Service, use your OpenSearch Ingestion pipeline endpoint with SigV4 authentication instead of a localhost endpoint. For more information about configuring OpenSearch Ingestion pipelines, see [Overview of Amazon OpenSearch Ingestion](ingestion.md).

### To view traces in OpenSearch UI
<a name="observability-ai-view-traces"></a>

After your instrumented application sends trace data, you can explore it in OpenSearch UI. Open your observability workspace. In the left navigation, under **Agent Monitoring**, choose **Traces**.

## Agent tracing UI
<a name="observability-ai-agent-tracing"></a>

The Agent Traces page in OpenSearch UI provides a purpose-built interface for exploring, debugging, and monitoring LLM agent execution traces. It gives developers and platform operators full observability into agentic AI applications, including hierarchical trace views, detail flyouts, flow visualizations, and aggregate metrics.

### Prerequisites
<a name="observability-ai-prereqs"></a>

Before you use Agent Traces, make sure you have the following:
+ An OpenSearch Service domain or an OpenSearch Serverless collection with trace data indexed in `otel-v1-apm-span*` indices.
**Note**
On a domain with the engine optimized for log analytics, an observability stack stores spans in `otel-v2-apm-span*` indexes instead.
+ OpenTelemetry instrumentation with GenAI semantic conventions enabled in your LLM application.
+ OpenSearch Ingestion configured with the `otel_traces` processor to ingest spans into OpenSearch.
+ PPL query support enabled in OpenSearch UI.

### Required span attributes
<a name="observability-ai-span-attributes"></a>

Agent Traces requires specific span attributes to render trace data correctly. The following tables describe the core fields and GenAI-specific attributes.

**Core span fields**
Each span must include the following core fields:

| Field | Type | Description |
| --- | --- | --- |
| traceId | String | Unique identifier for the entire trace. |
| spanId | String | Unique identifier for this span. |
| parentSpanId | String | Identifier of the parent span. Empty for root spans. |
| startTime | Timestamp | Time when the span started. |
| endTime | Timestamp | Time when the span ended. |
| durationInNanos | Long | Duration of the span in nanoseconds. |
| status.code | Integer | Span status code (0 = unset, 1 = OK, 2 = error). |

**GenAI attributes**
The following `gen_ai.*` attributes enable AI-specific features in the Agent Traces UI:

| Attribute | Example value | Description |
| --- | --- | --- |
| gen\_ai.operation.name | chat | The type of GenAI operation. Determines the span category. |
| gen\_ai.system | openai | The AI system or provider. |
| gen\_ai.request.model | gpt-4 | The model used for the request. |
| gen\_ai.usage.input\_tokens | 150 | Number of input tokens consumed. |
| gen\_ai.usage.output\_tokens | 85 | Number of output tokens generated. |
| gen\_ai.response.finish\_reasons | ["stop"] | Reasons the model stopped generating. |

### Page layout and metrics bar
<a name="observability-ai-page-layout"></a>

The Agent Traces page displays a metrics bar at the top that summarizes key statistics across all visible traces. Metrics include total trace count, average duration, error rate, and token usage. These values update dynamically based on your time filter and query.

### Traces tab
<a name="observability-ai-traces-tab"></a>

The Traces tab lists all root agent traces that match your current query and time range. Each row represents a single agent invocation.

![Table displaying agent traces with columns for time, kind, name, status, latency, tokens, input, and output.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/agent-traces/traces-table.png)

The following table describes the columns in the traces table:

| Column | Description |
| --- | --- |
| Trace ID | Unique identifier for the trace. Choose the link to open the trace details flyout. |
| Agent name | Name of the agent that initiated the trace. |
| Status | Overall trace status (OK or Error). |
| Duration | Total time from the first span to the last span in the trace. |
| Spans | Total number of spans in the trace. |
| Input tokens | Total input tokens consumed across all LLM calls in the trace. |
| Output tokens | Total output tokens generated across all LLM calls in the trace. |
| Start time | Timestamp when the trace started. |

### Span categories
<a name="observability-ai-span-categories"></a>

Spans are categorized based on the `gen_ai.operation.name` attribute. Each category is displayed with a unique color and icon in the UI.

| Operation name | Category | Description |
| --- | --- | --- |
| invoke\_agent, create\_agent | Agent | Agent orchestration step. |
| chat | LLM | LLM chat completion call. |
| text\_completion, generate\_content | Content | Text generation operation. |
| execute\_tool | Tool | Tool invocation. |
| embeddings | Embeddings | Embedding generation. |
| retrieval | Retrieval | Data retrieval operation. |

### Spans tab
<a name="observability-ai-spans-tab"></a>

The Spans tab displays individual spans across all traces. You can filter and sort spans to find specific operations.

![Spans tab showing a table with columns for Time, Kind, Name, Status, Latency, Tokens, Input, and Output.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/agent-traces/spans-table.png)

### Trace details flyout
<a name="observability-ai-trace-details"></a>

When you choose a trace ID, a flyout panel opens with two main areas:
+ **Left panel** – Displays the trace tree, which shows the hierarchical parent-child relationships between spans. It also includes a flow DAG (directed acyclic graph) that visualizes the execution path of the agent.
+ **Right panel** – Contains two tabs. The **Detail** tab shows span attributes, resource attributes, and GenAI-specific metadata. The **Timeline** tab shows a waterfall chart of span durations and their timing relationships.

### Querying traces
<a name="observability-ai-querying"></a>

Agent Traces uses PPL (Piped Processing Language) for all data fetching. You can write queries in the query panel at the top of the page.

**Note**
The following examples query the `otel-v1-apm-span*` index. On a domain with the engine optimized for log analytics, an observability stack stores spans in `otel-v2-apm-span*`. For such a domain, use that index name instead.

**To list root traces**
The following query returns the 100 most recent root agent traces:

```
source = otel-v1-apm-span*
| where parentSpanId = "" AND isnotnull(`attributes.gen_ai.operation.name`)
| sort - startTime
| head 100
```

**To fetch all spans for a trace**
The following query returns the complete span tree for a specific trace:

```
source = otel-v1-apm-span*
| where traceId = "{{trace-id}}"
| head 1000
```

**To compute aggregate metrics**
The following query computes average duration and total token usage grouped by model:

```
source = otel-v1-apm-span*
| where isnotnull(`attributes.gen_ai.request.model`)
| stats avg(durationInNanos) as avg_duration,
        sum(`attributes.gen_ai.usage.input_tokens`) as total_input_tokens,
        sum(`attributes.gen_ai.usage.output_tokens`) as total_output_tokens
    by `attributes.gen_ai.request.model`
```
