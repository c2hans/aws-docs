---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/datasources-opensearch-traces.html
---

# Traces support
<a name="datasources-opensearch-traces"></a>

The OpenSearch plugin has support for viewing a list of traces in table form, and a single trace in **Trace View**, which shows the timeline of trace spans.

**Note**
Querying OpenSearch traces is only available using Lucene queries.
Trace support is only available for Grafana workspaces that support version 9.4 or newer.

To create a query showing all traces, use the Lucene query type `Traces` with a blank query. If necessary, select the **Table** visualization type.

Selecting a trace ID in the table will open that trace in the trace view.

To create a query showing a single trace, use the query `traceid: {{{traceId}}}`, and, if necessary, select the **Traces** visualization type.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
