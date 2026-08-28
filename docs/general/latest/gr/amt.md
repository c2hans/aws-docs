---
source_url: https://docs.aws.amazon.com/general/latest/gr/amt.html
---

# Amazon Mechanical Turk endpoints and quotas
<a name="amt"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="amt_region"></a>

| Region | Endpoint | Protocol |
| --- | --- | --- |
| Sandbox endpoint for Amazon Mechanical Turk actions. | mturk-requester-sandbox.us-east-1.amazonaws.com | HTTPS |
| Production endpoint for Amazon Mechanical Turk actions. | mturk-requester.us-east-1.amazonaws.com | HTTPS |

## Service quotas
<a name="mturk_quotas"></a>

| Name | Default | Adjustable | Description |
| --- | --- | --- | --- |
| Monthly Usage | Each supported Region: 0.02 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/crowdscale-usagelimitservice/quotas/L-EC45676A)  | The maximum monthly spend in USD |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query general` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
