---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/quotas.html
---

# Quotas
<a name="quotas"></a>

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

## Quotas for AWS services in this solution
<a name="quotas-for-aws-services-in-this-solution"></a>

Make sure you have sufficient quota for each of the [services implemented in this solution](architecture-details.md#aws-services-in-this-solution). For more information, refer to [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html). To see the service quotas for all AWS services in the documentation without switching pages, view the information in the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf#aws-service-information) page in the PDF instead.

## AWS WAF quotas
<a name="aws-waf-quotas"></a>

AWS WAF can block a maximum of 10,000 IP address ranges in Classless Inter-Domain Routing (CIDR) notation per IP match condition. Each list that this solution creates is subject to this quota. For more information, refer to [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html). As of version 3.0, this solution creates two IP sets to attach to each rule, one for IPv4 and one for IPv6.

AWS WAF allows a maximum of one request per second, per account, per AWS Region for API calls to any individual `Create`, `Put`, or `Update` action. If you make these API calls outside the solution, you might encounter an API throttling issue. To prevent the issue, we recommend avoiding running other applications that make these API calls in the same account and Region where this solution is deployed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Automations for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
