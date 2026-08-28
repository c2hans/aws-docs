---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_GetOrganizationRecommendation.html
---

# GetOrganizationRecommendation
<a name="API_GetOrganizationRecommendation"></a>

Get a specific recommendation within an AWS Organizations organization. This API supports only prioritized recommendations and provides global priority recommendations, eliminating the need to call the API in each AWS Region.

## Request Syntax
<a name="API_GetOrganizationRecommendation_RequestSyntax"></a>

```
GET /v1/organization-recommendations/{{organizationRecommendationIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetOrganizationRecommendation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [organizationRecommendationIdentifier](#API_GetOrganizationRecommendation_RequestSyntax) **   <a name="ta-GetOrganizationRecommendation-request-uri-organizationRecommendationIdentifier"></a>
The Recommendation identifier
Length Constraints: Minimum length of 20. Maximum length of 200.
Pattern: `arn:[\w-]+:trustedadvisor:::organization-recommendation\/[\w-]+`
Required: Yes

## Request Body
<a name="API_GetOrganizationRecommendation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetOrganizationRecommendation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "organizationRecommendation": {
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
      "type": "string",
      "updatedOnBehalfOf": "string",
      "updatedOnBehalfOfJobTitle": "string",
      "updateReason": "string",
      "updateReasonCode": "string"
   }
}
```

## Response Elements
<a name="API_GetOrganizationRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [organizationRecommendation](#API_GetOrganizationRecommendation_ResponseSyntax) **   <a name="ta-GetOrganizationRecommendation-response-organizationRecommendation"></a>
The Recommendation
Type: [OrganizationRecommendation](API_OrganizationRecommendation.md) object

## Errors
<a name="API_GetOrganizationRecommendation_Errors"></a>

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
<a name="API_GetOrganizationRecommendation_Examples"></a>

### Get Organization Recommendation
<a name="API_GetOrganizationRecommendation_Example_1"></a>

Get an organization recommendation by identifier.

#### Sample Request
<a name="API_GetOrganizationRecommendation_Example_1_Request"></a>

```
{
                    "organizationRecommendationIdentifier": "arn:aws:trustedadvisor:::organization-recommendation/9534ec9b-bf3a-44e8-8213-2ed68b39d9d5"
                    }
```

#### Sample Response
<a name="API_GetOrganizationRecommendation_Example_1_Response"></a>

```
{
                    "organizationRecommendation": {
                    "arn": "arn:aws:trustedadvisor:::organization-recommendation/9534ec9b-bf3a-44e8-8213-2ed68b39d9d5",
                    "name": "Lambda Runtime Deprecation Warning",
                    "description": "One or more lambdas are using a deprecated runtime",
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
                    }
                    }
```

## See Also
<a name="API_GetOrganizationRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/trustedadvisor-2022-09-15/GetOrganizationRecommendation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/trustedadvisor-2022-09-15/GetOrganizationRecommendation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/GetOrganizationRecommendation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/trustedadvisor-2022-09-15/GetOrganizationRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/GetOrganizationRecommendation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/trustedadvisor-2022-09-15/GetOrganizationRecommendation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/trustedadvisor-2022-09-15/GetOrganizationRecommendation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/trustedadvisor-2022-09-15/GetOrganizationRecommendation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/trustedadvisor-2022-09-15/GetOrganizationRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/GetOrganizationRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Trusted Advisor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query trustedadvisor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
