---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/estimates-for-open-shift-to-aws-eks/phase-4-application-migration-execution.html
---

# Phase 4: Application migration execution
<a name="phase-4-application-migration-execution"></a>

**Considering migration** **scope of 1 cluster \| 100\+ applications. The following table represents the application migration execution effort.**

|
|
| Activity | Effort (Hours) |
| --- |--- |
| Manifest conversion (OpenShift to vanilla K8s) | 160 |
| Image migration to Amazon ECR | 80 |
| ConfigMaps and Secrets migration | 60 |
| Persistent volume migration and data transfer | 120 |
| Service and ingress reconfiguration | 80 |
| Role-Based Access Control (RBAC) and security context adjustments | 60 |
| Application deployment to Amazon EKS | 200 |
| Integration reconnection and validation | 120 |
| Smoke testing per application | 150 |
| Performance baseline validation | 80 |
| Issue resolution and troubleshooting | 160 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
