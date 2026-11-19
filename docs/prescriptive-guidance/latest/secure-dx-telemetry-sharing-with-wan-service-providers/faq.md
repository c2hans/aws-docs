---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/faq.html
---

# FAQ

## General
<a name="general.de832eee-8f85-5625-9e61-6c02a94a6add"></a>

**Q1: What problem does this framework solve?**
+ AWS does not provide a native mechanism for customers to share Direct Connect telemetry with their WAN/Enterprise Service Providers. An operational visibility gap where diagnosing a DX issue requires 30–60 minutes of manual coordination before the WSP can begin troubleshooting may exceed a customer's required recovery timeline. The framework provides a secure, customer-controlled pattern to mitigate such a gap.

**Q2: Does this framework give the WSP write access to my account?**
+ No. The IAM policy grants exclusively read-only actions (Describe, List, Get). No write, update, or delete permissions are included. The WSP cannot modify any resource in your account.

**Q3: Does AWS replicate or export my data to the WSP's account?**
+ No. AWS does not move data. The WSP retrieves data via read-only API calls using temporary STS credentials. Any data the WSP stores is done in their own systems, outside of this framework.

**Q4: What does this cost?**
+ Less than $5/month. IAM, STS, and CloudFormation are free. Nominal charges apply for CloudWatch API calls (\~$0.01/1,000 metrics) and CloudTrail management event logging (first copy free per Region).

**Q5: What AWS services does this framework use?**

The framework leverages:
+ AWS IAM — Cross-account roles with External ID for confused deputy prevention
+ AWS STS — Temporary credential issuance via AssumeRole
+ Amazon CloudWatch — Direct Connect metrics (connection-level and VIF-level)
+ AWS CloudTrail — Audit logging of all cross-account access
+ AWS Config (optional) — Compliance rules to validate tag presence and role configuration
+ AWS Resource Groups & Tag Editor — "DXInfoSharing" tags for scoping access
+ AWS CloudFormation — Infrastructure-as-Code deployment

**Q6: What data can the WSP/ESP access through the shared role?**

The framework grants read-only access to:

1. Connection-level CloudWatch metrics (ConnectionState, ConnectionBpsIngress/Egress, ConnectionPpsIngress/Egress, ConnectionLightLevelTx/Rx)

1. Virtual Interface-level CloudWatch metrics (VirtualInterfaceBpsIngress/Egress, BGPStatus, BGP prefix counts)

1. Direct Connect resource descriptions (connections, VIFs, LAGs) via Describe APIs

1. Resource tags (contacts, circuit IDs, maintenance windows) scoped to DXInfoSharing=enabled tagged resources (see Limitations section for more info)

It does NOT grant access to billing data, VPC configurations, route tables, or any resources beyond the DX scope.

**Q7: Can multiple WSPs/ESPs be granted access simultaneously?**
+ Yes. Create a separate IAM role per WSP/ESP relationship, each with its own External ID and DXInfoSharing tag value. This ensures independent lifecycle management — revoking access for one provider does not affect another. Tag values should uniquely identify each provider relationship.

**Q8: What resiliency model should be in place before implementing this framework?**
+ This framework is independent of the DX resiliency model. However, AWS recommends that customers select a resiliency model (Maximum for 99.99% SLA, High for 99.9% SLA, or Development/Test) appropriate for their workload criticality before onboarding providers. The telemetry shared via this framework helps WSPs optimize routing and detect issues faster, which complements any resiliency model.

## Security
<a name="security.686fa08b-58b3-59b8-b4b5-8c0a6f1e5746"></a>

**Q1: What is ExternalId and why does it matter?**
+ ExternalId is a unique value the WSP must provide when assuming the role. It mitigates the "confused deputy" problem — without it, a malicious actor who knows your Role ARN could trick the WSP into assuming the role on their behalf. ExternalId is not a secret; it works because only the trusted principal account (the WSP) can assume the role, and only when providing the correct customer-specific value.

**Q2: Can the WSP see ALL my DX connections?**
+ The WSP can see connection IDs and state for all connections via Describe APIs (these don't support tag-based filtering). However, operational metadata (contacts, circuit IDs, maintenance windows) is only accessible for resources you explicitly tag with `DXInfoSharing=enabled`. You control exactly which resources provide visibility to enriched metadata.

**Q3: Why can't I use ExternalId AND the AWS Console Switch Role?**
+ The AWS Console Switch Role feature does not support passing an ExternalId parameter. If your trust policy requires ExternalId, Console role switching fails by design. You must choose: ExternalId enforcement (CLI/SDK only, stronger security) or Console compatibility (remove ExternalId condition, rely on tightly scoped Principal \+ CloudTrail monitoring).

**Q4: How do I immediately cut off the WSP's access during a security incident?**
+ Attach the `AWSRevokeOlderSessions` inline policy to the role. This uses the `aws:TokenIssueTime` condition key to deny all permissions for credentials issued before the revocation timestamp. Takes effect within seconds. New sessions assumed after revocation still work — combine with trust policy modification to block new assumptions entirely.

**Q5: How is access audited and monitored?**
+ Every AssumeRole call and subsequent API action is logged in AWS CloudTrail. The framework recommends setting CloudWatch Alarms on unusual access patterns (e.g., calls outside business hours, from unexpected source IPs) and using AWS Config rules to detect drift (missing tags, overly permissive policies). Periodic manual audits (quarterly) complement automated governance.

**Q6: What is the maximum session duration for assumed credentials?**
+ The IAM role's MaxSessionDuration controls how long temporary credentials remain valid (default 1 hour, configurable up to 12 hours). AWS recommends setting the shortest practical duration to limit exposure if credentials are compromised. The WSP's monitoring system should re-assume the role as needed rather than extending session durations.

## Partitions & Compliance
<a name="partitions-9999999999999999amp--compliance.5a3127cd-7f3a-5f63-928c-74878d7d704e"></a>

**Q1: Does this work in GovCloud and isolated partitions?**
+ Yes. The CloudFormation template uses `AWS::Partition` to construct all ARNs dynamically. The same template deploys without modification in any partition. Cross-partition federation is NOT supported — both accounts must be in the same partition.

**Q2: Which compliance frameworks does this align with?**
+ FedRAMP High (AC-3, AC-17, AU-2, AU-6), SOC 2 Type II (CC6.1, CC7.2), ITAR/EAR data residency requirements, and partition isolation requirements for isolated partitions.

**Q3: Can this framework be used with AWS Organizations and SCPs?**
+ Yes. AWS Organizations Service Control Policies (SCPs) can be layered on top of this framework to enforce guardrails. For example, you can use SCPs to restrict which external accounts are permitted in trust policies across your organization, ensuring that only approved WSP/ESP accounts can be trusted. The framework's IAM role delegation is fully compatible with SCP enforcement.

## Operations
<a name="operations.eec5d6d2-e852-5278-b005-a26fc81e339d"></a>

**Q1: How often should the ExternalId be rotated?**
+ Rotation must be aligned with organizational security policy. Annual rotation is the baseline recommendation. Rotate immediately if the trust relationship changes (personnel turnover, contract renegotiation) or compromise is suspected. Choose coordinated rotation (recommended, brief visibility gap) or remove-then-rotate (no gap, temporarily reduced confused deputy protection).

**Q2: What if EventBridge or Network Monitor isn't available in my partition?**
+ Option 1 (IAM role delegation) requires only IAM and STS — available in all partitions. Options 2–4 depend on EventBridge or Network Monitor availability, which varies. In isolated partitions, Option 1 alone provides substantial operational value.

**Q3: What happens when a WSP/ESP contract is terminated?**
+ The framework includes a decommissioning workflow: (1) revoke active sessions using AWSRevokeOlderSessions inline policy, (2) disable the role by removing the WSP/ESP principal from the trust policy, (3) delete the IAM role, (4) remove all DXInfoSharing tags from resources, (5) disable governance rules, (6) review CloudTrail logs for anomalies preceding termination, (7) document the revocation date and findings, and (8) notify the WSP/ESP that access has been permanently revoked.

**Q4: How does this reduce Mean Time to Recovery (MTTR)?**
+ Without this framework, time-to-diagnosis typically requires \~50 minutes of sequential human coordination (customer detects issue, logs in, identifies connection, contacts WSP, shares data). With the framework, the WSP independently detects degradation, queries metrics, retrieves contact info from tags, and begins diagnosis within \~3 minutes — a 94% reduction. The WSP contacts the customer with a preliminary diagnosis rather than a data request.
