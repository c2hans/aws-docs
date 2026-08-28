---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/netskope-pipeline-setup.html
---

# CloudWatch pipelines configuration for Netskope
<a name="netskope-pipeline-setup"></a>

Collects security events and alerts from Netskope using REST API v2 token-based authentication.

Configure the Netskope source with the following parameters:

```
source:
  netskope_cloudexchange:
    tenant_url: "<<your-tenant-url>>"
    range: "P7D"
    authentication:
      api_token: "${{aws_secrets:netskope-account-credentials:apiToken}}"
```Parameters

`tenant_url` (required)
Netskope tenant URL (for example, mycompany.goskope.com).

`authentication.api_token` (required)
REST API v2 token generated from the Netskope Service Account under RBACv3.

`range` (optional)
The time range for log collection. Uses ISO 8601 duration format (for example, `P7D` for the last 7 days, `PT21H` for 21 hours). Default is 0 hours, and the maximum is 90 days.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
