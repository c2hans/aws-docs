---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_UpdateResourceConfiguration.html
---

# UpdateResourceConfiguration
<a name="API_UpdateResourceConfiguration"></a>

Updates the specified resource configuration.

## Request Syntax
<a name="API_UpdateResourceConfiguration_RequestSyntax"></a>

```
PATCH /resourceconfigurations/{{resourceConfigurationIdentifier}} HTTP/1.1
Content-type: application/json

{
   "allowAssociationToShareableServiceNetwork": {{boolean}},
   "portRanges": [ "{{string}}" ],
   "resourceConfigurationDefinition": { ... }
}
```

## URI Request Parameters
<a name="API_UpdateResourceConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceConfigurationIdentifier](#API_UpdateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-UpdateResourceConfiguration-request-uri-resourceConfigurationIdentifier"></a>
The ID of the resource configuration.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_UpdateResourceConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [allowAssociationToShareableServiceNetwork](#API_UpdateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-UpdateResourceConfiguration-request-allowAssociationToShareableServiceNetwork"></a>
Indicates whether to add the resource configuration to service networks that are shared with other accounts.
Type: Boolean
Required: No

 ** [portRanges](#API_UpdateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-UpdateResourceConfiguration-request-portRanges"></a>
The TCP port ranges that a consumer can use to access a resource configuration. You can separate port ranges with a comma. Example: 1-65535 or 1,2,22-30
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `((\d{1,5}\-\d{1,5})|(\d+))`
Required: No

 ** [resourceConfigurationDefinition](#API_UpdateResourceConfiguration_RequestSyntax) **   <a name="vpclattice-UpdateResourceConfiguration-request-resourceConfigurationDefinition"></a>
Identifies the resource configuration in one of the following ways:
+  **Amazon Resource Name (ARN)** - Supported resource-types that are provisioned by AWS services, such as RDS databases, can be identified by their ARN.
+  **Domain name** - Any domain name that is publicly resolvable.
+  **IP address** - For IPv4 and IPv6, only IP addresses in the VPC are supported.
Type: [ResourceConfigurationDefinition](API_ResourceConfigurationDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_UpdateResourceConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "allowAssociationToShareableServiceNetwork": boolean,
   "arn": "string",
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
<a name="API_UpdateResourceConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [allowAssociationToShareableServiceNetwork](#API_UpdateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-UpdateResourceConfiguration-response-allowAssociationToShareableServiceNetwork"></a>
Indicates whether to add the resource configuration to service networks that are shared with other accounts.
Type: Boolean

 ** [arn](#API_UpdateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-UpdateResourceConfiguration-response-arn"></a>
The Amazon Resource Name (ARN) of the resource configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9f\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}`

 ** [id](#API_UpdateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-UpdateResourceConfiguration-response-id"></a>
The ID of the resource configuration.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `rcfg-[0-9a-z]{17}`

 ** [name](#API_UpdateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-UpdateResourceConfiguration-response-name"></a>
The name of the resource configuration.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!rcfg-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [portRanges](#API_UpdateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-UpdateResourceConfiguration-response-portRanges"></a>
The TCP port ranges that a consumer can use to access a resource configuration. You can separate port ranges with a comma. Example: 1-65535 or 1,2,22-30
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `((\d{1,5}\-\d{1,5})|(\d+))`

 ** [protocol](#API_UpdateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-UpdateResourceConfiguration-response-protocol"></a>
The TCP protocol accepted by the specified resource configuration.
Type: String
Valid Values: `TCP | TCP_UDP`

 ** [resourceConfigurationDefinition](#API_UpdateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-UpdateResourceConfiguration-response-resourceConfigurationDefinition"></a>
The resource configuration.
Type: [ResourceConfigurationDefinition](API_ResourceConfigurationDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [resourceConfigurationGroupId](#API_UpdateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-UpdateResourceConfiguration-response-resourceConfigurationGroupId"></a>
The ID of the group resource configuration.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `rcfg-[0-9a-z]{17}`

 ** [resourceGatewayId](#API_UpdateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-UpdateResourceConfiguration-response-resourceGatewayId"></a>
The ID of the resource gateway associated with the resource configuration.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rgw-[0-9a-z]{17}`

 ** [status](#API_UpdateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-UpdateResourceConfiguration-response-status"></a>
The status of the resource configuration.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`

 ** [type](#API_UpdateResourceConfiguration_ResponseSyntax) **   <a name="vpclattice-UpdateResourceConfiguration-response-type"></a>
The type of resource configuration.
+  `SINGLE` - A single resource.
+  `GROUP` - A group of resources.
+  `CHILD` - A single resource that is part of a group resource configuration.
+  `ARN` - An AWS resource.
Type: String
Valid Values: `GROUP | CHILD | SINGLE | ARN`

## Errors
<a name="API_UpdateResourceConfiguration_Errors"></a>

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
<a name="API_UpdateResourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/UpdateResourceConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/UpdateResourceConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/UpdateResourceConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/UpdateResourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/UpdateResourceConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/UpdateResourceConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/UpdateResourceConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/UpdateResourceConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/UpdateResourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/UpdateResourceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
