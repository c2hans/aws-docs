---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AutoTuneOptionsInput.html
---

# AutoTuneOptionsInput
<a name="API_AutoTuneOptionsInput"></a>

Options for configuring Auto-Tune. For more information, see [Auto-Tune for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html)

## Contents
<a name="API_AutoTuneOptionsInput_Contents"></a>

 ** DesiredState **   <a name="opensearchservice-Type-AutoTuneOptionsInput-DesiredState"></a>
Whether Auto-Tune is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** MaintenanceSchedules **   <a name="opensearchservice-Type-AutoTuneOptionsInput-MaintenanceSchedules"></a>
A list of maintenance schedules during which Auto-Tune can deploy changes. Maintenance windows are deprecated and have been replaced with [off-peak windows](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html).
Type: Array of [AutoTuneMaintenanceSchedule](API_AutoTuneMaintenanceSchedule.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** UseOffPeakWindow **   <a name="opensearchservice-Type-AutoTuneOptionsInput-UseOffPeakWindow"></a>
Whether to schedule Auto-Tune optimizations that require blue/green deployments during the domain's configured daily off-peak window.
Type: Boolean
Required: No

## See Also
<a name="API_AutoTuneOptionsInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AutoTuneOptionsInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AutoTuneOptionsInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AutoTuneOptionsInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
