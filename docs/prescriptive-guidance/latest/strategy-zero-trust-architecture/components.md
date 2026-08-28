---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-zero-trust-architecture/components.html
---

# Key components of a zero trust architecture
<a name="components"></a>

To implement a zero trust architecture (ZTA) strategy effectively, your organization must understand the key components that make up a ZTA. These components work together to continuously improve upon a comprehensive security model that aligns with Zero Trust principles. This section covers those key components of a ZTA.

## Identity and access management
<a name="iam"></a>

Identity and access management forms the foundation of a ZTA by providing robust user authentication and coarse-grain access-control mechanisms. It includes technologies such as single sign-on (SSO), multi-factor authentication (MFA), and identity governance and management solutions. Identity and access management provides a high level of authentication assurance and important context that are integral to making zero trust authorization decisions. At the same time, ZTA is a security model in which access to applications and resources is granted on a per-user, per-device, and per-session basis. This helps to protect organizations from unauthorized access, even if a user's credentials are compromised.

## Secure access service edge
<a name="sase"></a>

Secure access service edge (SASE) is a new approach to network security that virtualizes, combines, and distributes networking and security functions into a single, cloud-based service. SASE can provide secure access to applications and resources, regardless of the user's location.

SASE includes a variety of security features, such as secure web gateways, firewall as a service, and zero trust network access (ZTNA). These features work together to protect organizations from a wide range of threats, including malware, phishing, and ransomware.

## Data loss prevention
<a name="dlp"></a>

Data loss prevention (DLP) technologies can help organizations protect sensitive data from unauthorized disclosure. DLP solutions monitor and control data in motion and at rest. This helps organizations to define and enforce policies that prevent data-related security events, helping to ensure that sensitive information remains protected throughout the network.

## Security information and event management
<a name="siem"></a>

Security information and event management (SIEM) solutions collect, aggregate, and analyze security event logs from various sources across an organization's infrastructure. You can use this data to detect security incidents, facilitate incident response, and provide insights into potential threats and vulnerabilities.

For ZTA specifically, a SIEM solution's ability to correlate and understand related telemetry from different security systems is critical to improved detection of and response to abnormal patterns.

## Enterprise resource ownership catalog
<a name="enterprise-resource-ownership-catalog"></a>

To properly grant access to enterprise resources, an organization must have a reliable system that catalogs these resources and, importantly, who owns them. This source of truth needs to provide workflows that facilitate access requests, the associated approval decisions, and regular attestations thereof. In time, this source of truth will contain the answers to "who can access what?" within the organization. You can use the answers for both authorization and audit and compliance.

## Unified endpoint management
<a name="unified-endpoint-management"></a>

In addition to strongly authenticating the user, a ZTA must also consider the health, posture, and state of the user's device to assess whether corporate data and resource access is secure. A unified endpoint management (UEM) platform provides the following capabilities:
+ Device provisioning
+ Ongoing configuration and patch management
+ Security baselining
+ Telemetry reporting
+ Device cleansing and retirement

## Policy-based enforcement points
<a name="policy-based-enforcement-points"></a>

In a ZTA, access to each resource should be explicitly authorized by a gating policy-based enforcement point. Initially, these enforcement points can be based on existing enforcement points in existing network and identity systems. The enforcement points can be made incrementally more capable by considering the wider array of context and signals that ZTA provides. Longer term, your organization should implement ZTA-specific enforcement points that operate on converged context, consistently integrate signal providers, maintain a comprehensive policy set, and are enhanced with intelligence gleaned from combined telemetry.

## Section summary
<a name="components-summary"></a>

Understanding these key components is essential for organizations planning to adopt a ZTA. By implementing these components and integrating them into a cohesive security model, your organization can establish a strong security posture based on the principles of Zero Trust. The following sections explore organizational readiness, phased adoption approaches, and best practices to help you successfully implement ZTA within your organization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
