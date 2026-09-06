---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_UpdateInvestigationState.html
---

# UpdateInvestigationState
<a name="API_UpdateInvestigationState"></a>

Updates the state of an investigation.

## Request Syntax
<a name="API_UpdateInvestigationState_RequestSyntax"></a>

```
POST /investigations/updateInvestigationState HTTP/1.1
Content-type: application/json

{
   "GraphArn": "{{string}}",
   "InvestigationId": "{{string}}",
   "State": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateInvestigationState_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateInvestigationState_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GraphArn](#API_UpdateInvestigationState_RequestSyntax) **   <a name="detective-UpdateInvestigationState-request-GraphArn"></a>
The Amazon Resource Name (ARN) of the behavior graph.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`
Required: Yes

 ** [InvestigationId](#API_UpdateInvestigationState_RequestSyntax) **   <a name="detective-UpdateInvestigationState-request-InvestigationId"></a>
The investigation ID of the investigation report.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `^[0-9]+$`
Required: Yes

 ** [State](#API_UpdateInvestigationState_RequestSyntax) **   <a name="detective-UpdateInvestigationState-request-State"></a>
The current state of the investigation. An archived investigation indicates you have completed reviewing the investigation.
Type: String
Valid Values: `ACTIVE | ARCHIVED`
Required: Yes

## Response Syntax
<a name="API_UpdateInvestigationState_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateInvestigationState_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateInvestigationState_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request issuer does not have permission to access this resource or perform this operation.
 ** ErrorCode **
The SDK default error code associated with the access denied exception.
 ** ErrorCodeReason **
The SDK default explanation of why access was denied.
 ** SubErrorCode **
The error code associated with the access denied exception.
 ** SubErrorCodeReason **
 An explanation of why access was denied.
HTTP Status Code: 403

 ** InternalServerException **
The request was valid but failed because of a problem with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request refers to a nonexistent resource.
HTTP Status Code: 404

 ** TooManyRequestsException **
The request cannot be completed because too many other requests are occurring at the same time.
HTTP Status Code: 429

 ** ValidationException **
The request parameters are invalid.
 ** ErrorCode **
The error code associated with the validation failure.
 ** ErrorCodeReason **
 An explanation of why validation failed.
HTTP Status Code: 400

## See Also
<a name="API_UpdateInvestigationState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/detective-2018-10-26/UpdateInvestigationState)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/detective-2018-10-26/UpdateInvestigationState)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/UpdateInvestigationState)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/detective-2018-10-26/UpdateInvestigationState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/UpdateInvestigationState)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/detective-2018-10-26/UpdateInvestigationState)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/detective-2018-10-26/UpdateInvestigationState)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/detective-2018-10-26/UpdateInvestigationState)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/detective-2018-10-26/UpdateInvestigationState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/UpdateInvestigationState)
