---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_StartAgentRecommendationGeneration.html
---

# StartAgentRecommendationGeneration
<a name="API_StartAgentRecommendationGeneration"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

Starts a recommendation generation process for the specified agent profile. This asynchronous operation returns immediately. Use `GetAgentRecommendationGeneration` to check the status of the generation.

Currently, only the `ARCHITECTURE` recommendation type is supported. `RESOURCE` and `APPLICATION` recommendations are generated only by the scheduled generation cycle and cannot be started with this operation.

For the `ARCHITECTURE` type, the generation analyzes the infrastructure as code (IaC) template that you specify in `additionalContext`, and returns updated templates with best practice fixes applied. You must specify `scope` and `additionalContext`. You can optionally specify `name`.

Architecture review generations are subject to a daily quota for each profile. For more information, see [Quotas and limits](https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-quotas.html) in the AWS Well-Architected User Guide.

## Request Syntax
<a name="API_StartAgentRecommendationGeneration_RequestSyntax"></a>

```
POST /api/v1/agent-profiles/{{profileArn}}/generations HTTP/1.1
Content-type: application/json

{
   "additionalContext": {{JSON value}},
   "name": "{{string}}",
   "scope": {
      "goalIds": [ "{{string}}" ],
      "items": [
         {
            "ids": [ "{{string}}" ],
            "pillar": "{{string}}"
         }
      ],
      "pillars": [ "{{string}}" ]
   },
   "types": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_StartAgentRecommendationGeneration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileArn](#API_StartAgentRecommendationGeneration_RequestSyntax) **   <a name="wellarchitected-StartAgentRecommendationGeneration-request-uri-profileArn"></a>
The Amazon Resource Name (ARN) of the optimization profile to use for generating recommendations.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_StartAgentRecommendationGeneration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [additionalContext](#API_StartAgentRecommendationGeneration_RequestSyntax) **   <a name="wellarchitected-StartAgentRecommendationGeneration-request-additionalContext"></a>
The location of the infrastructure as code (IaC) template to review, and the lenses to review it against. Required for the `ARCHITECTURE` type. Must be absent for other types. Specify a JSON object with the following members:
+  `s3Uri`: The Amazon S3 URI of the IaC template, .zip archive, or folder to review.
+  `s3VersionId`: The version ID of the Amazon S3 object. If you omit this member, the current version is used.
+  `lensArns`: The ARNs of the lenses to review against. Only `arn:aws:wellarchitected::aws:lens/wellarchitected` is supported.
Type: JSON value
Required: No

 ** [name](#API_StartAgentRecommendationGeneration_RequestSyntax) **   <a name="wellarchitected-StartAgentRecommendationGeneration-request-name"></a>
An optional name for this generation that identifies the architecture review in the console and in `ListAgentRecommendationGenerations` results. Applies to `ARCHITECTURE` type only. Must be absent for other types.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** [scope](#API_StartAgentRecommendationGeneration_RequestSyntax) **   <a name="wellarchitected-StartAgentRecommendationGeneration-request-scope"></a>
Defines which pillars, goals, and items the review covers. Required for the `ARCHITECTURE` type. Must be absent for other types.
Type: [Scope](API_Scope.md) object
Required: No

 ** [types](#API_StartAgentRecommendationGeneration_RequestSyntax) **   <a name="wellarchitected-StartAgentRecommendationGeneration-request-types"></a>
The types of recommendations to generate. You can specify up to two types in a single request. Currently, only `ARCHITECTURE` is supported for this operation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `RESOURCE | ARCHITECTURE | APPLICATION`
Required: Yes

## Response Syntax
<a name="API_StartAgentRecommendationGeneration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "createdBy": "string",
   "estimatedCompletionTime": "string",
   "id": "string",
   "lastModifiedAt": "string",
   "lastModifiedBy": "string",
   "name": "string",
   "profileArn": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_StartAgentRecommendationGeneration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_StartAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-StartAgentRecommendationGeneration-response-createdAt"></a>
The timestamp when the generation was started.
Type: Timestamp

 ** [createdBy](#API_StartAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-StartAgentRecommendationGeneration-response-createdBy"></a>
The identifier of the user or system that started this generation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [estimatedCompletionTime](#API_StartAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-StartAgentRecommendationGeneration-response-estimatedCompletionTime"></a>
The estimated time for the generation to complete.
Type: Timestamp

 ** [id](#API_StartAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-StartAgentRecommendationGeneration-response-id"></a>
The unique identifier of the recommendation generation.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [lastModifiedAt](#API_StartAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-StartAgentRecommendationGeneration-response-lastModifiedAt"></a>
The timestamp when the generation was last modified.
Type: Timestamp

 ** [lastModifiedBy](#API_StartAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-StartAgentRecommendationGeneration-response-lastModifiedBy"></a>
The identifier of the user or system that last modified this generation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [name](#API_StartAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-StartAgentRecommendationGeneration-response-name"></a>
The name of the recommendation generation.
Type: String

 ** [profileArn](#API_StartAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-StartAgentRecommendationGeneration-response-profileArn"></a>
The Amazon Resource Name (ARN) of the profile used for this generation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`

 ** [status](#API_StartAgentRecommendationGeneration_ResponseSyntax) **   <a name="wellarchitected-StartAgentRecommendationGeneration-response-status"></a>
The current status of the recommendation generation.
Type: String
Valid Values: `QUEUED | IN_PROGRESS | COMPLETED | ERROR`

## Errors
<a name="API_StartAgentRecommendationGeneration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The user has reached their resource quota.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 402

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
<a name="API_StartAgentRecommendationGeneration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/StartAgentRecommendationGeneration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/StartAgentRecommendationGeneration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/StartAgentRecommendationGeneration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/StartAgentRecommendationGeneration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/StartAgentRecommendationGeneration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/StartAgentRecommendationGeneration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/StartAgentRecommendationGeneration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/StartAgentRecommendationGeneration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/StartAgentRecommendationGeneration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/StartAgentRecommendationGeneration)
