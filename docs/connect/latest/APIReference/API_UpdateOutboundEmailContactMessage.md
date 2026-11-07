---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateOutboundEmailContactMessage.html
---

# UpdateOutboundEmailContactMessage
<a name="API_UpdateOutboundEmailContactMessage"></a>

Updates the draft outbound email message for a contact. Use this operation to save changes to an in-progress outbound email reply before you send it. This operation applies only to contacts with an `OUTBOUND` or `AGENT_REPLY` initiation method; it isn't supported for flow-initiated emails.

## Request Syntax
<a name="API_UpdateOutboundEmailContactMessage_RequestSyntax"></a>

```
PUT /instances/{{InstanceId}}/contacts/{{ContactId}}/outbound-email-message HTTP/1.1
Content-type: application/json

{
   "EmailMessage": {
      "MessageSourceType": "{{string}}",
      "RawMessage": {
         "Body": "{{string}}",
         "ContentType": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateOutboundEmailContactMessage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactId](#API_UpdateOutboundEmailContactMessage_RequestSyntax) **   <a name="connect-UpdateOutboundEmailContactMessage-request-uri-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_UpdateOutboundEmailContactMessage_RequestSyntax) **   <a name="connect-UpdateOutboundEmailContactMessage-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_UpdateOutboundEmailContactMessage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EmailMessage](#API_UpdateOutboundEmailContactMessage_RequestSyntax) **   <a name="connect-UpdateOutboundEmailContactMessage-request-EmailMessage"></a>
The email message body to update on the outbound email draft.
Type: [UpdateOutboundEmailContent](API_UpdateOutboundEmailContent.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateOutboundEmailContactMessage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactId": "string"
}
```

## Response Elements
<a name="API_UpdateOutboundEmailContactMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactId](#API_UpdateOutboundEmailContactMessage_ResponseSyntax) **   <a name="connect-UpdateOutboundEmailContactMessage-response-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_UpdateOutboundEmailContactMessage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateOutboundEmailContactMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateOutboundEmailContactMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateOutboundEmailContactMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateOutboundEmailContactMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateOutboundEmailContactMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateOutboundEmailContactMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateOutboundEmailContactMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateOutboundEmailContactMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateOutboundEmailContactMessage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateOutboundEmailContactMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateOutboundEmailContactMessage)
