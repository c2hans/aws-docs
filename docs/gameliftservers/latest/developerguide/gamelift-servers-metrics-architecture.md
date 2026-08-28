---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-servers-metrics-architecture.html
---

# How it works
<a name="gamelift-servers-metrics-architecture"></a>

The telemetry metrics system follows a simple four-stage data flow from your game servers to visualization dashboards.

**Collection:** Your game server, integrated with the GameLift Server SDK or plugin, automatically emits metrics to a local telemetry collector running on the same instance. The SDK captures both automatic metrics (server lifecycle, resource usage) and custom metrics you define in your code.

**Processing:** The telemetry collector aggregates metrics from your game server and combines them with instance-level performance data (CPU, memory, network, disk usage). This provides a complete picture of both your game's performance and the underlying infrastructure.

**Storage:** Processed metrics are exported to your choice of metrics warehouse - [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html) for high-performance time-series storage, Amazon CloudWatch for AWS service integration, or both. All data transmission is authenticated and encrypted.

**Visualization:** [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html) connects to your metrics warehouse to display pre-built GameLift dashboards. These dashboards provide fleet overviews, server performance details, and container monitoring views that help you monitor and troubleshoot your game hosting infrastructure.

**Note**
All metric transmission between your game server and the telemetry collector occurs locally on the instance for security. Only the collector communicates with AWS services using proper authentication.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
