---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/risk-and-mitigation-table.html
---

# Risk and Mitigation Table

The following table identifies the primary risks associated with the framework and the controls that mitigate each risk. The likelihood and impact ratings reflect a deployment where all recommended controls (ExternalId, CloudTrail, quarterly reviews) are in place.

|
|
| Risk | Likelihood | Impact | Mitigation |
| --- |--- |--- |--- |
| Unauthorized role assumption | Low | Disclosure of contact information | ExternalId condition. CloudTrail logging. Regular access reviews. |
| Data exfiltration via API | N/A | N/A - no path | Read-only access only. No data export capabilities. No S3/DB access. |
| Accidental read-only IAM role changed to mutating IAM role | Low | High | No write permissions. No iam:PassRole. No iam:Create\*. Scoped IAM self-audit. Utilize CloudTrail Alerts |
| Tag tampering / removal | Medium | Disclosure of contact information | AWS Config rules (where supported) or alternative compliance validation mechanisms, combined with periodic tag audits. |
| Confused deputy attack | Low (with ExternalId) / Medium (without) | Disclosure of contact information | ExternalId enforcement is configurable. When enabled, prevents confused deputy attacks. When removed for console compatibility, mitigation depends on tightly scoped Principal, least-privilege policy, and CloudTrail monitoring. |
| Stale access after contract end | Medium | Low | Quarterly access reviews. Documented revocation procedure. |
| ExternalId value misuse | Low | Medium | Periodic review or rotation aligned with organizational security policy. Unique value per customer relationship. Transmit via encrypted channel during initial exchange. Note: ExternalId alone is insufficient for role assumption without being the trusted principal. |

The highest-impact risks — unauthorized role assumption and confused deputy attacks — are mitigated by the ExternalId condition when it is enforced. When ExternalId enforcement is removed for console compatibility, mitigation depends on tightly scoped Principals, least-privilege permissions, and CloudTrail monitoring. Organizations should evaluate their security posture and trust relationship with the WSP/ESP before deciding whether to enforce or remove the ExternalId condition.
