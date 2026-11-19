---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/security-controls-mapping-well-architected-framework.html
---

# Security Controls Mapping (Well-Architected Framework)

The AWS Well-Architected Framework Security Pillar defines best practices for protecting information, systems, and assets. This section maps the framework's security controls to specific Well-Architected best practices, explaining not just what the framework implements but why each control matters in the context of cross-account third-party access.

|
|
| Best Practice | Framework Implementation |
| --- |--- |
| SEC01-BP01 Separate workloads using accounts | Customer and WSP/ESP operate in separate AWS accounts with no shared resources. The trust relationship is the only connection between accounts. |
| SEC02-BP02 Use temporary credentials | STS AssumeRole provides temporary credentials with a default 1-hour session. No long-term access keys are created or shared. |
| SEC03-BP02 Grant least privilege access | Read-only permissions only. CloudWatch read access scoped operationally to AWS/DX by monitoring system. IAM scoped to operator role ARN. No write, update, or delete actions. |
| SEC03-BP09 Share resources securely with third party | Cross-account IAM role. ExternalId enforcement is configurable: when enabled, prevents confused deputy attacks; when removed, enables Console role switching. Unique ExternalId per customer relationship recommended. |
| SEC04-BP01 Configure service and application logging | CloudTrail logs all role assumption events and API calls. Governance validation (tag compliance) is optional and external to this stack. |
| SEC04-BP04 Initiate remediation for non-compliant resources | Governance validation is optional. Customers may use AWS Config (where supported), custom rules, or scheduled audits to detect tag changes. |

The alignment with SEC03-BP09 is particularly significant. This best practice recommends using cross-account IAM roles with ExternalIds for third-party access. This framework implements that pattern with ExternalId enforcement as a configurable option. Organizations that require console compatibility may remove the ExternalId condition, accepting the tradeoff documented in the Limitations and Trade-offs section.
