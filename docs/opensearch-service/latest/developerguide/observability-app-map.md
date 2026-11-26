---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-app-map.html
---

# Application Map

The Application Map is an interactive topology visualization that OpenSearch Ingestion auto-generates from your trace data by using the `otel_apm_service_map` processor. The map displays services as nodes with directional edges that show communication patterns, overlaid with RED metrics (Rate, Errors, Duration).

To access the Application Map, navigate to the Observability workspace in OpenSearch UI and choose **APM** > **Application Map**.

The following image shows the Application Map.

![Application Map showing service dependencies with nodes for frontend-proxy, frontend, checkout, cart, currency, fraud-detection, email, mcp-server, weather-agent, and events-agent.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/apm/application-map.png)

The map displays the following RED metrics for each service:
+ **Rate** – Requests per second processed by the service.
+ **Errors** – Percentage of 4xx (errors) and 5xx (faults) responses.
+ **Duration** – P50 and P99 latency for the service.

The `otel_apm_service_map` processor generates these metrics and stores them in Amazon Managed Service for Prometheus through remote write.

The topology visualization represents services as nodes and communication direction as edges. Color coding indicates the health status of each service. The map updates automatically as OpenSearch Ingestion ingests new trace data.

## Grouping services
<a name="observability-app-map-groupby"></a>

You can group services by attributes such as programming language, team, or environment. When you select a group-by attribute, the map switches from a topology graph to a card grid view. Each card represents a group of services that share the same attribute value.

![Application Map showing services grouped by programming language including cpp, erlang, python, go, nodejs, rust, dotnet, java, ruby, and php with request and service counts.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/apm/groupby-attributes.png)

The available group-by attributes are determined by the `group_by_attributes` setting in the `otel_apm_service_map` processor configuration in OpenSearch Ingestion.

## Viewing node details
<a name="observability-app-map-node-details"></a>

To view details for a service, select a node on the map. A detail panel opens with the following sections.

![Application Map showing frontend service node selected with detail panel displaying health metrics, requests graph, and latency percentiles.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/apm/application-map-node-details.png)

The **Health** section displays the following summary metrics:
+ Total Requests
+ Total Errors 4xx
+ Total Faults 5xx

The **Metrics** section displays the following time-series charts:
+ Requests
+ Latency P50/P90/P99
+ Faults 5xx
+ Errors 4xx

Choose **View details** to navigate to the Services detail view for the selected service.

## Filtering the map
<a name="observability-app-map-filters"></a>

You can filter the Application Map by using the following filters:
+ **Fault rate** – Filter services by server-side fault rate (5xx).
+ **Error rate** – Filter services by client-side error rate (4xx).
+ **Environment** – Filter services by deployment environment.

The following image shows the map filtered by error rate.

![Application Map showing services filtered by fault rate greater than 5%, displaying frontend-proxy, frontend, weather-agent, travel-planner, and mcp-server services with request counts.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/apm/filter-by-error-rate.png)

## In-context correlations
<a name="observability-app-map-correlations"></a>

You can navigate from the topology view directly to related traces and logs. From any service node, the following correlation options are available:
+ **View related traces** – Opens a filtered trace view for the selected service.
+ **View related logs** – Opens a filtered log view for the selected service.
