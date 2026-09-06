---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_Stream.html
---

# Stream
<a name="API_Stream"></a>

Represents a change data capture stream for an Amazon Keyspaces table, which enables tracking and processing of data changes.

## Contents
<a name="API_Stream_Contents"></a>

 ** keyspaceName **   <a name="keyspaces-Type-Stream-keyspaceName"></a>
The name of the keyspace containing the table associated with this stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** streamArn **   <a name="keyspaces-Type-Stream-streamArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies this stream.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: Yes

 ** streamLabel **   <a name="keyspaces-Type-Stream-streamLabel"></a>
A unique identifier for this stream that can be used in stream operations.
Type: String
Required: Yes

 ** tableName **   <a name="keyspaces-Type-Stream-tableName"></a>
The name of the table associated with this stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

## See Also
<a name="API_Stream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspacesstreams-2024-09-09/Stream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspacesstreams-2024-09-09/Stream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/Stream)
