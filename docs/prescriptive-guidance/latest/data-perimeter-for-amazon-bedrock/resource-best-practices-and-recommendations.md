---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/resource-best-practices-and-recommendations.html
---

# Best practices and recommendations
<a name="resource-best-practices-and-recommendations"></a>

1. **Defense in depth**: Layer multiple controls (AWS KMS key policies, IAM, resource policies, encryption, tagging).

1. **Encryption context validation**: Use encryption context in AWS KMS key policies to ensure keys are only used for intended purposes.

1. **Regular audits**: Conduct monthly reviews of resource access patterns and policy effectiveness.

1. **Automated compliance**: Use AWS Config Rules to continuously monitor resource configurations.

1. **Incident response**: Establish procedures for responding to resource perimeter violations.

1. **Documentation**: Maintain detailed documentation of all resource classifications and access requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
