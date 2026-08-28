---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_ListRecommendations.html
---

# ListRecommendations
<a name="API_ListRecommendations"></a>

List a filterable set of Recommendations. This API provides global recommendations, eliminating the need to call the API in each AWS Region.

## Request Syntax
<a name="API_ListRecommendations_RequestSyntax"></a>

```
GET /v1/recommendations?afterLastUpdatedAt={{afterLastUpdatedAt}}&awsService={{awsService}}&beforeLastUpdatedAt={{beforeLastUpdatedAt}}&checkIdentifier={{checkIdentifier}}&language={{language}}&maxResults={{maxResults}}&nextToken={{nextToken}}&pillar={{pillar}}&source={{source}}&status={{status}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRecommendations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [afterLastUpdatedAt](#API_ListRecommendations_RequestSyntax) **   <a name="ta-ListRecommendations-request-uri-afterLastUpdatedAt"></a>
After the last update of the Recommendation

 ** [awsService](#API_ListRecommendations_RequestSyntax) **   <a name="ta-ListRecommendations-request-uri-awsService"></a>
The aws service associated with the Recommendation
Length Constraints: Minimum length of 2. Maximum length of 30.

 ** [beforeLastUpdatedAt](#API_ListRecommendations_RequestSyntax) **   <a name="ta-ListRecommendations-request-uri-beforeLastUpdatedAt"></a>
Before the last update of the Recommendation

 ** [checkIdentifier](#API_ListRecommendations_RequestSyntax) **   <a name="ta-ListRecommendations-request-uri-checkIdentifier"></a>
The check identifier of the Recommendation
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `arn:[\w-]+:trustedadvisor:::check\/[\w-]+`

 ** [language](#API_ListRecommendations_RequestSyntax) **   <a name="ta-ListRecommendations-request-uri-language"></a>
The ISO 639-1 code for the language that you want your recommendations to appear in.
Valid Values: `en | ja | zh | fr | de | ko | zh_TW | it | es | pt_BR | id`

 ** [maxResults](#API_ListRecommendations_RequestSyntax) **   <a name="ta-ListRecommendations-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 200.

 ** [nextToken](#API_ListRecommendations_RequestSyntax) **   <a name="ta-ListRecommendations-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 4. Maximum length of 10000.

 ** [pillar](#API_ListRecommendations_RequestSyntax) **   <a name="ta-ListRecommendations-request-uri-pillar"></a>
The pillar of the Recommendation
Valid Values: `cost_optimizing | performance | security | service_limits | fault_tolerance | operational_excellence`

 ** [source](#API_ListRecommendations_RequestSyntax) **   <a name="ta-ListRecommendations-request-uri-source"></a>
The source of the Recommendation
Valid Values: `aws_config | compute_optimizer | cost_explorer | lse | manual | pse | rds | resilience | resilience_hub | security_hub | stir | ta_check | well_architected | cost_optimization_hub`

 ** [status](#API_ListRecommendations_RequestSyntax) **   <a name="ta-ListRecommendations-request-uri-status"></a>
The status of the Recommendation
Valid Values: `ok | warning | error`

 ** [type](#API_ListRecommendations_RequestSyntax) **   <a name="ta-ListRecommendations-request-uri-type"></a>
The type of the Recommendation
Valid Values: `standard | priority`

## Request Body
<a name="API_ListRecommendations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "recommendationSummaries": [
      {
         "arn": "string",
         "awsServices": [ "string" ],
         "checkArn": "string",
         "createdAt": "string",
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
         "resourcesAggregates": {
            "errorCount": number,
            "excludedCount": number,
            "okCount": number,
            "warningCount": number
         },
         "source": "string",
         "status": "string",
         "statusReason": "string",
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRecommendations_ResponseSyntax) **   <a name="ta-ListRecommendations-response-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.

 ** [recommendationSummaries](#API_ListRecommendations_ResponseSyntax) **   <a name="ta-ListRecommendations-response-recommendationSummaries"></a>
The list of Recommendations
Type: Array of [RecommendationSummary](API_RecommendationSummary.md) objects

## Errors
<a name="API_ListRecommendations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Exception that access has been denied due to insufficient access
HTTP Status Code: 403

 ** InternalServerException **
Exception to notify that an unexpected internal error occurred during processing of the request
HTTP Status Code: 500

 ** ThrottlingException **
Exception to notify that requests are being throttled
HTTP Status Code: 429

 ** ValidationException **
Exception that the request failed to satisfy service constraints
HTTP Status Code: 400

## Examples
<a name="API_ListRecommendations_Examples"></a>

### List All Recommendations
<a name="API_ListRecommendations_Example_1"></a>

List all recommendations and do not include a filter.

#### Sample Response
<a name="API_ListRecommendations_Example_1_Response"></a>

```
{
                    "recommendationSummaries": [
                    {
                    "arn": "arn:aws:trustedadvisor::000000000000:recommendation/55fa4d2e-bbb7-491a-833b-5773e9589578",
                    "name": "MFA Recommendation",
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
                    },
                    {
                    "arn": "arn:aws:trustedadvisor::000000000000:recommendation/8b602b6f-452d-4cb2-8a9e-c7650955d9cd",
                    "name": "RDS clusters quota warning",
                    "awsServices": [
                    "rds"
                    ],
                    "checkArn": "arn:aws:trustedadvisor:::check/gjqMBn6pjz",
                    "id": "8b602b6f-452d-4cb2-8a9e-c7650955d9cd",
                    "lastUpdatedAt": "2023-11-01T15:58:17.397Z",
                    "pillarSpecificAggregates": {
                    "costOptimizing": {
                    "estimatedMonthlySavings": 0.0,
                    "estimatedPercentMonthlySavings": 0.0
                    }
                    },
                    "pillars": [
                    "service_limits"
                    ],
                    "resourcesAggregates": {
                    "errorCount": 0,
                    "okCount": 3,
                    "warningCount": 6
                    },
                    "source": "ta_check",
                    "status": "warning",
                    "type": "standard"
                    }
                    ],
                    "nextToken": "REDACTED"
                    }
```

### List Recommendations With Filter
<a name="API_ListRecommendations_Example_2"></a>

Filter and return a max of one Recommendation that regards AWS IAM.

#### Sample Request
<a name="API_ListRecommendations_Example_2_Request"></a>

```
{
                    "awsService": "iam",
                    "maxResults": 100
                    }
```

#### Sample Response
<a name="API_ListRecommendations_Example_2_Response"></a>

```
{
                    "recommendationSummaries": [{
                    "arn": "arn:aws:trustedadvisor::000000000000:recommendation/55fa4d2e-bbb7-491a-833b-5773e9589578",
                    "name": "MFA Recommendation",
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
                    }],
                    "nextToken": "REDACTED"
                    }
```

### Fetch The Next Page Of A Previous Request
<a name="API_ListRecommendations_Example_3"></a>

Use the "nextToken" returned from a previous request to fetch the next page of filtered Recommendations.

#### Sample Request
<a name="API_ListRecommendations_Example_3_Request"></a>

```
{
                    "nextToken": "REDACTED",
                    "awsService": "rds",
                    "maxResults": 100
                    }
```

#### Sample Response
<a name="API_ListRecommendations_Example_3_Response"></a>

```
{
                    "recommendationSummaries": [{
                    "arn": "arn:aws:trustedadvisor::000000000000:recommendation/8b602b6f-452d-4cb2-8a9e-c7650955d9cd",
                    "name": "RDS clusters quota warning",
                    "awsServices": [
                    "rds"
                    ],
                    "checkArn": "arn:aws:trustedadvisor:::check/gjqMBn6pjz",
                    "id": "8b602b6f-452d-4cb2-8a9e-c7650955d9cd",
                    "lastUpdatedAt": "2023-11-01T15:58:17.397Z",
                    "pillarSpecificAggregates": {
                    "costOptimizing": {
                    "estimatedMonthlySavings": 0.0,
                    "estimatedPercentMonthlySavings": 0.0
                    }
                    },
                    "pillars": [
                    "service_limits"
                    ],
                    "resourcesAggregates": {
                    "errorCount": 0,
                    "okCount": 3,
                    "warningCount": 6
                    },
                    "source": "ta_check",
                    "status": "warning",
                    "type": "standard"
                    }]
                    }
```

## See Also
<a name="API_ListRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/trustedadvisor-2022-09-15/ListRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/trustedadvisor-2022-09-15/ListRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/ListRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/trustedadvisor-2022-09-15/ListRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/ListRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/trustedadvisor-2022-09-15/ListRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/trustedadvisor-2022-09-15/ListRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/trustedadvisor-2022-09-15/ListRecommendations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/trustedadvisor-2022-09-15/ListRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/ListRecommendations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Trusted Advisor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query trustedadvisor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
