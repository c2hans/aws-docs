---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListTestGridSessions.html
---

# ListTestGridSessions
<a name="API_ListTestGridSessions"></a>

Retrieves a list of sessions for a [TestGridProject](API_TestGridProject.md).

## Request Syntax
<a name="API_ListTestGridSessions_RequestSyntax"></a>

```
{
   "creationTimeAfter": {{number}},
   "creationTimeBefore": {{number}},
   "endTimeAfter": {{number}},
   "endTimeBefore": {{number}},
   "maxResult": {{number}},
   "nextToken": "{{string}}",
   "projectArn": "{{string}}",
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTestGridSessions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [creationTimeAfter](#API_ListTestGridSessions_RequestSyntax) **   <a name="devicefarm-ListTestGridSessions-request-creationTimeAfter"></a>
Return only sessions created after this time.
Type: Timestamp
Required: No

 ** [creationTimeBefore](#API_ListTestGridSessions_RequestSyntax) **   <a name="devicefarm-ListTestGridSessions-request-creationTimeBefore"></a>
Return only sessions created before this time.
Type: Timestamp
Required: No

 ** [endTimeAfter](#API_ListTestGridSessions_RequestSyntax) **   <a name="devicefarm-ListTestGridSessions-request-endTimeAfter"></a>
Return only sessions that ended after this time.
Type: Timestamp
Required: No

 ** [endTimeBefore](#API_ListTestGridSessions_RequestSyntax) **   <a name="devicefarm-ListTestGridSessions-request-endTimeBefore"></a>
Return only sessions that ended before this time.
Type: Timestamp
Required: No

 ** [maxResult](#API_ListTestGridSessions_RequestSyntax) **   <a name="devicefarm-ListTestGridSessions-request-maxResult"></a>
Return only this many results at a time.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListTestGridSessions_RequestSyntax) **   <a name="devicefarm-ListTestGridSessions-request-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

 ** [projectArn](#API_ListTestGridSessions_RequestSyntax) **   <a name="devicefarm-ListTestGridSessions-request-projectArn"></a>
ARN of a [TestGridProject](API_TestGridProject.md).
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [status](#API_ListTestGridSessions_RequestSyntax) **   <a name="devicefarm-ListTestGridSessions-request-status"></a>
Return only sessions in this state.
Type: String
Valid Values: `ACTIVE | CLOSED | ERRORED`
Required: No

## Response Syntax
<a name="API_ListTestGridSessions_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "testGridSessions": [
      {
         "arn": "string",
         "billingMinutes": number,
         "created": number,
         "ended": number,
         "seleniumProperties": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTestGridSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTestGridSessions_ResponseSyntax) **   <a name="devicefarm-ListTestGridSessions-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

 ** [testGridSessions](#API_ListTestGridSessions_ResponseSyntax) **   <a name="devicefarm-ListTestGridSessions-response-testGridSessions"></a>
The sessions that match the criteria in a [ListTestGridSessionsRequest](API_ListTestGridSessionsRequest.md).
Type: Array of [TestGridSession](API_TestGridSession.md) objects

## Errors
<a name="API_ListTestGridSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** InternalServiceException **
An internal exception was raised in the service. Contact [aws-devicefarm-support@amazon.com](mailto:aws-devicefarm-support@amazon.com) if you see this error.
HTTP Status Code: 500

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListTestGridSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListTestGridSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListTestGridSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListTestGridSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListTestGridSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListTestGridSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListTestGridSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListTestGridSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListTestGridSessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListTestGridSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListTestGridSessions)
