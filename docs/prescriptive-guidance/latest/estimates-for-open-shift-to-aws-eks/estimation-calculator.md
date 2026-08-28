---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/estimates-for-open-shift-to-aws-eks/estimation-calculator.html
---

# Migration lifecycle phases
<a name="estimation-calculator"></a>

Structure your OpenShift to Amazon EKS migration using a phased approach that aligns with standard software development lifecycle (SDLC) practices. Each phase requires specific activities and effort allocation.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/estimates-for-open-shift-to-aws-eks/images/guide-img/36464cc7-72e2-4e8c-8f01-a2dcd63a2843/images/c1f6dbc1-7acd-4e91-bd68-9a4f2e459be8.png)

The migration lifecycle includes the following phases:

1. Assessment phase – Discovery, workload inventory, and complexity analysis

1. Infrastructure setup – Amazon EKS cluster provisioning and AWS service configuration

1. Application migration – Workload containerization, manifest conversion, and deployment

1. Security and AWS Identity and Access Management (Amazon IAM) – Policy migration, Role-Based Access Control (RBAC) configuration, and access control implementation

1. Networking – Network policy translation, ingress configuration, and service mesh setup

1. Storage – Persistent volume migration and storage class configuration

1. CI/CD pipeline migration – Build and deployment pipeline reconfiguration for Amazon EKS

1. Monitoring and logging – Observability implementation with Amazon CloudWatch and related services

1. Testing – Functional validation, performance testing, and acceptance criteria verification

1. Cutover and go-live – Production migration execution and post-migration validation

**Per-workload effort breakdown**

The following sections provide detailed effort estimation guidance for each migration phase on a per-workload basis.

**Create a spreadsheet to track effort estimates for each of the following phases.**

## Assessment and discovery
<a name="assessment-discovery"></a>

The assessment phase establishes the foundation for accurate migration planning. Use the following templates to capture essential information during discovery activities. Complete documentation enables informed effort estimation and risk identification.

|
|
| Task | Base Hours | Your Input | Calculated(Base hr \* Number of resources) |
| --- |--- |--- |--- |
| Count total applications | 4 | No of apps | \_\_\_ hrs |
| Document namespaces | 2/namespace | No of ns | \_\_\_ hrs |
| List deployments/pods | 1/app | No of apps | \_\_\_ hrs |
| Catalog ConfigMaps | 0.5/map | No of maps | \_\_\_ hrs |
| Catalog Secrets | 0.5/secret | No of secrets | \_\_\_ hrs |
| Document PVCs | 1/pvc | No of pvcs | \_\_\_ hrs |
| Network policies audit | 2/policy | No of policies | \_\_\_ hrs |
| Routes/Ingress mapping | 1/route | No of routes | \_\_\_ hrs |
| ImageStreams inventory | 0.5/stream | No of streams | \_\_\_ hrs |
| BuildConfigs analysis | 2/config | No of configs | \_\_\_ hrs |
| **total ** |  |  | \_\_\_ hrs |

**Dependency mapping**

|
|
| Task | Hours | Complexity Factor | Notes |
| --- |--- |--- |--- |
| Inter-service dependencies | 4 per 10 apps | Low=1x, Med=1.5x, High=2.5x |  |
| External service integrations | 3 per integration |  |  |
| Database connections | 4 per database |  |  |
| Message queue connections | 3 per queue |  |  |
| Third-party API integrations | 2 per API |  |  |
| Shared storage dependencies | 4 per share |  |  |

## Infrastructure build-out
<a name="infrastructure-build-out"></a>

In some organizations, platform teams manage Amazon EKS cluster provisioning and infrastructure configuration independently from application migration activities. If your platform team handles infrastructure setup outside the migration project scope, exclude the cluster setup estimates provided in this section from your overall effort calculation.

**EKS cluster setup(optional)**

|
|
| Component | Simple | Standard | Production | Total Hours(Number \* Hr) |
| --- |--- |--- |--- |--- |
| Amazon Virtual Private Cloud (Amazon VPC) design | 8 | 16 | 32 |  |
| Amazon EKS cluster creation | 4 | 8 | 16 |  |
| Node groups config | 4 | 12 | 24 |  |
| Amazon IAM roles/policies | 8 | 24 | 48 |  |
| Security groups | 4 | 12 | 24 |  |
| Elastic Load balancer setup | 4 | 8 | 16 |  |
| DNS configuration | 2 | 4 | 8 |  |
| AWS Certificate Management | 4 | 8 | 16 |  |
| Cluster Autoscaler | 4 | 8 | 16 |  |
| Karpenter (if used) | 0 | 12 | 24 |  |

**Supporting infrastructure setup**

The following estimates apply when the listed infrastructure components are required for your migration. Include these effort allocations in your overall project estimate based on your specific infrastructure requirements.

|
|
| Component | Hours | Applicable? | Total Hours(if Y then calculate Hr) |
| --- |--- |--- |--- |
| Amazon Elastic Container Registry (Amazon ECR) Repository setup | 8 | Y/N |  |
| AWS Transit gateway (hybrid) | 24 | Y/N |  |
| Direct connect config | 40 | Y/N |  |
| VPN configuration | 16 | Y/N |  |
| PrivateLink setup | 12 per endpoint | Y/N  |  |
| Amazon S3 Buckets (logs/backups) | 4 | Y/N |  |
| AWS KMS Key setup | 8 | Y/N |  |
| AWS Secrets manager setup | 8 | Y/N |  |
| AWS Systems Manager (SSM) Parameter store migration | 4 \+ (0.25 × params) | Y/N |  |

## Application migration
<a name="application-migration"></a>

**Per-application effort matrix**

The following estimates correspond to the workload complexity tiers (t-shirt sizes) established during the discovery phase. Apply these effort ranges based on each application's assigned complexity category.

|
|
| App Type | Count | Hours/App | Total Hours |
| --- |--- |--- |--- |
| Stateless - Simple (no deps) | \_\_\_ | 8 |  |
| Stateless - Standard | \_\_\_ | 16 |  |
| Stateless - Complex (many deps) | \_\_\_ | 32 |  |
| Stateful - Simple | \_\_\_ | 24 |  |
| Stateful - Standard | \_\_\_ | 48 |  |
| Stateful - Complex | \_\_\_ | 80 |  |
| Legacy/Monolith | \_\_\_ | 120 |  |
| Custom Operators | \_\_\_ | 60 |  |

**OpenShift-specific conversions**

|
|
| Item | Count | Hours Each | Total |
| --- |--- |--- |--- |
| Route → Ingress conversion | \_\_\_ | 2 |  |
| DeploymentConfig → Deployment | \_\_\_ | 3 |  |
| BuildConfig → Pipeline | \_\_\_ | 8 |  |
| ImageStream → ECR migration | \_\_\_ | 2 |  |
| SCC → PSP/PSS migration | \_\_\_ | 6 |  |
| OpenShift Templates → Helm | \_\_\_ | 12 |  |
| oc commands → kubectl scripts | \_\_\_ | 4 |  |
| OAuth config migration | 1 | 16 |  |

## Storage migration
<a name="storage-migration"></a>

**Persistent volume migration**

Storage migration is a critical prerequisite for stateful application migrations. Complete storage class configuration, persistent volume provisioning, and data migration activities before migrating applications that depend on persistent storage.

|
|
| Storage Type | Volume Count | Size (GB) | Hours formula | Total hours |
| --- |--- |--- |--- |--- |
| Block (gp2/gp3) | \_\_\_ | \_\_\_ | 2 \+ (0.01 × GB) per vol |  |
| Amazon EFS/NFS shared | \_\_\_ | \_\_\_ | 8 \+ (0.02 × GB) per vol |  |
| Database (Amazon RDS migration) | \_\_\_ | \_\_\_ | 16 \+ (0.05 × GB) per db |  |
| Object (S3) | \_\_\_ | \_\_\_ | 4 \+ (0.001 × GB) |  |

**Storage class mapping**

|
|
| Task | Hours |
| --- |--- |
| Analyze current storage classes | 4 |
| Design Amazon EKS storage class mapping | 8 |
| Amazon EBS CSI driver setup | 4 |
| Amazon EFS CSI driver setup (if needed) | 8 |
| Test storage performance | 16 |
| Data validation procedures | 8 |

## Security and compliance
<a name="security-compliance"></a>

Security and compliance requirements are critical considerations for every organization. Carefully evaluate security controls, access policies, and regulatory requirements during migration planning.

**Recommended approach**: Engage security and compliance teams early in the planning process. Their involvement ensures that IAM policies, network security controls, encryption requirements, and audit logging configurations align with organizational security standards and regulatory obligations.

**Identity & access**

|
|
| Task | Base | Complexity | Total Hours |
| --- |--- |--- |--- |
| Role-Based Access Control (RBAC)mapping analysis | 16 |  |  |
| Role/ClusterRole conversion | 2 per role  |  |  |
| Service account migration | 1 per SA  |  |  |
| IAM Roles for Service Accounts (IRSA) configuration | 4 per app  |  |  |
| OpenID Connect (OIDC) provider setup | 8 |  |  |
| AD/LDAP integration | 24-40 |  |  |
| SSO reconfiguration | 16-32 |  |  |

**Security Policies**

|
|
| Task | Hours |
| --- |--- |
| Security Context Constraints (SCC) → Pod Security standards mapping | 16 |
| Network policy conversion | 2 per policy  |
| Open Policy Agent (OPA)/Gatekeeper policies | 4 per policy  |
| Image scanning setup (Amazon ECR) | 8 |
| Secrets encryption config | 8 |
| Audit logging setup | 12 |
| Compliance documentation | 24-40 |

## CI/CD pipeline migration
<a name="ci-cd-pipeline-migration"></a>

Most organizations have existing CI/CD pipelines that require reconfiguration to deploy applications to Amazon EKS. The following estimates cover integration effort for common CI/CD platforms and deployment workflow updates.

Refer to the following table to estimate effort based on your tooling.

**Pipeline Conversion**

|
|
| Source pipeline type | Count | Target | Hours Each | Total |
| --- |--- |--- |--- |--- |
| OpenShift pipelines  | \_\_\_ | Same Openshift | 8 |  |
| OpenShift pipelines  | \_\_\_ | AWS CodePipeline | 16 |  |
| Jenkins (on OpenShift) | \_\_\_ | Jenkins (EKS) | 12 |  |
| Jenkins (on OpenShift) | \_\_\_ | AWS CodePipeline | 24 |  |
| Custom buildConfigs | \_\_\_ | CodeBuild | 16 |  |
| GitLab CI | \_\_\_ | GitLab CI (reconfig) | 6 |  |
| GitHub Actions | \_\_\_ | GitHub Actions (reconfig) | 4 |  |

**Registry migration**

|
|
| Task | Hours |
| --- |--- |
| Amazon ECR setup & organization | 8 |
| Image migration script development | 16 |
| Image migration execution | 2 \+ (0.1 × image count) |
| Image signing setup | 12 |
| Pull secret configuration | 4 |
| Lifecycle policies | 4 |

## Observability stack
<a name="observability-stack"></a>

Organizations approach observability implementation in different ways. Some have existing monitoring stacks that require integration with Amazon EKS, while others need to establish observability infrastructure from the ground up. Use the following effort estimates based on your organization's current observability maturity.

**Monitoring**

|
|
| Current → Target | Hours |
| --- |--- |
| Prometheus (keep) → Prometheus (EKS) | 24 |
| Prometheus → Amazon Managed Prometheus | 32 |
| Prometheus → CloudWatch Container Insights | 40 |
| Grafana (keep) → Grafana (EKS) | 16 |
| Grafana → Amazon Managed Grafana | 24 |
| Dashboard migration | 2 per dashboard  |
| Alert rules migration | 1 per rule  |
| Custom metrics validation | 4 per app  |

**Logging**

|
|
| Current → Target | Hours |
| --- |--- |
| EFK → EFK on Amazon EKS | 24 |
| EFK → Amazon OpenSearch | 32 |
| EFK → CloudWatch Logs | 24 |
| Fluentd/Fluent Bit config | 16 |
| Log parsing rules migration | 8 |
| Retention policy config | 4 |

Implementing comprehensive observability requires effort beyond basic infrastructure setup. The estimates below reflect the work required to configure monitoring dashboards, centralized logging, and alerting systems for your migrated applications.

## Testing and validation
<a name="testing-validation"></a>

**Testing effort**

|
|
| Test Type | Base Hours | Per App Factor | Your Hours |
| --- |--- |--- |--- |
| Unit test validation | 8 | \+1 per app |  |
| Integration testing | 24 | \+2 per app |  |
| Performance baseline | 16 | \+4 per critical app |  |
| Performance validation | 24 | \+4 per critical app |  |
| Security scanning | 16 | \+1 per app |  |
| DR/Failover testing | 24 | \+4 per critical app |  |
| User Acceptance Testing (UAT)coordination | 40 | fixed |  |
| Regression testing | 16 | \+2 per app |  |

## Documentation and training
<a name="documentation-training"></a>

Documentation is an essential component of migration activities. Comprehensive documentation supports operational readiness, knowledge transfer, and long-term platform maintainability.

|
|
| Deliverable | Hours |
| --- |--- |
| Architecture documentation | 24-40 |
| Runbook creation | 4 per app  |
| Incident response procedures | 16 |
| Admin training (per person) | 8 people |
| Developer training (per person) | 4 people |
| Knowledge transfer sessions | 16 |

## Project management and coordination
<a name="project-management-coordination"></a>

|
|
| Activity | Formula |
| --- |--- |
| Project management | 15% of total technical hours |
| Stakeholder meetings | 4 hrs/week weeks |
| Change management | 8% of total technical hours |
| Risk management | 4% of total technical hours |
| Vendor coordination | 8 hrs/week weeks |

## Executive summary
<a name="executive-summery"></a>

Use the following summary table to consolidate effort estimates from each migration phase. This provides a comprehensive view of total project effort based on your specific requirements and workload complexity.

**Technical hours summary**

|
|
| Section | Hours |
| --- |--- |
| 1. Assessment & discovery |  |
| 2. Infrastructure build-out |  |
| 3. Application migration |  |
| 4. Storage migration |  |
| 5. Security & compliance |  |
| 6. CI/CD pipeline migration |  |
| 7. Observability stack |  |
| 8. Testing & validation |  |
| 9. Documentation & training |  |
| **Technical subtotal** |  |
| Adjustment factor (section 3.3) | ×1 |
| **Adjusted technical total** |  |

Add below Project Management effort as part of the migration effort.

|
|
| Category | Calculation | Hours |
| --- |--- |--- |
| Technical (adjusted) | from above |  |
| Project Management (15%) |  |  |
| Meetings |  |  |
| Change Management (8%) |  |  |
| Risk Buffer (10-20%) |  |  |
| **Grand Total** |  |  |

COST ESTIMATION (**Optional**)

Organizations often require cost projections for migration activities to support budget planning and approval processes. Use the following template to translate effort estimates into financial projections based on your team composition and resource rates.

|
|
| Role | Rate/Hr | Hours | Cost |
| --- |--- |--- |--- |
| Solution architect | $\_\_\_ |  |  |
| Platform engineer | $\_\_\_ |  |  |
| DevOps engineer | $\_\_\_ |  |  |
| Security engineer | $\_\_\_ |  |  |
| QA engineer | $\_\_\_ |  |  |
| Project manager | $\_\_\_ |  |  |
| **Total labor** |  |  |  |

Additional Costs

|
|
| Item | Monthly | Months | Total |
| --- |--- |--- |--- |
| Parallel environment | $\_\_\_ | \_\_\_ |  |
| Migration tools | $\_\_\_ | \_\_\_ |  |
| Training/certification |  |  |  |
| Contingency (15%) |  |  |  |

**Notes and assumptions**

1. Estimates assume team has basic Kubernetes experience

1. Add 30-50% if team is new to EKS

1. Add 20% if strict compliance requirements (PCI, HIPAA)

1. Subtract 20% if using Infrastructure as Code already

1. All hours are person-hours, not elapsed time

1. Does not include AWS infrastructure costs

1. Assumes standard business hours availability

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
