---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/limitations-and-trade-offs.html
---

# Limitations and Trade-offs

This framework provides secure, auditable telemetry sharing with the following design trade-offs.

Describe API scope: Direct Connect Describe APIs return all connections and virtual interfaces in the account regardless of tags. The WSP/ESP can enumerate connection identifiers and state for all connections. Tag-based scoping applies only to operational metadata retrieved via the Resource Groups Tagging API.

Logical tag filtering: The DXInfoSharing=enabled tag is a governance-driven opt-in mechanism. The IAM policy does not enforce resource-level tag restrictions for tag:GetResources. Enforcement depends on the WSP/ESP including correct TagFilters in API requests, combined with tagging standards and periodic audits.

Polling model: Option 1 relies on periodic API polling. Detection latency depends on the WSP/ESP's monitoring frequency. Supplement with EventBridge (Option 2) for sub-minute notification requirements.

EventBridge delivery: Direct Connect events reach EventBridge via CloudTrail on a best-effort basis. Suitable for notification workflows, not guaranteed real-time telemetry.

Cross-partition restriction: Role assumption is supported only within the same AWS partition. Cross-partition federation is not supported.

AWS Config does not natively support Direct Connect connection and virtual interface resource types in all environments. Where customers require tag integrity validation, implement a custom compliance mechanism (for example, a custom AWS Config rule where appropriate, or scheduled audits) to verify required tags and detect unauthorized tag removal.

ExternalId tradeoff: The framework originally enforced an ExternalId condition in the trust policy to mitigate confused deputy attacks. This enforcement prevents AWS Console-based role switching because the Console Switch Role feature does not support passing an ExternalId parameter. Organizations must decide whether to maintain ExternalId enforcement (stronger third-party security posture, CLI/SDK access only) or remove it (console compatibility, reduced confused deputy protection). This is an architectural decision that must align with organizational security policy and the trust level established with the WSP/ESP.

Some AWS services aren't available in all AWS Regions. For Region availability, see the Service endpoints and quotas page in the AWS documentation, and choose the link for the service.
