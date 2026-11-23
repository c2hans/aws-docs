---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_StartDeploymentConfigurationJob.html
---

# StartDeploymentConfigurationJob

Starts a job that publishes a deployment configuration for a product and delivery option. The job runs asynchronously. Use `GetDeploymentConfigurationJob` to track its status. When the job reaches the `SUCCEEDED` status, its configuration becomes the active deployment configuration for the product and delivery option.

The populated member of `configuration` must match the `deliveryOptionType` in the request path.

## Request Syntax
<a name="API_marketplace-deployment_StartDeploymentConfigurationJob_RequestSyntax"></a>

```
POST /catalogs/{{catalog}}/products/{{productId}}/delivery-options/{{deliveryOptionType}}/deployment-configuration/jobs HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "configuration": { ... },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_marketplace-deployment_StartDeploymentConfigurationJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [catalog](#API_marketplace-deployment_StartDeploymentConfigurationJob_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_StartDeploymentConfigurationJob-request-uri-catalog"></a>
The catalog related to the request. Fixed value: `AWSMarketplace`
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z_-]+`
Required: Yes

 ** [deliveryOptionType](#API_marketplace-deployment_StartDeploymentConfigurationJob_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_StartDeploymentConfigurationJob-request-uri-deliveryOptionType"></a>
The delivery option type of the deployment configuration.
Valid Values: `data-as-a-service`
Required: Yes

 ** [productId](#API_marketplace-deployment_StartDeploymentConfigurationJob_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_StartDeploymentConfigurationJob-request-uri-productId"></a>
The ID of the AWS Marketplace product, for example `prod-1234567890abc`.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

## Request Body
<a name="API_marketplace-deployment_StartDeploymentConfigurationJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuration](#API_marketplace-deployment_StartDeploymentConfigurationJob_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_StartDeploymentConfigurationJob-request-configuration"></a>
The deployment configuration to publish.
Type: [DeploymentConfigurationDetail](API_marketplace-deployment_DeploymentConfigurationDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [clientToken](#API_marketplace-deployment_StartDeploymentConfigurationJob_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_StartDeploymentConfigurationJob-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you retry a request with the same token and the same input, the service returns the original job instead of starting a new one. If you reuse a token with different input, the request fails with a `ConflictException`.
This field is not required if you're calling using an AWS SDK. Otherwise, a `clientToken` must be provided with the request.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.
Pattern: `[a-zA-Z0-9/_+=.:@-]+`
Required: No

 ** [tags](#API_marketplace-deployment_StartDeploymentConfigurationJob_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_StartDeploymentConfigurationJob-request-tags"></a>
A map of key-value pairs, where each pair represents a tag to apply to the deployment configuration. Only the request that creates the deployment configuration can apply tags. If the deployment configuration already exists, a request that includes one or more tags fails with a `ValidationException`. To change tags on an existing deployment configuration, use `TagResource` and `UntagResource`.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## Response Syntax
<a name="API_marketplace-deployment_StartDeploymentConfigurationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuration": { ... },
   "createdAt": "string",
   "jobId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_marketplace-deployment_StartDeploymentConfigurationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuration](#API_marketplace-deployment_StartDeploymentConfigurationJob_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_StartDeploymentConfigurationJob-response-configuration"></a>
The deployment configuration submitted with the job.
Type: [DeploymentConfigurationDetail](API_marketplace-deployment_DeploymentConfigurationDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdAt](#API_marketplace-deployment_StartDeploymentConfigurationJob_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_StartDeploymentConfigurationJob-response-createdAt"></a>
The date and time when the job was created.
Type: Timestamp

 ** [jobId](#API_marketplace-deployment_StartDeploymentConfigurationJob_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_StartDeploymentConfigurationJob-response-jobId"></a>
The unique identifier of the deployment configuration job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [status](#API_marketplace-deployment_StartDeploymentConfigurationJob_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_StartDeploymentConfigurationJob-response-status"></a>
The status of the deployment configuration job. The value is `IN_PROGRESS`.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`

## Errors
<a name="API_marketplace-deployment_StartDeploymentConfigurationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
 ** resourceId **
The unique identifier for the resource associated with the error.
HTTP Status Code: 409

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
<a name="API_marketplace-deployment_StartDeploymentConfigurationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-deployment-2023-01-25/StartDeploymentConfigurationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-deployment-2023-01-25/StartDeploymentConfigurationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-deployment-2023-01-25/StartDeploymentConfigurationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-deployment-2023-01-25/StartDeploymentConfigurationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-deployment-2023-01-25/StartDeploymentConfigurationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-deployment-2023-01-25/StartDeploymentConfigurationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-deployment-2023-01-25/StartDeploymentConfigurationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-deployment-2023-01-25/StartDeploymentConfigurationJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-deployment-2023-01-25/StartDeploymentConfigurationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-deployment-2023-01-25/StartDeploymentConfigurationJob)
