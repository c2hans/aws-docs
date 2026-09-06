---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_PropertygraphRecord.html
---

# PropertygraphRecord
<a name="API_PropertygraphRecord"></a>

Structure of a property graph record.

## Contents
<a name="API_PropertygraphRecord_Contents"></a>

 ** commitTimestamp **   <a name="neptunedata-Type-PropertygraphRecord-commitTimestamp"></a>
The time at which the commit for the transaction was requested, in milliseconds from the Unix epoch.
Type: Long
Required: Yes

 ** data **   <a name="neptunedata-Type-PropertygraphRecord-data"></a>
The serialized Gremlin or openCypher change record.
Type: [PropertygraphData](API_PropertygraphData.md) object
Required: Yes

 ** eventId **   <a name="neptunedata-Type-PropertygraphRecord-eventId"></a>
The sequence identifier of the stream change record.
Type: String to string map
Required: Yes

 ** op **   <a name="neptunedata-Type-PropertygraphRecord-op"></a>
The operation that created the change.
Type: String
Required: Yes

 ** isLastOp **   <a name="neptunedata-Type-PropertygraphRecord-isLastOp"></a>
Only present if this operation is the last one in its transaction. If present, it is set to true. It is useful for ensuring that an entire transaction is consumed.
Type: Boolean
Required: No

## See Also
<a name="API_PropertygraphRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/PropertygraphRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/PropertygraphRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/PropertygraphRecord)
