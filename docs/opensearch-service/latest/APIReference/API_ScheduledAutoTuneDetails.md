---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ScheduledAutoTuneDetails.html
---

# ScheduledAutoTuneDetails
<a name="API_ScheduledAutoTuneDetails"></a>

Specifies details about a scheduled Auto-Tune action. For more information, see [Auto-Tune for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html).

## Contents
<a name="API_ScheduledAutoTuneDetails_Contents"></a>

 ** Action **   <a name="opensearchservice-Type-ScheduledAutoTuneDetails-Action"></a>
A description of the Auto-Tune action.
Type: String
Required: No

 ** ActionType **   <a name="opensearchservice-Type-ScheduledAutoTuneDetails-ActionType"></a>
The type of Auto-Tune action.
Type: String
Valid Values: `JVM_HEAP_SIZE_TUNING | JVM_YOUNG_GEN_TUNING`
Required: No

 ** Date **   <a name="opensearchservice-Type-ScheduledAutoTuneDetails-Date"></a>
The date and time when the Auto-Tune action is scheduled for the domain.
Type: Timestamp
Required: No

 ** Severity **   <a name="opensearchservice-Type-ScheduledAutoTuneDetails-Severity"></a>
The severity of the Auto-Tune action. Valid values are `LOW`, `MEDIUM`, and `HIGH`.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

## See Also
<a name="API_ScheduledAutoTuneDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ScheduledAutoTuneDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ScheduledAutoTuneDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ScheduledAutoTuneDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
