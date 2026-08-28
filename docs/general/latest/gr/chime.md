---
source_url: https://docs.aws.amazon.com/general/latest/gr/chime.html
---

# Amazon Chime endpoints and quotas
<a name="chime"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="chime_region"></a>

Amazon Chime has a single endpoint that supports HTTPS: service.chime.aws.amazon.com.

## Service quotas
<a name="limits_chime"></a>

The following table lists additional quotas for Amazon Chime rooms and memberships.

| Resource | Default |
| --- | --- |
| Rooms per account | 1,500 |
| Rooms per profile | 1,500 |
| Memberships per room | 1,000 |
| Memberships per profile | 1,000 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query general` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
