---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetResourceGateway.html
---

# GetResourceGateway
<a name="API_GetResourceGateway"></a>

Retrieves information about the specified resource gateway.

## Request Syntax
<a name="API_GetResourceGateway_RequestSyntax"></a>

```
GET /resourcegateways/{{resourceGatewayIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetResourceGateway_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceGatewayIdentifier](#API_GetResourceGateway_RequestSyntax) **   <a name="vpclattice-GetResourceGateway-request-uri-resourceGatewayIdentifier"></a>
The ID of the resource gateway.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((rgw-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourcegateway/rgw-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_GetResourceGateway_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetResourceGateway_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdAt": "string",
   "id": "string",
   "ipAddressType": "string",
   "ipv4AddressesPerEni": number,
   "lastUpdatedAt": "string",
   "managedBy": "string",
   "name": "string",
   "resourceConfigDnsResolution": "string",
   "securityGroupIds": [ "string" ],
   "serviceManaged": boolean,
   "status": "string",
   "subnetIds": [ "string" ],
   "vpcId": "string"
}
```

## Response Elements
<a name="API_GetResourceGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetResourceGateway_ResponseSyntax) **   <a name="vpclattice-GetResourceGateway-response-arn"></a>
The Amazon Resource Name (ARN) of the resource gateway.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourcegateway/rgw-[0-9a-z]{17}`

 ** [createdAt](#API_GetResourceGateway_ResponseSyntax) **   <a name="vpclattice-GetResourceGateway-response-createdAt"></a>
The date and time that the resource gateway was created, in ISO-8601 format.
Type: Timestamp

 ** [id](#API_GetResourceGateway_ResponseSyntax) **   <a name="vpclattice-GetResourceGateway-response-id"></a>
The ID of the resource gateway.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rgw-[0-9a-z]{17}`

 ** [ipAddressType](#API_GetResourceGateway_ResponseSyntax) **   <a name="vpclattice-GetResourceGateway-response-ipAddressType"></a>
The type of IP address for the resource gateway.
Type: String
Valid Values: `IPV4 | IPV6 | DUALSTACK`

 ** [ipv4AddressesPerEni](#API_GetResourceGateway_ResponseSyntax) **   <a name="vpclattice-GetResourceGateway-response-ipv4AddressesPerEni"></a>
The number of IPv4 addresses in each ENI for the resource gateway.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 62.

 ** [lastUpdatedAt](#API_GetResourceGateway_ResponseSyntax) **   <a name="vpclattice-GetResourceGateway-response-lastUpdatedAt"></a>
The date and time that the resource gateway was last updated, in ISO-8601 format.
Type: Timestamp

 ** [managedBy](#API_GetResourceGateway_ResponseSyntax) **   <a name="vpclattice-GetResourceGateway-response-managedBy"></a>
The AWS service that manages the resource gateway.
Type: String

 ** [name](#API_GetResourceGateway_ResponseSyntax) **   <a name="vpclattice-GetResourceGateway-response-name"></a>
The name of the resource gateway.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!rgw-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [resourceConfigDnsResolution](#API_GetResourceGateway_ResponseSyntax) **   <a name="vpclattice-GetResourceGateway-response-resourceConfigDnsResolution"></a>
The DNS resolution type for resource configurations that are associated with this resource gateway.
Type: String
Valid Values: `IN_VPC | PUBLIC`

 ** [securityGroupIds](#API_GetResourceGateway_ResponseSyntax) **   <a name="vpclattice-GetResourceGateway-response-securityGroupIds"></a>
The security group IDs associated with the resource gateway.
Type: Array of strings
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`

 ** [serviceManaged](#API_GetResourceGateway_ResponseSyntax) **   <a name="vpclattice-GetResourceGateway-response-serviceManaged"></a>
Indicates whether the resource gateway is managed by an AWS service.
Type: Boolean

 ** [status](#API_GetResourceGateway_ResponseSyntax) **   <a name="vpclattice-GetResourceGateway-response-status"></a>
The status for the resource gateway.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`

 ** [subnetIds](#API_GetResourceGateway_ResponseSyntax) **   <a name="vpclattice-GetResourceGateway-response-subnetIds"></a>
The IDs of the VPC subnets for resource gateway.
Type: Array of strings
Length Constraints: Minimum length of 5. Maximum length of 200.

 ** [vpcId](#API_GetResourceGateway_ResponseSyntax) **   <a name="vpclattice-GetResourceGateway-response-vpcId"></a>
The ID of the VPC for the resource gateway.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 50.
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`

## Errors
<a name="API_GetResourceGateway_Errors"></a>

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
<a name="API_GetResourceGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/GetResourceGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/GetResourceGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/GetResourceGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/GetResourceGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/GetResourceGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/GetResourceGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/GetResourceGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/GetResourceGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/GetResourceGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/GetResourceGateway)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
