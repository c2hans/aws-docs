---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAgentRecommendationStatus.html
---

# UpdateAgentRecommendationStatus
<a name="API_UpdateAgentRecommendationStatus"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

Updates the status of a recommendation to track its progress through the implementation lifecycle.

## Request Syntax
<a name="API_UpdateAgentRecommendationStatus_RequestSyntax"></a>

```
PATCH /api/v1/agent-recommendations/{{recommendationArn}}/status HTTP/1.1
Content-type: application/json

{
   "status": "{{string}}",
   "updateReason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAgentRecommendationStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recommendationArn](#API_UpdateAgentRecommendationStatus_RequestSyntax) **   <a name="wellarchitected-UpdateAgentRecommendationStatus-request-uri-recommendationArn"></a>
The Amazon Resource Name (ARN) of the recommendation to update.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-recommendation/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_UpdateAgentRecommendationStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [status](#API_UpdateAgentRecommendationStatus_RequestSyntax) **   <a name="wellarchitected-UpdateAgentRecommendationStatus-request-status"></a>
The new status to assign to the recommendation.
Type: String
Valid Values: `ACTIVE | SUPPRESSED | COMPLETED`
Required: Yes

 ** [updateReason](#API_UpdateAgentRecommendationStatus_RequestSyntax) **   <a name="wellarchitected-UpdateAgentRecommendationStatus-request-updateReason"></a>
A free-text reason explaining this status update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## Response Syntax
<a name="API_UpdateAgentRecommendationStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateAgentRecommendationStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateAgentRecommendationStatus_Errors"></a>

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
<a name="API_UpdateAgentRecommendationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/UpdateAgentRecommendationStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/UpdateAgentRecommendationStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/UpdateAgentRecommendationStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/UpdateAgentRecommendationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/UpdateAgentRecommendationStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/UpdateAgentRecommendationStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/UpdateAgentRecommendationStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/UpdateAgentRecommendationStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/UpdateAgentRecommendationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/UpdateAgentRecommendationStatus)
