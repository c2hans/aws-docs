---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetResourceConfiguration.html
---

# GetResourceConfiguration
<a name="API_GetResourceConfiguration"></a>

Retrieves information about the specified resource configuration.

## Request Syntax
<a name="API_GetResourceConfiguration_RequestSyntax"></a>

```
GET /resourceconfigurations/{{resourceConfigurationIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetResourceConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceConfigurationIdentifier](#API_GetResourceConfiguration_RequestSyntax) **   <a name="vpclattice-GetResourceConfiguration-request-uri-resourceConfigurationIdentifier"></a>
The ID of the resource configuration.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_GetResourceConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetResourceConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "allowAssociationToShareableServiceNetwork": boolean,
   "amazonManaged": boolean,
   "arn": "string",
   "createdAt": "string",
   "customDomainName": "string",
   "domainVerificationArn": "string",
   "domainVerificationId": "string",
   "domainVerificationStatus": "string",
   "failureReason": "string",
   "groupDomain": "string",
   "id": "string",
   "lastUpdatedAt": "string",
   "name": "string",
   "portRanges": [ "string" ],
   "protocol": "string",
   "resourceConfigurationDefinition": { ... },
   "resourceConfigurationGroupId": "string",
   "resourceGatewayId": "string",
   "status": "string",
   "type": "string"
}
```

## Response Elements
<a name="API_GetResourceConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [allowAssociationToShareableServiceNetwork](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-allowAssociationToShareableServiceNetwork"></a>
Specifies whether the resource configuration is associated with a sharable service network.
Type: Boolean

 ** [amazonManaged](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-amazonManaged"></a>
Indicates whether the resource configuration was created and is managed by Amazon.
Type: Boolean

 ** [arn](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-arn"></a>
The Amazon Resource Name (ARN) of the resource configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9f\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}`

 ** [createdAt](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-createdAt"></a>
The date and time that the resource configuration was created, in ISO-8601 format.
Type: Timestamp

 ** [customDomainName](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-customDomainName"></a>
The custom domain name of the resource configuration.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.

 ** [domainVerificationArn](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-domainVerificationArn"></a>
 The ARN of the domain verification.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9f\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:domainverification/dv-[a-fA-F0-9]{17}`

 ** [domainVerificationId](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-domainVerificationId"></a>
 The domain verification ID.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `dv-[a-fA-F0-9]{17}`

 ** [domainVerificationStatus](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-domainVerificationStatus"></a>
 The domain verification status.
Type: String
Valid Values: `VERIFIED | PENDING | VERIFICATION_TIMED_OUT`

 ** [failureReason](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-failureReason"></a>
The reason the create-resource-configuration request failed.
Type: String

 ** [groupDomain](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-groupDomain"></a>
 (GROUP) The group domain for a group resource configuration. Any domains that you create for the child resource are subdomains of the group domain. Child resources inherit the verification status of the domain.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.

 ** [id](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-id"></a>
The ID of the resource configuration.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `rcfg-[0-9a-z]{17}`

 ** [lastUpdatedAt](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-lastUpdatedAt"></a>
The most recent date and time that the resource configuration was updated, in ISO-8601 format.
Type: Timestamp

 ** [name](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-name"></a>
The name of the resource configuration.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!rcfg-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [portRanges](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-portRanges"></a>
The TCP port ranges that a consumer can use to access a resource configuration. You can separate port ranges with a comma. Example: 1-65535 or 1,2,22-30
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `((\d{1,5}\-\d{1,5})|(\d+))`

 ** [protocol](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-protocol"></a>
The TCP protocol accepted by the specified resource configuration.
Type: String
Valid Values: `TCP | TCP_UDP`

 ** [resourceConfigurationDefinition](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-resourceConfigurationDefinition"></a>
The resource configuration.
Type: [ResourceConfigurationDefinition](API_ResourceConfigurationDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [resourceConfigurationGroupId](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-resourceConfigurationGroupId"></a>
The ID of the group resource configuration.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `rcfg-[0-9a-z]{17}`

 ** [resourceGatewayId](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-resourceGatewayId"></a>
The ID of the resource gateway used to connect to the resource configuration in a given VPC. You can specify the resource gateway identifier only for resource configurations with type SINGLE, GROUP, or ARN.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rgw-[0-9a-z]{17}`

 ** [status](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-status"></a>
The status of the resource configuration.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`

 ** [type](#API_GetResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-GetResourceConfiguration-response-type"></a>
The type of resource configuration.
+  `SINGLE` - A single resource.
+  `GROUP` - A group of resources.
+  `CHILD` - A single resource that is part of a group resource configuration.
+  `ARN` - An AWS resource.
Type: String
Valid Values: `GROUP | CHILD | SINGLE | ARN`

## Errors
<a name="API_GetResourceConfiguration_Errors"></a>

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
<a name="API_GetResourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/GetResourceConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/GetResourceConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/GetResourceConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/GetResourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/GetResourceConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/GetResourceConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/GetResourceConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/GetResourceConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/GetResourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/GetResourceConfiguration)
