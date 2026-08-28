---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/paloalto-prismacloud-pipeline-setup.html
---

# CloudWatch pipelines configuration for Palo Alto Prisma Cloud
<a name="paloalto-prismacloud-pipeline-setup"></a>

Collects security data from Palo Alto Prisma Cloud using Access Key and Secret Key authentication through the CSPM and Compute APIs.

Configure the Palo Alto Prisma Cloud source with the following parameters:

```
source:
  paloaltonetworks_prismacloud:
    cspm_base_url: "https://api.prismacloud.io"
    compute_console_url: "https://us-east1.cloud.twistlock.com/us-1-123456789"
    compute_api_version: "33.01"
    authentication:
      oauth2:
        access_key: "${{aws_secrets:my-prismacloud-secret:username}}"
        secret_key: "${{aws_secrets:my-prismacloud-secret:password}}"
    range: "P30D"
```Parameters

`cspm_base_url` (required)
The base URL for the Prisma Cloud CSPM API, determined by your tenant region (for example, `https://api.prismacloud.io`).

`compute_console_url` (required)
The URL of the Prisma Cloud Compute Console (for example, `https://us-east1.cloud.twistlock.com/us-1-123456789`).

`compute_api_version` (required)
The Compute API version for your Prisma Cloud tenant (for example, `33.01`).

`authentication.oauth2.access_key` (required)
The Prisma Cloud Access Key ID, stored in AWS Secrets Manager.

`authentication.oauth2.secret_key` (required)
The Prisma Cloud Secret Key, stored in AWS Secrets Manager.

`range` (optional)
The historical time period for backfilling data. Uses ISO 8601 duration format. Minimum is `PT1H`, maximum is `P90D`. Default is `P30D`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
