---
source_url: https://docs.aws.amazon.com/general/latest/gr/verified-access-service.html
---

# AWS Verified Access endpoints and quotas
<a name="verified-access-service"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="verified-access-endpoints"></a>

The API actions to manage AWS Verified Access resources (for example, Verified Access endpoints, Verified Access groups, and Verified Access trust providers) are part of the Amazon EC2 API. For more information, see [AWS Verified Access actions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/operation-list-verified-access.html) in the *Amazon EC2 API Reference*.

For the service endpoints for Amazon EC2, see [Amazon EC2 endpoints and quotas](ec2-service.md).

## Service quotas
<a name="verified-access-quotas"></a>

| Name | Default | Adjustable | Description |
| --- | --- | --- | --- |
|  Verified Access Instances  |  5  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-17A8BD20) |  The maximum number of Verified Access Instances that customers can create in the current Region.  |
|  Verified Access Groups  |  10  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-3829BC77) |  The maximum number of Verified Access Groups that customers can create in the current Region.  |
|  Verified Access Trust Providers  |  15  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-AF309E5E) |  The maximum number of Verified Access Trust Providers that customers can create in the current Region.  |
|  Verified Access Endpoints  |  50  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5D439CF7) |  The maximum number of Verified Access Endpoints that customers can create in the current Region.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query general` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
