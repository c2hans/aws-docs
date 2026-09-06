---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cmmc-level-2-compliance-on-aws/how-aws-services-map-to-cmmc-level-2.html
---

# How AWS services map to CMMC Level 2
<a name="how-aws-services-map-to-cmmc-level-2"></a>

This section provides implementation guidance for the major NIST SP 800-171 control families. For each family, we identify the key AWS services, implementation patterns, and what your assessor will look for as evidence.

## Access Control (AC), 22 requirements
<a name="access-control-requirements"></a>

Access Control is the largest control family and receives significant assessor attention. Unauthorized access to CUI is among the highest-priority findings.

|  |  |  |
| --- |--- |--- |
| Requirement area | AWS implementation | Assessor evidence |
| Account management and least privilege | [IAM](https://aws.amazon.com/iam/) policies with least-privilege permissions. [ IAM Identity Center](https://aws.amazon.com/iam/identity-center/) for federated access with attribute-based access control (ABAC). IAM Access Analyzer to identify overly permissive policies. | IAM policy documents, IAM Access Analyzer findings, [IAM Identity Center](https://aws.amazon.com/iam/identity-center/) permission sets |
| Separation of duties | Separate IAM roles for administrators, operators, and auditors. Cross-account roles with explicit trust policies. | Role inventory showing distinct permission boundaries, CloudTrail role usage |
| Unsuccessful login attempts | IAM Identity Center lockout policies. [ CloudWatch](https://aws.amazon.com/cloudwatch/) alarms on ConsoleLogin failures. [ GuardDuty](https://aws.amazon.com/guardduty/) brute force findings. | CloudWatch alarm configuration, GuardDuty finding history, lockout policy documentation |
| Remote access | [Systems Manager ](https://aws.amazon.com/systems-manager/)Session Manager for administrative access (no SSH/RDP bastion required). VPN via [AWS Client VPN](https://aws.amazon.com/vpn/). | Session Manager audit logs in CloudTrail, VPN connection logs, network diagrams |
| CUI flow enforcement | Amazon VPC security groups and network access control lists (NACLs). [Network FirewallWS](https://aws.amazon.com/network-firewall/) for deep packet inspection. VPC endpoints for private API access. | Security group rules, Network Firewall policies, VPC endpoint configuration, Amazon VPC Flow Logs |

## Audit and Accountability (AU), 9 requirements
<a name="audit-and-accountability-requirements"></a>

Comprehensive audit logging with tamper-evident storage is foundational to CMMC. Assessors verify that you log all relevant events, protect those logs from modification, and can review and analyze them.

|  |  |  |
| --- |--- |--- |
| Requirement area | AWS implementation | Assessor evidence |
| Audit event logging | [CloudTrail](https://aws.amazon.com/cloudtrail/) organization trail capturing management and data events. Amazon VPC Flow Logs for network activity. Amazon S3 access logging. | CloudTrail trail configuration, event selectors, log file validation enabled |
| Audit log protection | Amazon S3 Object Lock (compliance mode) on log archive bucket. Separate Security and Log Archive Account with restricted access. SCPs preventing CloudTrail modification. | Object Lock configuration, bucket policy, SCP documents, IAM policies |
| Audit review and reporting | [Security Hub ](https://aws.amazon.com/security-hub/)dashboard with compliance scores. CloudWatch Logs Insights for ad-hoc queries. [Athena](https://aws.amazon.com/athena/) for cross-log analysis. | Security Hub screenshots, [Athena](https://aws.amazon.com/athena/) query history, documented review procedures |

By enabling CloudTrail as an organization trail and storing logs in a dedicated Security and Log Archive Account with Amazon S3 Object Lock, you create a tamper-evident audit trail that directly addresses the audit protection requirements C3PAO assessors validate. This pattern works in both GovCloud and commercial Regions.

## Configuration Management (CM), 9 requirements
<a name="configuration-management-requirements"></a>

Configuration management controls require baseline configurations, change tracking, and security configuration enforcement. These controls are well-suited to infrastructure as code (IaC) approaches on AWS.

|  |  |  |
| --- |--- |--- |
| Requirement area | AWS implementation | Assessor evidence |
| Baseline configurations | [CloudFormation](https://aws.amazon.com/cloudformation/) or Terraform templates defining approved configs. [AWS Config](https://aws.amazon.com/config/) recording all resource configurations. AWS Config conformance pack for CMMC 2.0 Level 2. | IaC templates, AWS Config resource inventory, conformance pack compliance dashboard |
| Change tracking | CloudFormation change sets with approval gates. AWS Config configuration timeline showing all changes. CloudTrail recording all API-driven changes. | Change set approval history, AWS Config timeline exports, CloudTrail change events |
| Security configuration enforcement | AWS Config rules evaluating security settings continuously. AWS Systems Manager State Manager for desired-state enforcement. SCPs preventing non-compliant configurations. | AWS Config rule evaluations, State Manager association status, SCP documents |

AWS provides a CMMC 2.0 Level 2 conformance pack for AWS Config that maps managed Config rules to CMMC controls. Deploying this conformance pack gives you continuous compliance evaluation and automated drift detection. The conformance pack is available in both GovCloud and commercial Regions.

## System and Communications Protection (SC), 16 requirements
<a name="system-and-communications-protection-requirements"></a>

SC controls mandate encryption of CUI at rest and in transit. These are among the controls the DoD considers critical, as failure to implement encryption can result in findings that block certification. CMMC Level 2 requires FIPS-validated cryptography for protecting CUI.

|  |  |  |
| --- |--- |--- |
| Requirement area | AWS implementation | Assessor evidence |
| Encryption at rest | [AWS KMS](https://aws.amazon.com/kms/) customer-managed keys in Shared Services Account. Amazon S3 default encryption (SSE-KMS). [ Amazon EBS](https://aws.amazon.com/ebs/) encryption by default. [A Amazon Relational Database Service ( ](https://aws.amazon.com/rds/)Amazon RDS) encrypted storage. | AWS KMS key policies, Amazon S3 bucket encryption settings, Amazon EBS encryption defaults, Amazon RDS configs |
| Encryption in transit | TLS 1.2\+ via [ACM](https://aws.amazon.com/certificate-manager/) certificates. FIPS-validated endpoints for all AWS API calls. AWS Network Firewall TLS inspection policies. | ACM certificate inventory, FIPS endpoint configuration, TLS policies |
| FIPS-validated cryptography | GovCloud: FIPS endpoints by default. Commercial: FIPS-specific endpoint URLs configured in SDK and application code. | Endpoint URL audit showing FIPS endpoints, SDK configuration files |
| Network boundary protection | Amazon VPC with public/private subnet separation. AWS Network Firewall at VPC perimeter. [AWS WAF](https://aws.amazon.com/waf/) on public-facing applications. VPC endpoints. | Amazon VPC architecture, AWS Network Firewall rules, AWS WAF rules, VPC endpoint configuration |
| Key management | AWS KMS key rotation enabled (annual). Key policies enforcing separation between administrators and users. CloudTrail logging all AWS KMS API calls. | Key rotation config, key policy documents, CloudTrail KMS events |

## Risk Assessment, Incident Response, and System Integrity
<a name="risk-assessment-incident-response-and-system-integrity"></a>

These families cover vulnerability management, incident handling, and system monitoring. They work together: Risk Assessment (RA) identifies issues, System and Information Integrity (SI) helps with timely remediation, and Incident Response (IR) handles incidents when they occur.

|  |  |  |
| --- |--- |--- |
| Requirement area | AWS implementation | Assessor evidence |
| Vulnerability scanning (RA) | [Amazon Inspector](https://aws.amazon.com/inspector/) for continuous scanning of [ Amazon EC2](https://aws.amazon.com/ec2/), containers, and [AWS Lambda](https://aws.amazon.com/lambda/). Amazon Inspector integrates with Security Hub. | Amazon Inspector findings dashboard, scan coverage report, remediation history |
| Vulnerability remediation (SI) | Systems Manager Patch Manager for automated patching. Systems Manager Compliance dashboard. [EventBridge](https://aws.amazon.com/eventbridge/) triggering remediation on critical findings. | Patch Manager compliance reports, remediation service-level agreement (SLA) tracking |
| Malicious code protection (SI) | GuardDuty malware scanning. Third-party endpoint protection via Systems Manager Distributor. [ Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) (Amazon ECR) image scanning via Amazon Inspector. | GuardDuty findings, endpoint protection status, container scan results |
| Incident response (IR) | Security Hub automated playbooks via EventBridge and Lambda. [Amazon SNS ](https://aws.amazon.com/sns/)notifications. Documented incident response (IR) procedures in SSP. | Playbook configurations, notification history, IR procedure documentation |

## Remaining control families
<a name="remaining-control-families"></a>

The following families have fewer technical controls but still require documented implementation.

|
|
| Family | Key AWS implementation | Notes |
| --- |--- |--- |
| Awareness and Training (AT) | Document training programs in SSP. Use IAM policies to enforce training completion before granting CUI access. | Primarily procedural. AWS does not replace your training program but IAM can help enforce access gates. |
| Identification and Authentication (IA) | IAM Identity Center with MFA enforcement. Password policies via IAM. Certificate-based authentication via ACM. | MFA should be enforced for all users, not just administrators. |
| Maintenance (MA) | Systems Manager Session Manager for remote maintenance (fully audited). Patch Manager for scheduled maintenance. | Session Manager helps eliminate bastion hosts and provides complete audit trails. |
| Media Protection (MP) | AWS KMS encryption for all storage. Amazon S3 lifecycle policies. Account-level Amazon EBS encryption defaults. | Cloud media protection is largely addressed by encryption controls. |
| Personnel Security (PS) | IAM access provisioning/deprovisioning. Identity Center lifecycle management. | Primarily procedural. Document onboarding/offboarding procedures. |
| Security Assessment (CA) | Security Hub compliance dashboards. AWS Config conformance packs. Automated evidence pipeline. | Your continuous monitoring and evidence pipeline directly address these controls. |
