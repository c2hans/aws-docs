---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

This section describes the [cost](cost.md), [network security](security-1.md), [quotas](quotas.md), and other considerations prior to deploying the guidance.

## Supported AWS Regions
<a name="supported-aws-regions"></a>

This guidance uses AWS services that are not currently available in all AWS Regions. You must launch this guidance in an AWS Region where Amazon Lex is available. See the [services implemented in this guidance](architecture-details.md#aws-services-in-this-solution) for more details on core services needed for the guidance. Note that the guidance is not supported in AWS GovCloud (US) or China Regions. For the most current availability by Region, see the [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) list.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for QnABot on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
