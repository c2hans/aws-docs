---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamSummary.html
---

# DescribeStreamSummary
<a name="API_DescribeStreamSummary"></a>

Provides a summarized description of the specified Kinesis data stream without the shard list.

**Note**
When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

The information returned includes the stream name, Amazon Resource Name (ARN), status, record retention period, approximate creation time, monitoring, encryption details, and open shard count.

 [DescribeStreamSummary](#API_DescribeStreamSummary) has a limit of 20 transactions per second per account.

## Request Syntax
<a name="API_DescribeStreamSummary_RequestSyntax"></a>

```
{
   "StreamARN": "{{string}}",
   "StreamId": "{{string}}",
   "StreamName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeStreamSummary_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [StreamARN](#API_DescribeStreamSummary_RequestSyntax) **   <a name="Streams-DescribeStreamSummary-request-StreamARN"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: No

 ** [StreamId](#API_DescribeStreamSummary_RequestSyntax) **   <a name="Streams-DescribeStreamSummary-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

 ** [StreamName](#API_DescribeStreamSummary_RequestSyntax) **   <a name="Streams-DescribeStreamSummary-request-StreamName"></a>
The name of the stream to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_DescribeStreamSummary_ResponseSyntax"></a>

```
{
   "StreamDescriptionSummary": {
      "ChannelCount": number,
      "ConsumerCount": number,
      "EncryptionType": "string",
      "EnhancedMonitoring": [
         {
            "ShardLevelMetrics": [ "string" ]
         }
      ],
      "KeyId": "string",
      "MaxRecordSizeInKiB": number,
      "OpenShardCount": number,
      "RetentionPeriodHours": number,
      "StreamARN": "string",
      "StreamCreationTimestamp": number,
      "StreamId": "string",
      "StreamModeDetails": {
         "StreamMode": "string"
      },
      "StreamName": "string",
      "StreamStatus": "string",
      "WarmThroughput": {
         "CurrentMiBps": number,
         "TargetMiBps": number
      }
   }
}
```

## Response Elements
<a name="API_DescribeStreamSummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StreamDescriptionSummary](#API_DescribeStreamSummary_ResponseSyntax) **   <a name="Streams-DescribeStreamSummary-response-StreamDescriptionSummary"></a>
A [StreamDescriptionSummary](API_StreamDescriptionSummary.md) containing information about the stream.
Type: [StreamDescriptionSummary](API_StreamDescriptionSummary.md) object

## Errors
<a name="API_DescribeStreamSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Specifies that you do not have the permissions required to perform this operation.
HTTP Status Code: 400

 ** InvalidArgumentException **
A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** LimitExceededException **
The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found. The stream might not be specified correctly.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## See Also
<a name="API_DescribeStreamSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/DescribeStreamSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/DescribeStreamSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/DescribeStreamSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/DescribeStreamSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/DescribeStreamSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/DescribeStreamSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/DescribeStreamSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/DescribeStreamSummary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DescribeStreamSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/DescribeStreamSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
