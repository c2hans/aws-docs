---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_ListOrganizationRecommendationResources.html
---

# ListOrganizationRecommendationResources
<a name="API_ListOrganizationRecommendationResources"></a>

List Resources of a Recommendation within an Organization. This API only supports prioritized recommendations and provides global priority recommendations, eliminating the need to call the API in each AWS Region.

## Request Syntax
<a name="API_ListOrganizationRecommendationResources_RequestSyntax"></a>

```
GET /v1/organization-recommendations/{{organizationRecommendationIdentifier}}/resources?affectedAccountId={{affectedAccountId}}&exclusionStatus={{exclusionStatus}}&maxResults={{maxResults}}&nextToken={{nextToken}}&regionCode={{regionCode}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListOrganizationRecommendationResources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [affectedAccountId](#API_ListOrganizationRecommendationResources_RequestSyntax) **   <a name="ta-ListOrganizationRecommendationResources-request-uri-affectedAccountId"></a>
An account affected by this organization recommendation
Length Constraints: Fixed length of 12.
Pattern: `\d+`

 ** [exclusionStatus](#API_ListOrganizationRecommendationResources_RequestSyntax) **   <a name="ta-ListOrganizationRecommendationResources-request-uri-exclusionStatus"></a>
The exclusion status of the resource
Valid Values: `excluded | included`

 ** [maxResults](#API_ListOrganizationRecommendationResources_RequestSyntax) **   <a name="ta-ListOrganizationRecommendationResources-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 200.

 ** [nextToken](#API_ListOrganizationRecommendationResources_RequestSyntax) **   <a name="ta-ListOrganizationRecommendationResources-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 4. Maximum length of 10000.

 ** [organizationRecommendationIdentifier](#API_ListOrganizationRecommendationResources_RequestSyntax) **   <a name="ta-ListOrganizationRecommendationResources-request-uri-organizationRecommendationIdentifier"></a>
The AWS Organization organization's Recommendation identifier
Length Constraints: Minimum length of 20. Maximum length of 200.
Pattern: `arn:[\w-]+:trustedadvisor:::organization-recommendation\/[\w-]+`
Required: Yes

 ** [regionCode](#API_ListOrganizationRecommendationResources_RequestSyntax) **   <a name="ta-ListOrganizationRecommendationResources-request-uri-regionCode"></a>
The AWS Region code of the resource

 ** [status](#API_ListOrganizationRecommendationResources_RequestSyntax) **   <a name="ta-ListOrganizationRecommendationResources-request-uri-status"></a>
The status of the resource
Valid Values: `ok | warning | error`

## Request Body
<a name="API_ListOrganizationRecommendationResources_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListOrganizationRecommendationResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "organizationRecommendationResourceSummaries": [
      {
         "accountId": "string",
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
<a name="API_ListOrganizationRecommendationResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListOrganizationRecommendationResources_ResponseSyntax) **   <a name="ta-ListOrganizationRecommendationResources-response-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.

 ** [organizationRecommendationResourceSummaries](#API_ListOrganizationRecommendationResources_ResponseSyntax) **   <a name="ta-ListOrganizationRecommendationResources-response-organizationRecommendationResourceSummaries"></a>
A list of Recommendation Resources
Type: Array of [OrganizationRecommendationResourceSummary](API_OrganizationRecommendationResourceSummary.md) objects

## Errors
<a name="API_ListOrganizationRecommendationResources_Errors"></a>

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
<a name="API_ListOrganizationRecommendationResources_Examples"></a>

### List All Organization Recommendation Resources
<a name="API_ListOrganizationRecommendationResources_Example_1"></a>

List all resources for an organization recommendation by its identifier.

#### Sample Request
<a name="API_ListOrganizationRecommendationResources_Example_1_Request"></a>

```
{
                    "organizationRecommendationIdentifier": "arn:aws:trustedadvisor:::organization-recommendation/5a694939-2e54-45a2-ae72-730598fa89d0"
                    }
```

#### Sample Response
<a name="API_ListOrganizationRecommendationResources_Example_1_Response"></a>

```
{
                    "organizationRecommendationResourceSummaries": [
                    {
                    "arn": "arn:aws:trustedadvisor::000000000000:recommendation-resource/5a694939-2e54-45a2-ae72-730598fa89d0/bb38affc0ce0681d9a6cd13f30238ba03a8f63dfe7a379dc403c619119d86af",
                    "awsResourceId": "database-1-instance-1",
                    "id": "bb38affc0ce0681d9a6cd13f302383ba03a8f63dfe7a379dc403c619119d86af",
                    "lastUpdatedAt": "2023-11-01T15:09:51.891Z",
                    "metadata": {
                    "0": "14",
                    "1": "208.79999999999998",
                    "2": "database-1-instance-1",
                    "3": "db.r5.large",
                    "4": "false",
                    "5": "us-west-2",
                    "6": "arn:aws:rds:us-west-2:000000000000:db:database-1-instance-1",
                    "7": "1"
                    },
                    "recommendationArn": "arn:aws:trustedadvisor:::organization-recommendation/5a694939-2e54-45a2-ae72-730598fa89d0",
                    "regionCode": "us-west-2",
                    "exclusionStatus": "included",
                    "status": "warning"
                    },
                    {
                    "arn": "arn:aws:trustedadvisor::000000000000:recommendation-resource/5a694939-2e54-45a2-ae72-730598fa89d0/51fded4d7a3278818df9cfe344ff5762cec46c095a6763d1ba1ba53bd0e1b0e6",
                    "awsResourceId": "database-1",
                    "id": "51fded4d7a3278818df9cfe344ff5762cec46c095a6763d1ba1ba53bd0e1b0e6",
                    "lastUpdatedAt": "2023-11-01T15:09:51.891Z",
                    "metadata": {
                    "0": "14",
                    "1": "31.679999999999996",
                    "2": "database-1",
                    "3": "db.t3.small",
                    "4": "false",
                    "5": "us-west-2",
                    "6": "arn:aws:rds:us-west-2:000000000000:db:database-1",
                    "7": "20"
                    },
                    "recommendationArn": "arn:aws:trustedadvisor:::organization-recommendation/5a694939-2e54-45a2-ae72-730598fa89d0",
                    "regionCode": "us-west-2",
                    "exclusionStatus": "included",
                    "status": "warning"
                    },
                    {
                    "arn": "arn:aws:trustedadvisor::000000000000:recommendation-resource/5a694939-2e54-45a2-ae72-730598fa89d0/f4d01bd20f4cd5372062aafc8786c489e48f0ead7cdab121463bf9f89e40a36b",
                    "awsResourceId": "database-2-instance-1-us-west-2a",
                    "id": "f4d01bd20f4cd5372062aafc8786c489e48f0ead7cdab121463bf9f89e40a36b",
                    "lastUpdatedAt": "2023-11-01T15:09:51.891Z",
                    "metadata": {
                    "0": "14",
                    "1": "187.20000000000002",
                    "2": "database-2-instance-1-us-west-2a",
                    "3": "db.r6g.large",
                    "4": "true",
                    "5": "us-west-2",
                    "6": "arn:aws:rds:us-west-2:000000000000:db:database-2-instance-1-us-west-2a",
                    "7": "1"
                    },
                    "recommendationArn": "arn:aws:trustedadvisor:::organization-recommendation/5a694939-2e54-45a2-ae72-730598fa89d0",
                    "regionCode": "us-west-2",
                    "exclusionStatus": "included",
                    "status": "warning"
                    },
                    ],
                    "nextToken": "REDACTED"
                    }
```

## See Also
<a name="API_ListOrganizationRecommendationResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/trustedadvisor-2022-09-15/ListOrganizationRecommendationResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/trustedadvisor-2022-09-15/ListOrganizationRecommendationResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/ListOrganizationRecommendationResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/trustedadvisor-2022-09-15/ListOrganizationRecommendationResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/ListOrganizationRecommendationResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/trustedadvisor-2022-09-15/ListOrganizationRecommendationResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/trustedadvisor-2022-09-15/ListOrganizationRecommendationResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/trustedadvisor-2022-09-15/ListOrganizationRecommendationResources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/trustedadvisor-2022-09-15/ListOrganizationRecommendationResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/ListOrganizationRecommendationResources)
