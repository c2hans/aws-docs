---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/estimates-for-open-shift-to-aws-eks/phase-3-ci-cd-pipeline-migration.html
---

# Phase 3: CI/CD pipeline migration
<a name="phase-3-ci-cd-pipeline-migration"></a>

**Considering migration** **scope of 1 cluster \| 100\+ applications. The following table represents the CI/CD setup effort.**

|
|
| Activity | Effort (Hours) |
| --- |--- |
| Pipeline inventory and analysis | 16 |
| Build pipeline modifications for Amazon ECR | 40 |
| Deployment pipeline updates for Amazon EKS | 56 |
| GitOps setup (ArgoCD / Flux) if applicable | 48 |
| Pipeline testing and validation | 40 |
| Rollback mechanism configuration | 24 |
| Documentation and runbook updates | 16 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
