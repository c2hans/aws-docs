---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/jaeger-data-source.html
---

# Connect to a Jaeger data source
<a name="jaeger-data-source"></a>

 The Jaeger data source provides open-source, end-to-end distributed tracing.

## Adding the data source
<a name="jaeger-adding-the-data-source"></a>

 To access Jaeger settings, choose the **Configuration** (gear) icon, then choose **Data Sources**, and then choose **Jaeger**.

|  Name  |  Description  |
| --- | --- |
|  Name  |  The data source name. This is how you see the data source in panels, queries, and Explore.  |
|  Default  |  Default data source means that it will be pre-selected for new panels.  |
|  URL  |  The URL of the Jaeger instance; e.g., http://localhost:16686.  |
|  Access  |  Server (default) = URL must be accessible from the Grafana backend/server.  |
|  Basic Auth  |  Enable basic authentication to the Jaeger data source.  |
|  User  |  User name for basic authentication.  |
|  Password  |  Password for basic authentication.  |

## Query traces
<a name="jaeger-query-traces"></a>

 You can query and display traces from Jaeger via Explore. For more information, see [Explore](explore.md).

 The Jaeger query editor allows you to query by trace ID directly or selecting a trace from trace selector. To query by trace ID, insert the ID into the text input.

 Use the trace selector to pick particular trace from all traces logged in the time range you have selected in Explore. The trace selector has three levels of nesting: 1. The service you are interested in. 1. Particular operation is part of the selected service. 1. Specific trace in which the selected operation occurred, represented by the root operation name and trace duration.

## Linking to the trace ID from logs
<a name="linking-trace-id-from-logs"></a>

 You can link to Jaeger trace from logs in Loki by configuring a derived field with internal link. For more information, see [Derived fields](using-loki-in-AMG.md#loki-derived-fields).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
