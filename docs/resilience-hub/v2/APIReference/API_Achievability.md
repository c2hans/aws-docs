---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_Achievability.html
---

# Achievability
<a name="API_Achievability"></a>

Describes the achievability status of a service's resilience targets based on the most recent assessment.

## Contents
<a name="API_Achievability_Contents"></a>

 ** availabilitySlo **   <a name="ngresiliencehub-Type-Achievability-availabilitySlo"></a>
The achievability status of the availability SLO target for the service.
Type: String
Valid Values: `ACHIEVABLE | NOT_ACHIEVABLE`
Required: No

 ** dataRecoveryTimeBetweenBackups **   <a name="ngresiliencehub-Type-Achievability-dataRecoveryTimeBetweenBackups"></a>
The achievability status of the data recovery time between backups for the service.
Type: String
Valid Values: `ACHIEVABLE | NOT_ACHIEVABLE`
Required: No

 ** multiAzRtoRpo **   <a name="ngresiliencehub-Type-Achievability-multiAzRtoRpo"></a>
The achievability status of the multi-AZ RTO and RPO targets for the service.
Type: String
Valid Values: `ACHIEVABLE | NOT_ACHIEVABLE`
Required: No

 ** multiRegionRtoRpo **   <a name="ngresiliencehub-Type-Achievability-multiRegionRtoRpo"></a>
The achievability status of the multi-Region RTO and RPO targets for the service.
Type: String
Valid Values: `ACHIEVABLE | NOT_ACHIEVABLE`
Required: No

## See Also
<a name="API_Achievability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/Achievability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/Achievability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/Achievability)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
