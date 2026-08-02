---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_ListBots.html
---

# ListBots
<a name="API_ListBots"></a>

Retrieves a paginated list of bots in a specified Wickr network. You can filter and sort the results based on various criteria.

## Request Syntax
<a name="API_ListBots_RequestSyntax"></a>

```
GET /networks/{{networkId}}/bots?displayName={{displayName}}&groupId={{groupId}}&maxResults={{maxResults}}&nextToken={{nextToken}}&sortDirection={{sortDirection}}&sortFields={{sortFields}}&status={{status}}&username={{username}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBots_RequestParameters"></a>

The request uses the following URI parameters.

 ** [displayName](#API_ListBots_RequestSyntax) **   <a name="wickr-ListBots-request-uri-displayName"></a>
Filter results to only include bots with display names matching this value.
Pattern: `[\S\s]*`

 ** [groupId](#API_ListBots_RequestSyntax) **   <a name="wickr-ListBots-request-uri-groupId"></a>
Filter results to only include bots belonging to this security group.
Pattern: `[\S\s]*`

 ** [maxResults](#API_ListBots_RequestSyntax) **   <a name="wickr-ListBots-request-uri-maxResults"></a>
The maximum number of bots to return in a single page. Valid range is 1-100. Default is 10.

 ** [networkId](#API_ListBots_RequestSyntax) **   <a name="wickr-ListBots-request-uri-networkId"></a>
The ID of the Wickr network from which to list bots.
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`
Required: Yes

 ** [nextToken](#API_ListBots_RequestSyntax) **   <a name="wickr-ListBots-request-uri-nextToken"></a>
The token for retrieving the next page of results. This is returned from a previous request when there are more results available.
Pattern: `[\S\s]*`

 ** [sortDirection](#API_ListBots_RequestSyntax) **   <a name="wickr-ListBots-request-uri-sortDirection"></a>
The direction to sort results. Valid values are 'ASC' (ascending) or 'DESC' (descending). Default is 'DESC'.
Valid Values: `ASC | DESC`

 ** [sortFields](#API_ListBots_RequestSyntax) **   <a name="wickr-ListBots-request-uri-sortFields"></a>
The fields to sort bots by. Multiple fields can be specified by separating them with '\+'. Accepted values include 'username', 'firstName', 'displayName', 'status', and 'groupId'.
Pattern: `[\S\s]*`

 ** [status](#API_ListBots_RequestSyntax) **   <a name="wickr-ListBots-request-uri-status"></a>
Filter results to only include bots with this status (1 for pending, 2 for active).

 ** [username](#API_ListBots_RequestSyntax) **   <a name="wickr-ListBots-request-uri-username"></a>
Filter results to only include bots with usernames matching this value.
Pattern: `[\S\s]*`

## Request Body
<a name="API_ListBots_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBots_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "bots": [
      {
         "botId": "string",
         "displayName": "string",
         "groupId": "string",
         "hasChallenge": boolean,
         "lastLogin": "string",
         "pubkey": "string",
         "status": number,
         "suspended": boolean,
         "uname": "string",
         "username": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBots_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [bots](#API_ListBots_ResponseSyntax) **   <a name="wickr-ListBots-response-bots"></a>
A list of bot objects matching the specified filters and within the current page.
Type: Array of [Bot](API_Bot.md) objects

 ** [nextToken](#API_ListBots_ResponseSyntax) **   <a name="wickr-ListBots-response-nextToken"></a>
The token to use for retrieving the next page of results. If this is not present, there are no more results.
Type: String
Pattern: `[\S\s]*`

## Errors
<a name="API_ListBots_Errors"></a>

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
<a name="API_ListBots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wickr-2024-02-01/ListBots)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wickr-2024-02-01/ListBots)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/ListBots)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wickr-2024-02-01/ListBots)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/ListBots)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wickr-2024-02-01/ListBots)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wickr-2024-02-01/ListBots)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wickr-2024-02-01/ListBots)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wickr-2024-02-01/ListBots)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/ListBots)
