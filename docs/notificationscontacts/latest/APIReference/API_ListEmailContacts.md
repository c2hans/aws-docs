---
source_url: https://docs.aws.amazon.com/notificationscontacts/latest/APIReference/API_ListEmailContacts.html
---

# ListEmailContacts
<a name="API_ListEmailContacts"></a>

Lists all email contacts created under the Account.

## Request Syntax
<a name="API_ListEmailContacts_RequestSyntax"></a>

```
GET /emailcontacts?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEmailContacts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListEmailContacts_RequestSyntax) **   <a name="notificationscontacts-ListEmailContacts-request-uri-maxResults"></a>
The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListEmailContacts_RequestSyntax) **   <a name="notificationscontacts-ListEmailContacts-request-uri-nextToken"></a>
An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.

## Request Body
<a name="API_ListEmailContacts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEmailContacts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "emailContacts": [
      {
         "address": "string",
         "arn": "string",
         "creationTime": "string",
         "name": "string",
         "status": "string",
         "updateTime": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEmailContacts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [emailContacts](#API_ListEmailContacts_ResponseSyntax) **   <a name="notificationscontacts-ListEmailContacts-response-emailContacts"></a>
A list of email contacts.
Type: Array of [EmailContact](API_EmailContact.md) objects

 ** [nextToken](#API_ListEmailContacts_ResponseSyntax) **   <a name="notificationscontacts-ListEmailContacts-response-nextToken"></a>
An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.
Type: String

## Errors
<a name="API_ListEmailContacts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service being throttled.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The list of input fields that are invalid.
 ** reason **
The reason why your input is considered invalid.
HTTP Status Code: 400

## See Also
<a name="API_ListEmailContacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notificationscontacts-2018-05-10/ListEmailContacts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notificationscontacts-2018-05-10/ListEmailContacts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notificationscontacts-2018-05-10/ListEmailContacts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notificationscontacts-2018-05-10/ListEmailContacts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notificationscontacts-2018-05-10/ListEmailContacts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notificationscontacts-2018-05-10/ListEmailContacts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notificationscontacts-2018-05-10/ListEmailContacts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notificationscontacts-2018-05-10/ListEmailContacts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notificationscontacts-2018-05-10/ListEmailContacts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notificationscontacts-2018-05-10/ListEmailContacts)
