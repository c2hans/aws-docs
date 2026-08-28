---
source_url: https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-query-APIs.html
---

# Query using Prometheus-compatible APIs
<a name="AMP-onboard-query-APIs"></a>

Although using a tool such as [Amazon Managed Grafana](AMP-amg.md) is the easiest way to view and query your metrics, Amazon Managed Service for Prometheus also supports several Prometheus-compatible APIs that you can use to query your metrics. For more information about all the available Prometheus-compatible APIs, see [Prometheus-compatible APIs](AMP-APIReference-Prometheus-Compatible-Apis.md).

The Prometheus-compatible APIs use the Prometheus query language, PromQL, to specify the data that you want to return. For details about PromQL and its syntax, see [Querying Prometheus](https://prometheus.io/docs/prometheus/latest/querying/basics/) in the Prometheus documentation.

When you use these APIs to query your metrics, the requests must be signed with the AWS Signature Version 4 signing process. You can set up [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to simplify the signing process. For more information, see [aws-sigv4-proxy](https://github.com/awslabs/aws-sigv4-proxy).

Signing through AWS SigV4 proxy can be performed using `awscurl`. The following topic [Using awscurl to query Prometheus-compatible APIs](AMP-compatible-APIs.md) walks you through using `awscurl` to set up AWS SigV4.

**Topics**
+ [Use awscurl to query with Prometheus-compatible APIs](AMP-compatible-APIs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
