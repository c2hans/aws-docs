---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/drupal-core-pipeline-setup.html
---

# CloudWatch pipelines configuration for Drupal Core
<a name="drupal-core-pipeline-setup"></a>

Collects audit logs from Drupal Core using basic authentication.

Configure the Drupal source with the following parameters:

```
source:
  drupal_core:
    range: "P7D"
    domain: "<drupal-site-domain>"
    api_endpoint: "<drupal-api-endpoint>"
    authentication:
      basic:
        username: "${{aws_secrets:<secret-name>:username}}"
        password: "${{aws_secrets:<secret-name>:password}}"
```Parameters

`range` (optional)
For pulling historical logs. Uses ISO 8601 duration format (for example, `P7D` for the last 7 days, `PT21H` for the last 21 hours). The default is 0 hours, and the maximum is 90 days.

`domain` (required)
The domain name of the Drupal Core site.

`api_endpoint` (required)
The path of the Drupal Core audit logs API endpoint. Must start with `/` (for example, `/api/v1/audit-logs`).

`authentication.basic.username` (required)
The username for Basic Authentication.

`authentication.basic.password` (required)
The password for Basic Authentication.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
