---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_OpenLineageRunEventSummary.html
---

# OpenLineageRunEventSummary
<a name="API_OpenLineageRunEventSummary"></a>

The open lineage run event summary.

## Contents
<a name="API_OpenLineageRunEventSummary_Contents"></a>

 ** eventType **   <a name="datazone-Type-OpenLineageRunEventSummary-eventType"></a>
The event type of the open lineage run event summary.
Type: String
Valid Values: `START | RUNNING | COMPLETE | ABORT | FAIL | OTHER`
Required: No

 ** inputs **   <a name="datazone-Type-OpenLineageRunEventSummary-inputs"></a>
The inputs of the open lineage run event summary.
Type: Array of [NameIdentifier](API_NameIdentifier.md) objects
Required: No

 ** job **   <a name="datazone-Type-OpenLineageRunEventSummary-job"></a>
The job of the open lineage run event summary.
Type: [NameIdentifier](API_NameIdentifier.md) object
Required: No

 ** outputs **   <a name="datazone-Type-OpenLineageRunEventSummary-outputs"></a>
The outputs of the open lineage run event summary.
Type: Array of [NameIdentifier](API_NameIdentifier.md) objects
Required: No

 ** runId **   <a name="datazone-Type-OpenLineageRunEventSummary-runId"></a>
The runID of the open lineage run event summary.
Type: String
Required: No

## See Also
<a name="API_OpenLineageRunEventSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/OpenLineageRunEventSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/OpenLineageRunEventSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/OpenLineageRunEventSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
