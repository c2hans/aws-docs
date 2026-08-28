---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec04-bp01.html
---

# SCSEC04-BP01 Implement least privilege access
<a name="scsec04-bp01"></a>

 Least privilege access and separation of duties create critical security boundaries between different supply chain functions, helping to prevent a single individual from controlling an entire process that could compromise data integrity or operational security.

 For organizations with complex supply chains, these principles form the foundation of a zero-trust security model that protects sensitive information, maintains regulatory compliance, and preserves the integrity of supply chain operations.

 **Desired outcome:** Minimized risk of unauthorized access and data breaches through granular access controls.

 **Benefits of establishing this best practice:** Enhanced security posture and compliance with regulatory requirements for access control.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-18"></a>

 Define IAM policies tailored to common supply chain roles such as supplier, logistics partner, and quality inspector, and use IAM Access Analyzer to refine permissions and verify strict adherence to the principle of least privilege across your supply chain environment. Implement a multi-account strategy with dedicated Organizational Units for different supply chain functions, using service control policies to enforce restrictions on actions within these OUs, and configure custom rules to monitor and enforce supply chain-specific compliance requirements.

### Implementation steps
<a name="implementation-steps-18"></a>

1.  Design a role-based access control framework with supply chain-specific roles, mapping each role to precisely defined permissions that align with job responsibilities and implementing automated access analyzers to identify and remove excessive permissions.

1.  Implement a multi-account architecture with dedicated Organizational Units for distinct supply chain functions, using service control policies to enforce boundaries between operational areas and help prevent unauthorized actions across account boundaries.

1.  Configure automated compliance monitoring with custom rules to detect violations of separation of duties, track changes to critical supply chain resources, and facilitate proper implementation of access controls across all environments.

1.  Develop standardized, pre-approved resource templates for common supply chain workloads with embedded security controls and access constraints that enforce least privilege by default during provisioning.

1.  Establish automated workflows for access requests, approvals, and provisioning that incorporate appropriate segregation of duties checks and maintain audit trails of all access changes across the supply chain environment.

1.  Implement regular access reviews and certification processes specific to supply chain roles, with automated detection of toxic combinations of permissions that could violate separation of duties principles.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
