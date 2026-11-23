---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_GetDeploymentConfigurationJob.html
---

# GetDeploymentConfigurationJob

Returns the details of a deployment configuration job. Only the seller that started the job can call this operation.

If the job doesn't belong to the product and delivery option in the request path, the operation returns a `ResourceNotFoundException`.

## Request Syntax
<a name="API_marketplace-deployment_GetDeploymentConfigurationJob_RequestSyntax"></a>

```
GET /catalogs/{{catalog}}/products/{{productId}}/delivery-options/{{deliveryOptionType}}/deployment-configuration/jobs/{{jobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_marketplace-deployment_GetDeploymentConfigurationJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [catalog](#API_marketplace-deployment_GetDeploymentConfigurationJob_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_GetDeploymentConfigurationJob-request-uri-catalog"></a>
The catalog related to the request. Fixed value: `AWSMarketplace`
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z_-]+`
Required: Yes

 ** [deliveryOptionType](#API_marketplace-deployment_GetDeploymentConfigurationJob_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_GetDeploymentConfigurationJob-request-uri-deliveryOptionType"></a>
The delivery option type of the deployment configuration.
Valid Values: `data-as-a-service`
Required: Yes

 ** [jobId](#API_marketplace-deployment_GetDeploymentConfigurationJob_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_GetDeploymentConfigurationJob-request-uri-jobId"></a>
The unique identifier of the deployment configuration job.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** [productId](#API_marketplace-deployment_GetDeploymentConfigurationJob_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_GetDeploymentConfigurationJob-request-uri-productId"></a>
The ID of the AWS Marketplace product, for example `prod-1234567890abc`.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

## Request Body
<a name="API_marketplace-deployment_GetDeploymentConfigurationJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_marketplace-deployment_GetDeploymentConfigurationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuration": { ... },
   "configurationArn": "string",
   "createdAt": "string",
   "endedAt": "string",
   "errorCode": "string",
   "jobId": "string",
   "message": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_marketplace-deployment_GetDeploymentConfigurationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuration](#API_marketplace-deployment_GetDeploymentConfigurationJob_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_GetDeploymentConfigurationJob-response-configuration"></a>
The deployment configuration submitted with the job.
Type: [DeploymentConfigurationDetail](API_marketplace-deployment_DeploymentConfigurationDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdAt](#API_marketplace-deployment_GetDeploymentConfigurationJob_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_GetDeploymentConfigurationJob-response-createdAt"></a>
The date and time when the job was created.
Type: Timestamp

 ** [jobId](#API_marketplace-deployment_GetDeploymentConfigurationJob_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_GetDeploymentConfigurationJob-response-jobId"></a>
The unique identifier of the deployment configuration job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [status](#API_marketplace-deployment_GetDeploymentConfigurationJob_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_GetDeploymentConfigurationJob-response-status"></a>
The status of the deployment configuration job.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`

 ** [configurationArn](#API_marketplace-deployment_GetDeploymentConfigurationJob_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_GetDeploymentConfigurationJob-response-configurationArn"></a>
The Amazon Resource Name (ARN) of the deployment configuration. This field is present only when the job status is `SUCCEEDED`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:*/-]+`

 ** [endedAt](#API_marketplace-deployment_GetDeploymentConfigurationJob_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_GetDeploymentConfigurationJob-response-endedAt"></a>
The date and time when the job reached the `SUCCEEDED` or `FAILED` status.
Type: Timestamp

 ** [errorCode](#API_marketplace-deployment_GetDeploymentConfigurationJob_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_GetDeploymentConfigurationJob-response-errorCode"></a>
The error code that describes why the job failed. This field is present only when the job status is `FAILED`.
Type: String
Valid Values: `FULFILLMENT_URL_UNREACHABLE | INTERNAL_ERROR | ENDPOINT_INVALID`

 ** [message](#API_marketplace-deployment_GetDeploymentConfigurationJob_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_GetDeploymentConfigurationJob-response-message"></a>
A message that describes why the job failed. This field is present only when the job status is `FAILED`.
Type: String

## Errors
<a name="API_marketplace-deployment_GetDeploymentConfigurationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
There was an internal service exception.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
Too many requests.
HTTP Status Code: 429

 ** ValidationException **
An error occurred during validation.
 ** fieldName **
The field name associated with the error.
HTTP Status Code: 400

## See Also
<a name="API_marketplace-deployment_GetDeploymentConfigurationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-deployment-2023-01-25/GetDeploymentConfigurationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-deployment-2023-01-25/GetDeploymentConfigurationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-deployment-2023-01-25/GetDeploymentConfigurationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-deployment-2023-01-25/GetDeploymentConfigurationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-deployment-2023-01-25/GetDeploymentConfigurationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-deployment-2023-01-25/GetDeploymentConfigurationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-deployment-2023-01-25/GetDeploymentConfigurationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-deployment-2023-01-25/GetDeploymentConfigurationJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-deployment-2023-01-25/GetDeploymentConfigurationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-deployment-2023-01-25/GetDeploymentConfigurationJob)
