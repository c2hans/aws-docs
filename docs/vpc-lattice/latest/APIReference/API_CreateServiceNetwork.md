---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateServiceNetwork.html
---

# CreateServiceNetwork
<a name="API_CreateServiceNetwork"></a>

Creates a service network. A service network is a logical boundary for a collection of services. You can associate services and VPCs with a service network.

For more information, see [Service networks](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html) in the *Amazon VPC Lattice User Guide*.

## Request Syntax
<a name="API_CreateServiceNetwork_RequestSyntax"></a>

```
POST /servicenetworks HTTP/1.1
Content-type: application/json

{
   "authType": "{{string}}",
   "clientToken": "{{string}}",
   "name": "{{string}}",
   "sharingConfig": {
      "enabled": {{boolean}}
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateServiceNetwork_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateServiceNetwork_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authType](#API_CreateServiceNetwork_RequestSyntax) **   <a name="vpclattice-CreateServiceNetwork-request-authType"></a>
The type of IAM policy.
+  `NONE`: The resource does not use an IAM policy. This is the default.
+  `AWS_IAM`: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.
Type: String
Valid Values: `NONE | AWS_IAM`
Required: No

 ** [clientToken](#API_CreateServiceNetwork_RequestSyntax) **   <a name="vpclattice-CreateServiceNetwork-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[!-~]+.*`
Required: No

 ** [name](#API_CreateServiceNetwork_RequestSyntax) **   <a name="vpclattice-CreateServiceNetwork-request-name"></a>
The name of the service network. The name must be unique to the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: Yes

 ** [sharingConfig](#API_CreateServiceNetwork_RequestSyntax) **   <a name="vpclattice-CreateServiceNetwork-request-sharingConfig"></a>
Specify if the service network should be enabled for sharing.
Type: [SharingConfig](API_SharingConfig.md) object
Required: No

 ** [tags](#API_CreateServiceNetwork_RequestSyntax) **   <a name="vpclattice-CreateServiceNetwork-request-tags"></a>
The tags for the service network.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateServiceNetwork_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "authType": "string",
   "id": "string",
   "name": "string",
   "sharingConfig": {
      "enabled": boolean
   }
}
```

## Response Elements
<a name="API_CreateServiceNetwork_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateServiceNetwork_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetwork-response-arn"></a>
The Amazon Resource Name (ARN) of the service network.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetwork/sn-[0-9a-z]{17}`

 ** [authType](#API_CreateServiceNetwork_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetwork-response-authType"></a>
The type of IAM policy.
Type: String
Valid Values: `NONE | AWS_IAM`

 ** [id](#API_CreateServiceNetwork_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetwork-response-id"></a>
The ID of the service network.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `sn-[0-9a-z]{17}`

 ** [name](#API_CreateServiceNetwork_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetwork-response-name"></a>
The name of the service network.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [sharingConfig](#API_CreateServiceNetwork_ResponseSyntax) **   <a name="vpclattice-CreateServiceNetwork-response-sharingConfig"></a>
Specifies if the service network is enabled for sharing.
Type: [SharingConfig](API_SharingConfig.md) object

## Errors
<a name="API_CreateServiceNetwork_Errors"></a>

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
<a name="API_CreateServiceNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/CreateServiceNetwork)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/CreateServiceNetwork)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/CreateServiceNetwork)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/CreateServiceNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/CreateServiceNetwork)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/CreateServiceNetwork)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/CreateServiceNetwork)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/CreateServiceNetwork)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/CreateServiceNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/CreateServiceNetwork)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
