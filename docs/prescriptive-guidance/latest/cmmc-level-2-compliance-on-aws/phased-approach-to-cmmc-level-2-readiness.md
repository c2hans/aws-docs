---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cmmc-level-2-compliance-on-aws/phased-approach-to-cmmc-level-2-readiness.html
---

# A phased approach to CMMC Level 2 readiness
<a name="phased-approach-to-cmmc-level-2-readiness"></a>

After reading this guide you will be able to:
+ Scope your CUI boundary on AWS using multi-account architecture
+ Implement all 110 NIST SP 800-171 Rev. 2 security requirements using AWS services
+ Build automated evidence collection pipelines for C3PAO assessment
+ Establish continuous monitoring for sustained compliance
+ Understand SPRS scoring, POA&M eligibility, and remediation prioritization
+ Prepare personnel and documentation for C3PAO assessment phases

## Phases of CMMC Level 2 readiness
<a name="phases-of-cmmc-level-2-readiness"></a>

These three phases provide a concrete path from initial scoping through assessment readiness. Each phase builds on the previous on. The timeline depends on whether you are working with an existing AWS environment or are building from scratch.

## Phase 1: Assess and scope your CUI environment
<a name="assess-and-scope-your-cui-environment"></a>
+ Identify all contracts that involve CUI and determine your required CMMC level
+ Choose your deployment Region: AWS GovCloud (US) for International Traffic in Arms Regulations (ITAR)/Security Requirements Guide (SRG) Impact Level 4 (IL4)\+ workloads, or commercial US East/West with FIPS endpoints for CUI workloads without those overlays
+ Design your multi-account structure - Management Account, CUI Workload Account(s), Shared Services Account, and Security and Log Archive Account
+ Classify all assets using the five CMMC scoping categories - CUI Assets, Security Protection Assets, Contractor Risk Managed Assets (CRMAs), Specialized Assets, Out-of-Scope
+ Map your CUI data flows and define your assessment boundary using AWS Organizations and Amazon Virtual Private Cloud (Amazon VPC)
+ Inventory all external service providers (ESPs) and cloud service providers (CSPs), determine Federal Risk and Authorization Management Program (FedRAMP) status, and begin Customer Responsibility Matrix (CRM) documentation
+ Enable foundational services: AWS Config, AWS CloudTrail (organization trail), AWS Security Hub, Amazon GuardDuty and Amazon Inspector
+ Conduct an initial gap assessment against NIST SP 800-171 Rev. 2 requirements and calculate your Supplier Performance Risk System (SPRS) score
+ Prioritize remediation - Plan of Action and Milestones (POA&M)-ineligible requirements first, then 5-point Basic requirements, then 1-point Derived requirements

## Phase 2: Implement controls and automate evidence
<a name="implement-controls-and-automate-evidence"></a>
+ Deploy the CMMC 2.0 Level 2 conformance pack in AWS Config for continuous compliance evaluation
+ Configure FIPS-validated endpoints for all AWS service calls within your CUI boundary
+ Implement access control, encryption, and boundary protection controls using AWS Identity and Access Management (IAM), AWS Key Management Service (AWS KMS), and AWS Network Firewall
+ Address the 10 customer-only controls that require organizational policies or non-AWS technology
+ Build continuous vulnerability scanning and patch management workflows with Amazon Inspector and AWS Systems Manager
+ Set up your security protection data (SPD) evidence pipeline: AWS Security Hub findings, AWS Config evaluations, CloudTrail logs, and Amazon Inspector reports flowing into the evidence repository
+ Document your System Security Plan (SSP) (addressing all assessment objectives per control), POA&Ms, and network diagrams
+ Complete CRM documentation for all ESPs and confirm ESP personnel availability for assessment interviews

## Phase 3: Validate and prepare for assessment
<a name="validate-and-prepare-for-assessment"></a>
+ Run a mock assessment against all 110 controls and 320 assessment objectives using your automated evidence
+ Conduct mock interviews with personnel who will be interviewed by the C3PAO
+ Close any remaining POA&M items (POA&Ms must be closed within 180 days)
+ Verify your SPRS score meets the 88-point threshold for Conditional status (or 110 for Final status)
+ Engage your C3PAO and provide access to your evidence repository and compliance dashboards
+ Establish ongoing continuous monitoring processes and annual affirmation procedures to maintain certification between assessments

Organizations with existing AWS environments and security tooling can typically complete Phases 1-3 in 90-120 days. Organizations building new environments should plan for 150-180 days. Either way, starting now positions you well ahead of the November 2026 Phase 2 deadline.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
