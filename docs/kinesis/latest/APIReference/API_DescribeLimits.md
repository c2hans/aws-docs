---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeLimits.html
---

# DescribeLimits
<a name="API_DescribeLimits"></a>

Describes the shard limits and usage for the account.

If you update your account limits, the old limits might be returned for a few minutes.

This operation has a limit of one transaction per second per account.

## Response Syntax
<a name="API_DescribeLimits_ResponseSyntax"></a>

```
{
   "ChannelCount": number,
   "ChannelCountLimit": number,
   "OnDemandStreamCount": number,
   "OnDemandStreamCountLimit": number,
   "OpenShardCount": number,
   "ShardLimit": number
}
```

## Response Elements
<a name="API_DescribeLimits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChannelCount](#API_DescribeLimits_ResponseSyntax) **   <a name="Streams-DescribeLimits-response-ChannelCount"></a>
The number of channels in the account.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000000.

 ** [ChannelCountLimit](#API_DescribeLimits_ResponseSyntax) **   <a name="Streams-DescribeLimits-response-ChannelCountLimit"></a>
The maximum number of channels allowed in the account.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000000.

 ** [OnDemandStreamCount](#API_DescribeLimits_ResponseSyntax) **   <a name="Streams-DescribeLimits-response-OnDemandStreamCount"></a>
 Indicates the number of data streams with the on-demand capacity mode.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000000.

 ** [OnDemandStreamCountLimit](#API_DescribeLimits_ResponseSyntax) **   <a name="Streams-DescribeLimits-response-OnDemandStreamCountLimit"></a>
 The maximum number of data streams with the on-demand capacity mode.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000000.

 ** [OpenShardCount](#API_DescribeLimits_ResponseSyntax) **   <a name="Streams-DescribeLimits-response-OpenShardCount"></a>
The number of open shards.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000000.

 ** [ShardLimit](#API_DescribeLimits_ResponseSyntax) **   <a name="Streams-DescribeLimits-response-ShardLimit"></a>
The maximum number of shards.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000000.

## Errors
<a name="API_DescribeLimits_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## Examples
<a name="API_DescribeLimits_Examples"></a>

### To display the shard limits for the account
<a name="API_DescribeLimits_Example_1"></a>

The following example displays the shard limits for the account.

#### Sample Request
<a name="API_DescribeLimits_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: kinesis.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Kinesis_20131202.DescribeLimits
```

#### Sample Response
<a name="API_DescribeLimits_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "OpenShardCount": 20,
    "ShardLimit": 70
}
```

## See Also
<a name="API_DescribeLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/DescribeLimits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/DescribeLimits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/DescribeLimits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/DescribeLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/DescribeLimits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/DescribeLimits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/DescribeLimits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/DescribeLimits)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DescribeLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/DescribeLimits)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
