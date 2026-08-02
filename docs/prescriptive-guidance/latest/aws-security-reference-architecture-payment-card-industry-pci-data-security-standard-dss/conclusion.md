---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-reference-architecture-payment-card-industry-pci-data-security-standard-dss/conclusion.html
---

# Conclusion
<a name="conclusion"></a>

This guidance demonstrates how the AWS Security Reference Architecture (AWS SRA) provides a strong, extensible foundation for PCI DSS v4.0.1 compliance in a multi-account AWS environment. By mapping AWS SRA patterns to PCI DSS requirements across nine control domains — Organization Architecture and Scoping, Network Security, System Hardening, Encryption and Key Management, Secure SDLC, Change Management, Access Control, Logging and Monitoring, and Vulnerability Management — the guide shows that PCI DSS compliance on AWS is an extension of sound cloud security architecture.

## Key Takeaways
<a name="key-takeaways"></a>

|
|
| Principle | Guidance |
| --- |--- |
| Scoping drives everything | A well-designed OU and account structure — segmenting CDE, Connected-To, and Out-of-Scope accounts — is one of the most impactful lever for reducing assessment surface and clarifying control ownership. |
| AWS SRA is necessary foundation with extension to meet PCI DSS | Each domain distinguishes "within the AWS SRA" (baseline already met) from "beyond the AWS SRA" (additional PCI-specific configuration required). Use this to target gaps without over-engineering. |
| Automate for continuous compliance | AWS Config, Security Hub, CloudTrail, and EventBridge enable a shift from point-in-time audits to continuous monitoring and automated remediation — essential for PCI DSS v4.0's emphasis on ongoing security. |
| Identity is the cloud perimeter | IAM, Organizations SCPs, and centralized federation enforce least privilege and strong authentication at the platform level (Requirements 7, 8). |
| Layered segmentation replaces flat perimeters | VPC architecture, Network Firewall, security groups, PrivateLink, and Transit Gateway — applied across accounts and OUs — satisfy Requirement 1 without reliance on single-appliance designs. |
| Tagging is infrastructure | A structured PCI tagging strategy underpins inventory management, automated compliance checks, and scope validation across the standard. |

## Next Steps
<a name="next-steps"></a>

1. Compare your existing AWS architecture against the OU structure and segmentation boundaries in this guide to identify scoping gaps.

1. Prioritize building a strong AWS multi-account security architecture following the AWS SRA to ensure you are building a strong security posture to meet the intent of PCI DSS requirements.

1. Automate controls and change management as much as possible to ensure consistency and continuous compliance.

1. Engage your Qualified Security Assessor (QSA) during the design phase to validate scoping decisions before implementation.

1. Download AWS's PCI DSS AOC and Shared Responsibility Matrix from [AWS Artifact](https://aws.amazon.com/artifact/) to establish inherited controls.

## PCI DSS on AWS - Related Resources
<a name="pci-dss-on-aws-related-resources"></a>

|
|
| Resource | Description | Link |
| --- |--- |--- |
| PCI DSS v4.0 on AWS Compliance Guide | Comprehensive guide covering requirement-by-requirement guidance, scoping, segmentation, and the Shared Responsibility Model for PCI DSS v4.0 on AWS | [Download PDF](https://d1.awsstatic.com/whitepapers/compliance/pci-dss-compliance-on-aws-v4-102023.pdf) |
| Architecting for PCI DSS Scoping and Segmentation on AWS | Detailed network architecture patterns, multi-account segmentation strategies, firewall rule examples, and reference architectures for defining PCI DSS scope boundaries on AWS | [Download PDF](https://d1.awsstatic.com/whitepapers/compliance/architecting-pci-dss-segmentation-scoping-aws.pdf) |
| Architecting on Amazon ECS for PCI DSS Compliance | Best practices for configuring Amazon ECS (Fargate and EC2 launch types) for PCI DSS compliance, covering network segmentation, host hardening, data protection, and monitoring | [Download PDF](https://d1.awsstatic.com/whitepapers/compliance/architecting-on-amazon-ecs-for-pci-dss-compliance.pdf) |
| Architecting Amazon EKS for PCI DSS Compliance | Guidance on configuring Amazon EKS (Fargate and EC2 launch types) for PCI DSS compliance, including Kubernetes network policies, pod security, secrets management, and container scanning | [Download PDF](https://d1.awsstatic.com/whitepapers/compliance/architecting-amazon-eks-for-pci-dss-compliance.pdf) |
