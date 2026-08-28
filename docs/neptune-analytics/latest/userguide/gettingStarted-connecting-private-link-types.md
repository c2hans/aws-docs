---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-connecting-private-link-types.html
---

# Types of interface endpoint services for Neptune Analytics
<a name="gettingStarted-connecting-private-link-types"></a>

 Neptune Analytics supports two services via interface VPC endpoints on AWS PrivateLink: `neptune-graph` for accessing Neptune Analytics control plane API operations like `CreateGraph`, `DeleteGraph` etc. and `neptune-graph-data` for accessing Neptune Analytics data plane API operations like `GetQuery`, `ListQueries`, `ExecuteQuery` etc. For more information about Neptune Analytics API operations see [Neptune Analytics APIs](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/Welcome.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
