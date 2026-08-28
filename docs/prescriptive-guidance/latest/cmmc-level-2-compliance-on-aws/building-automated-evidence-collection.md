---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cmmc-level-2-compliance-on-aws/building-automated-evidence-collection.html
---

# Building automated evidence collection
<a name="building-automated-evidence-collection"></a>

The difference between passing and failing a CMMC assessment often comes down to evidence. Assessors need to see that controls are not just implemented but operating effectively and consistently. Manually collecting evidence for 110 controls across 320 assessment objectives is time-consuming and error prone. Automating this process is where AWS provides a significant advantage.

Per the CMMC Assessment Process (CAP) v2.0 and 32 CFR § 170.17(c)(4), evidence must be in final form (no drafts, working guides, or unapproved documents), your organization must create a hash of assessment evidence (artifact names, hash values, hashing algorithm), and artifacts must be retained for six years from the date of the certification assessment.

## Evidence repository structure
<a name="evidence-repository-structure"></a>

Organize your evidence repository to mirror the assessment structure your C3PAO will use. This structure maps directly to NIST SP 800-171 control families and individual requirements:

|
|
| Amazon S3 path | Contents |
| --- |--- |
| s3://evidence-bucket/SSP/ | System Security Plan and network diagrams |
| s3://evidence-bucket/POA-M/ | Plans of Action and Milestones, tracked over time |
| s3://evidence-bucket/SPRS/ | SPRS score calculations and history |
| s3://evidence-bucket/AC/AC-3.1.1/ | Evidence for Access Control requirement 3.1.1 |
| s3://evidence-bucket/AU/AU-3.3.1/ | Evidence for Audit requirement 3.3.1 |
| s3://evidence-bucket/[FAMILY]/[FAMILY]-[REQ]/ | Pattern continues for all 110 requirements |
| s3://evidence-bucket/continuous-monitoring/[YYYY-MM]/ | Monthly continuous monitoring reports |

## Evidence types by control
<a name="evidence-types-by-control"></a>

Each control requires specific evidence types. This table shows representative examples:

|
|
| Control | Evidence source | Artifact | Collection method |
| --- |--- |--- |--- |
| AC-3.1.1 | IAM, IAM Identity Center | User/role inventory, MFA status | AWS Config rules, IAM credential report |
| AU-3.3.1 | CloudTrail | Audit log samples, trail config | CloudTrail org trail, Object Lock verification |
| CM-3.4.1 | AWS Config, CloudFormation | AWS Config snapshots, conformance pack results | AWS Config conformance pack, CloudFormation audit |
| SC-3.13.8 | ACM, Network Firewall | TLS certificate inventory, FIPS endpoint config | ACM certificate list, endpoint URL audit |
| SC-3.13.10 | AWS KMS | Key policies, rotation status, usage logs | AWS KMS key list, CloudTrail KMS events |
| SI-3.14.1 | Amazon Inspector, Systems Manager | Vulnerability findings, patch compliance | Amazon Inspector export, Systems Manager compliance summary |

By combining Security Hub compliance scores, AWS Config conformance pack evaluations, CloudTrail audit logs, and Amazon Inspector vulnerability reports into a centralized Amazon S3 evidence repository in the Security and Log Archive Account, you create a comprehensive, automated evidence pipeline. When your C3PAO arrives, you point them to organized, time-stamped, machine-readable evidence rather than scrambling to produce screenshots and spreadsheets.

## SSP and POA&M guidance
<a name="ssp-and-poam-guidance"></a>

Your SSP is a critical document in your CMMC assessment. It describes your system, your CUI boundary, and how you implement each of the 110 NIST SP 800-171 requirements. Your C3PAO will use the SSP as the roadmap for their assessment. Per the CAP v2.0, the Lead Certified CMMC Assessor (CCA) reviews the SSP for completeness, accuracy, and consistency as the first activity in Phase 1 (Pre-Assessment). The SSP must be ready before the assessment can proceed.

Each SSP control narrative should address every lettered assessment objective for the requirement. For example, if a requirement has objectives [a] through [f] defined in NIST SP 800-171A, the narrative must cover all six. For partially inheritable controls, reference the CRM to delineate what AWS provides and what your organization implements.

POA&Ms document controls that are not yet fully implemented. CMMC allows POA&Ms for eligible controls (see the SPRS scoring section above), but they must be closed within 180 days of your assessment. Each POA&M item should include the specific CMMC practice ID, a description of which assessment objectives are NOT MET, planned corrective actions, milestones with target dates, and required resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
