---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ServiceSyncBlockerSummary.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ServiceSyncBlockerSummary
<a name="API_ServiceSyncBlockerSummary"></a>

If a service instance is manually updated, Proton wants to prevent accidentally overriding a manual change.

A blocker is created because of the manual update or deletion of a service instance. The summary describes the blocker as being active or resolved.

## Contents
<a name="API_ServiceSyncBlockerSummary_Contents"></a>

 ** serviceName **   <a name="proton-Type-ServiceSyncBlockerSummary-serviceName"></a>
The name of the service that you want to get the sync blocker summary for. If given a service instance name and a service name, it will return the blockers only applying to the instance that is blocked.
If given only a service name, it will return the blockers that apply to all of the instances. In order to get the blockers for a single instance, you will need to make two distinct calls, one to get the sync blocker summary for the service and the other to get the sync blocker for the service instance.
Type: String
Required: Yes

 ** latestBlockers **   <a name="proton-Type-ServiceSyncBlockerSummary-latestBlockers"></a>
The latest active blockers for the synced service.
Type: Array of [SyncBlocker](API_SyncBlocker.md) objects
Required: No

 ** serviceInstanceName **   <a name="proton-Type-ServiceSyncBlockerSummary-serviceInstanceName"></a>
The name of the service instance that you want sync your service configuration with.
Type: String
Required: No

## See Also
<a name="API_ServiceSyncBlockerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ServiceSyncBlockerSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ServiceSyncBlockerSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ServiceSyncBlockerSummary)
