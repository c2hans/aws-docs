---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/security-1.html
---

# Security
<a name="security-1"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit the [AWS Security Center](https://aws.amazon.com/security/).

## Security Controls and Compliance
<a name="sec-controls-compliance"></a>

MDAA implements multiple security controls and compliance measures:
+ Compliance with multiple AWS CDK Nag rulesets:
+ AWS Solutions ruleset
+ NIST 800-53 Rev 5 ruleset
+ HIPAA ruleset
+ PCI-DSS ruleset
+ Adherence to ITSG-33 PBMM Security Control Requirements
+ Implementation of security best practices across all deployed resources

### Encryption
<a name="encryption"></a>

MDAA enforces comprehensive encryption measures:
+ Ubiquitous encryption at rest for all data storage components
+ Mandatory encryption in transit for all data transfers
+ Integration with AWS KMS for key management

### Access Control
<a name="access-control"></a>

The solution implements the principle of least privilege:
+ Least-privileged permissions by default for all deployed resources
+ Role-based access control (RBAC) implementation
+ Secure self-service deployments through AWS Service Catalog (optional)

### Governance Controls
<a name="governance-controls"></a>

MDAA provides several governance mechanisms:
+ AWS CloudFormation as the single deployment mechanism through CDK
+ Consistent resource naming conventions across all deployments
+ Standardized tagging strategy for all generated resources
+ Centralized change management through Infrastructure as Code

### Resource Management
<a name="resource-management"></a>

Security is enforced through:
+ Consistent deployment patterns across all MDAA modules
+ Standardized SSM parameter publication for secure resource reference
+ Compliant resource configurations by default

### Monitoring and Metrics
<a name="monitor-metrics"></a>

The solution includes:
+ Integration with AWS native security monitoring services
+ Compliance validation capabilities

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Modern Data Architecture Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
