---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_PutDeploymentParameter.html
---

# PutDeploymentParameter
<a name="API_marketplace-deployment_PutDeploymentParameter"></a>

Creates or updates a deployment parameter and is targeted by `catalog` and `agreementId`.

## Request Syntax
<a name="API_marketplace-deployment_PutDeploymentParameter_RequestSyntax"></a>

```
POST /catalogs/{{catalog}}/products/{{productId}}/deployment-parameters HTTP/1.1
Content-type: application/json

{
   "agreementId": "{{string}}",
   "clientToken": "{{string}}",
   "deploymentParameter": {
      "name": "{{string}}",
      "secretString": "{{string}}"
   },
   "expirationDate": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_marketplace-deployment_PutDeploymentParameter_RequestParameters"></a>

The request uses the following URI parameters.

 ** [catalog](#API_marketplace-deployment_PutDeploymentParameter_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_PutDeploymentParameter-request-uri-catalog"></a>
The catalog related to the request. Fixed value: `AWSMarketplace`
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z_-]+`
Required: Yes

 ** [productId](#API_marketplace-deployment_PutDeploymentParameter_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_PutDeploymentParameter-request-uri-productId"></a>
The product for which AWS Marketplace will save secrets for the buyer’s account.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

## Request Body
<a name="API_marketplace-deployment_PutDeploymentParameter_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agreementId](#API_marketplace-deployment_PutDeploymentParameter_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_PutDeploymentParameter-request-agreementId"></a>
The unique identifier of the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

 ** [deploymentParameter](#API_marketplace-deployment_PutDeploymentParameter_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_PutDeploymentParameter-request-deploymentParameter"></a>
The deployment parameter targeted to the acceptor of an agreement for which to create the AWS Secret Manager resource.
Type: [DeploymentParameterInput](API_marketplace-deployment_DeploymentParameterInput.md) object
Required: Yes

 ** [clientToken](#API_marketplace-deployment_PutDeploymentParameter_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_PutDeploymentParameter-request-clientToken"></a>
The idempotency token for deployment parameters. A unique identifier for the new version.
This field is not required if you're calling using an AWS SDK. Otherwise, a `clientToken` must be provided with the request.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.
Pattern: `[a-zA-Z0-9/_+=.:@-]+`
Required: No

 ** [expirationDate](#API_marketplace-deployment_PutDeploymentParameter_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_PutDeploymentParameter-request-expirationDate"></a>
The date when deployment parameters expire and are scheduled for deletion.
Type: Timestamp
Required: No

 ** [tags](#API_marketplace-deployment_PutDeploymentParameter_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_PutDeploymentParameter-request-tags"></a>
A map of key-value pairs, where each pair represents a tag saved to the resource. Tags will only be applied for create operations, and they'll be ignored if the resource already exists.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9/_+=.:@-]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9/_+=.:@-]+`
Required: No

## Response Syntax
<a name="API_marketplace-deployment_PutDeploymentParameter_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agreementId": "string",
   "deploymentParameterId": "string",
   "resourceArn": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_marketplace-deployment_PutDeploymentParameter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agreementId](#API_marketplace-deployment_PutDeploymentParameter_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_PutDeploymentParameter-response-agreementId"></a>
The unique identifier of the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`

 ** [deploymentParameterId](#API_marketplace-deployment_PutDeploymentParameter_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_PutDeploymentParameter-response-deploymentParameterId"></a>
The unique identifier of the deployment parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `dp-[a-zA-Z0-9]+`

 ** [resourceArn](#API_marketplace-deployment_PutDeploymentParameter_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_PutDeploymentParameter-response-resourceArn"></a>
The Amazon Resource Name (ARN) associated with the deployment parameter resource you want to create or update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:*/-]+`

 ** [tags](#API_marketplace-deployment_PutDeploymentParameter_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_PutDeploymentParameter-response-tags"></a>
A map of key-value pairs, where each pair represents a tag saved to the resource. Tags will only be applied for create operations, and they'll be ignored if the resource already exists.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9/_+=.:@-]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9/_+=.:@-]+`

## Errors
<a name="API_marketplace-deployment_PutDeploymentParameter_Errors"></a>

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

 ** ServiceQuotaExceededException **
The maximum number of requests per account has been exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
Too many requests.
HTTP Status Code: 429

 ** ValidationException **
An error occurred during validation.
 ** fieldName **
The field name associated with the error.
HTTP Status Code: 400

## See Also
<a name="API_marketplace-deployment_PutDeploymentParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-deployment-2023-01-25/PutDeploymentParameter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-deployment-2023-01-25/PutDeploymentParameter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-deployment-2023-01-25/PutDeploymentParameter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-deployment-2023-01-25/PutDeploymentParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-deployment-2023-01-25/PutDeploymentParameter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-deployment-2023-01-25/PutDeploymentParameter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-deployment-2023-01-25/PutDeploymentParameter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-deployment-2023-01-25/PutDeploymentParameter)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-deployment-2023-01-25/PutDeploymentParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-deployment-2023-01-25/PutDeploymentParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
