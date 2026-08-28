---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_ListOrganizationRecommendations.html
---

# ListOrganizationRecommendations
<a name="API_ListOrganizationRecommendations"></a>

List a filterable set of Recommendations within an Organization. This API only supports prioritized recommendations and provides global priority recommendations, eliminating the need to call the API in each AWS Region.

## Request Syntax
<a name="API_ListOrganizationRecommendations_RequestSyntax"></a>

```
GET /v1/organization-recommendations?afterLastUpdatedAt={{afterLastUpdatedAt}}&awsService={{awsService}}&beforeLastUpdatedAt={{beforeLastUpdatedAt}}&checkIdentifier={{checkIdentifier}}&maxResults={{maxResults}}&nextToken={{nextToken}}&pillar={{pillar}}&source={{source}}&status={{status}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListOrganizationRecommendations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [afterLastUpdatedAt](#API_ListOrganizationRecommendations_RequestSyntax) **   <a name="ta-ListOrganizationRecommendations-request-uri-afterLastUpdatedAt"></a>
After the last update of the Recommendation

 ** [awsService](#API_ListOrganizationRecommendations_RequestSyntax) **   <a name="ta-ListOrganizationRecommendations-request-uri-awsService"></a>
The aws service associated with the Recommendation
Length Constraints: Minimum length of 2. Maximum length of 30.

 ** [beforeLastUpdatedAt](#API_ListOrganizationRecommendations_RequestSyntax) **   <a name="ta-ListOrganizationRecommendations-request-uri-beforeLastUpdatedAt"></a>
Before the last update of the Recommendation

 ** [checkIdentifier](#API_ListOrganizationRecommendations_RequestSyntax) **   <a name="ta-ListOrganizationRecommendations-request-uri-checkIdentifier"></a>
The check identifier of the Recommendation
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `arn:[\w-]+:trustedadvisor:::check\/[\w-]+`

 ** [maxResults](#API_ListOrganizationRecommendations_RequestSyntax) **   <a name="ta-ListOrganizationRecommendations-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 200.

 ** [nextToken](#API_ListOrganizationRecommendations_RequestSyntax) **   <a name="ta-ListOrganizationRecommendations-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 4. Maximum length of 10000.

 ** [pillar](#API_ListOrganizationRecommendations_RequestSyntax) **   <a name="ta-ListOrganizationRecommendations-request-uri-pillar"></a>
The pillar of the Recommendation
Valid Values: `cost_optimizing | performance | security | service_limits | fault_tolerance | operational_excellence`

 ** [source](#API_ListOrganizationRecommendations_RequestSyntax) **   <a name="ta-ListOrganizationRecommendations-request-uri-source"></a>
The source of the Recommendation
Valid Values: `aws_config | compute_optimizer | cost_explorer | lse | manual | pse | rds | resilience | resilience_hub | security_hub | stir | ta_check | well_architected | cost_optimization_hub`

 ** [status](#API_ListOrganizationRecommendations_RequestSyntax) **   <a name="ta-ListOrganizationRecommendations-request-uri-status"></a>
The status of the Recommendation
Valid Values: `ok | warning | error`

 ** [type](#API_ListOrganizationRecommendations_RequestSyntax) **   <a name="ta-ListOrganizationRecommendations-request-uri-type"></a>
The type of the Recommendation
Valid Values: `standard | priority`

## Request Body
<a name="API_ListOrganizationRecommendations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListOrganizationRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "organizationRecommendationSummaries": [
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
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListOrganizationRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListOrganizationRecommendations_ResponseSyntax) **   <a name="ta-ListOrganizationRecommendations-response-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.

 ** [organizationRecommendationSummaries](#API_ListOrganizationRecommendations_ResponseSyntax) **   <a name="ta-ListOrganizationRecommendations-response-organizationRecommendationSummaries"></a>
The list of Recommendations
Type: Array of [OrganizationRecommendationSummary](API_OrganizationRecommendationSummary.md) objects

## Errors
<a name="API_ListOrganizationRecommendations_Errors"></a>

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
<a name="API_ListOrganizationRecommendations_Examples"></a>

### List All Organization Recommendations
<a name="API_ListOrganizationRecommendations_Example_1"></a>

List all organization recommendations and do not include a filter.

#### Sample Response
<a name="API_ListOrganizationRecommendations_Example_1_Response"></a>

```
{
                    "organizationRecommendationSummaries": [
                    {
                    "arn": "arn:aws:trustedadvisor:::organization-recommendation/9534ec9b-bf3a-44e8-8213-2ed68b39d9d5",
                    "name": "Lambda Runtime Deprecation Warning",
                    "awsServices": [
                    "lambda"
                    ],
                    "checkArn": "arn:aws:trustedadvisor:::check/L4dfs2Q4C5",
                    "id": "9534ec9b-bf3a-44e8-8213-2ed68b39d9d5",
                    "lifecycleStage": "resolved",
                    "pillars": [
                    "security"
                    ],
                    "resourcesAggregates": {
                    "errorCount": 0,
                    "okCount": 0,
                    "warningCount": 0
                    },
                    "source": "ta_check",
                    "status": "warning",
                    "type": "priority"
                    },
                    {
                    "arn": "arn:aws:trustedadvisor:::organization-recommendation/4ecff4d4-1bc1-4c99-a5b8-0fff9ee500d6",
                    "name": "Lambda Runtime Deprecation Warning",
                    "awsServices": [
                    "lambda"
                    ],
                    "checkArn": "arn:aws:trustedadvisor:::check/L4dfs2Q4C5",
                    "id": "4ecff4d4-1bc1-4c99-a5b8-0fff9ee500d6",
                    "lifecycleStage": "resolved",
                    "pillars": [
                    "security"
                    ],
                    "resourcesAggregates": {
                    "errorCount": 0,
                    "okCount": 0,
                    "warningCount": 0
                    },
                    "source": "ta_check",
                    "status": "warning",
                    "type": "priority"
                    },
                    ],
                    "nextToken": "REDACTED"
                    }
```

### List Organization Recommendations With Filter
<a name="API_ListOrganizationRecommendations_Example_2"></a>

Filter and return a max of one organization recommendation that is a part of the "security" pillar.

#### Sample Request
<a name="API_ListOrganizationRecommendations_Example_2_Request"></a>

```
{
                    "pillar": "security",
                    "maxResults": 100
                    }
```

#### Sample Response
<a name="API_ListOrganizationRecommendations_Example_2_Response"></a>

```
{
                    "organizationRecommendationSummaries": [{
                    "arn": "arn:aws:trustedadvisor:::organization-recommendation/9534ec9b-bf3a-44e8-8213-2ed68b39d9d5",
                    "name": "Lambda Runtime Deprecation Warning",
                    "awsServices": [
                    "lambda"
                    ],
                    "checkArn": "arn:aws:trustedadvisor:::check/L4dfs2Q4C5",
                    "id": "9534ec9b-bf3a-44e8-8213-2ed68b39d9d5",
                    "lifecycleStage": "resolved",
                    "pillars": [
                    "security"
                    ],
                    "resourcesAggregates": {
                    "errorCount": 0,
                    "okCount": 0,
                    "warningCount": 0
                    },
                    "source": "ta_check",
                    "status": "warning",
                    "type": "priority"
                    }],
                    "nextToken": "REDACTED"
                    }
```

### Fetch The Next Page Of A Previous Request
<a name="API_ListOrganizationRecommendations_Example_3"></a>

Use the "nextToken" returned from a previous request to fetch the next page of filtered organization recommendations that are a part of the "security" pillar.

#### Sample Request
<a name="API_ListOrganizationRecommendations_Example_3_Request"></a>

```
{
                    "nextToken": "REDACTED",
                    "pillar": "security",
                    "maxResults": 100
                    }
```

#### Sample Response
<a name="API_ListOrganizationRecommendations_Example_3_Response"></a>

```
{
                    "organizationRecommendationSummaries": [{
                    "arn": "arn:aws:trustedadvisor:::organization-recommendation/4ecff4d4-1bc1-4c99-a5b8-0fff9ee500d6",
                    "name": "Lambda Runtime Deprecation Warning",
                    "awsServices": [
                    "lambda"
                    ],
                    "checkArn": "arn:aws:trustedadvisor:::check/L4dfs2Q4C5",
                    "id": "4ecff4d4-1bc1-4c99-a5b8-0fff9ee500d6",
                    "lifecycleStage": "resolved",
                    "pillars": [
                    "security"
                    ],
                    "resourcesAggregates": {
                    "errorCount": 0,
                    "okCount": 0,
                    "warningCount": 0
                    },
                    "source": "ta_check",
                    "status": "warning",
                    "type": "priority"
                    }]
                    }
```

## See Also
<a name="API_ListOrganizationRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/trustedadvisor-2022-09-15/ListOrganizationRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/trustedadvisor-2022-09-15/ListOrganizationRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/ListOrganizationRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/trustedadvisor-2022-09-15/ListOrganizationRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/ListOrganizationRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/trustedadvisor-2022-09-15/ListOrganizationRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/trustedadvisor-2022-09-15/ListOrganizationRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/trustedadvisor-2022-09-15/ListOrganizationRecommendations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/trustedadvisor-2022-09-15/ListOrganizationRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/ListOrganizationRecommendations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Trusted Advisor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query trustedadvisor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
