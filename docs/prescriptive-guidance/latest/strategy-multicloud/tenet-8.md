---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud/tenet-8.html
---

# Tenet 8. Make sure that security is always a top priority
<a name="tenet-8"></a>

A multicloud approach makes it harder to ensure security by increasing the risk of unauthorized access, because your security posture must account for more attack surfaces. A multicloud strategy often forces companies to deal with multiple security models across CSPs in areas such as identity management, network security, asset management, and audit logging. This complexity risks making transparency harder, increases the burden on security teams, and elevates risk.

Security automation is essential in multicloud environments. Identity management must work seamlessly across environments; it must connect existing identity providers while maintaining consistent access policies. Security requires integrated protection across data, network, and endpoint layers. Data classification, encryption, and lifecycle management form the foundation. Network security builds on standardized designs and connection patterns. Endpoint protection completes the framework through consistent patch management and host-based controls.

These foundational elements are critical to successful and safe adoption of multiple cloud providers and must be considered early in any multicloud strategy planning.

**Our guidance:**
+ Implement an integrated security framework across your multicloud environment that focuses on three core elements: data protection through standardized classification and encryption, network security through consistent design patterns, and endpoint protection through systematic controls and patch management.
+ Establish a unified security operations model that takes advantage of each cloud provider's native security capabilities while maintaining centralized visibility and control through standardized tools and processes.
+ Centralize security data collection and analysis by using [Amazon Security Lake](https://aws.amazon.com/security-lake/). This platform aggregates security information from AWS, other cloud providers, SaaS applications, and on-premises systems into a single view. It supports the Open Cybersecurity Schema Framework (OCSF) and enables standardized analysis across your hybrid and multicloud environment. This centralized approach improves threat detection and response while simplifying security operations.
+ Deploy each provider's native security tools to enhance your protection capabilities. These purpose-built services address provider-specific features while feeding data back to your centralized security platform. A combination of native tools and centralized visibility helps provide comprehensive security coverage across your entire infrastructure.
+ Implement a unified observability strategy that provides comprehensive visibility across your entire cloud landscape, including operational and security data, from the ground up. Standardize on industry-leading monitoring approaches that enable consistent tracking of business services regardless of where they operate.
+ Establish enterprise-wide standards for operational data collection and visualization that enable rapid issue identification and resolution across your multicloud environment. Focus on creating a single source of truth for operational insights that serves both technical and business stakeholders.
