---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ScheduledAction.html
---

# ScheduledAction
<a name="API_ScheduledAction"></a>

Information about a scheduled configuration change for an OpenSearch Service domain. This actions can be a [service software update](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html) or a [blue/green Auto-Tune enhancement](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html#auto-tune-types).

## Contents
<a name="API_ScheduledAction_Contents"></a>

 ** Id **   <a name="opensearchservice-Type-ScheduledAction-Id"></a>
The unique identifier of the scheduled action.
Type: String
Required: Yes

 ** ScheduledTime **   <a name="opensearchservice-Type-ScheduledAction-ScheduledTime"></a>
The time when the change is scheduled to happen.
Type: Long
Required: Yes

 ** Severity **   <a name="opensearchservice-Type-ScheduledAction-Severity"></a>
The severity of the action.
Type: String
Valid Values: `HIGH | MEDIUM | LOW`
Required: Yes

 ** Type **   <a name="opensearchservice-Type-ScheduledAction-Type"></a>
The type of action that will be taken on the domain.
Type: String
Valid Values: `SERVICE_SOFTWARE_UPDATE | JVM_HEAP_SIZE_TUNING | JVM_YOUNG_GEN_TUNING`
Required: Yes

 ** Cancellable **   <a name="opensearchservice-Type-ScheduledAction-Cancellable"></a>
Whether or not the scheduled action is cancellable.
Type: Boolean
Required: No

 ** Description **   <a name="opensearchservice-Type-ScheduledAction-Description"></a>
A description of the action to be taken.
Type: String
Required: No

 ** Mandatory **   <a name="opensearchservice-Type-ScheduledAction-Mandatory"></a>
Whether the action is required or optional.
Type: Boolean
Required: No

 ** ScheduledBy **   <a name="opensearchservice-Type-ScheduledAction-ScheduledBy"></a>
Whether the action was scheduled manually (`CUSTOMER`, or by OpenSearch Service automatically (`SYSTEM`).
Type: String
Valid Values: `CUSTOMER | SYSTEM`
Required: No

 ** Status **   <a name="opensearchservice-Type-ScheduledAction-Status"></a>
The current status of the scheduled action.
Type: String
Valid Values: `PENDING_UPDATE | IN_PROGRESS | FAILED | COMPLETED | NOT_ELIGIBLE | ELIGIBLE`
Required: No

## See Also
<a name="API_ScheduledAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ScheduledAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ScheduledAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ScheduledAction)
