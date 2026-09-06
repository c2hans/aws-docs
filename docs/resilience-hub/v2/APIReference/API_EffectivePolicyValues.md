---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_EffectivePolicyValues.html
---

# EffectivePolicyValues
<a name="API_EffectivePolicyValues"></a>

Contains the effective resilience policy values for a service.

## Contents
<a name="API_EffectivePolicyValues_Contents"></a>

 ** availabilitySlo **   <a name="ngresiliencehub-Type-EffectivePolicyValues-availabilitySlo"></a>
The effective availability SLO value for the service.
Type: [SloSource](API_SloSource.md) object
Required: No

 ** dataRecoveryTimeBetweenBackups **   <a name="ngresiliencehub-Type-EffectivePolicyValues-dataRecoveryTimeBetweenBackups"></a>
The effective data recovery time between backups value for the service.
Type: [TargetSource](API_TargetSource.md) object
Required: No

 ** multiAzDrApproach **   <a name="ngresiliencehub-Type-EffectivePolicyValues-multiAzDrApproach"></a>
The effective multi-AZ disaster recovery approach for the service.
Type: [DisasterRecoverySource](API_DisasterRecoverySource.md) object
Required: No

 ** multiAzRpo **   <a name="ngresiliencehub-Type-EffectivePolicyValues-multiAzRpo"></a>
The effective multi-AZ RPO value for the service, in minutes.
Type: [TargetSource](API_TargetSource.md) object
Required: No

 ** multiAzRto **   <a name="ngresiliencehub-Type-EffectivePolicyValues-multiAzRto"></a>
The effective multi-AZ RTO value for the service, in minutes.
Type: [TargetSource](API_TargetSource.md) object
Required: No

 ** multiRegionDrApproach **   <a name="ngresiliencehub-Type-EffectivePolicyValues-multiRegionDrApproach"></a>
The effective multi-Region disaster recovery approach for the service.
Type: [DisasterRecoverySource](API_DisasterRecoverySource.md) object
Required: No

 ** multiRegionRpo **   <a name="ngresiliencehub-Type-EffectivePolicyValues-multiRegionRpo"></a>
The effective multi-Region RPO value for the service, in minutes.
Type: [TargetSource](API_TargetSource.md) object
Required: No

 ** multiRegionRto **   <a name="ngresiliencehub-Type-EffectivePolicyValues-multiRegionRto"></a>
The effective multi-Region RTO value for the service, in minutes.
Type: [TargetSource](API_TargetSource.md) object
Required: No

## See Also
<a name="API_EffectivePolicyValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/EffectivePolicyValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/EffectivePolicyValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/EffectivePolicyValues)
