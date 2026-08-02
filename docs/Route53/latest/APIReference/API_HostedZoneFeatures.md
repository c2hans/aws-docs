---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_HostedZoneFeatures.html
---

# HostedZoneFeatures
<a name="API_HostedZoneFeatures"></a>

Represents the features configuration for a hosted zone, including the status of various features and any associated failure reasons.

## Contents
<a name="API_HostedZoneFeatures_Contents"></a>

 ** AcceleratedRecoveryStatus **   <a name="Route53-Type-HostedZoneFeatures-AcceleratedRecoveryStatus"></a>
The current status of accelerated recovery for the hosted zone.
Type: String
Valid Values: `ENABLING | ENABLE_FAILED | ENABLING_HOSTED_ZONE_LOCKED | ENABLED | DISABLING | DISABLE_FAILED | DISABLED | DISABLING_HOSTED_ZONE_LOCKED`
Required: No

 ** FailureReasons **   <a name="Route53-Type-HostedZoneFeatures-FailureReasons"></a>
Information about any failures that occurred when attempting to enable or configure features for the hosted zone.
Type: [HostedZoneFailureReasons](API_HostedZoneFailureReasons.md) object
Required: No

## See Also
<a name="API_HostedZoneFeatures_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/HostedZoneFeatures)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/HostedZoneFeatures)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/HostedZoneFeatures)
