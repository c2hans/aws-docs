---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-app-services.html
---

# Services

The Services view provides a centralized catalog of all instrumented services, displaying RED metrics (Rate, Errors, Duration) at a glance. You can use this view to quickly identify unhealthy services and drill into detail views for deeper analysis.

To access the Services view, navigate to the Observability workspace in OpenSearch UI and choose **APM** > **Services**.

The Services home page displays a table of all instrumented services along with summary panels. The following image shows the Services home page.

![Services page showing top services by fault rate, dependency paths, and service catalog with latency and throughput metrics.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/apm/services-home.png)

The following table describes the columns in the services table.

| Column | Description |
| --- | --- |
| Service name | The name of the instrumented service. |
| P99 latency | The 99th percentile latency for the service. |
| P90 latency | The 90th percentile latency for the service. |
| P50 latency | The 50th percentile (median) latency for the service. |
| Total requests | The total number of requests processed during the selected time range. |
| Failure ratio | The ratio of failed requests to total requests. |
| Environment | The deployment environment of the service, such as production or staging. |

The home page also includes the following summary panels:
+ **Top services by fault rate** – Services with the highest percentage of 5xx responses.
+ **Top dependency paths by fault rate** – Service-to-service dependency paths with the highest fault rates.

You can filter the services table by using the following filters:
+ **Environment** – Filter by deployment environment.
+ **Latency** – Filter by latency range.
+ **Throughput** – Filter by request throughput range.
+ **Failure ratio** – Filter by failure ratio range.

## Service overview
<a name="observability-app-services-overview"></a>

To open the service detail view, select a service name in the services table. The Overview tab displays metric tiles and time-series charts for the selected service.

![Service overview dashboard showing throughput, fault rate, error rate, availability, and latency metrics for frontend service.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/apm/services-overview.png)

The Overview tab includes the following time-series charts:
+ **Latency by service dependencies** – P50, P90, and P99 latency broken down by downstream dependencies.
+ **Requests by operations** – Request volume for each operation of the service.
+ **Availability by operations** – Percentage of successful responses for each operation.
+ **Fault rate and error rate by operations** – Percentage of 5xx and 4xx responses for each operation.

## Operations
<a name="observability-app-services-operations"></a>

The Operations tab provides a per-operation breakdown for the selected service. You can sort the table by any column to identify problematic operations.

![Operations table showing POST /api/checkout with 50.0% availability, accompanied by request, error, and latency graphs.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/apm/service-operations.png)

The following table describes the columns in the operations table.

| Column | Description |
| --- | --- |
| Operation name | The name of the operation. |
| P50/P90/P99 latency | The 50th, 90th, and 99th percentile latency for the operation. |
| Total requests | The total number of requests for the operation during the selected time range. |
| Error rate | The percentage of requests that returned errors. |
| Availability | The percentage of successful responses for the operation. |

## Dependencies
<a name="observability-app-services-dependencies"></a>

The Dependencies tab displays the downstream services that the selected service calls.

![Dependencies tab showing checkout and product-reviews services with latency, requests, error rate, and availability metrics.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/apm/service-dependencies.png)

The following table describes the columns in the dependencies table.

| Column | Description |
| --- | --- |
| Dependency service | The name of the downstream service. |
| Remote operation | The operation called on the downstream service. |
| Service operations | The operations on the current service that call this dependency. |
| P99/P90/P50 latency | The 99th, 90th, and 50th percentile latency for the dependency path. |
| Total requests | The total number of requests to the dependency during the selected time range. |
| Error rate | The percentage of requests to the dependency that returned errors. |
| Availability | The percentage of successful responses from the dependency. |

## Correlations
<a name="observability-app-services-correlations"></a>

The service detail view provides in-context correlations that let you navigate from service metrics directly to related traces and logs. You can use correlations to investigate the root cause of latency spikes or error rate increases.

![Table showing correlated spans for POST /api/checkout operation with columns for Time, Status, HTTP Status, Kind, Operation, and Span ID.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/apm/service-span-correlations.png)

The following correlation options are available:
+ **View related traces** – Opens a filtered trace view for the selected service or operation.
+ **View related logs** – Opens a filtered log view for the selected service or operation.
+ **Filter by attributes** – Narrows correlation results by specific span attributes.
