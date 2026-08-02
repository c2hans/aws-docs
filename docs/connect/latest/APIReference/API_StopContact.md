---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_StopContact.html
---

# StopContact
<a name="API_StopContact"></a>

Ends the specified contact. Use this API to stop queued callbacks. It does not work for voice contacts that use the following initiation methods:
+ DISCONNECT
+ TRANSFER
+ QUEUE\_TRANSFER
+ EXTERNAL\_OUTBOUND
+ MONITOR

Chat and task contacts can be terminated in any state, regardless of initiation method.

## Request Syntax
<a name="API_StopContact_RequestSyntax"></a>

```
POST /contact/stop HTTP/1.1
Content-type: application/json

{
   "ContactId": "{{string}}",
   "DisconnectReason": {
      "Code": "{{string}}"
   },
   "InstanceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StopContact_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StopContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ContactId](#API_StopContact_RequestSyntax) **   <a name="connect-StopContact-request-ContactId"></a>
The ID of the contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [DisconnectReason](#API_StopContact_RequestSyntax) **   <a name="connect-StopContact-request-DisconnectReason"></a>
The reason a contact can be disconnected. Only Connect Customer outbound campaigns can provide this field. For a list and description of all the possible disconnect reasons by channel (including outbound campaign voice contacts) see DisconnectReason under [ContactTraceRecord](https://docs.aws.amazon.com/connect/latest/adminguide/ctr-data-model.html#ctr-ContactTraceRecord) in the *Connect Customer Administrator Guide*.
Type: [DisconnectReason](API_DisconnectReason.md) object
Required: No

 ** [InstanceId](#API_StopContact_RequestSyntax) **   <a name="connect-StopContact-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_StopContact_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StopContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ContactNotFoundException **
The contact with the specified ID does not exist.
 ** Message **
The message.
HTTP Status Code: 410

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidActiveRegionException **
This exception occurs when an API request is made to a non-active region in an Amazon Connect instance configured with Amazon Connect Global Resiliency. For example, if the active region is US West (Oregon) and a request is made to US East (N. Virginia), the exception will be returned.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

## See Also
<a name="API_StopContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/StopContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/StopContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/StopContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/StopContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/StopContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/StopContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/StopContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/StopContact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/StopContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/StopContact)
