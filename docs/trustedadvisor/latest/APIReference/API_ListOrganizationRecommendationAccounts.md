---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_ListOrganizationRecommendationAccounts.html
---

# ListOrganizationRecommendationAccounts
<a name="API_ListOrganizationRecommendationAccounts"></a>

Lists the accounts that own the resources for an organization aggregate recommendation. This API only supports prioritized recommendations and provides global priority recommendations, eliminating the need to call the API in each AWS Region.

## Request Syntax
<a name="API_ListOrganizationRecommendationAccounts_RequestSyntax"></a>

```
GET /v1/organization-recommendations/{{organizationRecommendationIdentifier}}/accounts?affectedAccountId={{affectedAccountId}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListOrganizationRecommendationAccounts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [affectedAccountId](#API_ListOrganizationRecommendationAccounts_RequestSyntax) **   <a name="ta-ListOrganizationRecommendationAccounts-request-uri-affectedAccountId"></a>
An account affected by this organization recommendation
Length Constraints: Fixed length of 12.
Pattern: `\d+`

 ** [maxResults](#API_ListOrganizationRecommendationAccounts_RequestSyntax) **   <a name="ta-ListOrganizationRecommendationAccounts-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 200.

 ** [nextToken](#API_ListOrganizationRecommendationAccounts_RequestSyntax) **   <a name="ta-ListOrganizationRecommendationAccounts-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 4. Maximum length of 10000.

 ** [organizationRecommendationIdentifier](#API_ListOrganizationRecommendationAccounts_RequestSyntax) **   <a name="ta-ListOrganizationRecommendationAccounts-request-uri-organizationRecommendationIdentifier"></a>
The Recommendation identifier
Length Constraints: Minimum length of 20. Maximum length of 200.
Pattern: `arn:[\w-]+:trustedadvisor:::organization-recommendation\/[\w-]+`
Required: Yes

## Request Body
<a name="API_ListOrganizationRecommendationAccounts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListOrganizationRecommendationAccounts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accountRecommendationLifecycleSummaries": [
      {
         "accountId": "string",
         "accountRecommendationArn": "string",
         "lastUpdatedAt": "string",
         "lifecycleStage": "string",
         "updatedOnBehalfOf": "string",
         "updatedOnBehalfOfJobTitle": "string",
         "updateReason": "string",
         "updateReasonCode": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListOrganizationRecommendationAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountRecommendationLifecycleSummaries](#API_ListOrganizationRecommendationAccounts_ResponseSyntax) **   <a name="ta-ListOrganizationRecommendationAccounts-response-accountRecommendationLifecycleSummaries"></a>
The account recommendations lifecycles that are applicable to the Recommendation
Type: Array of [AccountRecommendationLifecycleSummary](API_AccountRecommendationLifecycleSummary.md) objects

 ** [nextToken](#API_ListOrganizationRecommendationAccounts_ResponseSyntax) **   <a name="ta-ListOrganizationRecommendationAccounts-response-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.

## Errors
<a name="API_ListOrganizationRecommendationAccounts_Errors"></a>

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
<a name="API_ListOrganizationRecommendationAccounts_Examples"></a>

### List Accounts For An Organization Recommendation
<a name="API_ListOrganizationRecommendationAccounts_Example_1"></a>

List all account recommendation summaries for an organization recommendation by its identifier.

#### Sample Request
<a name="API_ListOrganizationRecommendationAccounts_Example_1_Request"></a>

```
{
                    "organizationRecommendationIdentifier": "arn:aws:trustedadvisor:::organization-recommendation/9534ec9b-bf3a-44e8-8213-2ed68b39d9d5"
                    }
```

#### Sample Response
<a name="API_ListOrganizationRecommendationAccounts_Example_1_Response"></a>

```
{
                    "accountRecommendationLifecycleSummaries": [{
                    "accountId": "000000000000",
                    "accountRecommendationArn": "arn:aws:trustedadvisor::000000000000:recommendation/9534ec9b-bf3a-44e8-8213-2ed68b39d9d5",
                    "lifecycleStage": "resolved",
                    "updateReason": "Resolved issue",
                    "updateReasonCode": "valid_business_case",
                    "lastUpdatedAt": "2023-01-17T18:25:44.552Z"
                    }],
                    "nextToken": "REDACTED"
                    }
```

## See Also
<a name="API_ListOrganizationRecommendationAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/trustedadvisor-2022-09-15/ListOrganizationRecommendationAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/trustedadvisor-2022-09-15/ListOrganizationRecommendationAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/ListOrganizationRecommendationAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/trustedadvisor-2022-09-15/ListOrganizationRecommendationAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/ListOrganizationRecommendationAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/trustedadvisor-2022-09-15/ListOrganizationRecommendationAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/trustedadvisor-2022-09-15/ListOrganizationRecommendationAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/trustedadvisor-2022-09-15/ListOrganizationRecommendationAccounts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/trustedadvisor-2022-09-15/ListOrganizationRecommendationAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/ListOrganizationRecommendationAccounts)
