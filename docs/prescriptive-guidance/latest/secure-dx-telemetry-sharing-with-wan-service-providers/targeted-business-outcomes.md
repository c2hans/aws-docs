---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/targeted-business-outcomes.html
---

# Targeted business outcomes

**Targeted outcomes include MTTR reduction (\~94%); support case reduction (30% target); near-zero cost (<$5/mo); and compliance alignment (FedRAMP, SOC 2, ITAR/EAR). See below for a complete listing of targeted outcomes. **

|
|
| **Outcome** | **Description** | **Measurable Impact** |
| --- |--- |--- |
| **Reduce Mean Time to Recovery (MTTR)** | Transform troubleshooting from reactive, sequential coordination to proactive, parallel diagnosis by giving WSP/ESPs independent read-only access to DX telemetry | \~94% reduction in time-to-diagnosis (from \~50 min to \~3 min in illustrative scenarios) |
| **Eliminate Manual Coordination Overhead** | Remove the need for customers to manually gather and relay connection data during outages | Avoid 30–60 minutes of sequential phone/email coordination per incident |
| **Reduce AWS Support Escalations** | Enable WSP/ESP self-service troubleshooting so issues are resolved without opening support cases | Target 30% reduction in "Is DX broken?" support cases within 6 months |
| **Improve Hybrid Connectivity Reliability** | Give providers full topology visibility (Maximum Resiliency, High Resiliency, Dev/Test models) to make informed restoration decisions | WSP can assess redundancy impact without requesting topology from customer mid-incident |
| **Strengthen Security & Compliance Posture** | Replace ad-hoc credential sharing or screenshot exchanges with a governed, auditable, least-privilege IAM pattern | Full CloudTrail audit trail; maps to FedRAMP High (AC-3, AC-17, AU-2), SOC 2 Type II (CC6.1, CC7.2), and ITAR/EAR controls |
| **Enable Partition-Independent Operations** | Single CloudFormation template deploys across all AWS partitions with no code changes | Uniform operational model across classified and unclassified environments |
| **Near-Zero Cost to Operate** | Framework uses IAM, STS, and CloudFormation (all free-tier); only CloudWatch API and CloudTrail logging incur nominal charges | < $5/month base cost for a typical deployment |
