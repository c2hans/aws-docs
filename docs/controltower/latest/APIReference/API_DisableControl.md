---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_DisableControl.html
---

# DisableControl
<a name="API_DisableControl"></a>

This API call turns off a control. It starts an asynchronous operation that deletes AWS resources on the specified organizational unit and the accounts it contains. The resources will vary according to the control that you specify. For usage examples, see the [*Controls Reference Guide*](https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html).

## Request Syntax
<a name="API_DisableControl_RequestSyntax"></a>

```
POST /disable-control HTTP/1.1
Content-type: application/json

{
   "controlIdentifier": "{{string}}",
   "enabledControlIdentifier": "{{string}}",
   "targetIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DisableControl_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DisableControl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [controlIdentifier](#API_DisableControl_RequestSyntax) **   <a name="controltower-DisableControl-request-controlIdentifier"></a>
The ARN of the control. Only **Strongly recommended** and **Elective** controls are permitted, with the exception of the **Region deny** control. For information on how to find the `controlIdentifier`, see [the overview page](https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** [enabledControlIdentifier](#API_DisableControl_RequestSyntax) **   <a name="controltower-DisableControl-request-enabledControlIdentifier"></a>
The ARN of the enabled control to be disabled, which uniquely identifies the control instance on the target organizational unit.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** [targetIdentifier](#API_DisableControl_RequestSyntax) **   <a name="controltower-DisableControl-request-targetIdentifier"></a>
The ARN of the organizational unit. For information on how to find the `targetIdentifier`, see [the overview page](https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

## Response Syntax
<a name="API_DisableControl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "operationIdentifier": "string"
}
```

## Response Elements
<a name="API_DisableControl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operationIdentifier](#API_DisableControl_ResponseSyntax) **   <a name="controltower-DisableControl-response-operationIdentifier"></a>
The ID of the asynchronous operation, which is used to track status. The operation is available for 90 days.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_DisableControl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting the resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during processing of a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded. See [Service quotas](https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html).
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DisableControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controltower-2018-05-10/DisableControl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/DisableControl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/DisableControl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controltower-2018-05-10/DisableControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/DisableControl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controltower-2018-05-10/DisableControl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controltower-2018-05-10/DisableControl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controltower-2018-05-10/DisableControl)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/DisableControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/DisableControl)
