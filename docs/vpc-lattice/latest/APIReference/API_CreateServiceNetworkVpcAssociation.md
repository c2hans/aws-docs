---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateServiceNetworkVpcAssociation.html
---

# CreateServiceNetworkVpcAssociation
<a name="API_CreateServiceNetworkVpcAssociation"></a>

Associates a VPC with a service network. When you associate a VPC with the service network, it enables all the resources within that VPC to be clients and communicate with other services in the service network. For more information, see [Manage VPC associations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-vpc-associations) in the *Amazon VPC Lattice User Guide*.

You can't use this operation if there is a disassociation in progress. If the association fails, retry by deleting the association and recreating it.

As a result of this operation, the association gets created in the service network account and the VPC owner account.

If you add a security group to the service network and VPC association, the association must continue to always have at least one security group. You can add or edit security groups at any time. However, to remove all security groups, you must first delete the association and recreate it without security groups.

## Request Syntax
<a name="API_CreateServiceNetworkVpcAssociation_RequestSyntax"></a>

```
POST /servicenetworkvpcassociations HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "dnsOptions": {
      "privateDnsPreference": "{{string}}",
      "privateDnsSpecifiedDomains": [ "{{string}}" ]
   },
   "privateDnsEnabled": {{boolean}},
   "securityGroupIds": [ "{{string}}" ],
   "serviceNetworkIdentifier": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "vpcIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateServiceNetworkVpcAssociation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateServiceNetworkVpcAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateServiceNetworkVpcAssociation_RequestSyntax) **   <a name="vpclattice-CreateServiceNetworkVpcAssociation-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[!-~]+.*`
Required: No

 ** [dnsOptions](#API_CreateServiceNetworkVpcAssociation_RequestSyntax) **   <a name="vpclattice-CreateServiceNetworkVpcAssociation-request-dnsOptions"></a>
 DNS options for the service network VPC association.
Type: [DnsOptions](API_DnsOptions.md) object
Required: No

 ** [privateDnsEnabled](#API_CreateServiceNetworkVpcAssociation_RequestSyntax) **   <a name="vpclattice-CreateServiceNetworkVpcAssociation-request-privateDnsEnabled"></a>
 Indicates if private DNS is enabled for the VPC association.
Type: Boolean
Required: No

 ** [securityGroupIds](#API_CreateServiceNetworkVpcAssociation_RequestSyntax) **   <a name="vpclattice-CreateServiceNetworkVpcAssociation-request-securityGroupIds"></a>
The IDs of the security groups. Security groups aren't added by default. You can add a security group to apply network level controls to control which resources in a VPC are allowed to access the service network and its services. For more information, see [Control traffic to resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) in the *Amazon VPC User Guide*.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
Required: No

 ** [serviceNetworkIdentifier](#API_CreateServiceNetworkVpcAssociation_RequestSyntax) **   <a name="vpclattice-CreateServiceNetworkVpcAssociation-request-serviceNetworkIdentifier"></a>
The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 2048.
Pattern: `((sn-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetwork/sn-[0-9a-z]{17}))`
Required: Yes

 ** [tags](#API_CreateServiceNetworkVpcAssociation_RequestSyntax) **   <a name="vpclattice-CreateServiceNetworkVpcAssociation-request-tags"></a>
The tags for the association.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [vpcIdentifier](#API_CreateServiceNetworkVpcAssociation_RequestSyntax) **   <a name="vpclattice-CreateServiceNetworkVpcAssociation-request-vpcIdentifier"></a>
The ID of the VPC.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 50.
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
Required: Yes

## Response Syntax
<a name="API_CreateServiceNetworkVpcAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdBy": "string",
   "dnsOptions": {
      "privateDnsPreference": "string",
      "privateDnsSpecifiedDomains": [ "string" ]
   },
   "id": "string",
   "privateDnsEnabled": boolean,
   "securityGroupIds": [ "string" ],
   "status": "string"
}
```

## Response Elements
<a name="API_CreateServiceNetworkVpcAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkVpcAssociation-response-arn"></a>
The Amazon Resource Name (ARN) of the association.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkvpcassociation/snva-[0-9a-z]{17}`

 ** [createdBy](#API_CreateServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkVpcAssociation-response-createdBy"></a>
The account that created the association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[0-9]{12}`

 ** [dnsOptions](#API_CreateServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkVpcAssociation-response-dnsOptions"></a>
 The DNS configuration options.
Type: [DnsOptions](API_DnsOptions.md) object

 ** [id](#API_CreateServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkVpcAssociation-response-id"></a>
The ID of the association.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `snva-[0-9a-z]{17}`

 ** [privateDnsEnabled](#API_CreateServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkVpcAssociation-response-privateDnsEnabled"></a>
 Indicates if private DNS is enabled for the VPC association.
Type: Boolean

 ** [securityGroupIds](#API_CreateServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkVpcAssociation-response-securityGroupIds"></a>
The IDs of the security groups.
Type: Array of strings
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`

 ** [status](#API_CreateServiceNetworkVpcAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkVpcAssociation-response-status"></a>
The association status.
Type: String
Valid Values: `CREATE_IN_PROGRESS | ACTIVE | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED | UPDATE_FAILED`

## Errors
<a name="API_CreateServiceNetworkVpcAssociation_Errors"></a>

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
<a name="API_CreateServiceNetworkVpcAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/CreateServiceNetworkVpcAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/CreateServiceNetworkVpcAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/CreateServiceNetworkVpcAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/CreateServiceNetworkVpcAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/CreateServiceNetworkVpcAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/CreateServiceNetworkVpcAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/CreateServiceNetworkVpcAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/CreateServiceNetworkVpcAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/CreateServiceNetworkVpcAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/CreateServiceNetworkVpcAssociation)
