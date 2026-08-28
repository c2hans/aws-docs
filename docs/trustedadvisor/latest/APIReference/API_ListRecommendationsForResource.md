---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_ListRecommendationsForResource.html
---

# ListRecommendationsForResource
<a name="API_ListRecommendationsForResource"></a>

List all Trusted Advisor recommendations for a given AWS resource ARN.

## Request Syntax
<a name="API_ListRecommendationsForResource_RequestSyntax"></a>

```
GET /v1/recommendations-for-resource/{{awsResourceArn}}?checkArn={{checkArn}}&language={{language}}&maxResults={{maxResults}}&nextToken={{nextToken}}&pillar={{pillar}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRecommendationsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [awsResourceArn](#API_ListRecommendationsForResource_RequestSyntax) **   <a name="ta-ListRecommendationsForResource-request-uri-awsResourceArn"></a>
The ARN of the AWS resource to query recommendations for
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*`
Required: Yes

 ** [checkArn](#API_ListRecommendationsForResource_RequestSyntax) **   <a name="ta-ListRecommendationsForResource-request-uri-checkArn"></a>
The AWS Trusted Advisor Check ARN that relates to the Recommendation
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w-]+:trustedadvisor:::check\/[\w-]+`

 ** [language](#API_ListRecommendationsForResource_RequestSyntax) **   <a name="ta-ListRecommendationsForResource-request-uri-language"></a>
The ISO 639-1 code for the language that you want your recommendations to appear in.
Valid Values: `en | ja | zh | fr | de | ko | zh_TW | it | es | pt_BR | id`

 ** [maxResults](#API_ListRecommendationsForResource_RequestSyntax) **   <a name="ta-ListRecommendationsForResource-request-uri-maxResults"></a>
The maximum number of results to return per page
Valid Range: Minimum value of 1. Maximum value of 600.

 ** [nextToken](#API_ListRecommendationsForResource_RequestSyntax) **   <a name="ta-ListRecommendationsForResource-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 4. Maximum length of 10000.

 ** [pillar](#API_ListRecommendationsForResource_RequestSyntax) **   <a name="ta-ListRecommendationsForResource-request-uri-pillar"></a>
The pillar that the recommendation belongs to
Valid Values: `cost_optimizing | performance | security | service_limits | fault_tolerance | operational_excellence`

 ** [status](#API_ListRecommendationsForResource_RequestSyntax) **   <a name="ta-ListRecommendationsForResource-request-uri-status"></a>
The current status of the Recommendation Resource
Valid Values: `ok | warning | error`

## Request Body
<a name="API_ListRecommendationsForResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRecommendationsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "recommendationForResourceSummaries": [
      {
         "awsResourceArn": "string",
         "checkArn": "string",
         "exclusionStatus": "string",
         "lastUpdatedAt": "string",
         "metadata": {
            "string" : "string"
         },
         "pillars": [ "string" ],
         "recommendationArn": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRecommendationsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRecommendationsForResource_ResponseSyntax) **   <a name="ta-ListRecommendationsForResource-response-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.

 ** [recommendationForResourceSummaries](#API_ListRecommendationsForResource_ResponseSyntax) **   <a name="ta-ListRecommendationsForResource-response-recommendationForResourceSummaries"></a>
List of Trusted Advisor recommendations associated with the given AWS resource
Type: Array of [RecommendationForResourceSummary](API_RecommendationForResourceSummary.md) objects

## Errors
<a name="API_ListRecommendationsForResource_Errors"></a>

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
<a name="API_ListRecommendationsForResource_Examples"></a>

### List All Recommendations for an AWS Resource
<a name="API_ListRecommendationsForResource_Example_1"></a>

List all Trusted Advisor recommendations associated with an AWS resource by its ARN.

#### Sample Request
<a name="API_ListRecommendationsForResource_Example_1_Request"></a>

```
{
                    "awsResourceArn": "arn:aws:ec2:us-east-1:000000000000:instance/i-0abcd1234efgh5678"
                    }
```

#### Sample Response
<a name="API_ListRecommendationsForResource_Example_1_Response"></a>

```
{
                    "recommendationForResourceSummaries": [
                    {
                    "checkArn": "arn:aws:trustedadvisor:::check/Qch7DwouX1",
                    "recommendationArn": "arn:aws:trustedadvisor::000000000000:recommendation/55fa4d2e-bbb7-491a-833b-5773e9589578",
                    "awsResourceArn": "arn:aws:ec2:us-east-1:000000000000:instance/i-0abcd1234efgh5678",
                    "status": "warning",
                    "lastUpdatedAt": "2026-05-21T15:09:51.891Z",
                    "exclusionStatus": "included",
                    "metadata": {
                    "Region": "us-east-1",
                    "Resource": "i-0abcd1234efgh5678",
                    "Status": "Yellow"
                    },
                    "pillars": [
                    "cost_optimizing"
                    ]
                    }
                    ],
                    "nextToken": "REDACTED"
                    }
```

## See Also
<a name="API_ListRecommendationsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/trustedadvisor-2022-09-15/ListRecommendationsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/trustedadvisor-2022-09-15/ListRecommendationsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/ListRecommendationsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/trustedadvisor-2022-09-15/ListRecommendationsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/ListRecommendationsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/trustedadvisor-2022-09-15/ListRecommendationsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/trustedadvisor-2022-09-15/ListRecommendationsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/trustedadvisor-2022-09-15/ListRecommendationsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/trustedadvisor-2022-09-15/ListRecommendationsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/ListRecommendationsForResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Trusted Advisor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query trustedadvisor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
