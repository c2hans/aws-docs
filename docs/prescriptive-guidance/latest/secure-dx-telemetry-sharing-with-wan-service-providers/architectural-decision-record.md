---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/architectural-decision-record.html
---

# Architectural Decision Record

Cross-account IAM role delegation was selected as the primary pattern after evaluating four candidate approaches against the constraints identified.

## Context and Constraints
<a name="context-and-constraints.6b5a455b-8c59-583a-a987-249dd8d0ea8a"></a>

AWS does not provide a native DX telemetry sharing feature. The solution must be customer-controlled, partition-independent, and must not require the WSP/ESP to deploy infrastructure in the customer account.

## Options Evaluated
<a name="options-evaluated.6a583eaf-b261-5674-bb08-12d959095ddf"></a>

Option 1 (IAM role delegation) provides the broadest data access — describe APIs, CloudWatch metrics, and resource tags — using standard AWS security primitives. Option 2 (EventBridge) provides event-driven notifications via CloudTrail integration, but no metric or tag access. Option 3 (CloudWatch Network Synthetic Monitor) provides fault isolation metrics (NHI) but requires VPC deployment and depends on Option 1 for sharing. Option 4 (AWS Health events) provides AWS-side health awareness but no customer-side data.

## Decision and Rationale
<a name="decision-and-rationale.b3de044e-55c0-5495-8dfc-46bc1b17cb5f"></a>

Option 1 satisfies all constraints and provides the broadest operational value. AWS Security Token Service (AWS STS) temporary credentials prevent long-term key exposure, the ExternalIdcondition prevents confused deputy attacks, and CloudTrail provides a complete audit trail. The pattern requires no additional AWS services, which is critical for AWS partitions with fewer services available. Options 2 through 4 are documented as complementary patterns for specific use cases.

**Note**
*AWS RAM does not support sharing CloudWatch metrics or dashboards. CloudWatch Cross-Account Observability (OAM) is a separate feature requiring mutual opt-in and is not required for this framework.*
