---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListSessions.html
---

# ListSessions
<a name="API_ListSessions"></a>

Returns a list of approval sessions. For more information, see [Session](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html) in the *Multi-party approval User Guide*.

## Request Syntax
<a name="API_ListSessions_RequestSyntax"></a>

```
POST /approval-teams/{{ApprovalTeamArn}}/sessions/?List HTTP/1.1
Content-type: application/json

{
   "Filters": [
      {
         "FieldName": "{{string}}",
         "Operator": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListSessions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApprovalTeamArn](#API_ListSessions_RequestSyntax) **   <a name="mpa-ListSessions-request-uri-ApprovalTeamArn"></a>
Amazon Resource Name (ARN) for the approval team.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:approval-team/[a-zA-Z0-9._-]+`
Required: Yes

## Request Body
<a name="API_ListSessions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_ListSessions_RequestSyntax) **   <a name="mpa-ListSessions-request-Filters"></a>
An array of `Filter` objects. Contains the filter to apply when listing sessions.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [MaxResults](#API_ListSessions_RequestSyntax) **   <a name="mpa-ListSessions-request-MaxResults"></a>
The maximum number of items to return in the response. If more results exist than the specified `MaxResults` value, a token is included in the response so that you can retrieve the remaining results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** [NextToken](#API_ListSessions_RequestSyntax) **   <a name="mpa-ListSessions-request-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a next call to the operation to get more output. You can repeat this until the `NextToken` response element returns `null`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

## Response Syntax
<a name="API_ListSessions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Sessions": [
      {
         "ActionCompletionStrategy": "string",
         "ActionName": "string",
         "AdditionalSecurityRequirements": [ "string" ],
         "ApprovalTeamArn": "string",
         "ApprovalTeamName": "string",
         "CompletionTime": "string",
         "Description": "string",
         "ExpirationTime": "string",
         "InitiationTime": "string",
         "ProtectedResourceArn": "string",
         "RequesterAccountId": "string",
         "RequesterPrincipalArn": "string",
         "RequesterRegion": "string",
         "RequesterServicePrincipal": "string",
         "SessionArn": "string",
         "Status": "string",
         "StatusCode": "string",
         "StatusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSessions_ResponseSyntax) **   <a name="mpa-ListSessions-response-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a next call to the operation to get more output. You can repeat this until the `NextToken` response element returns `null`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [Sessions](#API_ListSessions_ResponseSyntax) **   <a name="mpa-ListSessions-response-Sessions"></a>
An array of `ListSessionsResponseSession` objects. Contains details for the sessions.
Type: Array of [ListSessionsResponseSession](API_ListSessionsResponseSession.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

## Errors
<a name="API_ListSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You do not have sufficient access to perform this action. Check your permissions, and try again.
 ** Message **
Message for the `AccessDeniedException` error.
HTTP Status Code: 403

 [InternalServerException](API_InternalServerException.md)
The service encountered an internal error. Try your request again. If the problem persists, contact AWS Support.
 ** Message **
Message for the `InternalServerException` error.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The specified resource doesn't exist. Check the resource ID, and try again.
 ** Message **
Message for the `ResourceNotFoundException` error.
HTTP Status Code: 404

 [ThrottlingException](API_ThrottlingException.md)
The request was denied due to request throttling.
 ** Message **
Message for the `ThrottlingException` error.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
The input fails to satisfy the constraints specified by an AWS service.
 ** Message **
Message for the `ValidationException` error.
HTTP Status Code: 400

## See Also
<a name="API_ListSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mpa-2022-07-26/ListSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mpa-2022-07-26/ListSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/ListSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mpa-2022-07-26/ListSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/ListSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mpa-2022-07-26/ListSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mpa-2022-07-26/ListSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mpa-2022-07-26/ListSessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mpa-2022-07-26/ListSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/ListSessions)
