---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_RepositorySyncEvent.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# RepositorySyncEvent
<a name="API_RepositorySyncEvent"></a>

Repository sync event detail data for a sync attempt.

## Contents
<a name="API_RepositorySyncEvent_Contents"></a>

 ** event **   <a name="proton-Type-RepositorySyncEvent-event"></a>
Event detail for a repository sync attempt.
Type: String
Required: Yes

 ** time **   <a name="proton-Type-RepositorySyncEvent-time"></a>
The time that the sync event occurred.
Type: Timestamp
Required: Yes

 ** type **   <a name="proton-Type-RepositorySyncEvent-type"></a>
The type of event.
Type: String
Required: Yes

 ** externalId **   <a name="proton-Type-RepositorySyncEvent-externalId"></a>
The external ID of the sync event.
Type: String
Required: No

## See Also
<a name="API_RepositorySyncEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/RepositorySyncEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/RepositorySyncEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/RepositorySyncEvent)
