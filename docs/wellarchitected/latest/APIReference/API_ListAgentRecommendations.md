---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentRecommendations.html
---

# ListAgentRecommendations
<a name="API_ListAgentRecommendations"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

**Important**
Application-level recommendations are a new recommendation format currently in beta. We are actively seeking customer feedback to improve their quality and relevance. As with any AI-generated content, please thoroughly review each recommendation before taking any action based on it.

Lists active optimization recommendations for a specified profile with optional filtering by state.

## Request Syntax
<a name="API_ListAgentRecommendations_RequestSyntax"></a>

```
GET /api/v1/agent-profiles/{{profileArn}}/recommendations?maxResults={{maxResults}}&nextToken={{nextToken}}&pillar={{pillar}}&state={{state}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAgentRecommendations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAgentRecommendations_RequestSyntax) **   <a name="wellarchitected-ListAgentRecommendations-request-uri-maxResults"></a>
The maximum number of recommendations to return in a single response.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListAgentRecommendations_RequestSyntax) **   <a name="wellarchitected-ListAgentRecommendations-request-uri-nextToken"></a>
A pagination token returned from a previous call to continue retrieving results.
Length Constraints: Minimum length of 1.
Pattern: `[A-Za-z0-9+\/=_-]+`

 ** [pillar](#API_ListAgentRecommendations_RequestSyntax) **   <a name="wellarchitected-ListAgentRecommendations-request-uri-pillar"></a>
Optional filter to return only recommendations for the specified pillar.
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`

 ** [profileArn](#API_ListAgentRecommendations_RequestSyntax) **   <a name="wellarchitected-ListAgentRecommendations-request-uri-profileArn"></a>
The Amazon Resource Name (ARN) of the optimization profile to list recommendations for.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

 ** [state](#API_ListAgentRecommendations_RequestSyntax) **   <a name="wellarchitected-ListAgentRecommendations-request-uri-state"></a>
Optional filter to return only recommendations with the specified state (OPEN or CLOSED).
Valid Values: `OPEN | CLOSED`

## Request Body
<a name="API_ListAgentRecommendations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAgentRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "applications": [ "string" ],
         "awsServices": [ "string" ],
         "businessUnits": [ "string" ],
         "createdAt": "string",
         "createdBy": "string",
         "description": "string",
         "effort": "string",
         "generationId": "string",
         "impact": "string",
         "lastModifiedAt": "string",
         "lastModifiedBy": "string",
         "numberOfResources": number,
         "pillar": "string",
         "priority": "string",
         "profileArn": "string",
         "recommendationArn": "string",
         "roi": {
            "detail": "string",
            "estimate": "string"
         },
         "state": "string",
         "status": "string",
         "title": "string",
         "type": "string",
         "updateReason": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAgentRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListAgentRecommendations_ResponseSyntax) **   <a name="wellarchitected-ListAgentRecommendations-response-items"></a>
A list of recommendation summaries.
Type: Array of [AgentRecommendationSummary](API_AgentRecommendationSummary.md) objects

 ** [nextToken](#API_ListAgentRecommendations_ResponseSyntax) **   <a name="wellarchitected-ListAgentRecommendations-response-nextToken"></a>
A pagination token to retrieve the next set of results, if available.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[A-Za-z0-9+\/=_-]+`

## Errors
<a name="API_ListAgentRecommendations_Errors"></a>

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

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

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
<a name="API_ListAgentRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/ListAgentRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/ListAgentRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ListAgentRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/ListAgentRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ListAgentRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/ListAgentRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/ListAgentRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/ListAgentRecommendations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/ListAgentRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ListAgentRecommendations)
