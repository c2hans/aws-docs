---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/best-practices.html
---

# Best practices

Best practices are organized into Architecture & Design, Security, and Operations & Governance categories. You will also find best practices to employ before, during, and after deployment in this section, followed by helpful tips.

## Architecture and Design
<a name="architecture-and-design.3c967ca7-d279-5fa1-b2b8-bc1400eac670"></a>

1. **Deploy Option 1 (Cross-Account IAM Role) as your baseline** — it is the only option that provides connection configuration, CloudWatch metrics, and resource tag metadata. No other option substitutes for it.

1. **Layer complementary options based on operational need:**
   + Add EventBridge (Option 2) \+ Health Events (Option 4) for real-time alerting
   + Add CloudWatch Network Synthetic Monitor (Option 3) for fault isolation and NHI metrics
   + In isolated partitions with limited service availability, Option 1 alone provides substantial value

1. **Use the two-tier opt-in model:**
   + Tier 1 — Organizational governance team approves and authorizes the IAM role template
   + Tier 2 — Individual account owners tag DX resources with `DXInfoSharing=enabled` before metadata is accessible

1. **Maintain partition independence** — Use `AWS::Partition` in all CloudFormation ARN references; never hardcode partition strings.

## Security
<a name="security.a7646e61-9475-5d75-a799-7c109bc987d6"></a>

1. **Enforce ExternalId by default (Deployment Model A)** — Remove only when the ESP account is fully trusted and console role switching is required. Document the architectural decision.

1. **Generate ExternalId as UUID v4** — unique per customer relationship, stored consistently, transmitted via encrypted channel, and rotated aligned with organizational security policy.

1. **Grant least privilege rigorously:**
   + Read-only actions only (Describe, List, Get)
   + No `iam:PassRole`, no `iam:Create*`, no `iam:Update*`, no `iam:Delete*`
   + IAM self-audit scoped exclusively to the operator role and policy ARNs

1. **Enforce RoleSessionName conventions** — Require descriptive session names (e.g., `wsp-monitoring-system`, `noc-operator-jsmith`) via SCPs for meaningful CloudTrail analysis.

1. **Scope CloudWatch queries operationally to **`AWS/DX` (and `AWS/NetworkMonitor` if applicable) — IAM cannot enforce namespace-level conditions on CloudWatch read APIs; discipline is enforced at the monitoring workflow level.

## Operations and Governance
<a name="operations-and-governance.3ef2acb8-07e3-546d-94e7-cc6c2a51feec"></a>

1. **Tag all DX resources in your resiliency topology** — Include connections across all locations so the WSP can assess redundancy during a failure.

1. **Maintain resource tags as living metadata:**
   + Tag on creation; update on contact change; remove on decommission
   + Include: `AccountPOC`, `TechnicalPOC`, `NOCContact`, `Criticality`, circuit IDs, maintenance windows

1. **Conduct quarterly access reviews** — Verify business need, ExternalId currency, and authorized personnel. Document outcomes.

1. **Implement graduated revocation** — Know the four levels (scope reduction → session revocation → role disablement → role deletion) and escalate only as needed.

1. **Execute a formal offboarding workflow** when a WSP/ESP contract ends — revoke sessions, disable role, delete role, remove all tags, review CloudTrail, document actions.

## Before Deployment
<a name="before-deployment.c429f935-072f-568d-834e-9656ccd89bd2"></a>
+ **Identify your DX resiliency model **(Maximum, High, or Dev/Test) — this determines how many connections need tagging and informs the WSP about failover behavior.
+ **Establish a tagging standard — **Define mandatory tags (DXInfoSharing, AccountPOC, TechnicalPOC, NOCContact, Criticality) and assign ownership for maintenance.
+ **Make an architectural decision on ExternalId — **Document whether you'll enforce it (Model A) or remove it for console compatibility (Model B). Get security team sign-off.
+ **Coordinate with your WSP/ESP — **Confirm they have an AWS account in the same partition and that their monitoring system supports STS AssumeRole. Exchange ExternalId via encrypted channel.
+ **Verify service availability **in your target partition/Region — Especially CloudWatch Network Synthetic Monitor and EventBridge if deploying Options 2–4.
+ **Review your organization's cross-account access stance — **Ensure your security team approves the trust policy pattern. Consider using AWS Organizations SCPs to restrict which external accounts can be trusted.
+ **Assess CloudWatch VIF-level metrics availability — **Since March 2026, AWS Direct Connect supports BGP health metrics and prefix count at the VIF level. Confirm these are available in your Region for enhanced provider visibility.

## During Deployment
<a name="during-deployment.4e55ef3a-9ef5-565e-bacc-73a958c78d40"></a>
+ **Deploy the CloudFormation stack** using the operational runbook commands
+ **Tag DX resources incrementally** — Start with your most critical connections, validate WSP access, then expand.
+ **Validate role assumption from the WSP account** using CLI commands before relying on automated monitoring.
+ **Confirm CloudTrail is capturing events** for the `DXNetworkOperatorRole`.
+ **Test with temporary credentials yourself — **Before granting access to the WSP/ESP, test the role using aws sts assume-role with the External ID to validate the access scope and confirm least-privilege.
+ **Verify tag-based scoping — **Confirm that tag:GetResources with TagFilters for DXInfoSharing=enabled returns only the intended resources. Check for untagged resources that should be included.

## After Deployment
<a name="after-deployment.6c1bb139-adc6-5a34-9c2e-ffd90ac554de"></a>
+ **Establish your operational cadence:**
  + Weekly: governance compliance monitoring (if implemented)
  + Monthly: tag accuracy verification
  + Quarterly: formal WSP access review
  + Annually: ExternalId rotation
+ **Measure MTTR improvement** — Establish a baseline before deployment and compare incident timelines after.
+ **Train NOC teams** — Ensure your operations center knows the revocation procedures and escalation paths.
+ **Plan for WSP transitions** — If you change providers, execute the full offboarding workflow before onboarding the new WSP.
+ **Integrate with AWS Security Hub — **Feed Config rule findings and CloudTrail anomaly detections into Security Hub for centralized visibility and automated remediation workflows.
+ **Enable CloudWatch Alarms for DX metrics — **Set alarms on ConnectionState changes, optical light level thresholds (ConnectionLightLevelRx/Tx), and BGP status transitions. These complement the WSP's monitoring and provide customer-side awareness.
+ **Document the relationship register — **Maintain a register mapping each IAM role ARN, External ID, provider identity, tagged resources, and contract expiration date for audit readiness.

## Tips for Isolated Partitions
<a name="tips-for-isolated-partitions.d53d5f4d-b195-5536-9de5-cb5bbe9b9252"></a>
+ Coordinate with your Cloud Provisioning Office (CPO) early — additional clearances may be required.
+ The tag-based metadata approach is especially valuable in isolated partitions where external collaboration tools are limited.
+ Verify DX, CloudWatch, and (if needed) Config availability in your target Region before building automation around them
+ In all AWS partitions, Option 1 (IAM role delegation) alone provides substantial operational value since EventBridge and Network Monitor may not be available.

## Additional Tips and Recommendations
<a name="additional-tips-and-recommendations.79158316-d269-572d-937d-a34f1bf2ef7c"></a>
+ **Use unique External IDs per relationship: **Generate a UUID for each WSP/ESP engagement. Never reuse External IDs across providers.
+ **Tag early, tag consistently: **Apply DXInfoSharing tags at resource creation time using AWS CloudFormation, Terraform, or AWS Service Catalog. Retroactive tagging is error-prone.
+ **Leverage CloudWatch VIF-level metrics: **Since March 2026, AWS Direct Connect supports BGP health metrics and prefix count at the VIF level in CloudWatch. Share these with providers for faster BGP troubleshooting.
+ **Automate governance with AWS Config: **Deploy custom Config rules that check for: (a) DXInfoSharing tag presence on all DX resources, (b) IAM role policy compliance, (c) trust policy External ID presence.
+ **Implement session duration limits: **Set the maximum session duration on the IAM role to the shortest practical period (e.g., 1 hour). This limits the window of exposure if a session token is compromised.
+ **Consider CloudWatch Metric Streams for real-time: **For providers requiring near-real-time telemetry, consider CloudWatch Metric Streams to push DX metrics to a Kinesis Data Firehose destination the provider controls, instead of pull-based GetMetricData calls.
+ **Adopt Infrastructure as Code: **Define the IAM role, trust policy, and Config rules in AWS CloudFormation or Terraform. This ensures reproducibility, version control, and drift detection.
+ **Review Well-Architected Framework Reliability Pillar: **Ensure your overall DX architecture aligns with REL02-BP02 (Provision redundant connectivity between private networks) before optimizing telemetry sharing.
