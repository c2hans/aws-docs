---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_Stream.html
---

# Stream
<a name="API_streams_Stream"></a>

Represents all of the data describing a particular stream.

## Contents
<a name="API_streams_Stream_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** StreamArn **   <a name="DDB-Type-streams_Stream-StreamArn"></a>
The Amazon Resource Name (ARN) for the stream.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: No

 ** StreamLabel **   <a name="DDB-Type-streams_Stream-StreamLabel"></a>
A timestamp, in ISO 8601 format, for this stream.
Note that `LatestStreamLabel` is not a unique identifier for the stream, because it is possible that a stream from another table might have the same timestamp. However, the combination of the following three elements is guaranteed to be unique:
+ the AWS customer ID.
+ the table name
+ the `StreamLabel`
Type: String
Required: No

 ** TableName **   <a name="DDB-Type-streams_Stream-TableName"></a>
The DynamoDB table with which the stream is associated.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_streams_Stream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/streams-dynamodb-2012-08-10/Stream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/streams-dynamodb-2012-08-10/Stream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/streams-dynamodb-2012-08-10/Stream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
