---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_ListSessions.html
---

# ListSessions

Lists AWS Sign-In Sessions associated with a principal. If you don't specify `principalArn`, the operation returns sessions associated with the caller's identity. With the required IAM permissions, you can list sessions for a specific principal or across your AWS account.

You can filter sessions by OAuth client, session creation time, and status. When you specify multiple filters, only sessions matching all specified criteria are returned.

## Request Syntax
<a name="API_ListSessions_RequestSyntax"></a>

```
{
   "clientId": "{{string}}",
   "issuedAfter": {{number}},
   "issuedBefore": {{number}},
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "principalArn": "{{string}}",
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSessions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientId](#API_ListSessions_RequestSyntax) **   <a name="signin-ListSessions-request-clientId"></a>
Filters results to sessions created by the specified OAuth client ID. This parameter identifies the OAuth client, not the client type.
Type: String
Required: No

 ** [issuedAfter](#API_ListSessions_RequestSyntax) **   <a name="signin-ListSessions-request-issuedAfter"></a>
Filters results to sessions created at or after the specified time, expressed as a NumericDate (seconds since the Unix epoch). This filter uses the session creation time.
Type: Long
Required: No

 ** [issuedBefore](#API_ListSessions_RequestSyntax) **   <a name="signin-ListSessions-request-issuedBefore"></a>
Filters results to sessions created before the specified time, expressed as a NumericDate (seconds since the Unix epoch). This filter uses the session creation time.
Type: Long
Required: No

 ** [maxResults](#API_ListSessions_RequestSyntax) **   <a name="signin-ListSessions-request-maxResults"></a>
The maximum number of sessions to return in a single response. Valid range is 1 to 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListSessions_RequestSyntax) **   <a name="signin-ListSessions-request-nextToken"></a>
A pagination token returned by a previous request. Specify this value to retrieve the next page of results. Omit this parameter for the first request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/_]*`
Required: No

 ** [principalArn](#API_ListSessions_RequestSyntax) **   <a name="signin-ListSessions-request-principalArn"></a>
The ARN of the principal whose Sign-In Sessions you want to list. If you omit this parameter, the operation lists sessions associated with the caller's identity. Specify a supported IAM user, IAM role, federated user, or root user ARN to list sessions for that principal, or an account wildcard such as `arn:aws:iam::123456789012:*` to list sessions across your account. The principal or account wildcard must be in the caller's AWS account. Listing sessions for another principal requires appropriate IAM permissions.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]+)*:((iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@-]{1,64})|(iam::[0-9]{12}:user/[a-zA-Z0-9_+=,.@-]{1,64})|(sts::[0-9]{12}:federated-user/[a-zA-Z0-9_+=,.@-]{2,193})|(iam::[0-9]{12}:root)|(iam::[0-9]{12}:[*]))`
Required: No

 ** [status](#API_ListSessions_RequestSyntax) **   <a name="signin-ListSessions-request-status"></a>
Filters results by session status. Specify `ACTIVE` to return active sessions or `REVOKED` to return revoked sessions. Expired sessions are not returned.
Type: String
Valid Values: `ACTIVE | REVOKED`
Required: No

## Response Syntax
<a name="API_ListSessions_ResponseSyntax"></a>

```
{
   "items": [
      {
         "clientId": "string",
         "clientType": "string",
         "expiresAt": number,
         "issuedAt": number,
         "principalArn": "string",
         "resource": "string",
         "role": "string",
         "sessionArn": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListSessions_ResponseSyntax) **   <a name="signin-ListSessions-response-items"></a>
A list of Sign-In Session summaries that match the specified request filters.
Type: Array of [Session](API_Session.md) objects

 ** [nextToken](#API_ListSessions_ResponseSyntax) **   <a name="signin-ListSessions-response-nextToken"></a>
If this value is present, additional results are available. Pass it as `nextToken` in a subsequent request to retrieve the next page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/_]*`

## Errors
<a name="API_ListSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 400

 ** InternalServerException **
An internal error occurred while processing the request.
HTTP Status Code: 500

 ** ThrottlingException **
Your request was throttled because you exceeded the allowed request rate.
HTTP Status Code: 400

 ** ValidationException **
The request contains invalid or incorrectly formatted input.
HTTP Status Code: 400

## See Also
<a name="API_ListSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signincontrolplane-2022-07-26/ListSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signincontrolplane-2022-07-26/ListSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signincontrolplane-2022-07-26/ListSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signincontrolplane-2022-07-26/ListSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signincontrolplane-2022-07-26/ListSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signincontrolplane-2022-07-26/ListSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signincontrolplane-2022-07-26/ListSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signincontrolplane-2022-07-26/ListSessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/signincontrolplane-2022-07-26/ListSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signincontrolplane-2022-07-26/ListSessions)
