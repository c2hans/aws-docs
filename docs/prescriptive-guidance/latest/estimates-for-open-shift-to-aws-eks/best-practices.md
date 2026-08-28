---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/estimates-for-open-shift-to-aws-eks/best-practices.html
---

# Best practices
<a name="best-practices"></a>

**General best practices:**
+ Work backwards from workload requirements to design well-architected clusters
+ Maintain parity between production and non-production environments
+ Create Architectural Decision Records (ADRs) for key decisions
+ Separate one-way door decisions (irreversible) from two-way door decisions (reversible)
+ Add 15% for project management overhead and 10-20% risk buffer
+ Ensure Kubernetes version compatibility (Amazon EKS doesn't support alpha features)

**Related resources **

1. [What is Red Hat OpenShift Service on AWS](https://docs.aws.amazon.com/rosa/latest/userguide/what-is-rosa.html)

   Overview of ROSA architecture and capabilities

1. [Amazon EKS Best Practices Guide](https://docs.aws.amazon.com/eks/latest/best-practices/introduction.html)

   Operational best practices for running workloads on Amazon EKS

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
