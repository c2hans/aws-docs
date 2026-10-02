---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentRecommendationGeneration.html
---

# GetAgentRecommendationGeneration
<a name="API_GetAgentRecommendationGeneration"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

**Important**
Application-level recommendations are a new recommendation format currently in beta. We are actively seeking customer feedback to improve their quality and relevance. As with any AI-generated content, please thoroughly review each recommendation before taking any action based on it.

Retrieves information about a recommendation generation process, including its status, progress, and results. Recommendation generation is asynchronous: poll this operation until status reaches a terminal value of COMPLETED (results are ready) or ERROR (see errorDetails). Intermediate values are QUEUED and IN\_PROGRESS.

## Request Syntax
<a name="API_GetAgentRecommendationGeneration_RequestSyntax"></a>

```
GET /api/v1/agent-profiles/{{profileArn}}/generations/{{generationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAgentRecommendationGeneration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [generationId](#API_GetAgentRecommendationGeneration_RequestSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-request-uri-generationId"></a>
The unique identifier of the recommendation generation to retrieve.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [profileArn](#API_GetAgentRecommendationGeneration_RequestSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-request-uri-profileArn"></a>
The ARN of the optimization profile associated with this generation.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_GetAgentRecommendationGeneration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAgentRecommendationGeneration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "additionalContext": JSON value,
   "createdAt": "string",
   "createdBy": "string",
   "endedAt": "string",
   "errorDetails": {
      "code": "string",
      "message": "string"
   },
   "estimatedCompletionTime": "string",
   "id": "string",
   "lastModifiedAt": "string",
   "lastModifiedBy": "string",
   "name": "string",
   "profileArn": "string",
   "progress": {
      "completionPercentage": number,
      "stepsCompleted": number,
      "totalSteps": number
   },
   "scope": {
      "goalIds": [ "string" ],
      "items": [
         {
            "ids": [ "string" ],
            "pillar": "string"
         }
      ],
      "pillars": [ "string" ]
   },
   "startedAt": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetAgentRecommendationGeneration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [additionalContext](#API_GetAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-response-additionalContext"></a>
The additional context that was provided when the generation was started. For `ARCHITECTURE` generations, this includes the location of the reviewed IaC template and the lenses used.
Type: JSON value

 ** [createdAt](#API_GetAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-response-createdAt"></a>
The timestamp when the generation was started.
Type: Timestamp

 ** [createdBy](#API_GetAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-response-createdBy"></a>
The identifier of the user or system that started this generation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [endedAt](#API_GetAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-response-endedAt"></a>
The timestamp when the recommendation generation process completed.
Type: Timestamp

 ** [errorDetails](#API_GetAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-response-errorDetails"></a>
Details about the error if the generation status is ERROR.
Type: [ErrorDetails](API_ErrorDetails.md) object

 ** [estimatedCompletionTime](#API_GetAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-response-estimatedCompletionTime"></a>
The estimated time for the generation to complete.
Type: Timestamp

 ** [id](#API_GetAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-response-id"></a>
The unique identifier of the recommendation generation.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [lastModifiedAt](#API_GetAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-response-lastModifiedAt"></a>
The timestamp when the generation was last modified.
Type: Timestamp

 ** [lastModifiedBy](#API_GetAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-response-lastModifiedBy"></a>
The identifier of the user or system that last modified this generation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [name](#API_GetAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-response-name"></a>
The name of the recommendation generation.
Type: String

 ** [profileArn](#API_GetAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-response-profileArn"></a>
The Amazon Resource Name (ARN) of the profile used for this generation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`

 ** [progress](#API_GetAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-response-progress"></a>
Current progress information including steps completed and completion percentage.
Type: [Progress](API_Progress.md) object

 ** [scope](#API_GetAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-response-scope"></a>
The scope configuration that defines which pillars and goals to focus on during generation.
Type: [Scope](API_Scope.md) object

 ** [startedAt](#API_GetAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-response-startedAt"></a>
The timestamp when the recommendation generation process started.
Type: Timestamp

 ** [status](#API_GetAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendationGeneration-response-status"></a>
The current status of the recommendation generation.
Type: String
Valid Values: `QUEUED | IN_PROGRESS | COMPLETED | ERROR`

## Errors
<a name="API_GetAgentRecommendationGeneration_Errors"></a>

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
<a name="API_GetAgentRecommendationGeneration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/GetAgentRecommendationGeneration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/GetAgentRecommendationGeneration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/GetAgentRecommendationGeneration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/GetAgentRecommendationGeneration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/GetAgentRecommendationGeneration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/GetAgentRecommendationGeneration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/GetAgentRecommendationGeneration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/GetAgentRecommendationGeneration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/GetAgentRecommendationGeneration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/GetAgentRecommendationGeneration)
