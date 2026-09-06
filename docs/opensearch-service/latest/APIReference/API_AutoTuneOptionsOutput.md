---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AutoTuneOptionsOutput.html
---

# AutoTuneOptionsOutput
<a name="API_AutoTuneOptionsOutput"></a>

The Auto-Tune settings for a domain, displayed when enabling or disabling Auto-Tune.

## Contents
<a name="API_AutoTuneOptionsOutput_Contents"></a>

 ** ErrorMessage **   <a name="opensearchservice-Type-AutoTuneOptionsOutput-ErrorMessage"></a>
Any errors that occurred while enabling or disabling Auto-Tune.
Type: String
Required: No

 ** State **   <a name="opensearchservice-Type-AutoTuneOptionsOutput-State"></a>
The current state of Auto-Tune on the domain.
Type: String
Valid Values: `ENABLED | DISABLED | ENABLE_IN_PROGRESS | DISABLE_IN_PROGRESS | DISABLED_AND_ROLLBACK_SCHEDULED | DISABLED_AND_ROLLBACK_IN_PROGRESS | DISABLED_AND_ROLLBACK_COMPLETE | DISABLED_AND_ROLLBACK_ERROR | ERROR`
Required: No

 ** UseOffPeakWindow **   <a name="opensearchservice-Type-AutoTuneOptionsOutput-UseOffPeakWindow"></a>
Whether the domain's off-peak window will be used to deploy Auto-Tune changes rather than a maintenance schedule.
Type: Boolean
Required: No

## See Also
<a name="API_AutoTuneOptionsOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AutoTuneOptionsOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AutoTuneOptionsOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AutoTuneOptionsOutput)
