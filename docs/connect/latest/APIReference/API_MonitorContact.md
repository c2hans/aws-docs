---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_MonitorContact.html
---

# MonitorContact
<a name="API_MonitorContact"></a>

Initiates silent monitoring of a contact. The Contact Control Panel (CCP) of the user specified by *userId* will be set to silent monitoring mode on the contact.

## Request Syntax
<a name="API_MonitorContact_RequestSyntax"></a>

```
POST /contact/monitor HTTP/1.1
Content-type: application/json

{
   "AllowedMonitorCapabilities": [ "{{string}}" ],
   "ClientToken": "{{string}}",
   "ContactId": "{{string}}",
   "InstanceId": "{{string}}",
   "UserId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_MonitorContact_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_MonitorContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AllowedMonitorCapabilities](#API_MonitorContact_RequestSyntax) **   <a name="connect-MonitorContact-request-AllowedMonitorCapabilities"></a>
Specify which monitoring actions the user is allowed to take. For example, whether the user is allowed to escalate from silent monitoring to barge. AllowedMonitorCapabilities is required if barge is enabled.
Type: Array of strings
Array Members: Maximum number of 2 items.
Valid Values: `SILENT_MONITOR | BARGE`
Required: No

 ** [ClientToken](#API_MonitorContact_RequestSyntax) **   <a name="connect-MonitorContact-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [ContactId](#API_MonitorContact_RequestSyntax) **   <a name="connect-MonitorContact-request-ContactId"></a>
The identifier of the contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_MonitorContact_RequestSyntax) **   <a name="connect-MonitorContact-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [UserId](#API_MonitorContact_RequestSyntax) **   <a name="connect-MonitorContact-request-UserId"></a>
The identifier of the user account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_MonitorContact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactArn": "string",
   "ContactId": "string"
}
```

## Response Elements
<a name="API_MonitorContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactArn](#API_MonitorContact_ResponseSyntax) **   <a name="connect-MonitorContact-response-ContactArn"></a>
The ARN of the contact.
Type: String

 ** [ContactId](#API_MonitorContact_ResponseSyntax) **   <a name="connect-MonitorContact-response-ContactId"></a>
The identifier of the contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_MonitorContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** IdempotencyException **
An entity with the same name already exists.
HTTP Status Code: 409

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_MonitorContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/MonitorContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/MonitorContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/MonitorContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/MonitorContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/MonitorContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/MonitorContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/MonitorContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/MonitorContact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/MonitorContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/MonitorContact)
