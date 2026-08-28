---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateServiceNetworkResourceAssociation.html
---

# CreateServiceNetworkResourceAssociation
<a name="API_CreateServiceNetworkResourceAssociation"></a>

Associates the specified service network with the specified resource configuration. This allows the resource configuration to receive connections through the service network, including through a service network VPC endpoint.

## Request Syntax
<a name="API_CreateServiceNetworkResourceAssociation_RequestSyntax"></a>

```
POST /servicenetworkresourceassociations HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "privateDnsEnabled": {{boolean}},
   "resourceConfigurationIdentifier": "{{string}}",
   "serviceNetworkIdentifier": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateServiceNetworkResourceAssociation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateServiceNetworkResourceAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateServiceNetworkResourceAssociation_RequestSyntax) **   <a name="vpclattice-CreateServiceNetworkResourceAssociation-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[!-~]+.*`
Required: No

 ** [privateDnsEnabled](#API_CreateServiceNetworkResourceAssociation_RequestSyntax) **   <a name="vpclattice-CreateServiceNetworkResourceAssociation-request-privateDnsEnabled"></a>
 Indicates if private DNS is enabled for the service network resource association.
Type: Boolean
Required: No

 ** [resourceConfigurationIdentifier](#API_CreateServiceNetworkResourceAssociation_RequestSyntax) **   <a name="vpclattice-CreateServiceNetworkResourceAssociation-request-resourceConfigurationIdentifier"></a>
The ID of the resource configuration to associate with the service network.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
Required: Yes

 ** [serviceNetworkIdentifier](#API_CreateServiceNetworkResourceAssociation_RequestSyntax) **   <a name="vpclattice-CreateServiceNetworkResourceAssociation-request-serviceNetworkIdentifier"></a>
The ID of the service network to associate with the resource configuration.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 2048.
Required: Yes

 ** [tags](#API_CreateServiceNetworkResourceAssociation_RequestSyntax) **   <a name="vpclattice-CreateServiceNetworkResourceAssociation-request-tags"></a>
A key-value pair to associate with a resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateServiceNetworkResourceAssociation_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "createdBy": "string",
   "id": "string",
   "privateDnsEnabled": boolean,
   "status": "string"
}
```

## Response Elements
<a name="API_CreateServiceNetworkResourceAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkResourceAssociation-response-arn"></a>
The Amazon Resource Name (ARN) of the association.
Type: String
Length Constraints: Minimum length of 22. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkresourceassociation/snra-[0-9a-f]{17}`

 ** [createdBy](#API_CreateServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkResourceAssociation-response-createdBy"></a>
The ID of the account that created the association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[0-9]{12}`

 ** [id](#API_CreateServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkResourceAssociation-response-id"></a>
The ID of the association.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `snra-[0-9a-f]{17}`

 ** [privateDnsEnabled](#API_CreateServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkResourceAssociation-response-privateDnsEnabled"></a>
 Indicates if private DNS is is enabled for the service network resource association.
Type: Boolean

 ** [status](#API_CreateServiceNetworkResourceAssociation_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetworkResourceAssociation-response-status"></a>
The status of the association.
Type: String
Valid Values: `CREATE_IN_PROGRESS | ACTIVE | PARTIAL | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED`

## Errors
<a name="API_CreateServiceNetworkResourceAssociation_Errors"></a>

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
<a name="API_CreateServiceNetworkResourceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/CreateServiceNetworkResourceAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/CreateServiceNetworkResourceAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/CreateServiceNetworkResourceAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/CreateServiceNetworkResourceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/CreateServiceNetworkResourceAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/CreateServiceNetworkResourceAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/CreateServiceNetworkResourceAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/CreateServiceNetworkResourceAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/CreateServiceNetworkResourceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/CreateServiceNetworkResourceAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
