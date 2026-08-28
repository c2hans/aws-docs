---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/pingidentity-pingone-pipeline-setup.html
---

# CloudWatch pipelines configuration for PingIdentity PingOne
<a name="pingidentity-pingone-pipeline-setup"></a>

Collects audit logs from PingIdentity PingOne using OAuth2 authentication.

Configure the PingIdentity PingOne source with the following parameters:

```
source:
  pingidentity_pingone:
    range: "P7D"
    region: "NA"
    environment_id: "<your-environment-id>"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```Parameters

`range` (optional)
For pulling historical logs. Uses ISO 8601 duration format (for example, `P7D` for the last 7 days, `PT21H` for the last 21 hours). The default is 0 hours, and the maximum is 90 days.

`region` (optional)
PingOne region code (NA, EU, AP, AU, CA, SG). The default is "NA".

`environment_id` (required)
The PingOne environment ID.

`authentication.oauth2.client_id` (required)
OAuth2 client ID for PingIdentity PingOne API authentication.

`authentication.oauth2.client_secret` (required)
OAuth2 client secret for PingIdentity PingOne API authentication.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
