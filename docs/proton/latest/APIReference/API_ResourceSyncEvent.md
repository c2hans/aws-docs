---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ResourceSyncEvent.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ResourceSyncEvent
<a name="API_ResourceSyncEvent"></a>

Detail data for a resource sync event.

## Contents
<a name="API_ResourceSyncEvent_Contents"></a>

 ** event **   <a name="proton-Type-ResourceSyncEvent-event"></a>
A resource sync event.
Type: String
Required: Yes

 ** time **   <a name="proton-Type-ResourceSyncEvent-time"></a>
The time when the event occurred.
Type: Timestamp
Required: Yes

 ** type **   <a name="proton-Type-ResourceSyncEvent-type"></a>
The type of event.
Type: String
Required: Yes

 ** externalId **   <a name="proton-Type-ResourceSyncEvent-externalId"></a>
The external ID for the event.
Type: String
Required: No

## See Also
<a name="API_ResourceSyncEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ResourceSyncEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ResourceSyncEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ResourceSyncEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
