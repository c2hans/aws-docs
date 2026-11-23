---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_ListDeploymentConfigurationJobs.html
---

# ListDeploymentConfigurationJobs

Lists the deployment configuration jobs that you started for a product and delivery option, ordered from newest to oldest. Results are paginated. Use the `nextToken` parameter to retrieve additional results.

If you haven't started any jobs for the product and delivery option, the operation returns an empty `jobs` list.

## Request Syntax
<a name="API_marketplace-deployment_ListDeploymentConfigurationJobs_RequestSyntax"></a>

```
GET /catalogs/{{catalog}}/products/{{productId}}/delivery-options/{{deliveryOptionType}}/deployment-configuration/jobs?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_marketplace-deployment_ListDeploymentConfigurationJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [catalog](#API_marketplace-deployment_ListDeploymentConfigurationJobs_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_ListDeploymentConfigurationJobs-request-uri-catalog"></a>
The catalog related to the request. Fixed value: `AWSMarketplace`
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z_-]+`
Required: Yes

 ** [deliveryOptionType](#API_marketplace-deployment_ListDeploymentConfigurationJobs_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_ListDeploymentConfigurationJobs-request-uri-deliveryOptionType"></a>
The delivery option type of the deployment configuration.
Valid Values: `data-as-a-service`
Required: Yes

 ** [maxResults](#API_marketplace-deployment_ListDeploymentConfigurationJobs_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_ListDeploymentConfigurationJobs-request-uri-maxResults"></a>
The maximum number of jobs to return in a single page. Valid values are 1 through 100. The default is 20.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_marketplace-deployment_ListDeploymentConfigurationJobs_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_ListDeploymentConfigurationJobs-request-uri-nextToken"></a>
The token for the next page of results. Use the value returned in the previous response.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [productId](#API_marketplace-deployment_ListDeploymentConfigurationJobs_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_ListDeploymentConfigurationJobs-request-uri-productId"></a>
The ID of the AWS Marketplace product, for example `prod-1234567890abc`.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

## Request Body
<a name="API_marketplace-deployment_ListDeploymentConfigurationJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_marketplace-deployment_ListDeploymentConfigurationJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobs": [
      {
         "configuration": { ... },
         "createdAt": "string",
         "jobId": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_marketplace-deployment_ListDeploymentConfigurationJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_marketplace-deployment_ListDeploymentConfigurationJobs_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_ListDeploymentConfigurationJobs-response-jobs"></a>
A list of deployment configuration job summaries, ordered from newest to oldest.
Type: Array of [DeploymentConfigurationJobSummary](API_marketplace-deployment_DeploymentConfigurationJobSummary.md) objects

 ** [nextToken](#API_marketplace-deployment_ListDeploymentConfigurationJobs_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_ListDeploymentConfigurationJobs-response-nextToken"></a>
The token for the next page of results. This value is absent when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_marketplace-deployment_ListDeploymentConfigurationJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
There was an internal service exception.
HTTP Status Code: 500

 ** ThrottlingException **
Too many requests.
HTTP Status Code: 429

 ** ValidationException **
An error occurred during validation.
 ** fieldName **
The field name associated with the error.
HTTP Status Code: 400

## See Also
<a name="API_marketplace-deployment_ListDeploymentConfigurationJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-deployment-2023-01-25/ListDeploymentConfigurationJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-deployment-2023-01-25/ListDeploymentConfigurationJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-deployment-2023-01-25/ListDeploymentConfigurationJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-deployment-2023-01-25/ListDeploymentConfigurationJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-deployment-2023-01-25/ListDeploymentConfigurationJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-deployment-2023-01-25/ListDeploymentConfigurationJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-deployment-2023-01-25/ListDeploymentConfigurationJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-deployment-2023-01-25/ListDeploymentConfigurationJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-deployment-2023-01-25/ListDeploymentConfigurationJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-deployment-2023-01-25/ListDeploymentConfigurationJobs)
