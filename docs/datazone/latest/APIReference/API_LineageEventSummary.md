---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_LineageEventSummary.html
---

# LineageEventSummary
<a name="API_LineageEventSummary"></a>

The data lineage event summary.

## Contents
<a name="API_LineageEventSummary_Contents"></a>

 ** createdAt **   <a name="datazone-Type-LineageEventSummary-createdAt"></a>
The timestamp at which data lineage event was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-LineageEventSummary-createdBy"></a>
The user who created the data lineage event.
Type: String
Required: No

 ** domainId **   <a name="datazone-Type-LineageEventSummary-domainId"></a>
The domain ID of the lineage event.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: No

 ** eventSummary **   <a name="datazone-Type-LineageEventSummary-eventSummary"></a>
The summary of the data lineate event.
Type: [EventSummary](API_EventSummary.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** eventTime **   <a name="datazone-Type-LineageEventSummary-eventTime"></a>
The time of the data lineage event.
Type: Timestamp
Required: No

 ** id **   <a name="datazone-Type-LineageEventSummary-id"></a>
The ID of the data lineage event.
Type: String
Pattern: `[a-z0-9]{14}`
Required: No

 ** processingStatus **   <a name="datazone-Type-LineageEventSummary-processingStatus"></a>
The processing status of the data lineage event.
Type: String
Valid Values: `REQUESTED | PROCESSING | SUCCESS | FAILED`
Required: No

## See Also
<a name="API_LineageEventSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/LineageEventSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/LineageEventSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/LineageEventSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
