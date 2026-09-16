---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateResourceGateway.html
---

# CreateResourceGateway
<a name="API_CreateResourceGateway"></a>

A resource gateway is a point of ingress into the VPC where a resource resides. It spans multiple Availability Zones. For your resource to be accessible from all Availability Zones, you should create your resource gateways to span as many Availability Zones as possible. A VPC can have multiple resource gateways.

## Request Syntax
<a name="API_CreateResourceGateway_RequestSyntax"></a>

```
POST /resourcegateways HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "ipAddressType": "{{string}}",
   "ipv4AddressesPerEni": {{number}},
   "name": "{{string}}",
   "resourceConfigDnsResolution": "{{string}}",
   "securityGroupIds": [ "{{string}}" ],
   "subnetIds": [ "{{string}}" ],
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "vpcIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateResourceGateway_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateResourceGateway_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateResourceGateway_RequestSyntax) **   <a name="vpclattice-CreateResourceGateway-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[!-~]+.*`
Required: No

 ** [ipAddressType](#API_CreateResourceGateway_RequestSyntax) **   <a name="vpclattice-CreateResourceGateway-request-ipAddressType"></a>
A resource gateway can have IPv4, IPv6 or dualstack addresses. The IP address type of a resource gateway must be compatible with the subnets of the resource gateway and the IP address type of the resource, as described here:
+  **IPv4**Assign IPv4 addresses to your resource gateway network interfaces. This option is supported only if all selected subnets have IPv4 address ranges, and the resource also has an IPv4 address.
+  **IPv6**Assign IPv6 addresses to your resource gateway network interfaces. This option is supported only if all selected subnets are IPv6 only subnets, and the resource also has an IPv6 address.
+  **Dualstack**Assign both IPv4 and IPv6 addresses to your resource gateway network interfaces. This option is supported only if all selected subnets have both IPv4 and IPv6 address ranges, and the resource either has an IPv4 or IPv6 address.
The IP address type of the resource gateway is independent of the IP address type of the client or the VPC endpoint through which the resource is accessed.
Type: String
Valid Values: `IPV4 | IPV6 | DUALSTACK`
Required: No

 ** [ipv4AddressesPerEni](#API_CreateResourceGateway_RequestSyntax) **   <a name="vpclattice-CreateResourceGateway-request-ipv4AddressesPerEni"></a>
The number of IPv4 addresses in each ENI for the resource gateway.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 62.
Required: No

 ** [name](#API_CreateResourceGateway_RequestSyntax) **   <a name="vpclattice-CreateResourceGateway-request-name"></a>
The name of the resource gateway.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!rgw-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: Yes

 ** [resourceConfigDnsResolution](#API_CreateResourceGateway_RequestSyntax) **   <a name="vpclattice-CreateResourceGateway-request-resourceConfigDnsResolution"></a>
Indicates how DNS is resolved for resource configurations associated to this resource gateway. ResourceConfigDnsResolution is set at creation time and cannot be changed.
+  `IN_VPC` - DNS resolution occurs privately within the resource gateway's VPC. DNS queries for resources behind this resource gateway resolve using the DNS resolvers defined in the VPC's DHCP option sets. Use this when your resource domain names are hosted in private Route 53 hosted zones or on-premises DNS servers reachable from the VPC.
+  `PUBLIC` - DNS resolution occurs against public DNS resolvers. DNS queries for resources behind this resource gateway resolve using standard public DNS. Use this when your resource domain names are publicly resolvable.
Type: String
Valid Values: `IN_VPC | PUBLIC`
Required: No

 ** [securityGroupIds](#API_CreateResourceGateway_RequestSyntax) **   <a name="vpclattice-CreateResourceGateway-request-securityGroupIds"></a>
The IDs of the security groups to apply to the resource gateway. The security groups must be in the same VPC.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
Required: No

 ** [subnetIds](#API_CreateResourceGateway_RequestSyntax) **   <a name="vpclattice-CreateResourceGateway-request-subnetIds"></a>
The IDs of the VPC subnets in which to create the resource gateway.
Type: Array of strings
Length Constraints: Minimum length of 5. Maximum length of 200.
Required: No

 ** [tags](#API_CreateResourceGateway_RequestSyntax) **   <a name="vpclattice-CreateResourceGateway-request-tags"></a>
The tags for the resource gateway.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [vpcIdentifier](#API_CreateResourceGateway_RequestSyntax) **   <a name="vpclattice-CreateResourceGateway-request-vpcIdentifier"></a>
The ID of the VPC for the resource gateway.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 50.
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
Required: No

## Response Syntax
<a name="API_CreateResourceGateway_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "ipAddressType": "string",
   "ipv4AddressesPerEni": number,
   "name": "string",
   "resourceConfigDnsResolution": "string",
   "securityGroupIds": [ "string" ],
   "status": "string",
   "subnetIds": [ "string" ],
   "vpcIdentifier": "string"
}
```

## Response Elements
<a name="API_CreateResourceGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateResourceGateway_ResponseSyntax) **   <a name="vpclattice-CreateResourceGateway-response-arn"></a>
The Amazon Resource Name (ARN) of the resource gateway.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourcegateway/rgw-[0-9a-z]{17}`

 ** [id](#API_CreateResourceGateway_ResponseSyntax) **   <a name="vpclattice-CreateResourceGateway-response-id"></a>
The ID of the resource gateway.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rgw-[0-9a-z]{17}`

 ** [ipAddressType](#API_CreateResourceGateway_ResponseSyntax) **   <a name="vpclattice-CreateResourceGateway-response-ipAddressType"></a>
The type of IP address for the resource gateway.
Type: String
Valid Values: `IPV4 | IPV6 | DUALSTACK`

 ** [ipv4AddressesPerEni](#API_CreateResourceGateway_ResponseSyntax) **   <a name="vpclattice-CreateResourceGateway-response-ipv4AddressesPerEni"></a>
The number of IPv4 addresses in each ENI for the resource gateway.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 62.

 ** [name](#API_CreateResourceGateway_ResponseSyntax) **   <a name="vpclattice-CreateResourceGateway-response-name"></a>
The name of the resource gateway.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!rgw-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [resourceConfigDnsResolution](#API_CreateResourceGateway_ResponseSyntax) **   <a name="vpclattice-CreateResourceGateway-response-resourceConfigDnsResolution"></a>
The DNS resolution type for resource configurations that are associated with this resource gateway.
Type: String
Valid Values: `IN_VPC | PUBLIC`

 ** [securityGroupIds](#API_CreateResourceGateway_ResponseSyntax) **   <a name="vpclattice-CreateResourceGateway-response-securityGroupIds"></a>
The IDs of the security groups for the resource gateway.
Type: Array of strings
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`

 ** [status](#API_CreateResourceGateway_ResponseSyntax) **   <a name="vpclattice-CreateResourceGateway-response-status"></a>
The status of the resource gateway.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`

 ** [subnetIds](#API_CreateResourceGateway_ResponseSyntax) **   <a name="vpclattice-CreateResourceGateway-response-subnetIds"></a>
The IDs of the resource gateway subnets.
Type: Array of strings
Length Constraints: Minimum length of 5. Maximum length of 200.

 ** [vpcIdentifier](#API_CreateResourceGateway_ResponseSyntax) **   <a name="vpclattice-CreateResourceGateway-response-vpcIdentifier"></a>
The ID of the VPC.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 50.
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`

## Errors
<a name="API_CreateResourceGateway_Errors"></a>

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
<a name="API_CreateResourceGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/CreateResourceGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/CreateResourceGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/CreateResourceGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/CreateResourceGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/CreateResourceGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/CreateResourceGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/CreateResourceGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/CreateResourceGateway)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/CreateResourceGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/CreateResourceGateway)
