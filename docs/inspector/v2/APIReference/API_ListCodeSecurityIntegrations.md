---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCodeSecurityIntegrations.html
---

# ListCodeSecurityIntegrations
<a name="API_ListCodeSecurityIntegrations"></a>

Lists all code security integrations in your account.

## Request Syntax
<a name="API_ListCodeSecurityIntegrations_RequestSyntax"></a>

```
POST /codesecurity/integration/list?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCodeSecurityIntegrations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListCodeSecurityIntegrations_RequestSyntax) **   <a name="inspector2-ListCodeSecurityIntegrations-request-uri-maxResults"></a>
The maximum number of results to return in a single call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListCodeSecurityIntegrations_RequestSyntax) **   <a name="inspector2-ListCodeSecurityIntegrations-request-uri-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.

## Request Body
<a name="API_ListCodeSecurityIntegrations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCodeSecurityIntegrations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "integrations": [
      {
         "createdOn": number,
         "integrationArn": "string",
         "lastUpdateOn": number,
         "name": "string",
         "status": "string",
         "statusReason": "string",
         "tags": {
            "string" : "string"
         },
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCodeSecurityIntegrations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [integrations](#API_ListCodeSecurityIntegrations_ResponseSyntax) **   <a name="inspector2-ListCodeSecurityIntegrations-response-integrations"></a>
A list of code security integration summaries.
Type: Array of [CodeSecurityIntegrationSummary](API_CodeSecurityIntegrationSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [nextToken](#API_ListCodeSecurityIntegrations_ResponseSyntax) **   <a name="inspector2-ListCodeSecurityIntegrations-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.
Type: String

## Errors
<a name="API_ListCodeSecurityIntegrations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListCodeSecurityIntegrations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/ListCodeSecurityIntegrations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/ListCodeSecurityIntegrations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ListCodeSecurityIntegrations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/ListCodeSecurityIntegrations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ListCodeSecurityIntegrations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/ListCodeSecurityIntegrations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/ListCodeSecurityIntegrations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/ListCodeSecurityIntegrations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/ListCodeSecurityIntegrations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ListCodeSecurityIntegrations)
