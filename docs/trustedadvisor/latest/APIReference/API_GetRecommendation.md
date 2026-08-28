---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_GetRecommendation.html
---

# GetRecommendation
<a name="API_GetRecommendation"></a>

Get a specific Recommendation. This API provides global recommendations, eliminating the need to call the API in each AWS Region.

## Request Syntax
<a name="API_GetRecommendation_RequestSyntax"></a>

```
GET /v1/recommendations/{{recommendationIdentifier}}?language={{language}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRecommendation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [language](#API_GetRecommendation_RequestSyntax) **   <a name="ta-GetRecommendation-request-uri-language"></a>
The ISO 639-1 code for the language that you want your recommendations to appear in.
Valid Values: `en | ja | zh | fr | de | ko | zh_TW | it | es | pt_BR | id`

 ** [recommendationIdentifier](#API_GetRecommendation_RequestSyntax) **   <a name="ta-GetRecommendation-request-uri-recommendationIdentifier"></a>
The Recommendation identifier
Length Constraints: Minimum length of 20. Maximum length of 200.
Pattern: `arn:[\w-]+:trustedadvisor::\d{12}:recommendation\/[\w-]+`
Required: Yes

## Request Body
<a name="API_GetRecommendation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRecommendation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "recommendation": {
      "arn": "string",
      "awsServices": [ "string" ],
      "checkArn": "string",
      "createdAt": "string",
      "createdBy": "string",
      "description": "string",
      "id": "string",
      "lastUpdatedAt": "string",
      "lifecycleStage": "string",
      "name": "string",
      "pillars": [ "string" ],
      "pillarSpecificAggregates": {
         "costOptimizing": {
            "estimatedMonthlySavings": number,
            "estimatedPercentMonthlySavings": number
         }
      },
      "resolvedAt": "string",
      "resourcesAggregates": {
         "errorCount": number,
         "excludedCount": number,
         "okCount": number,
         "warningCount": number
      },
      "source": "string",
      "status": "string",
      "statusReason": "string",
      "type": "string",
      "updatedOnBehalfOf": "string",
      "updatedOnBehalfOfJobTitle": "string",
      "updateReason": "string",
      "updateReasonCode": "string"
   }
}
```

## Response Elements
<a name="API_GetRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [recommendation](#API_GetRecommendation_ResponseSyntax) **   <a name="ta-GetRecommendation-response-recommendation"></a>
The Recommendation
Type: [Recommendation](API_Recommendation.md) object

## Errors
<a name="API_GetRecommendation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Exception that access has been denied due to insufficient access
HTTP Status Code: 403

 ** InternalServerException **
Exception to notify that an unexpected internal error occurred during processing of the request
HTTP Status Code: 500

 ** ResourceNotFoundException **
Exception that the requested resource has not been found
HTTP Status Code: 404

 ** ThrottlingException **
Exception to notify that requests are being throttled
HTTP Status Code: 429

 ** ValidationException **
Exception that the request failed to satisfy service constraints
HTTP Status Code: 400

## Examples
<a name="API_GetRecommendation_Examples"></a>

### Get A Recommendation
<a name="API_GetRecommendation_Example_1"></a>

Get a recommendation by identifier.

#### Sample Request
<a name="API_GetRecommendation_Example_1_Request"></a>

```
{
                    "recommendationIdentifier": "arn:aws:trustedadvisor::000000000000:recommendation/55fa4d2e-bbb7-491a-833b-5773e9589578",
                    }
```

#### Sample Response
<a name="API_GetRecommendation_Example_1_Response"></a>

```
{
                    "recommendation": {
                    "arn": "arn:aws:trustedadvisor::000000000000:recommendation/55fa4d2e-bbb7-491a-833b-5773e9589578",
                    "name": "MFA Recommendation",
                    "description": "Enable multi-factor authentication",
                    "awsServices": [
                    "iam"
                    ],
                    "checkArn": "arn:aws:trustedadvisor:::check/7DAFEmoDos",
                    "id": "55fa4d2e-bbb7-491a-833b-5773e9589578",
                    "lastUpdatedAt": "2023-11-01T15:57:58.673Z",
                    "pillarSpecificAggregates": {
                    "costOptimizing": {
                    "estimatedMonthlySavings": 0.0,
                    "estimatedPercentMonthlySavings": 0.0
                    }
                    },
                    "pillars": [
                    "security"
                    ],
                    "resourcesAggregates": {
                    "errorCount": 1,
                    "okCount": 0,
                    "warningCount": 0
                    },
                    "source": "ta_check",
                    "status": "error",
                    "type": "standard"
                    }
                    }
```

## See Also
<a name="API_GetRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/trustedadvisor-2022-09-15/GetRecommendation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/trustedadvisor-2022-09-15/GetRecommendation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/GetRecommendation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/trustedadvisor-2022-09-15/GetRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/GetRecommendation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/trustedadvisor-2022-09-15/GetRecommendation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/trustedadvisor-2022-09-15/GetRecommendation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/trustedadvisor-2022-09-15/GetRecommendation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/trustedadvisor-2022-09-15/GetRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/GetRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Trusted Advisor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query trustedadvisor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
