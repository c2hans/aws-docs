---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/estimates-for-open-shift-to-aws-eks/estimation-example.html
---

# Estimation example
<a name="estimation-example"></a>

The following worked example applies the estimation framework from the Migration lifecycle phases section to a specific scenario:

1 OpenShift cluster with 100\+ applications migrating to Amazon EKS. Use this as a reference template — *adjust values based on your environment*.

## Executive summary
<a name="executive-summary"></a>

**OpenShift to AWS EKS Migration** **Scope: 1 Cluster \| 100\+ Applications**

|
|
| Parameter | Details |
| --- |--- |
| Source Platform | OpenShift (1 Cluster) |
| Target Platform | AWS EKS |
| Application Count | 100\+ Applications |
| Base Effort Range: | 2,800 - 3,400 Hours |
| Estimated Duration | 16 - 20 Weeks |
| Recommended Team Size | 6 - 8 Members |

**Note**
The base effort range of 2,800–3,400 hours represents core migration activities. The grand total of approximately 4,255 hours includes 20% contingency reserve and 15% project management overhead applied to the base effort.

Refer to the following estimation breakdown.

## Assumptions and prerequisites
<a name="assumptions-and-prerequisites"></a>

The effort estimates provided in this guide are based on the following baseline assumptions. Deviations from these conditions will impact actual migration effort and timelines.

**Technical environment:**

1. Applications are containerized and running on OpenShift 4.x

1. Target AWS account is provisioned with required IAM permissions and service quotas

1. Network connectivity is established between source environments and AWS (for hybrid or on-premises migrations)

1. Migration approach is lift-and-shift with platform-specific adjustments; no major application refactoring required

**Organizational readiness:**

1. Business stakeholders are available for validation and sign-off activities

1. Team possesses foundational Kubernetes knowledge with limited Amazon EKS operational experience

1. Standard business hours are available for migration work, with flexibility for off-hours cutover windows as needed

If your environment differs from these assumptions, such as requiring application modernization, operating on OpenShift 3.x, or having teams with no Kubernetes experience, adjust effort estimates accordingly using the complexity multipliers and learning curve factors described in earlier sections.

## Application complexity breakdown
<a name="application-complexity-breakdown"></a>

Based on a typical enterprise distribution for 100\+ applications:

|
|
| Complexity Tier | Count (Estimated) | Effort Per App | Total Hours |
| --- |--- |--- |--- |
| Simple | 40 apps | 8-12 hours | 320-480 |
| Moderate | 35 apps | 16-24 hours | 560-840 |
| Complex | 20 apps | 32-48 hours | 640-960 |
| High Risk / Critical | 8 apps | 56-72 hours | 448-576 |

**Complexity Tier Definitions**

**Simple Applications**
+ Stateless services
+ Standard Kubernetes manifests
+ No custom operators
+ Minimal external dependencies
+ Examples: Static APIs, utility services, batch jobs

**Moderate Applications**
+ Some stateful components
+ ConfigMaps and Secrets dependencies
+ Standard persistent volume requirements
+ 2-3 external integrations
+ Examples: Backend services with database connections, queue consumers

**Complex Applications**
+ Custom operators or CRDs
+ Advanced networking requirements
+ Multiple persistent volumes
+ Heavy integration dependencies
+ Custom security contexts
+ Examples: Data processing pipelines, middleware services

**High Risk / Critical Applications**
+ Business critical with strict SLAs
+ Zero or near-zero downtime requirements
+ Complex state management
+ Undocumented legacy configurations
+ Requires extensive rollback planning
+ Examples: Payment services, core APIs, customer-facing applications
