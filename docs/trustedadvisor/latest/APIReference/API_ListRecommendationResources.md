---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_ListRecommendationResources.html
---

# ListRecommendationResources
<a name="API_ListRecommendationResources"></a>

List Resources of a Recommendation. This API provides global recommendations, eliminating the need to call the API in each AWS Region.

## Request Syntax
<a name="API_ListRecommendationResources_RequestSyntax"></a>

```
GET /v1/recommendations/{{recommendationIdentifier}}/resources?exclusionStatus={{exclusionStatus}}&language={{language}}&maxResults={{maxResults}}&nextToken={{nextToken}}&regionCode={{regionCode}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRecommendationResources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [exclusionStatus](#API_ListRecommendationResources_RequestSyntax) **   <a name="ta-ListRecommendationResources-request-uri-exclusionStatus"></a>
The exclusion status of the resource
Valid Values: `excluded | included`

 ** [language](#API_ListRecommendationResources_RequestSyntax) **   <a name="ta-ListRecommendationResources-request-uri-language"></a>
The ISO 639-1 code for the language that you want your recommendations to appear in.
Valid Values: `en | ja | zh | fr | de | ko | zh_TW | it | es | pt_BR | id`

 ** [maxResults](#API_ListRecommendationResources_RequestSyntax) **   <a name="ta-ListRecommendationResources-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 5000.

 ** [nextToken](#API_ListRecommendationResources_RequestSyntax) **   <a name="ta-ListRecommendationResources-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 4. Maximum length of 10000.

 ** [recommendationIdentifier](#API_ListRecommendationResources_RequestSyntax) **   <a name="ta-ListRecommendationResources-request-uri-recommendationIdentifier"></a>
The Recommendation identifier
Length Constraints: Minimum length of 20. Maximum length of 200.
Pattern: `arn:[\w-]+:trustedadvisor::\d{12}:recommendation\/[\w-]+`
Required: Yes

 ** [regionCode](#API_ListRecommendationResources_RequestSyntax) **   <a name="ta-ListRecommendationResources-request-uri-regionCode"></a>
The AWS Region code of the resource

 ** [status](#API_ListRecommendationResources_RequestSyntax) **   <a name="ta-ListRecommendationResources-request-uri-status"></a>
The status of the resource
Valid Values: `ok | warning | error`

## Request Body
<a name="API_ListRecommendationResources_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRecommendationResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "recommendationResourceSummaries": [
      {
         "arn": "string",
         "awsResourceId": "string",
         "exclusionStatus": "string",
         "id": "string",
         "lastUpdatedAt": "string",
         "metadata": {
            "string" : "string"
         },
         "recommendationArn": "string",
         "regionCode": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRecommendationResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRecommendationResources_ResponseSyntax) **   <a name="ta-ListRecommendationResources-response-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.

 ** [recommendationResourceSummaries](#API_ListRecommendationResources_ResponseSyntax) **   <a name="ta-ListRecommendationResources-response-recommendationResourceSummaries"></a>
A list of Recommendation Resources
Type: Array of [RecommendationResourceSummary](API_RecommendationResourceSummary.md) objects

## Errors
<a name="API_ListRecommendationResources_Errors"></a>

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
<a name="API_ListRecommendationResources_Examples"></a>

### List All Recommendation Resources
<a name="API_ListRecommendationResources_Example_1"></a>

List all resources for a recommendation by its identifier.

#### Sample Request
<a name="API_ListRecommendationResources_Example_1_Request"></a>

```
{
                    "recommendationIdentifier": "arn:aws:trustedadvisor::000000000000:recommendation/55fa4d2e-bbb7-491a-833b-5773e9589578"
                    }
```

#### Sample Response
<a name="API_ListRecommendationResources_Example_1_Response"></a>

```
{
                    "recommendationResourceSummaries": [
                    {
                    "arn": "arn:aws:trustedadvisor::000000000000:recommendation-resource/55fa4d2e-bbb7-491a-833b-5773e9589578/18959a1f1973cff8e706e9d9bde28bba36cd602a6b2cb86c8b61252835236010",
                    "id": "18959a1f1973cff8e706e9d9bde28bba36cd602a6b2cb86c8b61252835236010",
                    "awsResourceId": "webcms-dev-01",
                    "lastUpdatedAt": "2023-11-01T15:09:51.891Z",
                    "metadata": {
                    "0": "14",
                    "1": "123.12000000000002",
                    "2": "webcms-dev-01",
                    "3": "db.m6i.large",
                    "4": "false",
                    "5": "us-east-1",
                    "6": "arn:aws:rds:us-east-1:000000000000:db:webcms-dev-01",
                    "7": "20"
                    },
                    "recommendationArn": "arn:aws:trustedadvisor::000000000000:recommendation/55fa4d2e-bbb7-491a-833b-5773e9589578",
                    "regionCode": "us-east-1",
                    "exclusionStatus": "included",
                    "status": "warning"
                    },
                    {
                    "arn": "arn:aws:trustedadvisor::000000000000:recommendation-resource/55fa4d2e-bbb7-491a-833b-5773e9589578/e6367ff500ac90db8e4adeb4892e39ee9c36bbf812dcbce4b9e4fefcec9eb63e",
                    "id": "e6367ff500ac90db8e4adeb4892e39ee9c36bbf812dcbce4b9e4fefcec9eb63e",
                    "awsResourceId": "aws-dev-db-stack-instance-1",
                    "lastUpdatedAt": "2023-11-01T15:09:51.891Z",
                    "metadata": {
                    "0": "14",
                    "1": "29.52",
                    "2": "aws-dev-db-stack-instance-1",
                    "3": "db.t2.small",
                    "4": "false",
                    "5": "us-east-1",
                    "6": "arn:aws:rds:us-east-1:000000000000:db:aws-dev-db-stack-instance-1",
                    "7": "1"
                    },
                    "recommendationArn": "arn:aws:trustedadvisor::000000000000:recommendation/55fa4d2e-bbb7-491a-833b-5773e9589578",
                    "regionCode": "us-east-1",
                    "exclusionStatus": "included",
                    "status": "warning"
                    },
                    {
                    "arn": "arn:aws:trustedadvisor::000000000000:recommendation-resource/55fa4d2e-bbb7-491a-833b-5773e9589578/31aa78ba050a5015d2d38cca7f5f1ce88f70857c4e1c3ad03f8f9fd95dad7459",
                    "id": "31aa78ba050a5015d2d38cca7f5f1ce88f70857c4e1c3ad03f8f9fd95dad7459",
                    "awsResourceId": "aws-awesome-apps-stack-db",
                    "lastUpdatedAt": "2023-11-01T15:09:51.891Z",
                    "metadata": {
                    "0": "14",
                    "1": "114.48000000000002",
                    "2": "aws-awesome-apps-stack-db",
                    "3": "db.m6g.large",
                    "4": "false",
                    "5": "us-east-1",
                    "6": "arn:aws:rds:us-east-1:000000000000:db:aws-awesome-apps-stack-db",
                    "7": "100"
                    },
                    "recommendationArn": "arn:aws:trustedadvisor::000000000000:recommendation/55fa4d2e-bbb7-491a-833b-5773e9589578",
                    "regionCode": "us-east-1",
                    "exclusionStatus": "included",
                    "status": "warning"
                    }
                    ],
                    "nextToken": "REDACTED"
                    }
```

## See Also
<a name="API_ListRecommendationResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/trustedadvisor-2022-09-15/ListRecommendationResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/trustedadvisor-2022-09-15/ListRecommendationResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/ListRecommendationResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/trustedadvisor-2022-09-15/ListRecommendationResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/ListRecommendationResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/trustedadvisor-2022-09-15/ListRecommendationResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/trustedadvisor-2022-09-15/ListRecommendationResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/trustedadvisor-2022-09-15/ListRecommendationResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/trustedadvisor-2022-09-15/ListRecommendationResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/ListRecommendationResources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Trusted Advisor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query trustedadvisor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
