---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/obs-stack-use.html
---

# Use and manage your observability stack

When a stack is created, its workspace in OpenSearch UI is ready to use. This topic describes what is set up for you and where each task is documented.

If the stack includes the demo workload, sample logs, metrics, and traces appear in the workspace within a few minutes after the stack is created. The demo workload is an optional Amazon EC2 instance that runs the OpenTelemetry demo application. For more information, see [Start, stop, or open the demo workload](#obs-stack-manage-demo).

## What is set up for you
<a name="obs-stack-use-setup"></a>

Workspace
An observability workspace, with the stack's storage and its Prometheus workspace already attached as data sources.

Datasets
For logs (`logs-otel-v1*`), traces (`otel-v1-apm-span*`, or `otel-v2-apm-span*` on a domain that uses the engine optimized for log analytics), the service map (`otel-v2-apm-service-map*`), and agent evaluation results (`otel-v1-genai-evaluation*`). A stack that is created from template version 3.4.0 or later has the dataset for evaluation results.

Correlations
Traces are linked to their logs, and services are linked to their metrics by an application monitoring configuration that connects the trace and service map datasets to the Prometheus data source.

Saved queries
For error logs, agent invocations, tool executions, slow spans, and token usage.

Dashboards
An overview dashboard and an agent observability dashboard.

## Alert monitors that a stack creates
<a name="obs-stack-use-alerts"></a>

A stack that is created from template version 3.3.0 or later creates alert monitors, which you can see in its workspace. The version is the `TemplateVersion` output of the CloudFormation stack. The monitors have no notification actions. To add notifications, or to create your own monitors, see [Alerting and monitoring](observability-alerting-monitoring.md).

The following table lists the monitors and when a stack creates them.

| Monitor | Triggers when | Created for |
| --- | --- | --- |
| `Observability Stack - Cluster Health Red` | The health of the domain is red | Stacks with an OpenSearch Service domain |
| `OTel Demo - Checkout Errors` | Any trace from the `checkout` service arrived in the last 10 minutes (demo only: triggers while the demo workload runs) | Stacks with the demo workload |
| `OTel Demo - Payment Failures` | Any trace from the `payment` service arrived in the last 10 minutes (demo only) | Stacks with the demo workload, except stacks with a domain that uses the engine optimized for log analytics |
| `OTel Demo - Frontend Error Logs` | Any log arrived in the last 10 minutes (demo only) | Stacks with the demo workload |
| `OTel Demo - Slow Frontend Responses` | Any trace from the `frontend` service arrived in the last 10 minutes (demo only) | Stacks with the demo workload |
| `OTel Demo - Cart Service Errors` | Any trace from the `cart` service arrived in the last 10 minutes (demo only) | Stacks with the demo workload |

The monitors for the demo workload trigger on any matching data, not on errors. They trigger while the demo workload sends data, so that you can see alerts in the workspace without waiting for a failure.

The `AlertMonitors` output of the CloudFormation stack reports how many monitors were created and names any that were not, for example `5 of 6 ready (skipped: Observability Stack - Cluster Health Red)`. A monitor that can't be created doesn't stop the stack from being created.

## Where each task is documented
<a name="obs-stack-use-tasks"></a>

An observability stack is made of existing Amazon OpenSearch Service capabilities, so each task is documented where that capability is documented. Use the following table to find it.

| To do this | See |
| --- | --- |
| Open and manage the user interface, workspaces, and access | [Using OpenSearch UI in Amazon OpenSearch Service](application.md) |
| Search and filter logs | [Discover Logs](observability-analyze-logs.md) |
| Follow a request across services | [Discover Traces](observability-analyze-traces.md) |
| Query metrics | [Discover Metrics](observability-metrics.md) |
| Go from a trace to the logs behind it | [Correlations](observability-correlations.md) |
| Monitor services and view the service map | [Application monitoring](observability-app-monitoring.md) |
| Trace AI agent workflows: LLM calls, tool calls, and token usage | [AI observability](observability-ai.md) |
| Build and share dashboards | [Dashboards](observability-dashboards.md) |
| Query with Piped Processing Language (PPL) | [Querying logs using PPL](observability-analyze-logs.md#observability-logs-query-ppl) |
| Get alerted when something goes wrong | [Alerting and monitoring](observability-alerting-monitoring.md) |
| Detect anomalies | [Anomaly detection in Amazon OpenSearch Service](ad.md) |
| Investigate an issue with an AI agent | [Investigation Agent in Amazon OpenSearch Service](application-investigation-agent.md) |
| Query your observability data from your own AI agents | [Set up the AWS MCP Server](aws-mcp-server.md) and [Agentic Observability with MCP Apps](opensearch-observability-mcp-app.md) |
| Send data from your applications and infrastructure | [Send data to your observability stack](observability-get-started.md#obs-stack-send-data) |

## Manage your observability stack
<a name="obs-stack-manage"></a>

An observability stack is a AWS CloudFormation stack. You view it on the Amazon OpenSearch Service console, and you change or delete it by updating or deleting the CloudFormation stack.

### View a stack
<a name="obs-stack-manage-view"></a>

On the [Amazon OpenSearch Service console](https://console.aws.amazon.com/aos/home), under **Observability stack**, choose **Stacks**, and then choose the name of a stack. The stack's page shows its status, its OTLP endpoint, and a list of its components. Each component links to the console page that manages it.

### Change settings
<a name="obs-stack-manage-settings"></a>

The settings of a stack are parameters of its CloudFormation stack. To change one, update the stack in the CloudFormation console, keep the current template, and change the parameter. For more information, see [Update stacks directly](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-direct.html) in the *AWS CloudFormation User Guide*.

Which settings you can change depends on how the stack was created. A stack created with Standard create, or with Easy create without the demo workload, has a parameter for each setting. A stack created with Easy create and the demo workload has only the administrators as a parameter. The storage backend, and for a domain its engine, are always fixed when the stack is created. For the list of settings, see [Settings](obs-stack-reference.md#obs-stack-reference-parameters).

### Add or remove administrators
<a name="obs-stack-manage-admins"></a>

The `AdminRoleArns` parameter lists the IAM roles that administer the stack's OpenSearch UI application and can read and write its data. When you create a stack from the console, it contains the role that you were signed in with. To give another role access, update the stack and add the role's ARN to the list, separated by a comma.

### Start, stop, or open the demo workload
<a name="obs-stack-manage-demo"></a>

With the demo workload, you get sample logs, metrics, and traces in your stack without instrumenting anything. The demo workload is an Amazon EC2 instance (`t3.xlarge`) that runs the OpenTelemetry demo application. You are billed for the instance while it runs.
+ To stop it, update the stack and set the `DeployDemoWorkload` parameter to `false`. CloudFormation removes the instance.
+ To start it, update the stack and set the parameter to `true`.
+ A stack created with Easy create and the demo workload has no `DeployDemoWorkload` parameter.
+ The instance has no public endpoint. To open the demo application's own web page, use the command in the `DemoAccessHint` output of the CloudFormation stack. It forwards a local port to the instance through Session Manager, a capability of AWS Systems Manager.

### Delete a stack
<a name="obs-stack-manage-delete"></a>

To delete an observability stack, select it on the **Stacks** page of the [Amazon OpenSearch Service console](https://console.aws.amazon.com/aos/home) and choose **Delete**. The console opens the CloudFormation console, where you confirm the deletion. Deleting the stack deletes the resources that it created, including the stored logs, traces, and metrics.
