---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/windows-events-pipeline-setup.html
---

# CloudWatch pipelines configuration for Microsoft Windows Events
<a name="windows-events-pipeline-setup"></a>

Collects log data from Microsoft Windows Event logs using OAuth2 authentication.

Configure the Microsoft Windows Event source with the following parameters:

```
source:
  microsoft_windows:
    tenant_id: "<example-tenant-ID>"
    workspace_id: "<example-workspace-ID>"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```Parameters

`tenant_id` (required)
The Microsoft tenant ID for your organization.

`workspace_id` (required)
The Microsoft Log Analytics workspace ID.

`authentication.oauth2.client_id` (required)
OAuth2 client ID for Log Analytics workspace API authentication.

`authentication.oauth2.client_secret` (required)
OAuth2 client secret for Log Analytics workspace API authentication.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
