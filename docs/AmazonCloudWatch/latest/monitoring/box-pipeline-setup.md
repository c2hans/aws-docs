---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/box-pipeline-setup.html
---

# CloudWatch pipelines configuration for Box
<a name="box-pipeline-setup"></a>

Collects enterprise events, user inventory, group inventory, group memberships, and group collaborations from Box using OAuth2 Client Credentials authentication.

Configure the Box source with the following parameters:

```
source:
  box:
    enterprise_id: "123456789"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:my-box-secret:client_id}}"
        client_secret: "${{aws_secrets:my-box-secret:client_secret}}"
```Parameters

`enterprise_id` (required)
The Box Enterprise ID (numeric). Found in the Box Admin Console under Account & Billing > Enterprise ID.

`authentication.oauth2.client_id` (required)
The OAuth2 Client ID from the Box Custom App. Stored in AWS Secrets Manager.

`authentication.oauth2.client_secret` (required)
The OAuth2 Client Secret from the Box Custom App. Stored in AWS Secrets Manager.

**Note**
The `client_id` and `client_secret` values are retrieved from AWS Secrets Manager. These credentials can be found in the Box Developer Console under your Custom App's Configuration tab.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
