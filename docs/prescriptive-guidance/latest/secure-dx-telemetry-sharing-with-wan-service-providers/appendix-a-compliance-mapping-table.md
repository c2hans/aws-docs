---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/appendix-a-compliance-mapping-table.html
---

# Appendix A: Compliance Mapping Table

The following table maps the framework's controls to specific compliance requirements. For each control, the table identifies the regulatory framework, the specific requirement, and how this framework satisfies it. The intent is to provide compliance teams with a ready-made mapping that can be incorporated into authorization packages and audit documentation.

|
|
| Framework | Requirement | How Satisfied |
| --- |--- |--- |
| FedRAMP High | AC-3 Access Enforcement | IAM policy enforces read-only access at the action level. Namespace and tag scoping are implemented operationally by the monitoring system. ExternalId prevents unauthorized assumption. |
| FedRAMP High | AC-17 Remote Access | Cross-account role with STS temporary credentials. No persistent access. Session duration limited to 1 hour. |
| FedRAMP High | AU-2 Audit Events | CloudTrail logs all role assumption events and every API call made with assumed credentials. |
| FedRAMP High | AU-6 Audit Review | Quarterly access reviews defined in operational model. Review outcomes documented and retained. |
| AWS isolated partitions | Partition isolation | No cross-partition data flow. CPO coordination documented. |
| SOC 2 Type II | CC6.1 Logical access | Least-privilege IAM with ExternalId. Tag-based opt-in ensures explicit consent. No default access. |
| SOC 2 Type II | CC7.2 System monitoring | CloudTrail provides continuous monitoring of role assumption and API calls. Governance validation (tag compliance) is optional and external. |
| ITAR / EAR | Data residency | AWS does not replicate or export DX data to an ESP account. WSP/ESP retrieves via read-only API with temporary credentials. WSP/ESP may store retrieved data in their own systems. |

The FedRAMP AC-3 mapping is particularly important for government customers. The framework's IAM policy enforces access at the API action level (read-only) and the resource level (scoped IAM ARNs). Namespace scoping for CloudWatch and tag-based opt-in are implemented as operational governance controls by the monitoring system, complementing the IAM enforcement layers. Together, these controls satisfy the AC-3 requirement for access enforcement at the information system level.
