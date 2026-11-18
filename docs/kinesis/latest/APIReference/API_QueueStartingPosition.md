---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_QueueStartingPosition.html
---

# QueueStartingPosition
<a name="API_QueueStartingPosition"></a>

The position in a data stream from which a queue begins delivering records.

## Contents
<a name="API_QueueStartingPosition_Contents"></a>

 ** Type **   <a name="Streams-Type-QueueStartingPosition-Type"></a>
You can set the starting position to one of the following values:
 `LATEST`: Delivers records that arrive after you create the queue. This is the default.
 `TRIM_HORIZON`: Start delivering at the last untrimmed record in the stream, which is the oldest record the stream still retains.
 `AT_TIMESTAMP`: Delivers records that arrive at or after a time stamp that you provide.
Type: String
Valid Values: `TRIM_HORIZON | LATEST | AT_TIMESTAMP`
Required: Yes

 ** Timestamp **   <a name="Streams-Type-QueueStartingPosition-Timestamp"></a>
The approximate time from which the queue begins delivering records. Records that arrive at approximately this time or later are delivered.
In a request, specify this value only when `Type` is `AT_TIMESTAMP`. It is required in that case, and specifying it for any other type returns a `ValidationException`.
In a response, this value is approximate and reflects the queue's effective starting position. While the queue is `CREATING`, the response echoes what you configured: for `AT_TIMESTAMP`, the timestamp you provided, and for `TRIM_HORIZON` and `LATEST`, this member is absent because the effective position is not yet determined. Once the queue is `ACTIVE`, the response always includes this member. For `AT_TIMESTAMP`, it is the timestamp you provided or the earliest time the stream can be read from, whichever is later.
Type: Timestamp
Required: No

## See Also
<a name="API_QueueStartingPosition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/QueueStartingPosition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/QueueStartingPosition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/QueueStartingPosition)
