---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateResourceConfiguration.html
---

# CreateResourceConfiguration
<a name="API_CreateResourceConfiguration"></a>

Creates a resource configuration. A resource configuration defines a specific resource. You can associate a resource configuration with a service network or a VPC endpoint.

## Request Syntax
<a name="API_CreateResourceConfiguration_RequestSyntax"></a>

```
POST /resourceconfigurations HTTP/1.1
Content-type: application/json

{
   "allowAssociationToShareableServiceNetwork": {{boolean}},
   "clientToken": "{{string}}",
   "customDomainName": "{{string}}",
   "domainVerificationIdentifier": "{{string}}",
   "groupDomain": "{{string}}",
   "name": "{{string}}",
   "portRanges": [ "{{string}}" ],
   "protocol": "{{string}}",
   "resourceConfigurationDefinition": { ... },
   "resourceConfigurationGroupIdentifier": "{{string}}",
   "resourceGatewayIdentifier": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateResourceConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateResourceConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [allowAssociationToShareableServiceNetwork](#API_CreateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-CreateResourceConfiguration-request-allowAssociationToShareableServiceNetwork"></a>
(SINGLE, GROUP, ARN) Specifies whether the resource configuration can be associated with a sharable service network. The default is false.
Type: Boolean
Required: No

 ** [clientToken](#API_CreateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-CreateResourceConfiguration-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[!-~]+.*`
Required: No

 ** [customDomainName](#API_CreateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-CreateResourceConfiguration-request-customDomainName"></a>
 A custom domain name for your resource configuration. Additionally, provide a DomainVerificationID to prove your ownership of a domain.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: No

 ** [domainVerificationIdentifier](#API_CreateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-CreateResourceConfiguration-request-domainVerificationIdentifier"></a>
 The domain verification ID of your verified custom domain name. If you don't provide an ID, you must configure the DNS settings yourself.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((dv-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:domainverification/dv-[a-fA-F0-9]{17}))`
Required: No

 ** [groupDomain](#API_CreateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-CreateResourceConfiguration-request-groupDomain"></a>
 (GROUP) The group domain for a group resource configuration. Any domains that you create for the child resource are subdomains of the group domain. Child resources inherit the verification status of the domain.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: No

 ** [name](#API_CreateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-CreateResourceConfiguration-request-name"></a>
The name of the resource configuration. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!rcfg-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: Yes

 ** [portRanges](#API_CreateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-CreateResourceConfiguration-request-portRanges"></a>
(SINGLE, GROUP, CHILD) The TCP port ranges that a consumer can use to access a resource configuration (for example: 1-65535). You can separate port ranges using commas (for example: 1,2,22-30).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `((\d{1,5}\-\d{1,5})|(\d+))`
Required: No

 ** [protocol](#API_CreateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-CreateResourceConfiguration-request-protocol"></a>
(SINGLE, GROUP) The protocol accepted by the resource configuration.
Type: String
Valid Values: `TCP | TCP_UDP`
Required: No

 ** [resourceConfigurationDefinition](#API_CreateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-CreateResourceConfiguration-request-resourceConfigurationDefinition"></a>
Identifies the resource configuration in one of the following ways:
+  **Amazon Resource Name (ARN)** - Supported resource-types that are provisioned by AWS services, such as RDS databases, can be identified by their ARN.
+  **Domain name** - Any domain name that is publicly resolvable.
+  **IP address** - For IPv4 and IPv6, only IP addresses in the VPC are supported.
Type: [ResourceConfigurationDefinition](API_ResourceConfigurationDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [resourceConfigurationGroupIdentifier](#API_CreateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-CreateResourceConfiguration-request-resourceConfigurationGroupIdentifier"></a>
(CHILD) The ID or ARN of the parent resource configuration of type `GROUP`. This is used to associate a child resource configuration with a group resource configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
Required: No

 ** [resourceGatewayIdentifier](#API_CreateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-CreateResourceConfiguration-request-resourceGatewayIdentifier"></a>
(SINGLE, GROUP, ARN) The ID or ARN of the resource gateway used to connect to the resource configuration. For a child resource configuration, this value is inherited from the parent resource configuration.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((rgw-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourcegateway/rgw-[0-9a-z]{17}))`
Required: No

 ** [tags](#API_CreateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-CreateResourceConfiguration-request-tags"></a>
The tags for the resource configuration.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [type](#API_CreateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-CreateResourceConfiguration-request-type"></a>
The type of resource configuration. A resource configuration can be one of the following types:
+  **SINGLE** - A single resource.
+  **GROUP** - A group of resources. You must create a group resource configuration before you create a child resource configuration.
+  **CHILD** - A single resource that is part of a group resource configuration.
+  **ARN** - An AWS resource.
Type: String
Valid Values: `GROUP | CHILD | SINGLE | ARN`
Required: Yes

## Response Syntax
<a name="API_CreateResourceConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "allowAssociationToShareableServiceNetwork": boolean,
   "arn": "string",
   "createdAt": "string",
   "customDomainName": "string",
   "domainVerificationArn": "string",
   "domainVerificationId": "string",
   "failureReason": "string",
   "groupDomain": "string",
   "id": "string",
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
<a name="API_CreateResourceConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [allowAssociationToShareableServiceNetwork](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-allowAssociationToShareableServiceNetwork"></a>
Specifies whether the resource configuration can be associated with a sharable service network.
Type: Boolean

 ** [arn](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-arn"></a>
The Amazon Resource Name (ARN) of the resource configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9f\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}`

 ** [createdAt](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-createdAt"></a>
The date and time that the resource configuration was created, in ISO-8601 format.
Type: Timestamp

 ** [customDomainName](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-customDomainName"></a>
 The custom domain name for your resource configuration.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.

 ** [domainVerificationArn](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-domainVerificationArn"></a>
 The verification ID ARN
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9f\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:domainverification/dv-[a-fA-F0-9]{17}`

 ** [domainVerificationId](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-domainVerificationId"></a>
 The domain name verification ID.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `dv-[a-fA-F0-9]{17}`

 ** [failureReason](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-failureReason"></a>
The reason that the request failed.
Type: String

 ** [groupDomain](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-groupDomain"></a>
 (GROUP) The group domain for a group resource configuration. Any domains that you create for the child resource are subdomains of the group domain. Child resources inherit the verification status of the domain.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.

 ** [id](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-id"></a>
The ID of the resource configuration.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `rcfg-[0-9a-z]{17}`

 ** [name](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-name"></a>
The name of the resource configuration.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!rcfg-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [portRanges](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-portRanges"></a>
The port range.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `((\d{1,5}\-\d{1,5})|(\d+))`

 ** [protocol](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-protocol"></a>
The protocol.
Type: String
Valid Values: `TCP | TCP_UDP`

 ** [resourceConfigurationDefinition](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-resourceConfigurationDefinition"></a>
Identifies the resource configuration in one of the following ways:
+  **Amazon Resource Name (ARN)** - Supported resource-types that are provisioned by AWS services, such as RDS databases, can be identified by their ARN.
+  **Domain name** - Any domain name that is publicly resolvable.
+  **IP address** - For IPv4 and IPv6, only IP addresses in the VPC are supported.
Type: [ResourceConfigurationDefinition](API_ResourceConfigurationDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [resourceConfigurationGroupId](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-resourceConfigurationGroupId"></a>
The ID of the parent resource configuration of type `GROUP`.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `rcfg-[0-9a-z]{17}`

 ** [resourceGatewayId](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-resourceGatewayId"></a>
The ID of the resource gateway associated with the resource configuration.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rgw-[0-9a-z]{17}`

 ** [status](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-status"></a>
The current status of the resource configuration.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`

 ** [type](#API_CreateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-CreateResourceConfiguration-response-type"></a>
The type of resource configuration. A resource configuration can be one of the following types:
+  **SINGLE** - A single resource.
+  **GROUP** - A group of resources. You must create a group resource configuration before you create a child resource configuration.
+  **CHILD** - A single resource that is part of a group resource configuration.
+  **ARN** - An AWS resource.
Type: String
Valid Values: `GROUP | CHILD | SINGLE | ARN`

## Errors
<a name="API_CreateResourceConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
 ** serviceCode **
The service code.
HTTP Status Code: 402

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
<a name="API_CreateResourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/CreateResourceConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/CreateResourceConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/CreateResourceConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/CreateResourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/CreateResourceConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/CreateResourceConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/CreateResourceConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/CreateResourceConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/CreateResourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/CreateResourceConfiguration)
