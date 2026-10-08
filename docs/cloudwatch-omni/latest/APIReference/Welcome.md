---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

CloudWatch Omni is an AI-powered observability experience in Amazon CloudWatch for your applications and AI agents — either alone, or together. You reach Omni through a dedicated URL for your organization and sign in with the identities you already manage; Omni is accessible outside of the AWS Management Console.

 **Your applications and your agents, together.** Omni is built on OpenTelemetry. Telemetry you already send to CloudWatch appears in Omni with nothing to reconfigure, and any other workload you instrument with OpenTelemetry sends its telemetry to an OpenTelemetry Protocol (OTLP) endpoint. Work in the Omni web UI, or in the IDE extension for VS Code, Kiro, and Cursor while you develop AI agents.

 **Answers before you build a query.** Omni discovers your services and their dependencies from your telemetry and reports the RED metrics — the request rate, errors, and duration — of each one, without manual configuration. Ask a question in plain language and Omni writes the query for you, in SQL or PromQL (Prometheus Query Language). The Omni agent is Omni's built-in AI assistant, and it answers those questions from your own telemetry. When an alert fires, you can start an investigation with the AWS DevOps Agent to find the root cause. Alerts reach your team in Slack, or any destination of your choice through Amazon Simple Notification Service (Amazon SNS).

 **Quality signals for agents, alongside the operational ones.** Omni scores your agents' responses with evaluators — continuously in production, and on demand against a dataset. This catches the failure no error rate shows: an agent can return a well-formed response that is wrong. The scores appear alongside latency, errors, and token usage on the same trace. You can bring your own evaluators, including custom criteria scored by a judge model.

 **How CloudWatch Omni is organized**

Three concepts determine where your telemetry lives and who can reach it.
+  **Domain** — your organization's entry point. You choose a domain name during setup, and that name becomes your team's sign-in URL, in the format `https://<domain-name>.cloudwatch-omni.global.app.aws`. Setup also creates a domain ID, which identifies your domain at sign-in and in programmatic requests. Record both values. Your identity provider connects at the domain, not per space. See *Set up Omni*.
+  **Space** — where you work. A space gives you access to telemetry from the account and Region in which the space is hosted, and controls who can see it. Because a space maps to one account and Region, that boundary is what separates spaces, rather than a filter applied when you query. You create a space inside your domain, and one domain can contain multiple spaces. To observe multiple accounts or Regions, see *Set up a space*.
+  **CloudWatch Dataset** — how Omni brings your telemetry together. A Dataset makes your logs, metrics, and traces queryable and correlated across signals in one place. Data ingestion and storage management remains via existing CloudWatch endpoints and resources (for example, log groups). Enabling Omni creates one Dataset for your space.

 **How Omni relates to CloudWatch**

Omni is an interface and set of workflows built on Amazon CloudWatch. It is not a replacement, and enabling it does not change anything you already run.
+  **Built on CloudWatch data.** Omni reads from the same CloudWatch data stores you use today. Your existing console pages, metrics, alarms, dashboards, Logs Insights queries, and APIs keep working unchanged.
+  **No re-instrumentation.** Instrumentation you already run — the CloudWatch agent, OTLP pipelines, and AWS SDKs — keeps sending telemetry without changes, and that telemetry appears in Omni.
+  **Centralization stays with CloudWatch.** Omni does not aggregate telemetry across accounts and Regions on its own. Telemetry you centralize with CloudWatch centralization rules appears in your space like any other telemetry. See *Set up a space*.

You continue to configure how telemetry is collected and stored — log groups, retention, and ingestion endpoints — in the CloudWatch console.

This document was last published on October 7, 2026.
