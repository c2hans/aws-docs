---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cmmc-level-2-compliance-on-aws/cmmc-scoping-on-aws.html
---

# CMMC scoping on AWS
<a name="cmmc-scoping-on-aws"></a>

It is critical to understand the complete flow of CUI within your applications and the rest of your environment, including interactions with procedures and application code. The evaluation of data flow in the environment, as well as all connected to and supporting system components, determines the applicability of CMMC requirements and defines the boundaries and components of your CUI environment and the scope of your CMMC assessment.

## Key terms
<a name="key-terms"></a>

The following assessment vocabulary appears throughout this guide. Skip this if you are familiar with NIST SP 800-171A and the CMMC Assessment Process.

|
|
| Term | Definition |
| --- |--- |
| Assessment objective | A specific, lettered evaluation criterion (for example, [a] through [f]) defined in NIST SP 800-171A for each requirement. The 110 requirements expand to 320 assessment objectives. |
| Examine, Interview, Test | The three evidence-gathering methods assessors use. Examine reviews documents and configurations, Interview asks personnel to explain implementation, Test observes controls operating. |
| MET / NOT MET / NOT APPLICABLE | The three possible findings per requirement. MET means all assessment objectives are satisfied with final-form evidence. NOT MET means one or more objectives are not satisfied. |
| Depth and coverage | How thoroughly an assessor evaluates a requirement (depth) and how broadly across the environment (coverage). Determined by the assessor based on risk and scope. |
| POA&M | Plan of Action and Milestones. A formal remediation plan for a NOT MET requirement that is POA&M-eligible. Must be closed within 180 days. |
| Final form | Evidence that is approved, signed, dated, and authoritative. Drafts, working documents, and unapproved policies are not accepted. |

## Understand CMMC Level 2 scoping
<a name="understand-cmmc-level-2-scoping"></a>

CMMC Level 2 requires implementation of all 110 security requirements from NIST SP 800-171 Rev. 2, organized across 14 control families. Your C3PAO assessor evaluates these requirements against 320 assessment objectives defined in [NIST SP 800-171A](https://csrc.nist.gov/publications/detail/sp/800-171a/final). The assessment is evidence-based: for each control, your assessor looks for three types of evidence.

|
|
| Evidence type | What it proves | Example |
| --- |--- |--- |
| Examine | Policies, procedures, configurations, and documentation exist | SSP, [AWS Config](https://aws.amazon.com/config/) rule evaluations, IAM policies |
| Interview | Personnel understand and can explain control implementation | Security team explains incident response procedures |
| Test | Controls function as intended in the operational environment | Assessor observes multi-factor authentication (MFA) enforcement, reviews[ CloudTrail](https://aws.amazon.com/cloudtrail/) logs showing access denials |

The difference between organizations that pass and those that receive findings typically comes down to evidence quality. Assessors want time-stamped, machine-readable, immutable evidence that demonstrates controls are operating continuously, not screenshots collected the week before the assessment.

## CMMC scoping categories
<a name="cmmc-scoping-categories"></a>

Per 32 CFR § 170.19(c)(1) and the CMMC Scoping Guide Level 2 v2.13, every in-scope asset must be classified into one of five categories. Understanding these categories is essential for defining your assessment boundary on AWS.

|
|
| Category | Description | Assessment rigor | AWS example |
| --- |--- |--- |--- |
| CUI Assets | Process, store, or transmit CUI | Assessed against all 110 Level 2 requirements | Amazon Elastic Compute Cloud (Amazon EC2) instances running CUI workloads, [Amazon Simple Storage Service(](https://aws.amazon.com/s3/)Amazon S3[)](https://aws.amazon.com/s3/) buckets storing CUI |
| Security Protection Assets | Provide security functions or capabilities to the assessment scope | Assessed against Level 2 requirements relevant to the capabilities they provide | [AWS Security Hub](https://aws.amazon.com/security-hub/), [GuardDuty](https://aws.amazon.com/guardduty/), [CloudTrail](https://aws.amazon.com/cloudtrail/), your Security and Log Archive Account |
| CRMAs | Can but are not intended to process CUI; not required to be physically or logically separated | Assessor reviews SSP documentation first; limited check only if documentation raises questions | Corporate laptops on the same network segment, development environments without CUI |
| Specialized Assets | Government Furnished Equipment (GFE), Internet of Things (IoT)/Industrial IoT (IIoT), Operational Technology (OT), restricted information systems, and test equipment | Assessed based on applicability; managed using risk-based security policies | Test lab equipment, IoT sensors connected to the CUI environment |
| Out-of-Scope Assets | Cannot process, store, or transmit CUI and do not provide security protection | Not assessed; must be physically or logically separated from CUI assets | Corporate website hosting, marketing systems in a separate AWS account with no connectivity to the CUI boundary |

Security Protection Data (SPD), which includes log files, configuration data, vulnerability data, and passwords granting access to the in-scope environment, is also in scope. This is why the Security and Log Archive Account in the reference architecture is classified as a Security Protection Asset even though it sits outside the CUI boundary.

Effective separation techniques include logical separation (firewalls, VLANs, VPNs, separate AWS accounts) or physical separation (no wired or wireless connection). On AWS, account-level isolation through Organizations provides the strongest form of logical separation. A new assessment is required if there are significant architectural or boundary changes.

## CMMC rollout phases
<a name="cmmc-rollout-phases"></a>

The DoD is implementing CMMC through a phased approach over a three-year period. Understanding where you are today and what comes next determines your preparation strategy.

|
|
| Phase | Dates | What happens |
| --- |--- |--- |
| Phase 1 (Current) | Nov 10, 2025 - Nov 9, 2026 | CMMC Program Office selects contracts requiring Level 1 or Level 2 self-assessments. C3PAO certification may be required for select solicitations at DoD discretion. |
| Phase 2 | Nov 10, 2026 - Nov 9, 2027 | DoD solicitations and contracts widely require Level 2 C3PAO certification. This is the deadline most contractors are planning around. |
| Phase 3 | Nov 10, 2027 - Nov 9, 2028 | Level 3 Defense Industrial Base Cybersecurity Assessment Center (DIBCAC) assessments begin for high-sensitivity programs. |
| Phase 4 | Nov 10, 2028 onward | Full implementation across all DoD contracts requiring Federal Contract Information (FCI) or CUI processing, storage, or transmission. |

Organizations typically need 6 to 12 months to fully prepare for a C3PAO assessment. Starting now positions you to meet the November 2026 milestone with time for remediation and mock assessment.

## The 14 control families
<a name="control-families"></a>

This table shows all 14 NIST SP 800-171 control families, the number of requirements in each, and the primary AWS services that help address them. Detailed mappings appear later in this guide.

|  |  |  |  |
| --- |--- |--- |--- |
| Family | ID | \# Controls | Primary AWS services |
| Access Control | AC | 22 | [IAM](https://aws.amazon.com/iam/), [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/), Amazon VPC, Security Groups, [AWS Network Firewall](https://aws.amazon.com/network-firewall/), [AWS Verified Access](https://aws.amazon.com/verified-access/) |
| Awareness and Training | AT | 3 | IAM (policy documentation), AWS Organizations |
| Audit and Accountability | AU | 9 | CloudTrail, [ CloudWatch](https://aws.amazon.com/cloudwatch/), Amazon S3 (log archive), Security Hub |
| Configuration Management | CM | 9 | AWS Config, [AWS Systems Manager](https://aws.amazon.com/systems-manager/), [AWS CloudFormation](https://aws.amazon.com/cloudformation/), [AWS Service Catalog](https://aws.amazon.com/servicecatalog/) |
| Identification and Authentication | IA | 11 | IAM, IAM Identity Center, [AWS KMS](https://aws.amazon.com/kms/), AWS Certificate Manager(ACM) |
| Incident Response | IR | 3 | GuardDuty, Security Hub, [AAmazon EventBridge](https://aws.amazon.com/eventbridge/), [AWS Lambda](https://aws.amazon.com/lambda/), [ Amazon Simple Notification Service, ](https://aws.amazon.com/sns/)(Amazon SNS), [Amazon Detective](https://aws.amazon.com/detective/) |
| Maintenance | MA | 6 | Systems Manager (Session Manager, Patch Manager) |
| Media Protection | MP | 4 | AWS KMS, Amazon S3 (encryption, lifecycle), [Amazon Elastic Block Store ](https://aws.amazon.com/ebs/)(Amazon EBS) encryption |
| Personnel Security | PS | 2 | IAM (access provisioning/deprovisioning) |
| Physical Protection | PE | 6 | Inherited from AWS (Federal Risk and Authorization Management Program (FedRAMP)) |
| Risk Assessment | RA | 3 | [Amazon Inspector](https://aws.amazon.com/inspector/), GuardDuty, Security Hub |
| Security Assessment | CA | 4 | Security Hub, AWS Config conformance packs |
| System and Comm. Protection | SC | 16 | AWS KMS, ACM, Network Firewall, Amazon VPC, [AWSWAF](https://aws.amazon.com/waf/), FIPS endpoints, AWS Verified Access |
| System and Info. Integrity | SI | 7 | Amazon Inspector, GuardDuty, CloudWatch Systems Manager, CloudTrail |
