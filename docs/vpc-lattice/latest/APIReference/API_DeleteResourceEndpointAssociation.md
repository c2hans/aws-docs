---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteResourceEndpointAssociation.html
---

# DeleteResourceEndpointAssociation
<a name="API_DeleteResourceEndpointAssociation"></a>

Disassociates the resource configuration from the resource VPC endpoint.

## Request Syntax
<a name="API_DeleteResourceEndpointAssociation_RequestSyntax"></a>

```
DELETE /resourceendpointassociations/{{resourceEndpointAssociationIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteResourceEndpointAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceEndpointAssociationIdentifier](#API_DeleteResourceEndpointAssociation_RequestSyntax) **   <a name="vpclattice-DeleteResourceEndpointAssociation-request-uri-resourceEndpointAssociationIdentifier"></a>
The ID or ARN of the association.
Length Constraints: Minimum length of 21. Maximum length of 2048.
Pattern: `((rea-[0-9a-f]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceendpointassociation/rea-[0-9a-f]{17}))`
Required: Yes

## Request Body
<a name="API_DeleteResourceEndpointAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteResourceEndpointAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "resourceConfigurationArn": "string",
   "resourceConfigurationId": "string",
   "vpcEndpointId": "string"
}
```

## Response Elements
<a name="API_DeleteResourceEndpointAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_DeleteResourceEndpointAssociation_ResponseSyntax) **   <a name="vpclattice-DeleteResourceEndpointAssociation-response-arn"></a>
The Amazon Resource Name (ARN) of the association.
Type: String
Length Constraints: Minimum length of 21. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceendpointassociation/rea-[0-9a-f]{17}`

 ** [id](#API_DeleteResourceEndpointAssociation_ResponseSyntax) **   <a name="vpclattice-DeleteResourceEndpointAssociation-response-id"></a>
The ID of the association.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rea-[0-9a-f]{17}`

 ** [resourceConfigurationArn](#API_DeleteResourceEndpointAssociation_ResponseSyntax) **   <a name="vpclattice-DeleteResourceEndpointAssociation-response-resourceConfigurationArn"></a>
The Amazon Resource Name (ARN) of the resource configuration associated with the VPC endpoint of type resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9f\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}`

 ** [resourceConfigurationId](#API_DeleteResourceEndpointAssociation_ResponseSyntax) **   <a name="vpclattice-DeleteResourceEndpointAssociation-response-resourceConfigurationId"></a>
The ID of the resource configuration.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `rcfg-[0-9a-z]{17}`

 ** [vpcEndpointId](#API_DeleteResourceEndpointAssociation_ResponseSyntax) **   <a name="vpclattice-DeleteResourceEndpointAssociation-response-vpcEndpointId"></a>
The ID of the resource VPC endpoint that is associated with the resource configuration.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `vpce-[0-9a-f]{17}`

## Errors
<a name="API_DeleteResourceEndpointAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
 ** serviceCode **
The service code.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** fieldList **
The fields that failed validation.
 ** reason **
The reason.
HTTP Status Code: 400

## See Also
<a name="API_DeleteResourceEndpointAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/DeleteResourceEndpointAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/DeleteResourceEndpointAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/DeleteResourceEndpointAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/DeleteResourceEndpointAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/DeleteResourceEndpointAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/DeleteResourceEndpointAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/DeleteResourceEndpointAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/DeleteResourceEndpointAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/DeleteResourceEndpointAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/DeleteResourceEndpointAssociation)
