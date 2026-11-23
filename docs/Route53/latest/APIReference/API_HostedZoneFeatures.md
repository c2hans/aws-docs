---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_HostedZoneFeatures.html
---

# HostedZoneFeatures

Represents the features configuration for a hosted zone, including the status of various features and any associated failure reasons.

## Contents
<a name="API_HostedZoneFeatures_Contents"></a>

 ** AcceleratedRecoveryStatus **   <a name="Route53-Type-HostedZoneFeatures-AcceleratedRecoveryStatus"></a>
The current status of accelerated recovery for the hosted zone.
Type: String
Valid Values: `ENABLING | ENABLE_FAILED | ENABLING_HOSTED_ZONE_LOCKED | ENABLED | DISABLING | DISABLE_FAILED | DISABLED | DISABLING_HOSTED_ZONE_LOCKED`
Required: No

 ** ChangeGuardrails **   <a name="Route53-Type-HostedZoneFeatures-ChangeGuardrails"></a>
The name and status of each Change Guardrail for the hosted zone. For the guardrail names and statuses, see `ChangeGuardrail`.
Type: Array of [ChangeGuardrail](API_ChangeGuardrail.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** ChangeHistory **   <a name="Route53-Type-HostedZoneFeatures-ChangeHistory"></a>
The status of Change History for the hosted zone, and the earliest time from which you can read its change history.
Type: [ChangeHistoryFeature](API_ChangeHistoryFeature.md) object
Required: No

 ** FailureReasons **   <a name="Route53-Type-HostedZoneFeatures-FailureReasons"></a>
Information about any failures that occurred when attempting to enable or configure features for the hosted zone.
Type: [HostedZoneFailureReasons](API_HostedZoneFailureReasons.md) object
Required: No

 ** PublicDNSFallbackStatus **   <a name="Route53-Type-HostedZoneFeatures-PublicDNSFallbackStatus"></a>
The current status of public DNS fallback for the hosted zone. Valid values:
+  `ENABLED`: Public DNS fallback is enabled.
+  `DISABLED`: Public DNS fallback is disabled.
+  `ENABLING`: A request to enable public DNS fallback is still propagating.
+  `DISABLING`: A request to disable public DNS fallback is still propagating.
Type: String
Valid Values: `ENABLED | DISABLED | ENABLING | DISABLING`
Required: No

## See Also
<a name="API_HostedZoneFeatures_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/HostedZoneFeatures)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/HostedZoneFeatures)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/HostedZoneFeatures)
