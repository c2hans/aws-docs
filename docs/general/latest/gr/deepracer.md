---
source_url: https://docs.aws.amazon.com/general/latest/gr/deepracer.html
---

# AWS DeepRacer endpoints and quotas
<a name="deepracer"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="deepracer_region"></a>

## Service quotas
<a name="quotas_deepracer"></a>

| Name | Default | Adjustable | Description |
| --- | --- | --- | --- |
| Cars | Each supported Region: 20 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/deepracer/quotas/L-47A52EC0)  | The maximum number of cars any account can have at same time. |
| Evaluation jobs | Each supported Region: 3 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/deepracer/quotas/L-E84DEF70)  | The maximum number of concurrent evaluation jobs in same account in the same region. |
| Training jobs | Each supported Region: 4 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/deepracer/quotas/L-B8B892E1)  | The maximum number of concurrent training jobs in same account in the same region. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query general` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
