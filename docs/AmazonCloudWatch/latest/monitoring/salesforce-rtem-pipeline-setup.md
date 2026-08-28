---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/salesforce-rtem-pipeline-setup.html
---

# CloudWatch pipelines configuration for Salesforce RTEM
<a name="salesforce-rtem-pipeline-setup"></a>

Collects real-time events from Salesforce using OAuth2 authentication.

Configure the Salesforce RTEM source with the following parameters:

```
source:
  salesforce_rtem:
    instance_url: "<<your-instance-url>>"
    org_id: "<<your-org-id>>"
    authentication:
      client_id: "${{aws_secrets:salesforce-credentials:client_id}}"
      client_secret: "${{aws_secrets:salesforce-credentials:client_secret}}"
```Parameters

`instance_url` (required)
Salesforce instance URL (for example, `https://myorg.my.salesforce.com`). Must use HTTPS.

`org_id` (required)
Salesforce organization ID (15 or 18 character alphanumeric).

`authentication.client_id` (required)
OAuth2 Consumer Key. Supports `${{aws_secrets:...}}`.

`authentication.client_secret` (required)
OAuth2 Consumer Secret. Supports `${{aws_secrets:...}}`.

`additional_topics` (optional)
Extra topics beyond the 19 defaults (CDC, custom Platform Events).

`replay_preset` (optional)
Controls where to start consuming events. Valid values: `LATEST`, `EARLIEST`. Default: `EARLIEST`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
