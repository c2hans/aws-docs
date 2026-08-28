---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cisco-duo-pipeline-setup.html
---

# CloudWatch pipelines configuration for Cisco Duo
<a name="cisco-duo-pipeline-setup"></a>

Collects log data from Cisco Duo using HMAC authentication through the Duo Admin API.

Configure the Cisco Duo source with the following parameters:

```
source:
  cisco_duo:
    api_host: "api-XXXXXXXX.duosecurity.com"
    authentication:
      hmac:
        integration_key: "${{aws_secrets:<secret-name>:integration_key}}"
        secret_key: "${{aws_secrets:<secret-name>:secret_key}}"
    range: "P30D"
```Parameters

`api_host` (required)
The Duo API hostname for your organization (for example, `api-XXXXXXXX.duosecurity.com`).

`authentication.hmac.integration_key` (required)
The Duo Admin API integration key, stored in AWS Secrets Manager.

`authentication.hmac.secret_key` (required)
The Duo Admin API secret key, stored in AWS Secrets Manager.

`range` (optional)
The historical time period for backfilling data. Uses ISO 8601 duration format. Minimum is `PT1H`, maximum is `P180D`. Default is `P180D`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
