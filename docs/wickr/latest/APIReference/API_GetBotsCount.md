---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_GetBotsCount.html
---

# GetBotsCount
<a name="API_GetBotsCount"></a>

Retrieves the count of bots in a Wickr network, categorized by their status (pending, active, and total).

## Request Syntax
<a name="API_GetBotsCount_RequestSyntax"></a>

```
GET /networks/{{networkId}}/bots/count HTTP/1.1
```

## URI Request Parameters
<a name="API_GetBotsCount_RequestParameters"></a>

The request uses the following URI parameters.

 ** [networkId](#API_GetBotsCount_RequestSyntax) **   <a name="wickr-GetBotsCount-request-uri-networkId"></a>
The ID of the Wickr network for which to retrieve bot counts.
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`
Required: Yes

## Request Body
<a name="API_GetBotsCount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBotsCount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "active": number,
   "pending": number,
   "total": number
}
```

## Response Elements
<a name="API_GetBotsCount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [active](#API_GetBotsCount_ResponseSyntax) **   <a name="wickr-GetBotsCount-response-active"></a>
The number of bots with active status.
Type: Integer

 ** [pending](#API_GetBotsCount_ResponseSyntax) **   <a name="wickr-GetBotsCount-response-pending"></a>
The number of bots with pending status (invited but not yet activated).
Type: Integer

 ** [total](#API_GetBotsCount_ResponseSyntax) **   <a name="wickr-GetBotsCount-response-total"></a>
The total number of bots in the network (active and pending).
Type: Integer

## Errors
<a name="API_GetBotsCount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [BadRequestError](API_BadRequestError.md)
The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.
 ** message **
A detailed message explaining what was wrong with the request and how to correct it.
HTTP Status Code: 400

 [ForbiddenError](API_ForbiddenError.md)
Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.
 ** message **
A message explaining why access was denied and what permissions are required.
HTTP Status Code: 403

 [InternalServerError](API_InternalServerError.md)
An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact AWS Support.
 ** message **
A message describing the internal server error that occurred.
HTTP Status Code: 500

 [RateLimitError](API_RateLimitError.md)
The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.
 ** message **
A message indicating that the rate limit was exceeded and suggesting when to retry.
HTTP Status Code: 429

 [ResourceNotFoundError](API_ResourceNotFoundError.md)
The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.
 ** message **
A message identifying which resource was not found.
HTTP Status Code: 404

 [UnauthorizedError](API_UnauthorizedError.md)
The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.
 ** message **
A message explaining why the authentication failed.
HTTP Status Code: 401

 [ValidationError](API_ValidationError.md)
One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.
 ** message **
A message describing the validation error error that occurred.
 ** reasons **
A list of validation error details, where each item identifies a specific field that failed validation and explains the reason for the failure.
HTTP Status Code: 422

## See Also
<a name="API_GetBotsCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wickr-2024-02-01/GetBotsCount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wickr-2024-02-01/GetBotsCount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/GetBotsCount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wickr-2024-02-01/GetBotsCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/GetBotsCount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wickr-2024-02-01/GetBotsCount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wickr-2024-02-01/GetBotsCount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wickr-2024-02-01/GetBotsCount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wickr-2024-02-01/GetBotsCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/GetBotsCount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
