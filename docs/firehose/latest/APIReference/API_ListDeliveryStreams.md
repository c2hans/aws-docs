---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_ListDeliveryStreams.html
---

# ListDeliveryStreams
<a name="API_ListDeliveryStreams"></a>

Lists your Firehose streams in alphabetical order of their names.

The number of Firehose streams might be too large to return using a single call to `ListDeliveryStreams`. You can limit the number of Firehose streams returned, using the `Limit` parameter. To determine whether there are more delivery streams to list, check the value of `HasMoreDeliveryStreams` in the output. If there are more Firehose streams to list, you can request them by calling this operation again and setting the `ExclusiveStartDeliveryStreamName` parameter to the name of the last Firehose stream returned in the last call.

## Request Syntax
<a name="API_ListDeliveryStreams_RequestSyntax"></a>

```
{
   "DeliveryStreamType": "{{string}}",
   "ExclusiveStartDeliveryStreamName": "{{string}}",
   "Limit": {{number}}
}
```

## Request Parameters
<a name="API_ListDeliveryStreams_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DeliveryStreamType](#API_ListDeliveryStreams_RequestSyntax) **   <a name="Firehose-ListDeliveryStreams-request-DeliveryStreamType"></a>
The Firehose stream type. This can be one of the following values:
+  `DirectPut`: Provider applications access the Firehose stream directly.
+  `KinesisStreamAsSource`: The Firehose stream uses a Kinesis data stream as a source.
This parameter is optional. If this parameter is omitted, Firehose streams of all types are returned.
Type: String
Valid Values: `DirectPut | KinesisStreamAsSource | MSKAsSource | DatabaseAsSource`
Required: No

 ** [ExclusiveStartDeliveryStreamName](#API_ListDeliveryStreams_RequestSyntax) **   <a name="Firehose-ListDeliveryStreams-request-ExclusiveStartDeliveryStreamName"></a>
The list of Firehose streams returned by this call to `ListDeliveryStreams` will start with the Firehose stream whose name comes alphabetically immediately after the name you specify in `ExclusiveStartDeliveryStreamName`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** [Limit](#API_ListDeliveryStreams_RequestSyntax) **   <a name="Firehose-ListDeliveryStreams-request-Limit"></a>
The maximum number of Firehose streams to list. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

## Response Syntax
<a name="API_ListDeliveryStreams_ResponseSyntax"></a>

```
{
   "DeliveryStreamNames": [ "string" ],
   "HasMoreDeliveryStreams": boolean
}
```

## Response Elements
<a name="API_ListDeliveryStreams_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeliveryStreamNames](#API_ListDeliveryStreams_ResponseSyntax) **   <a name="Firehose-ListDeliveryStreams-response-DeliveryStreamNames"></a>
The names of the Firehose streams.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [HasMoreDeliveryStreams](#API_ListDeliveryStreams_ResponseSyntax) **   <a name="Firehose-ListDeliveryStreams-response-HasMoreDeliveryStreams"></a>
Indicates whether there are more Firehose streams available to list.
Type: Boolean

## Errors
<a name="API_ListDeliveryStreams_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ListDeliveryStreams_Examples"></a>

### Example
<a name="API_ListDeliveryStreams_Example_1"></a>

The following JSON example lists up to three Firehose streams configured for `DirectPut`. The response indicates that there are more `DirectPut` Firehose streams to be listed. To list the remaining `DirectPut` Firehose streams, set `DeliveryStreamType` to `DirectPut` and `ExclusiveStartDeliveryStreamName` to `last_stream_in_first_listing`, and then run the operation again.

#### Sample Request
<a name="API_ListDeliveryStreams_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: firehose.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Firehose_20150804.ListDeliveryStreams
{
    "DeliveryStreamType": "DirectPut",
    "Limit": 3
}
```

#### Sample Response
<a name="API_ListDeliveryStreams_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "DeliveryStreamNames": [
        "some_delivery_stream",
        "another_example_delivery_stream",
        "last_stream_in_first_listing"
    ],
    "HasMoreDeliveryStreams": true
}
```

## See Also
<a name="API_ListDeliveryStreams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/firehose-2015-08-04/ListDeliveryStreams)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/firehose-2015-08-04/ListDeliveryStreams)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/ListDeliveryStreams)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/firehose-2015-08-04/ListDeliveryStreams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/ListDeliveryStreams)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/firehose-2015-08-04/ListDeliveryStreams)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/firehose-2015-08-04/ListDeliveryStreams)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/firehose-2015-08-04/ListDeliveryStreams)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/firehose-2015-08-04/ListDeliveryStreams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/ListDeliveryStreams)
