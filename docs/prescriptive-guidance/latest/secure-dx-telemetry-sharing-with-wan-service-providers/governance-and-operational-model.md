---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/governance-and-operational-model.html
---

# Governance and Operational Model

Deploying the framework is only the first step. Sustaining its value requires an operational model that keeps tags accurate, access reviews current, and compliance monitoring active. This section defines the governance structure and operational cadence.

## Two-Tier Opt-In Process
<a name="two-tier-opt-in-process.147262ee-3e12-5cbe-9965-9341411278a7"></a>

The framework uses a two-tier consent model to ensure that information sharing is both organizationally sanctioned and individually consented. At the first tier, the organization's cloud governance team reviews the IAM policy, evaluates the security controls, and authorizes deployment of the role template across participating accounts. This organizational approval establishes the policy framework but does not, by itself, expose any customer data.

At the second tier, individual account owners decide whether to participate by tagging their Direct Connect resources with DXInfoSharing=enabled. Until an account owner applies this tag, no operational metadata is accessible to the WSP/ESP through the Resource Groups Tagging API. This two-tier model respects both organizational governance and individual account autonomy.

## Operational Cadence
<a name="operational-cadence.9be7ab54-ca35-519e-bb60-708a99a7c612"></a>

The following table defines the recommended operational activities, their frequency, and the responsible team. *The frequencies in this table are provided as illustrative guidance. Actual cadence should be aligned with organizational security policy, risk posture, and applicable compliance requirements.*

|
|
| Activity | Frequency[AC1] [CC2] | Owner |
| --- |--- |--- |
| Review CloudTrail logs for ESP access patterns | Per organizational security policy | Security / Network Ops |
| Monitor governance compliance (if implemented) | Weekly | Cloud Governance |
| Verify tag accuracy on DX resources | Monthly | Network Ops |
| Conduct ESP access review | Quarterly | Security / Compliance |
| Rotate ExternalId | Annually | Cloud Admin |
| Tag new DX connections/VIFs | On creation | Network Ops |
| Update tags when contacts change | On change | Network Ops |
| Remove tags from decommissioned resources | On decommission | Network Ops |

The quarterly access review is the most important governance activity. During this review, the security team verifies that the WSP/ESP still has a legitimate business need for access, that the ExternalId remains current and aligned with the active trust relationship, and that the ESP personnel authorized to use the role are current. The review outcome should be documented and retained per the organization's compliance requirements.

## Revocation Procedures
<a name="revocation-procedures.8baf8dbd-653f-5535-880b-aa2b86abd76f"></a>

The framework provides four graduated revocation methods each appropriate for different scenarios.

|
|
| Level | Method | Effect | Reversible |
| --- |--- |--- |--- |
| **Scope reduction** | Remove DXInfoSharing=enabled tags from resources | WSP/ESP can still assume role and query describe APIs and CloudWatch metrics, but tag:GetResources returns no operational metadata. Does not invalidate issued STS credentials. | Yes |
| **Session revocation** | Attach AWSRevokeOlderSessions inline policy to role | All credentials issued before the revocation timestamp are denied. New sessions assumed after revocation remain functional. Role remains intact and assumable. | Yes |
| **Role disablement** | Modify trust policy to remove WSP/ESP principal, or attach deny-all policy | Prevents new role assumptions. Does not invalidate already-issued credentials; combine with session revocation for complete effect. | Yes |
| **Role deletion** | Delete DXNetworkOperatorRole | Permanent removal. Requires redeployment to restore. AWS recommends considering disablement before deletion. | No (redeploy) |

Scope reduction is appropriate when the customer wants to limit the operational metadata visible to the WSP/ESP while preserving their ability to view connection state and metrics. Session revocation is appropriate during a security incident when in-flight credentials must be invalidated immediately — this is the fastest-acting mechanism documented by AWS and takes effect within seconds. Role disablement is appropriate when the customer wants to prevent new role assumptions while preserving the role for potential re-enablement; combine with session revocation to ensure complete access termination. Role deletion is appropriate when the trust relationship is permanently ended. After role deletion, the customer should review CloudTrail logs for unauthorized activity, follow organizational incident response procedures, and determine whether to redeploy the framework.

## Lifecycle Management
<a name="lifecycle-management.dccb86c4-b62a-5cd2-9de8-f4031450bd89"></a>

Sustaining the framework over time requires deliberate lifecycle management. The ExternalId should be reviewed periodically and rotated when required by organizational security policy, when the trust relationship changes, or if compromise is suspected. Where rotation is implemented, organizations should select an approach that aligns with their tolerance for temporary visibility impairment versus temporary reduction in confused deputy protection. Access reviews should be performed at a cadence defined by the organization, ideally using automated controls where possible, to verify that the WSP/ESP continues to have a legitimate business need for access, that the ExternalId remains aligned with the active trust relationship, and that only authorized personnel retain access. Tag audits should also be performed periodically, and where possible mechanized, to ensure that contact information remains accurate, that new Direct Connect resources are appropriately tagged, and that decommissioned resources have had their tags removed.

When a WSP/ESP contract is terminated, execute the following decommissioning workflow as part of the contract offboarding process: (1) revoke active sessions by attaching the AWSRevokeOlderSessions inline policy, (2) disable the role by modifying the trust policy to remove the WSP/ESP principal, (3) delete the IAM role, (4) remove all DXInfoSharing tags from resources, (5) disable any governance validation mechanisms (Config rules, scheduled audits), (6) review CloudTrail logs for a period preceding termination, (7) document the revocation date, reason, and review findings, and (8) notify the WSP/ESP that access has been permanently revoked.
