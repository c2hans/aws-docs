---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentContexts.html
---

# ListAgentContexts
<a name="API_ListAgentContexts"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

Lists contexts associated with a profile.

## Request Syntax
<a name="API_ListAgentContexts_RequestSyntax"></a>

```
GET /api/v1/agent-profiles/{{profileArn}}/contexts?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAgentContexts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAgentContexts_RequestSyntax) **   <a name="wellarchitected-ListAgentContexts-request-uri-maxResults"></a>
The maximum number of results to return for this request.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListAgentContexts_RequestSyntax) **   <a name="wellarchitected-ListAgentContexts-request-uri-nextToken"></a>
The token to use to retrieve the next set of results.
Length Constraints: Minimum length of 1.
Pattern: `[A-Za-z0-9+\/=_-]+`

 ** [profileArn](#API_ListAgentContexts_RequestSyntax) **   <a name="wellarchitected-ListAgentContexts-request-uri-profileArn"></a>
The Amazon Resource Name (ARN) of the profile to list contexts for.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_ListAgentContexts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAgentContexts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "applicationType": "string",
         "content": {
            "accountIds": [ "string" ],
            "additionalContext": "string",
            "applicationOverview": "string",
            "applicationType": "string",
            "architectureOverview": "string",
            "awsServices": [ "string" ],
            "criticality": "string",
            "industry": "string",
            "organizationalUnitIds": [ "string" ],
            "regions": [ "string" ],
            "resourceTags": [
               {
                  "key": "string",
                  "value": "string"
               }
            ],
            "resourceTypes": [ "string" ]
         },
         "contextType": "string",
         "createdAt": "string",
         "createdBy": "string",
         "criticality": "string",
         "id": "string",
         "lastModifiedAt": "string",
         "lastModifiedBy": "string",
         "profileArn": "string",
         "title": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAgentContexts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListAgentContexts_ResponseSyntax) **   <a name="wellarchitected-ListAgentContexts-response-items"></a>
A list of context summaries associated with the profile.
Type: Array of [ContextSummary](API_ContextSummary.md) objects

 ** [nextToken](#API_ListAgentContexts_ResponseSyntax) **   <a name="wellarchitected-ListAgentContexts-response-nextToken"></a>
The token to use to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[A-Za-z0-9+\/=_-]+`

## Errors
<a name="API_ListAgentContexts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListAgentContexts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/ListAgentContexts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/ListAgentContexts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ListAgentContexts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/ListAgentContexts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ListAgentContexts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/ListAgentContexts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/ListAgentContexts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/ListAgentContexts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/ListAgentContexts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ListAgentContexts)
