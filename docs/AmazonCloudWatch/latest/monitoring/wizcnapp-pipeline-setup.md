---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/wizcnapp-pipeline-setup.html
---

# CloudWatch pipelines configuration for WIZ
<a name="wizcnapp-pipeline-setup"></a>

Collects cloud-native application protection platform (CNAPP) data from Wiz using OAuth2 authentication.

Configure the Wiz CNAPP source with the following parameters:

```
source:
  wiz_cnapp:
    region: "<example-region>"
    range: "P7D"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```Parameters

`region` (required)
Wiz region for your organization.

`authentication.oauth2.client_id` (required)
OAuth2 client ID for Wiz API authentication.

`authentication.oauth2.client_secret` (required)
OAuth2 client secret for Wiz API authentication.

`range` (optional)
The time range for log collection. Uses ISO 8601 duration format (for example, `P7D` for the last 7 days, `PT21H` for 21 hours). Default is 0 hours, and the maximum is 90 days.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
