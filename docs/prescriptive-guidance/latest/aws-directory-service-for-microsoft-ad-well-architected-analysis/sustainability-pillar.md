---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-directory-service-for-microsoft-ad-well-architected-analysis/sustainability-pillar.html
---

# Sustainability pillar
<a name="sustainability-pillar"></a>

The sustainability pillar focuses on minimizing the environmental impacts of running cloud workloads. The following recommendations can help you meet the** **sustainability design principles and architectural best practices for AWS Managed Microsoft AD.

**Key focus areas**
+ Shared responsibility model for sustainability
+ Understanding impact
+ Maximizing utilization to minimize required resources and reduce downstream impacts

## Understand your impact
<a name="understand-your-impact"></a>
+ Track AWS Managed Microsoft AD metrics to understand the impact of its current consumption and any configuration changes you apply.

## Maximize utilization
<a name="maximize-utilization"></a>
+ Share your directory with other AWS accounts that include AWS services that need to access AWS Managed Microsoft AD. For more information, see [Tutorial: Sharing your AWS Managed Microsoft AD directory for seamless EC2 domain-join](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_directory_sharing.html) in the AWS Directory Service documentation.
+ Automate AWS Managed Microsoft AD scaling based on utilization metrics.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
