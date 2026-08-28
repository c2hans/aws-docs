---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AutoTuneOptions.html
---

# AutoTuneOptions
<a name="API_AutoTuneOptions"></a>

Auto-Tune settings when updating a domain. For more information, see [Auto-Tune for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html).

## Contents
<a name="API_AutoTuneOptions_Contents"></a>

 ** DesiredState **   <a name="opensearchservice-Type-AutoTuneOptions-DesiredState"></a>
Whether Auto-Tune is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** MaintenanceSchedules **   <a name="opensearchservice-Type-AutoTuneOptions-MaintenanceSchedules"></a>
DEPRECATED. Use [off-peak window](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html) instead.
A list of maintenance schedules during which Auto-Tune can deploy changes.
Type: Array of [AutoTuneMaintenanceSchedule](API_AutoTuneMaintenanceSchedule.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** RollbackOnDisable **   <a name="opensearchservice-Type-AutoTuneOptions-RollbackOnDisable"></a>
When disabling Auto-Tune, specify `NO_ROLLBACK` to retain all prior Auto-Tune settings or `DEFAULT_ROLLBACK` to revert to the OpenSearch Service defaults. If you specify `DEFAULT_ROLLBACK`, you must include a `MaintenanceSchedule` in the request. Otherwise, OpenSearch Service is unable to perform the rollback.
Type: String
Valid Values: `NO_ROLLBACK | DEFAULT_ROLLBACK`
Required: No

 ** UseOffPeakWindow **   <a name="opensearchservice-Type-AutoTuneOptions-UseOffPeakWindow"></a>
Whether to use the domain's [off-peak window](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_OffPeakWindow.html) to deploy configuration changes on the domain rather than a maintenance schedule.
Type: Boolean
Required: No

## See Also
<a name="API_AutoTuneOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AutoTuneOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AutoTuneOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AutoTuneOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
