---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_SparqlRecord.html
---

# SparqlRecord
<a name="API_SparqlRecord"></a>

A serialized SPARQL stream record capturing a change-log entry for the RDF graph.

## Contents
<a name="API_SparqlRecord_Contents"></a>

 ** commitTimestamp **   <a name="neptunedata-Type-SparqlRecord-commitTimestamp"></a>
The time at which the commit for the transaction was requested, in milliseconds from the Unix epoch.
Type: Long
Required: Yes

 ** data **   <a name="neptunedata-Type-SparqlRecord-data"></a>
The serialized SPARQL change record. The serialization formats of each record are described in more detail in [Serialization Formats in Neptune Streams](https://docs.aws.amazon.com/neptune/latest/userguide/streams-change-formats.html).
Type: [SparqlData](API_SparqlData.md) object
Required: Yes

 ** eventId **   <a name="neptunedata-Type-SparqlRecord-eventId"></a>
The sequence identifier of the stream change record.
Type: String to string map
Required: Yes

 ** op **   <a name="neptunedata-Type-SparqlRecord-op"></a>
The operation that created the change.
Type: String
Required: Yes

 ** isLastOp **   <a name="neptunedata-Type-SparqlRecord-isLastOp"></a>
Only present if this operation is the last one in its transaction. If present, it is set to true. It is useful for ensuring that an entire transaction is consumed.
Type: Boolean
Required: No

## See Also
<a name="API_SparqlRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/SparqlRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/SparqlRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/SparqlRecord)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Neptune Data API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
