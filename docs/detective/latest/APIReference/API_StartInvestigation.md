---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_StartInvestigation.html
---

# StartInvestigation
<a name="API_StartInvestigation"></a>

Detective investigations lets you investigate IAM users and IAM roles using indicators of compromise. An indicator of compromise (IOC) is an artifact observed in or on a network, system, or environment that can (with a high level of confidence) identify malicious activity or a security incident. `StartInvestigation` initiates an investigation on an entity in a behavior graph.

## Request Syntax
<a name="API_StartInvestigation_RequestSyntax"></a>

```
POST /investigations/startInvestigation HTTP/1.1
Content-type: application/json

{
   "EntityArn": "{{string}}",
   "GraphArn": "{{string}}",
   "ScopeEndTime": "{{string}}",
   "ScopeStartTime": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartInvestigation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartInvestigation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EntityArn](#API_StartInvestigation_RequestSyntax) **   <a name="detective-StartInvestigation-request-EntityArn"></a>
The unique Amazon Resource Name (ARN) of the IAM user and IAM role.
Type: String
Pattern: `^arn:.*`
Required: Yes

 ** [GraphArn](#API_StartInvestigation_RequestSyntax) **   <a name="detective-StartInvestigation-request-GraphArn"></a>
The Amazon Resource Name (ARN) of the behavior graph.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`
Required: Yes

 ** [ScopeEndTime](#API_StartInvestigation_RequestSyntax) **   <a name="detective-StartInvestigation-request-ScopeEndTime"></a>
The data and time when the investigation ended. The value is an UTC ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z`.
Type: Timestamp
Required: Yes

 ** [ScopeStartTime](#API_StartInvestigation_RequestSyntax) **   <a name="detective-StartInvestigation-request-ScopeStartTime"></a>
The data and time when the investigation began. The value is an UTC ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z`.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_StartInvestigation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "InvestigationId": "string"
}
```

## Response Elements
<a name="API_StartInvestigation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InvestigationId](#API_StartInvestigation_ResponseSyntax) **   <a name="detective-StartInvestigation-response-InvestigationId"></a>
The investigation ID of the investigation report.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `^[0-9]+$`

## Errors
<a name="API_StartInvestigation_Errors"></a>

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
<a name="API_StartInvestigation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/detective-2018-10-26/StartInvestigation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/detective-2018-10-26/StartInvestigation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/StartInvestigation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/detective-2018-10-26/StartInvestigation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/StartInvestigation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/detective-2018-10-26/StartInvestigation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/detective-2018-10-26/StartInvestigation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/detective-2018-10-26/StartInvestigation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/detective-2018-10-26/StartInvestigation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/StartInvestigation)
