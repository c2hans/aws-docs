---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/proofpoint-tap-pipeline-setup.html
---

# CloudWatch pipelines configuration for Proofpoint TAP
<a name="proofpoint-tap-pipeline-setup"></a>

Collects email security event data from Proofpoint TAP using HTTP Basic authentication.

Configure the Proofpoint TAP source with the following parameters:

```
source:
  proofpoint_tap:
    authentication:
      basic:
        service_principal: "${{aws_secrets:proofpoint-tap-account-credentials:servicePrincipal}}"
        secret: "${{aws_secrets:proofpoint-tap-account-credentials:secret}}"
    range: "P1D"
```Parameters

`authentication.basic.service_principal` (required)
The Proofpoint TAP service principal for HTTP Basic authentication, stored in AWS Secrets Manager.

`authentication.basic.secret` (required)
The Proofpoint TAP secret for HTTP Basic authentication, stored in AWS Secrets Manager.

`range` (optional)
The historical time period for backfilling data. Uses ISO 8601 duration format. Minimum is `PT30S`, maximum is `P1D`. Default is `P1D`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
