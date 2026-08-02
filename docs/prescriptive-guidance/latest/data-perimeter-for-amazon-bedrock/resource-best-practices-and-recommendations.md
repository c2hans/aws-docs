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
