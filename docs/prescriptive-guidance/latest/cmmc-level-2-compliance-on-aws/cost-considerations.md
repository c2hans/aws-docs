---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cmmc-level-2-compliance-on-aws/cost-considerations.html
---

# Cost considerations
<a name="cost-considerations"></a>

The cost of implementing CMMC Level 2 controls on AWS depends on factors such as the number of accounts in your CUI boundary, the volume of monitored resources, data processing and storage volumes, and whether you deploy in AWS GovCloud (US) or commercial Regions. The most effective way to control costs is to tightly scope your CUI boundary. Every account, Amazon VPC, and resource inside the boundary increases monitoring costs and assessment complexity. The multi-account architecture in this guide is designed specifically to help minimize your boundary while maintaining comprehensive security coverage.

Use the [AWS Pricing Calculator](https://calculator.aws/) to estimate costs for your specific workload profile. Each service page linked in this guide includes current pricing details. Beyond AWS service costs, plan for C3PAO assessment fees, dedicated security and compliance engineering personnel, and consulting support if you lack internal CMMC expertise. Prices are subject to change. Additionally, your costs may vary depending on your AWS Region, AWS service quotas, and other factors related to your cloud environment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
