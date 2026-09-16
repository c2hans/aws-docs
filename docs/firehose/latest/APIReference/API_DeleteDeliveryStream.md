---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_DeleteDeliveryStream.html
---

# DeleteDeliveryStream
<a name="API_DeleteDeliveryStream"></a>

Deletes a Firehose stream and its data.

You can delete a Firehose stream only if it is in one of the following states: `ACTIVE`, `DELETING`, `CREATING_FAILED`, or `DELETING_FAILED`. You can't delete a Firehose stream that is in the `CREATING` state. To check the state of a Firehose stream, use [DescribeDeliveryStream](API_DescribeDeliveryStream.md).

DeleteDeliveryStream is an asynchronous API. When an API request to DeleteDeliveryStream succeeds, the Firehose stream is marked for deletion, and it goes into the `DELETING` state.While the Firehose stream is in the `DELETING` state, the service might continue to accept records, but it doesn't make any guarantees with respect to delivering the data. Therefore, as a best practice, first stop any applications that are sending records before you delete a Firehose stream.

Removal of a Firehose stream that is in the `DELETING` state is a low priority operation for the service. A stream may remain in the `DELETING` state for several minutes. Therefore, as a best practice, applications should not wait for streams in the `DELETING` state to be removed.

## Request Syntax
<a name="API_DeleteDeliveryStream_RequestSyntax"></a>

```
{
   "AllowForceDelete": {{boolean}},
   "DeliveryStreamName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDeliveryStream_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AllowForceDelete](#API_DeleteDeliveryStream_RequestSyntax) **   <a name="Firehose-DeleteDeliveryStream-request-AllowForceDelete"></a>
Set this to true if you want to delete the Firehose stream even if Firehose is unable to retire the grant for the CMK. Firehose might be unable to retire the grant due to a customer error, such as when the CMK or the grant are in an invalid state. If you force deletion, you can then use the [RevokeGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html) operation to revoke the grant you gave to Firehose. If a failure to retire the grant happens due to an AWS KMS issue, Firehose keeps retrying the delete operation.
The default value is false.
Type: Boolean
Required: No

 ** [DeliveryStreamName](#API_DeleteDeliveryStream_RequestSyntax) **   <a name="Firehose-DeleteDeliveryStream-request-DeliveryStreamName"></a>
The name of the Firehose stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Elements
<a name="API_DeleteDeliveryStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteDeliveryStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUseException **
The resource is already in use and not available for this operation.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## Examples
<a name="API_DeleteDeliveryStream_Examples"></a>

### Example
<a name="API_DeleteDeliveryStream_Example_1"></a>

The following JSON example deletes a Firehose stream named `exampleStreamName`.

#### Sample Request
<a name="API_DeleteDeliveryStream_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: firehose.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Firehose_20150804.DeleteDeliveryStream
{
    "DeliveryStreamName": "exampleStreamName"
}
```

#### Sample Response
<a name="API_DeleteDeliveryStream_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See Also
<a name="API_DeleteDeliveryStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/firehose-2015-08-04/DeleteDeliveryStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/firehose-2015-08-04/DeleteDeliveryStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/DeleteDeliveryStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/firehose-2015-08-04/DeleteDeliveryStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/DeleteDeliveryStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/firehose-2015-08-04/DeleteDeliveryStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/firehose-2015-08-04/DeleteDeliveryStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/firehose-2015-08-04/DeleteDeliveryStream)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/firehose-2015-08-04/DeleteDeliveryStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/DeleteDeliveryStream)
