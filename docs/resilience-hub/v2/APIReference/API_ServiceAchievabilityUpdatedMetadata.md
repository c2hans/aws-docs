---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ServiceAchievabilityUpdatedMetadata.html
---

# ServiceAchievabilityUpdatedMetadata
<a name="API_ServiceAchievabilityUpdatedMetadata"></a>

Metadata for a service achievability updated event.

## Contents
<a name="API_ServiceAchievabilityUpdatedMetadata_Contents"></a>

 ** assessmentId **   <a name="ngresiliencehub-Type-ServiceAchievabilityUpdatedMetadata-assessmentId"></a>
The assessment identifier that triggered the update.
Type: String
Required: No

 ** availabilitySlo **   <a name="ngresiliencehub-Type-ServiceAchievabilityUpdatedMetadata-availabilitySlo"></a>
The updated achievability status of the availability SLO.
Type: String
Required: No

 ** multiAzRtoRpo **   <a name="ngresiliencehub-Type-ServiceAchievabilityUpdatedMetadata-multiAzRtoRpo"></a>
The updated achievability status of the multi-AZ RTO and RPO targets.
Type: String
Required: No

 ** multiRegionRtoRpo **   <a name="ngresiliencehub-Type-ServiceAchievabilityUpdatedMetadata-multiRegionRtoRpo"></a>
The updated achievability status of the multi-Region RTO and RPO targets.
Type: String
Required: No

## See Also
<a name="API_ServiceAchievabilityUpdatedMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ServiceAchievabilityUpdatedMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ServiceAchievabilityUpdatedMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ServiceAchievabilityUpdatedMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
