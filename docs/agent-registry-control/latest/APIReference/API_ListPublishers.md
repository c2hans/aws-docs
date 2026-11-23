---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_ListPublishers.html
---

# ListPublishers

Lists the publishers that your account owns, followed by the `ACTIVE` publishers that are shared with your account.

## Request Syntax
<a name="API_ListPublishers_RequestSyntax"></a>

```
GET /publishers?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPublishers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListPublishers_RequestSyntax) **   <a name="agentregistrycontrol-ListPublishers-request-uri-maxResults"></a>
The maximum number of results to return in a single call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListPublishers_RequestSyntax) **   <a name="agentregistrycontrol-ListPublishers-request-uri-nextToken"></a>
The token for the next page of results. Use the value returned in the previous response.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

## Request Body
<a name="API_ListPublishers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPublishers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "associationCount": number,
         "createdAt": number,
         "identifierType": "string",
         "pendingAssociationApprovalCount": number,
         "publisherArn": "string",
         "status": "string",
         "value": { ... }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListPublishers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListPublishers_ResponseSyntax) **   <a name="agentregistrycontrol-ListPublishers-response-items"></a>
Summaries of the publishers on this page of results.
Type: Array of [PublisherSummary](API_PublisherSummary.md) objects

 ** [nextToken](#API_ListPublishers_ResponseSyntax) **   <a name="agentregistrycontrol-ListPublishers-response-nextToken"></a>
The token to use to get the next page of results. Absent when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

## Errors
<a name="API_ListPublishers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform the requested action.
HTTP Status Code: 403

 ** InternalServerException **
The request failed due to an unexpected internal error; the caller may retry.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling; the caller may retry after a delay.
HTTP Status Code: 429

 ** ValidationException **
The request failed validation of one or more input fields.
 ** fieldList **
The list of input fields that failed validation.
 ** reason **
The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListPublishers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/ListPublishers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/ListPublishers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/ListPublishers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/ListPublishers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/ListPublishers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/ListPublishers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/ListPublishers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/ListPublishers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/ListPublishers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/ListPublishers)
