---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ResourceDiscoveryStatus.html
---

# ResourceDiscoveryStatus
<a name="API_ResourceDiscoveryStatus"></a>

Contains the status of resource discovery for a service.

## Contents
<a name="API_ResourceDiscoveryStatus_Contents"></a>

 ** errorCode **   <a name="ngresiliencehub-Type-ResourceDiscoveryStatus-errorCode"></a>
The error code if resource discovery failed.
Type: String
Valid Values: `INVALID_PERMISSIONS | STACK_NOT_FOUND | CLUSTER_NOT_FOUND | STATE_FILE_NOT_FOUND | ACCESS_DENIED | UNSUPPORTED_CLUSTER | INTERNAL_ERROR`
Required: No

 ** errorMessage **   <a name="ngresiliencehub-Type-ResourceDiscoveryStatus-errorMessage"></a>
A message describing the error if resource discovery failed.
Type: String
Required: No

 ** lastRunAt **   <a name="ngresiliencehub-Type-ResourceDiscoveryStatus-lastRunAt"></a>
The timestamp of the last resource discovery run.
Type: Timestamp
Required: No

 ** status **   <a name="ngresiliencehub-Type-ResourceDiscoveryStatus-status"></a>
The current status of resource discovery.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | COMPLETED_WITH_FAILURES | NOT_STARTED`
Required: No

## See Also
<a name="API_ResourceDiscoveryStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ResourceDiscoveryStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ResourceDiscoveryStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ResourceDiscoveryStatus)
