---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dsops02-bp01.html
---

# DSOPS02-BP01 Baseline your compliance requirements
<a name="dsops02-bp01"></a>

 Compliance requirements accumulate from multiple sources: cybersecurity directives, data privacy legislation, industry regulations, and internal policies. These requirements can overlap or diverge, whether you operate in one jurisdiction or many. A compliance baseline maps each requirement to specific technical controls so that teams can implement, test, and audit them consistently.

 **Desired outcome:**
+  Your organization maintains a compliance catalog that maps regulatory requirements to technical controls, validation criteria, and audit evidence.
+  The catalog covers organizational controls that apply across jurisdictions and workload-specific controls where regulations differ.
+  Teams use the catalog to identify gaps, resolve divergences between overlapping frameworks, and demonstrate compliance posture to auditors on demand.

 **Common anti-patterns:**
+  Making decisions based on informal understanding rather than documented requirements.
+  Applying the same compliance controls across workloads without considering specific regulatory requirements.
+  Only identifying requirements after a compliance issue or audit finding occurs.
+  Creating compliance baselines once and rarely updating them as regulations evolve.

 **Benefits of establishing this best practice:**
+  Risk reduction through proactive identification of compliance gaps before they appear in audits or incidents.
+  Cost optimization by implementing controls proportionate to regulatory requirements, avoiding over-engineering.
+  Improved audit readiness with documented traceability from regulatory requirements to technical controls and validation criteria.
+  Faster onboarding of new workloads or jurisdictions by reusing an established compliance baseline.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Compliance requirements arrive from many sources at once and at different levels of specificity. A compliance catalog provides traceability by creating a single, structured artifact that connects each regulatory obligation to specific technical controls, validation criteria, and audit evidence. Teams implement controls consistently because the mapping is explicit, and auditors can verify coverage directly from the catalog rather than through manual investigation.

 Many regulatory frameworks overlap in their requirements. The General Data Protection Regulation (GDPR), the Network and Information Systems Directive (NIS2), and Payment Card Industry Data Security Standard (PCI-DSS) may all require encryption at rest, or access logging, but express these requirements in different terminology and at different levels of specificity. A well-structured catalog maps multiple framework requirements to shared control objectives, so that a single implementation satisfies multiple regulatory obligations without duplicating effort. This multi-framework convergence reduces the total number of controls to implement and maintain while providing auditors with clear traceability from a requirement to its shared implementation.

 The catalog benefits from separating cloud service provider (CSP) agnostic control objectives from CSP-specific implementations. A control objective such as "restrict data processing to approved jurisdictions" is universal and maps to multiple standards. The CSP-specific implementation (for example, applying a Region deny Service Control Policy through [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/ou-region-deny.html)) is how that objective is technically applied on AWS. This separation enables organizations to maintain portability of their compliance logic while documenting precisely how each objective is met in their chosen environment.

 The catalog tiers controls by applicability into organizational, jurisdiction-specific, and workload-specific levels. This tiering enables reuse because new workloads inherit applicable organizational and jurisdiction-specific controls automatically, requiring only workload-specific controls to be defined.

### Implementation steps
<a name="implementation-steps"></a>

1.  **Develop a compliance catalog:** Create a compliance catalog (also known as a compliance workbook) that maps regulatory requirements to specific technical controls, validation criteria, and audit evidence. Structure the catalog using a control hierarchy organized by domains and categories. The [AWS Control Catalog](https://docs.aws.amazon.com/controlcatalog/latest/userguide/what-is-controlcatalog.html) uses one such hierarchy, which you can observe in the AWS Management Console when viewing control details such as [CT.S3.PR.11 - Require an Amazon S3 bucket to have versioning enabled](https://docs.aws.amazon.com/controltower/latest/controlreference/s3-rules.html#ct-s3-pr-11-description). The Cloud Security Alliance [Cloud Controls Matrix (CCM v4.1)](https://cloudsecurityalliance.org/research/cloud-controls-matrix/) offers an alternative meta-framework that maps control specifications to multiple standards. These are two examples of how to structure a compliance workbook. Other approaches exist, and the right structure depends on your organization's specific requirements. Collaborate with your compliance teams to define the structure that fits your needs.

1.  **Define controls:** Whichever structure you choose, for a compliance catalog to be useful, consider the following.
   +  List a set of fully defined non-overlapping controls. Controls are usually identified by an internally recognized unique id. For example, OPS-001, DRC-002.
   +  Organize controls logically by CSP-agnostic domains, functions, and control objectives. (See tables in Steps 5 and 6 below).
   +  Include CSP-agnostic implementation guidance for each control. If required, also include jurisdiction-specific implementation guidelines.
   +  Map control objectives to standards.
   +  List CSP-specific technical controls (for example, [AWS Control Tower Controls](https://docs.aws.amazon.com/controltower/latest/controlreference/controls-reference.html)) for each control id. Also list procedural controls when a control objective can't be met through technical measures only.
   +  State a control's applicability: the *class of workloads*, *data classification levels*, or *jurisdictions* it applies to.
   +  State enablement tier. Whether the control is applied at an organizational level, per jurisdiction or is workload-specific.
   +  Show how the CSP-specific technical controls will be verified (unit testing, integration testing) and monitored (metrics) at runtime.
   +  List what data or documentation needs to be collected as evidence in support of audits.

1.  **Assign ownership:** Assign ownership of sections of the catalog to teams and roles best positioned to maintain them. Security and compliance subject matter experts (SMEs) typically define CSP-agnostic control domains, control objectives, implementation guidelines, and standards mappings. DevSecOps and engineering teams list CSP-specific controls, validation criteria, and compliance metrics. Compliance SMEs supporting audits define the evidence requirements.

1.  **Document organizational-level controls:** The following example illustrates a fully documented organization-level control applicable to workloads across all jurisdictions. The control id **OPS-001** is an internal id and is unique to your organization.

    **Note:** The control mapping shown in the following table is only for illustration purposes. It isn't accurate and may not be up to date with the latest AWS Documentation. Your compliance workbook might be structured differently.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dsops02-bp01.html)

1.  **Document jurisdiction-specific and workload-specific controls:** Document jurisdiction-specific and workload-specific cybersecurity, data privacy, and industry-specific regulatory requirements. The following is an example of a workload-specific control. Backup requirements may not be applicable to a workload if it is stateless (for example a tax calculation microservice). The control id DRC-002 is an internal id and is unique to your organization.

    **Note:** The control mapping shown in the following table is only for illustration purposes. It isn't accurate and may not be up to date with the latest AWS Documentation. Your compliance workbook might be structured differently.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dsops02-bp01.html)

1.  **Conduct gap analysis:** Discover potential gaps in your compliance posture.
   +  Conduct data protection impact assessments (DPIAs) where there is a high risk of non-compliance because of the location and sensitivity of the data involved.
   +  To identify compliance issues, enable AWS Security Hub CSPM. Then, enable a [Security Hub CSPM standard](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference.html) to automatically start collecting data about noncompliant resources.

1.  **Log and manage risks:** Maintain a risk register. Log and manage compliance-related risks that can't be addressed by the current design. Document compensatory measures applied to mitigate risks.

1.  **Maintain the baseline as regulations evolve:** Update your compliance baseline as regulations change. Validate requirements through reviews with stakeholders such as legal experts and your compliance teams. Document the potential economic impact of meeting regulations (cost of compliance) to guide yearly planning and budgeting.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [DSOPS01-BP01 Organize compliance for multi-jurisdictional operations](dsops01-bp01.html)
+  [DSOPS04-BP01 Maintain continuous visibility of your compliance status](dsops04-bp01.html)
+  [DSOPS06-BP01 Track regulatory changes across jurisdictions](dsops06-bp01.html)
+  [DSOPS06-BP02 Manage regulatory changes](dsops06-bp02.html)
+  [OPS01-BP03 Evaluate governance requirements](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_governance_reqs.html)
+  [OPS01-BP04 Evaluate compliance requirements](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_compliance_reqs.html)
+  [[AG.ACG.1] Adopt a risk-based compliance framework](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.1-adopt-a-risk-based-compliance-framework.html)

 **Related documents:**
+  [Implementing a compliance and reporting strategy for NIST SP 800-53 Rev. 5](https://aws.amazon.com/blogs/security/implementing-a-compliance-and-reporting-strategy-for-nist-sp-800-53-rev-5/)
+  [Scaling a governance, risk, and compliance program for the cloud](https://aws.amazon.com/blogs/security/scaling-a-governance-risk-and-compliance-program-for-the-cloud/)
+  [AWS Security Reference Architecture (SRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html)
+  [AWS Risk and Compliance Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/welcome.html)
+  [Exploring the new AWS European Sovereign Cloud: Sovereign Reference Framework](https://aws.amazon.com/blogs/security/exploring-the-new-aws-european-sovereign-cloud-sovereign-reference-framework/)
+  [Architecting for HIPAA Security and Compliance on Amazon Web Services](https://docs.aws.amazon.com/whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/welcome.html)
+  [AWS Config Conformance Packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html)
+  [AWS Security Hub CSPM Compliance Standards](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference.html)
+  [AWS Artifact User Guide](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html)

 **Related videos:**
+  [Global Security & Compliance Acceleration Program](https://www.youtube.com/watch?v=BJWQ_DPbp1U)
+  [Global Security & Compliance Acceleration (GSCA) Bundles](https://www.youtube.com/watch?v=W6jlDur1Yos)

 **Related examples:**
+  [Secure Controls Framework (SCF)](https://github.com/securecontrolsframework/securecontrolsframework/tree/main)
+  [AWS Config Conformance Pack Samples](https://docs.aws.amazon.com/config/latest/developerguide/conformancepack-sample-templates.html)
+  [AWS Well-Architected Labs - Security](https://wellarchitectedlabs.com/security/)

 **Related services:**
+  [AWS Control Tower](https://aws.amazon.com/controltower/)
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
+  [AWS Config](https://aws.amazon.com/config/)
+  [AWS Artifact](https://aws.amazon.com/artifact/)
+  [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html)
