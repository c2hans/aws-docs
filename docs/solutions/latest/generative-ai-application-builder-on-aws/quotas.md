---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/quotas.html
---

# Quotas
<a name="quotas"></a>

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

## Quotas for AWS services in this solution
<a name="quotas-for-aws-services-in-this-solution"></a>

Make sure you have sufficient quota for each of the [services implemented in this solution](architecture-details.md#aws-services-in-this-solution). For more information, refer to [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

Use the following links to go to the page for that service. To view the service quotas for all AWS services in the documentation without switching pages, view the information in the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf#aws-service-information) page in the PDF instead.

## Amazon Bedrock AgentCore quotas
<a name="agentcore-quotas"></a>

For Agent Builder deployments, be aware of the following Amazon [Bedrock AgentCore service quotas](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/bedrock-agentcore-limits.html):

| Quota | US East (N. Virginia) | Other Regions |
| --- | --- | --- |
| Active Session workloads per account | 1000 | 500 |
| Total agents per account | 1,000 | 1,000 |
| Versions per account | 1,000 | 1,000 |
