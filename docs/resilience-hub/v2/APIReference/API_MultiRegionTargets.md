---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_MultiRegionTargets.html
---

# MultiRegionTargets
<a name="API_MultiRegionTargets"></a>

Defines the multi-Region disaster recovery targets for a resilience policy.

## Contents
<a name="API_MultiRegionTargets_Contents"></a>

 ** disasterRecoveryApproach **   <a name="ngresiliencehub-Type-MultiRegionTargets-disasterRecoveryApproach"></a>
The disaster recovery approach for multi-Region.
Type: String
Valid Values: `ACTIVE_ACTIVE | HOT_STANDBY | WARM_STANDBY | PILOT_LIGHT | BACKUP_AND_RESTORE`
Required: No

 ** rpoInMinutes **   <a name="ngresiliencehub-Type-MultiRegionTargets-rpoInMinutes"></a>
The recovery point objective (RPO) target for multi-Region, in minutes.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** rtoInMinutes **   <a name="ngresiliencehub-Type-MultiRegionTargets-rtoInMinutes"></a>
The recovery time objective (RTO) target for multi-Region, in minutes.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_MultiRegionTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/MultiRegionTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/MultiRegionTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/MultiRegionTargets)
