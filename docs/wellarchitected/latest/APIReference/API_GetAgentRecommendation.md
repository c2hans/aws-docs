---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentRecommendation.html
---

# GetAgentRecommendation
<a name="API_GetAgentRecommendation"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

**Important**
Application-level recommendations are a new recommendation format currently in beta. We are actively seeking customer feedback to improve their quality and relevance. As with any AI-generated content, please thoroughly review each recommendation before taking any action based on it.

Retrieves detailed information about a specific optimization recommendation, including its impact analysis, content, and implementation guidance.

## Request Syntax
<a name="API_GetAgentRecommendation_RequestSyntax"></a>

```
GET /api/v1/agent-recommendations/{{recommendationArn}}?remediationType={{remediationType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAgentRecommendation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recommendationArn](#API_GetAgentRecommendation_RequestSyntax) **   <a name="wellarchitected-GetAgentRecommendation-request-uri-recommendationArn"></a>
The Amazon Resource Name (ARN) of the recommendation to retrieve.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-recommendation/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [remediationType](#API_GetAgentRecommendation_RequestSyntax) **   <a name="wellarchitected-GetAgentRecommendation-request-uri-remediationType"></a>
Optional filter on remediation type.
Valid Values: `AUTO_REMEDIATION | CONSOLE | CLI | SDK | IAC | MCP`

## Request Body
<a name="API_GetAgentRecommendation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAgentRecommendation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applications": [ "string" ],
   "awsServices": [ "string" ],
   "businessUnits": [ "string" ],
   "createdAt": "string",
   "createdBy": "string",
   "crossPillarBenefits": [
      {
         "description": "string",
         "impact": "string",
         "pillar": "string",
         "title": "string"
      }
   ],
   "description": "string",
   "effort": "string",
   "generationId": "string",
   "goals": [
      {
         "title": "string"
      }
   ],
   "highlights": [ "string" ],
   "impact": "string",
   "impactDetails": [ "string" ],
   "insights": [
      {
         "signalsDetected": "string",
         "usagePattern": "string"
      }
   ],
   "lastModifiedAt": "string",
   "lastModifiedBy": "string",
   "numberOfResources": number,
   "pillar": "string",
   "priority": "string",
   "profileArn": "string",
   "recommendationArn": "string",
   "remediations": [
      {
         "createdAt": "string",
         "createdBy": "string",
         "lastModifiedAt": "string",
         "lastModifiedBy": "string",
         "recommendationArn": "string",
         "resourceLinks": [
            {
               "title": "string",
               "url": "string"
            }
         ],
         "steps": [
            {
               "content": "string",
               "title": "string"
            }
         ],
         "type": "string"
      }
   ],
   "remediationSummary": {
      "recommendation": "string",
      "steps": [ "string" ]
   },
   "roi": {
      "detail": "string",
      "estimate": "string"
   },
   "sources": [ "string" ],
   "state": "string",
   "status": "string",
   "tags": [
      {
         "key": "string",
         "value": "string"
      }
   ],
   "title": "string",
   "tradeOffs": [
      {
         "description": "string",
         "mitigation": "string",
         "pillar": "string",
         "risk": "string",
         "riskExplanation": "string",
         "title": "string"
      }
   ],
   "type": "string",
   "updateReason": "string"
}
```

## Response Elements
<a name="API_GetAgentRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applications](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-applications"></a>
The applications that the recommendation targets.
Type: Array of strings

 ** [awsServices](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-awsServices"></a>
The AWS services that the recommendation applies to.
Type: Array of strings

 ** [businessUnits](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-businessUnits"></a>
The business units that own the affected resources.
Type: Array of strings

 ** [createdAt](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-createdAt"></a>
The timestamp when the recommendation was created.
Type: Timestamp

 ** [createdBy](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-createdBy"></a>
The identifier of the user or system that created this recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [crossPillarBenefits](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-crossPillarBenefits"></a>
Cross-pillar benefits of acting on the recommendation.
Type: Array of [CrossPillarBenefit](API_CrossPillarBenefit.md) objects

 ** [description](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-description"></a>
A description of the recommendation.
Type: String
Length Constraints: Minimum length of 80. Maximum length of 500.

 ** [effort](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-effort"></a>
The effort required to implement the recommendation.
Type: String
Valid Values: `LARGE | MEDIUM | SMALL`

 ** [generationId](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-generationId"></a>
The identifier of the generation that produced this recommendation.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [goals](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-goals"></a>
Goals that this recommendation targets.
Type: Array of [RecommendationGoal](API_RecommendationGoal.md) objects

 ** [highlights](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-highlights"></a>
Highlights describing what was detected.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 20. Maximum length of 250.

 ** [impact](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-impact"></a>
The severity of the recommendation's impact.
Type: String
Valid Values: `HIGH | MEDIUM | LOW`

 ** [impactDetails](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-impactDetails"></a>
Detailed impact information for the recommendation.
Type: Array of strings
Array Members: Minimum number of 2 items. Maximum number of 3 items.
Length Constraints: Minimum length of 10. Maximum length of 100.

 ** [insights](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-insights"></a>
A list of insights about the recommendation.
Type: Array of [Insight](API_Insight.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [lastModifiedAt](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-lastModifiedAt"></a>
The timestamp when the recommendation was last modified.
Type: Timestamp

 ** [lastModifiedBy](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-lastModifiedBy"></a>
The identifier of the user or system that last modified this recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [numberOfResources](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-numberOfResources"></a>
The number of AWS resources this recommendation affects.
Type: Integer

 ** [pillar](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-pillar"></a>
The AWS Well-Architected Framework pillar that the recommendation addresses.
Type: String
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`

 ** [priority](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-priority"></a>
The priority of the recommendation.
Type: String
Valid Values: `HIGH | MEDIUM | LOW`

 ** [profileArn](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-profileArn"></a>
The Amazon Resource Name (ARN) of the associated profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`

 ** [recommendationArn](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-recommendationArn"></a>
The Amazon Resource Name (ARN) of the recommendation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-recommendation/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [remediations](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-remediations"></a>
A list of remediations for the recommendation.
Type: Array of [AgentRecommendationRemediation](API_AgentRecommendationRemediation.md) objects

 ** [remediationSummary](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-remediationSummary"></a>
A high-level summary of the recommended remediation.
Type: [RemediationSummary](API_RemediationSummary.md) object

 ** [roi](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-roi"></a>
The return on investment estimate for the recommendation.
Type: [Roi](API_Roi.md) object

 ** [sources](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-sources"></a>
Sources that generated this recommendation.
Type: Array of strings
Valid Values: `TRUSTED_ADVISOR | COST_EXPLORER | CLOUDWATCH | WELL_ARCHITECTED_TOOL | WELL_ARCHITECTED_AGENT | CUSTOMER_IAC`

 ** [state](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-state"></a>
The current state of the recommendation.
Type: String
Valid Values: `OPEN | CLOSED`

 ** [status](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-status"></a>
The current status of the recommendation.
Type: String
Valid Values: `ACTIVE | SUPPRESSED | COMPLETED`

 ** [tags](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-tags"></a>
A set of key-value pairs associated with the recommendation, used for cost allocation and access control.
Type: Array of [Tag](API_Tag.md) objects

 ** [title](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-title"></a>
The title of the recommendation.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 120.

 ** [tradeOffs](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-tradeOffs"></a>
Trade-offs of acting on the recommendation.
Type: Array of [TradeOff](API_TradeOff.md) objects

 ** [type](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-type"></a>
The type of the recommendation.
Type: String
Valid Values: `RESOURCE | ARCHITECTURE | APPLICATION`

 ** [updateReason](#API_GetAgentRecommendation_ResponseSyntax) **   <a name="wellarchitected-GetAgentRecommendation-response-updateReason"></a>
The free-text reason associated with the recommendation's most recent status update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Errors
<a name="API_GetAgentRecommendation_Errors"></a>

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
<a name="API_GetAgentRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/GetAgentRecommendation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/GetAgentRecommendation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/GetAgentRecommendation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/GetAgentRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/GetAgentRecommendation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/GetAgentRecommendation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/GetAgentRecommendation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/GetAgentRecommendation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/GetAgentRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/GetAgentRecommendation)
