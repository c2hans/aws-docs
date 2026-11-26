---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability.html
---

# Observability stack in Amazon OpenSearch Service

An observability stack in Amazon OpenSearch Service is one place to watch your applications and AI agents, get alerted when something goes wrong, and go from a trace to the logs behind it. You name the stack. Everything it needs is created and connected for you.

An observability stack is not a separate service. It brings together existing Amazon OpenSearch Service capabilities for storage, ingestion, metrics, and visualization, already connected to each other. Each capability works the same way as when you set it up yourself, so the rest of this guide applies to a stack unchanged.

## What Amazon OpenSearch Service provides
<a name="observability-what"></a>

Amazon OpenSearch Service provides a unified observability solution by collecting, correlating, and visualizing three types of telemetry data:
+ **Logs** – Timestamped records of events.
+ **Traces** – End-to-end journey of requests through distributed services.
+ **Metrics** – Time-series data representing system health, through the Amazon Managed Service for Prometheus direct query integration.

By bringing these together in a single interface, Amazon OpenSearch Service helps operations teams, and developers detect, diagnose, and resolve issues faster.

## What an observability stack creates
<a name="observability-stack-creates"></a>

You create a stack from the Amazon OpenSearch Service console, which uses AWS CloudFormation to create the resources. Each stack is a CloudFormation stack named `ObsStack-{{stack-name}}` that creates the following resources in your account:
+ **Storage for logs and traces** – An Amazon OpenSearch Serverless collection, or an OpenSearch Service domain if you choose one.
+ **Ingestion** – An Amazon OpenSearch Ingestion pipeline with one OpenTelemetry Protocol (OTLP) endpoint for logs, metrics, and traces.
+ **Metrics** – An Amazon Managed Service for Prometheus workspace.
+ **User interface** – An OpenSearch UI application with an observability workspace that is already connected to the storage and the metrics workspace, with pre-built dashboards and saved queries.
+ **Demo workload (optional)** – An Amazon EC2 instance that runs the OpenTelemetry demo application and sends sample logs, metrics, and traces, so that you can see results right away.

The stack also creates the IAM roles for ingestion, metrics queries, and setup. For an Amazon OpenSearch Serverless collection, the stack also creates the encryption, network, and data access policies that the collection needs.

## How it works
<a name="observability-stack-how"></a>

The following diagram shows how telemetry flows through an observability stack. AI agents, services, and infrastructure send metrics, logs, and traces over OTLP to Amazon OpenSearch Ingestion. The pipeline stores logs and traces in OpenSearch and metrics in Amazon Managed Service for Prometheus. Users query both in OpenSearch UI, and AI agents can query them through an MCP server.

![OTLP telemetry flows through Amazon OpenSearch Ingestion into OpenSearch and Prometheus storage that OpenSearch UI queries.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/obs-stack/observability-stack-architecture.png)

1. **Create** – Name your stack and create it with recommended settings, or choose the storage backend yourself.

1. **Collect** – Send logs, metrics, and traces from your applications and AI agents to one OTLP endpoint.

1. **Store** – Logs and traces are stored in OpenSearch. On an Amazon OpenSearch Serverless collection, they are kept for 30 days by default. On an OpenSearch Service domain, the stack doesn't set a retention period. Metrics are stored in a Prometheus-compatible workspace. To compare the storage backends, see [Choose a storage backend](observability-get-started.md#obs-stack-create-backend).

1. **Observe** – Open OpenSearch UI for pre-built dashboards, queries across logs, metrics, and traces, agent traces, and alerting.

## Pricing
<a name="observability-stack-pricing"></a>

You pay for the resources that your stack creates, based on what the stack ingests, stores, and queries. The ingestion pipeline and the metrics workspace are billed separately from storage, and the demo workload is billed while it runs. For more information, see the following pricing pages:
+ [Amazon OpenSearch Service pricing](https://aws.amazon.com/opensearch-service/pricing/) – Covers the storage of the stack, which is an OpenSearch Service domain or an Amazon OpenSearch Serverless collection, and the Amazon OpenSearch Ingestion pipeline.
+ [Amazon Managed Service for Prometheus pricing](https://aws.amazon.com/prometheus/pricing/) – Covers the metrics workspace.
+ [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/) – Covers the instance that runs the optional demo workload.
