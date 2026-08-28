---
source_url: https://docs.aws.amazon.com/general/latest/gr/tnb.html
---

# AWS Telco Network Builder endpoints and quotas
<a name="tnb"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="tnb_endpoints"></a>

| Region Name | Region | Endpoint | Protocol |
| --- | --- | --- | --- |
| US East (N. Virginia) | us-east-1 |  tnb.us-east-1.amazonaws.com  | HTTPS |
| US West (Oregon) | us-west-2 |  tnb.us-west-2.amazonaws.com  | HTTPS |
| Asia Pacific (Seoul) | ap-northeast-2 |  tnb.ap-northeast-2.amazonaws.com  | HTTPS |
| Asia Pacific (Sydney) | ap-southeast-2 |  tnb.ap-southeast-2.amazonaws.com  | HTTPS |
| Canada (Central) | ca-central-1 |  tnb.ca-central-1.amazonaws.com  | HTTPS |
| Europe (Frankfurt) | eu-central-1 |  tnb.eu-central-1.amazonaws.com  | HTTPS |
| Europe (Paris) | eu-west-3 |  tnb.eu-west-3.amazonaws.com  | HTTPS |
| Europe (Spain) | eu-south-2 |  tnb.eu-south-2.amazonaws.com  | HTTPS |
| Europe (Stockholm) | eu-north-1 |  tnb.eu-north-1.amazonaws.com  | HTTPS |
| South America (São Paulo) | sa-east-1 |  tnb.sa-east-1.amazonaws.com  | HTTPS |

## Service quotas
<a name="limits_tnb"></a>

| Name | Default | Adjustable | Description |
| --- | --- | --- | --- |
| Concurrent ongoing network service operations | Each supported Region: 40 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/tnb/quotas/L-81A3E723)  | The maximum number of concurrent ongoing network service operations in one Region. |
| Function packages | Each supported Region: 200 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/tnb/quotas/L-08069DBD)  | The maximum number of function packages in one Region. |
| Network packages | Each supported Region: 40 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/tnb/quotas/L-3328748B)  | The maximum number of network packages in one Region. |
| Network service instances | Each supported Region: 800 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/tnb/quotas/L-C92FB107)  | The maximum number of network service instances in one Region. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query general` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
