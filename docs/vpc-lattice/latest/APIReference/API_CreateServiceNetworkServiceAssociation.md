---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateServiceNetworkServiceAssociation.html
---

# CreateServiceNetworkServiceAssociation
<a name="API_CreateServiceNetworkServiceAssociation"></a>

Associates the specified service with the specified service network. For more information, see [Manage service associations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-service-associations) in the *Amazon VPC Lattice User Guide*.

You can't use this operation if the service and service network are already associated or if there is a disassociation or deletion in progress. If the association fails, you can retry the operation by deleting the association and recreating it.

You cannot associate a service and service network that are shared with a caller. The caller must own either the service or the service network.

As a result of this operation, the association is created in the service network account and the association owner account.

## Request Syntax
<a name="API_CreateServiceNetworkServiceAssociation_RequestSyntax"></a>

```
POST /servicenetworkserviceassociations HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "serviceIdentifier": "{{string}}",
   "serviceNetworkIdentifier": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateServiceNetworkServiceAssociation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateServiceNetworkServiceAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateServiceNetworkServiceAssociation_RequestSyntax) **   <a name="vpclattice-CreateServiceNetworkServiceAssociation-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[!-~]+.*`
Required: No

 ** [serviceIdentifier](#API_CreateServiceNetworkServiceAssociation_RequestSyntax) **   <a name="vpclattice-CreateServiceNetworkServiceAssociation-request-serviceIdentifier"></a>
The ID or ARN of the service.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((svc-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}))`
Required: Yes

 ** [serviceNetworkIdentifier](#API_CreateServiceNetworkServiceAssociation_RequestSyntax) **   <a name="vpclattice-CreateServiceNetworkServiceAssociation-request-serviceNetworkIdentifier"></a>
The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 2048.
Pattern: `((sn-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetwork/sn-[0-9a-z]{17}))`
Required: Yes

 ** [tags](#API_CreateServiceNetworkServiceAssociation_RequestSyntax) **   <a name="vpclattice-CreateServiceNetworkServiceAssociation-request-tags"></a>
The tags for the association.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateServiceNetworkServiceAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdBy": "string",
   "customDomainName": "string",
   "dnsEntry": {
      "domainName": "string",
      "hostedZoneId": "string"
   },
   "id": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateServiceNetworkServiceAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkServiceAssociation-response-arn"></a>
The Amazon Resource Name (ARN) of the association.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkserviceassociation/snsa-[0-9a-z]{17}`

 ** [createdBy](#API_CreateServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkServiceAssociation-response-createdBy"></a>
The account that created the association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[0-9]{12}`

 ** [customDomainName](#API_CreateServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkServiceAssociation-response-customDomainName"></a>
The custom domain name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.

 ** [dnsEntry](#API_CreateServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkServiceAssociation-response-dnsEntry"></a>
The DNS name of the service.
Type: [DnsEntry](API_DnsEntry.md) object

 ** [id](#API_CreateServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkServiceAssociation-response-id"></a>
The ID of the association.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((snsa-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkserviceassociation/snsa-[0-9a-z]{17}))`

 ** [status](#API_CreateServiceNetworkServiceAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkServiceAssociation-response-status"></a>
The association status.
Type: String
Valid Values: `CREATE_IN_PROGRESS | ACTIVE | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED`

## Errors
<a name="API_CreateServiceNetworkServiceAssociation_Errors"></a>

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
<a name="API_CreateServiceNetworkServiceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/CreateServiceNetworkServiceAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/CreateServiceNetworkServiceAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/CreateServiceNetworkServiceAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/CreateServiceNetworkServiceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/CreateServiceNetworkServiceAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/CreateServiceNetworkServiceAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/CreateServiceNetworkServiceAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/CreateServiceNetworkServiceAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/CreateServiceNetworkServiceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/CreateServiceNetworkServiceAssociation)
