---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cmmc-level-2-compliance-on-aws/design-a-multi-account-architecture-for-cmmc.html
---

# Design a multi-account architecture for CMMC
<a name="design-a-multi-account-architecture-for-cmmc"></a>

A well-designed multi-account strategy is one of the most effective ways to reduce the scope and complexity of your CMMC assessment. By isolating CUI workloads, shared services, and security functions into separate AWS accounts under AWS Organizations you create clear, assessor-friendly boundaries that map directly to CMMC scoping categories.

## Components of a multi-account architecture
<a name="components-of-a-multi-account-architecture"></a>

Organize your AWS environment into four account types under [AWS Organizations](https://aws.amazon.com/organizations/). This table describes each account and its role in your CMMC architecture.

|
|
| Account | Purpose | CMMC scoping category |
| --- |--- |--- |
| Management Account | AWS Organizations root. Service control policies (SCPs) enforce guardrails across all accounts. No workloads run here. | Security Protection Asset |
| CUI Workload Account(s) | Where CUI is processed, stored, and transmitted. Compute, storage, and application services operate here. This is the core of your assessment boundary. | CUI Asset |
| Shared Services Account | Centralized security services shared across the CUI boundary: AWS KMS key management, IAM Identity Center, shared Amazon VPC infrastructure. | Security Protection Asset |
| Security and Log Archive Account | Aggregates SPD: AWS Security Hub findings, CloudTrail logs, AWS Config evaluations, Amazon VPC Flow Logs. Protected by Amazon S3 Object Lock for immutability. Also serves as the evidence pipeline, transforming SPD into assessment-ready artifacts using Amazon Athena. | Security Protection Asset |

This architecture is intentionally straightforward. It provides the minimum number of accounts needed to achieve clear CUI boundary separation while maintaining centralized security visibility. You can extend it with additional workload accounts as your environment grows, but the four-account foundation covers the core requirements for most DIB organizations.

This figure shows the multi-account architecture in relation to CMMC scope and segmentation. The CUI boundary (red dashed border) wraps around your CUI Workload Account(s). The Management Account, Shared Services Account, and Security and Log Archive Account are Security Protection Assets that sit outside the CUI boundary but within your AWS Organizations structure, supporting the boundary with governance guardrails, centralized key management, aggregated security data, and evidence pipelines.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/cmmc-level-2-compliance-on-aws/images/guide-img/0fdea3e4-e685-4123-b5d4-00cba3e6b30c/images/d2689330-0eaa-46fa-9ef0-431c805db330.png)

Figure 1: CMMC Level 2 multi-account architecture on AWS.

1. The management account contains no workloads. Service control policies (SCPs) enforce guardrails across AWS Organizations.

1. SCP enforcement extends from the management account to the CUI workload accounts.

1. CUI enters the workload account through the sole sanctioned ingress, inspected by AWS WAF and AWS Network Firewall at the VPC perimeter.

1. AWS KMS in the shared services account exchanges key material with CUI workloads.

1. The CUI workload account sends security protection data (telemetry, findings, and logs) to the security and log archive account.

1. The security and log archive account retains an immutable audit trail and assessment-ready evidence.

## Management account
<a name="management-account"></a>

You should consider the management account in-scope for CMMC because it impacts the security of your organization and your CUI environment. We recommend that you use the management account only for tasks that can only be performed by that account. Store your AWS resources in other accounts in the organization and keep them out of the management account. One important reason for this is that AWS Organizations SCPs do not restrict users or roles in the management account.

## CUI workload account
<a name="cui-workload-account"></a>

Your CUI application accounts are a highly sensitive part of your CMMC infrastructure. This is where you host workloads that store, process, or transmit CUI. System components in these accounts can bring other resources in scope, meaning that resources these accounts connect to have the potential to be considered in-scope regardless of the data involved. Highly restrict communication to and from these accounts to only the necessary resources in other accounts, based on system management or business requirements.

The general resource types hosted in these accounts include:
+ Compute and network resources that receive or transmit CUI from and to external entities
+ Compute resources that process CUI
+ Resources that store CUI at rest
+ Resources that establish network or application-level connections to the preceding resources

## Shared services account
<a name="shared-services-account"></a>

This account supports the services that multiple workloads use to deliver their outcomes, including IAM Identity Center for federated access, AWS KMS for centralized key management, and shared Amazon VPC infrastructure. To maintain separation of duties, keep the shared services account separate from the security and log archive account.

## Security and log archive account
<a name="security-and-log-archive-account"></a>

This account serves a dual purpose. First, it acts as the audit trail consolidation point for SPD collected from the accounts in the organization, including the CUI Workload accounts. This includes CloudTrail logs, AWS Config evaluations, Security Hub findings, Amazon VPC Flow Logs, and Amazon Inspector reports. The log data housed in this account is immutable and protected from being changed or deleted using Amazon S3 Object Lock in compliance mode.

Second, this account hosts the automated evidence pipeline that transforms SPD into assessment-ready artifacts. Amazon Athena runs queries to extract control-specific evidence, and results land in an Amazon S3 evidence repository organized by the control family and assessment objective.

This account is also typically one that has been delegated access from services like Security Hub and GuardDuty for centralized management of your security posture tooling in your AWS organization.

Resrtrict access to this account to read-only for specific roles or users who consume data for auditing, security analysis, and troubleshooting. This helps limit who needs to access your CUI workload account.

## Service control policies
<a name="service-control-policies"></a>

SCPs on the Management Account enforce baseline guardrails across all other accounts in your organization. At minimum, implement these deny policies:
+ Deny disabling or modifying CloudTrail organization trails
+ Deny disabling or modifying AWS Config recording
+ Deny deletion of Amazon S3 Object Lock configurations on log archive buckets
+ Deny disabling GuardDuty, Security Hub, or Amazon Inspector
+ Deny creation of resources outside approved regions
+ Deny use of non-FIPS endpoints within CUI boundary accounts (for commercial region deployments)
+ Deny removal of encryption on Amazon S3 buckets and Amazon EBS volumes in CUI accounts

SCPs and IAM policies work in tandem to define granular access controls, specifying who can access specific resources within accounts. This account-level isolation can be changed only by establishing explicit communication channels between resources in separate accounts, helping prevent accidental scope creep.
