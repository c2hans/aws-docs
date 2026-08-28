---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_StreamRecord.html
---

# StreamRecord
<a name="API_streams_StreamRecord"></a>

A description of a single data modification that was performed on an item in a DynamoDB table.

## Contents
<a name="API_streams_StreamRecord_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ApproximateCreationDateTime **   <a name="DDB-Type-streams_StreamRecord-ApproximateCreationDateTime"></a>
The approximate date and time when the stream record was created, in [UNIX epoch time](http://www.epochconverter.com/) format and rounded down to the closest second. Some tools and SDKs may convert this value to a different format, such as [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html).
Type: Timestamp
Required: No

 ** Keys **   <a name="DDB-Type-streams_StreamRecord-Keys"></a>
The primary key attribute(s) for the DynamoDB item that was modified.
Type: String to [AttributeValue](API_streams_AttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.
Required: No

 ** NewImage **   <a name="DDB-Type-streams_StreamRecord-NewImage"></a>
The item in the DynamoDB table as it appeared after it was modified.
Type: String to [AttributeValue](API_streams_AttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.
Required: No

 ** OldImage **   <a name="DDB-Type-streams_StreamRecord-OldImage"></a>
The item in the DynamoDB table as it appeared before it was modified.
Type: String to [AttributeValue](API_streams_AttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.
Required: No

 ** SequenceNumber **   <a name="DDB-Type-streams_StreamRecord-SequenceNumber"></a>
The sequence number of the stream record.
Type: String
Length Constraints: Minimum length of 21. Maximum length of 40.
Required: No

 ** SizeBytes **   <a name="DDB-Type-streams_StreamRecord-SizeBytes"></a>
The size of the stream record, in bytes.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** StreamViewType **   <a name="DDB-Type-streams_StreamRecord-StreamViewType"></a>
The type of data from the modified DynamoDB item that was captured in this stream record:
+  `KEYS_ONLY` - only the key attributes of the modified item.
+  `NEW_IMAGE` - the entire item, as it appeared after it was modified.
+  `OLD_IMAGE` - the entire item, as it appeared before it was modified.
+  `NEW_AND_OLD_IMAGES` - both the new and the old item images of the item.
Type: String
Valid Values: `NEW_IMAGE | OLD_IMAGE | NEW_AND_OLD_IMAGES | KEYS_ONLY`
Required: No

## See Also
<a name="API_streams_StreamRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/streams-dynamodb-2012-08-10/StreamRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/streams-dynamodb-2012-08-10/StreamRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/streams-dynamodb-2012-08-10/StreamRecord)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
