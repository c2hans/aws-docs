---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-dual-stack.html
---

# Connect to Amazon SNS using Dual-stack (IPv4 and IPv6) endpoints
<a name="sns-dual-stack"></a>

 Dual-stack endpoints support both IPv4 and IPv6 traffic. When you make a request to a dual-stack endpoint, the endpoint URL resolves to an IPv4 or an IPv6 address. For more information on dual-stack and FIPS endpoints, see the [SDK Reference guide](https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html).

 Amazon SNS supports Regional dual-stack endpoints, which means that you must specify the AWS Region as part of the endpoint name. Dual-stack endpoint names use the following naming convention: `sns.{{Region}}.amazonaws.com`. For example, the dual-stack endpoint name for the `eu-west-1` Region is `sns.{{eu-west-1}}.amazonaws.com`.

For the full list of Amazon SNS endpoints, see the [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/sns.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
