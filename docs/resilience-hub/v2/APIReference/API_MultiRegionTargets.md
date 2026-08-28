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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
