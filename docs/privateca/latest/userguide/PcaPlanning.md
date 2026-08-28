---
source_url: https://docs.aws.amazon.com/privateca/latest/userguide/PcaPlanning.html
---

# Architect your solution for AWS Private CA
<a name="PcaPlanning"></a>

AWS Private CA gives you complete, cloud-based control over your organization's private PKI (public key infrastructure), extending from a root certificate authority (CA), through subordinate CAs, to end-entity certificates. Thorough planning is essential for a PKI that is secure, maintainable, extensible, and suited to your organization's needs. This section provides guidance on designing a CA hierarchy, managing your private CA and private end-entity certificate lifecycles, and applying best practices for security.

This section describes how to prepare AWS Private CA for use before you create a private certificate authority (CA). It also explains the option to add revocation support through Online Certificate Status Protocol (OCSP) or a certificate revocation list (CRL).

In addition, you should determine whether your organization prefers to host its private root CA credentials on premises rather than with AWS. In that case, you need to set up and secure a self-managed private PKI before using AWS Private CA. In this scenario, you then create a subordinate CA in AWS Private CA backed by a parent CA outside of AWS Private CA. For more information, see [Installing a subordinate CA certificate signed by an external parent CA](https://docs.aws.amazon.com/privateca/latest/userguide/PCACertInstall.html#InstallSubordinateExternal).

**Topics**
+ [Design a CA hierarchy](ca-hierarchy.md)
+ [Manage the private CA lifecycle](ca-lifecycle.md)
+ [Plan your AWS Private CA certificate revocation method](revocation-setup.md)
+ [Understand AWS Private CA CA modes](short-lived-certificates.md)
+ [Plan for resilience in AWS Private CA](disaster-recovery-resilience.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private Certificate Authority. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
