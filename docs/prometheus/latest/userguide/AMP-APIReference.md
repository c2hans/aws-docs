---
source_url: https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference.html
---

# Amazon Managed Service for Prometheus API Reference
<a name="AMP-APIReference"></a>

Amazon Managed Service for Prometheus offers two types of APIs:

1. **Amazon Managed Service for Prometheus APIs** – These APIs allow you to create and manage your Amazon Managed Service for Prometheus workspaces, including operations for workspaces, scrapers, alert manager definitions, rule groups namespaces, and logging. You use the AWS SDKs, available for various programming languages, to interact with these APIs.

1. **Prometheus-compatible APIs** – Amazon Managed Service for Prometheus supports HTTP APIs that are compatible with Prometheus. These APIs enable building custom applications, automate workflows, integrate with other services or tools, and query and interact with your monitoring data using the Prometheus query language (PromQL).

This section lists the API operations and data structures supported by Amazon Managed Service for Prometheus.

For information about quotas for the series, labels, and API requests, see [Amazon Managed Service for Prometheus service quotas](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP_quotas.html) in the *Amazon Managed Service for Prometheus User Guide*.

**Topics**
+ [Amazon Managed Service for Prometheus APIs](AMP-APIReference-AMPApis.md)
+ [Prometheus-compatible APIs](AMP-APIReference-Prometheus-Compatible-Apis.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
