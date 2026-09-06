---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AutoTuneStatus.html
---

# AutoTuneStatus
<a name="API_AutoTuneStatus"></a>

The current status of Auto-Tune for the domain. For more information, see [Auto-Tune for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html).

## Contents
<a name="API_AutoTuneStatus_Contents"></a>

 ** CreationDate **   <a name="opensearchservice-Type-AutoTuneStatus-CreationDate"></a>
Date and time when Auto-Tune was enabled for the domain.
Type: Timestamp
Required: Yes

 ** State **   <a name="opensearchservice-Type-AutoTuneStatus-State"></a>
The current state of Auto-Tune on the domain.
Type: String
Valid Values: `ENABLED | DISABLED | ENABLE_IN_PROGRESS | DISABLE_IN_PROGRESS | DISABLED_AND_ROLLBACK_SCHEDULED | DISABLED_AND_ROLLBACK_IN_PROGRESS | DISABLED_AND_ROLLBACK_COMPLETE | DISABLED_AND_ROLLBACK_ERROR | ERROR`
Required: Yes

 ** UpdateDate **   <a name="opensearchservice-Type-AutoTuneStatus-UpdateDate"></a>
Date and time when the Auto-Tune options were last updated for the domain.
Type: Timestamp
Required: Yes

 ** ErrorMessage **   <a name="opensearchservice-Type-AutoTuneStatus-ErrorMessage"></a>
Any errors that occurred while enabling or disabling Auto-Tune.
Type: String
Required: No

 ** PendingDeletion **   <a name="opensearchservice-Type-AutoTuneStatus-PendingDeletion"></a>
Indicates whether the domain is being deleted.
Type: Boolean
Required: No

 ** UpdateVersion **   <a name="opensearchservice-Type-AutoTuneStatus-UpdateVersion"></a>
The latest version of the Auto-Tune options.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_AutoTuneStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AutoTuneStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AutoTuneStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AutoTuneStatus)
