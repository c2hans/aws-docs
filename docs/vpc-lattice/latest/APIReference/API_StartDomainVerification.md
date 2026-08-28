---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_StartDomainVerification.html
---

# StartDomainVerification
<a name="API_StartDomainVerification"></a>

 Starts the domain verification process for a custom domain name.

## Request Syntax
<a name="API_StartDomainVerification_RequestSyntax"></a>

```
POST /domainverifications HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "domainName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartDomainVerification_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartDomainVerification_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartDomainVerification_RequestSyntax) **   <a name="vpclattice-StartDomainVerification-request-clientToken"></a>
 A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[!-~]+.*`
Required: No

 ** [domainName](#API_StartDomainVerification_RequestSyntax) **   <a name="vpclattice-StartDomainVerification-request-domainName"></a>
 The domain name to verify ownership for.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: Yes

 ** [tags](#API_StartDomainVerification_RequestSyntax) **   <a name="vpclattice-StartDomainVerification-request-tags"></a>
 The tags for the domain verification.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_StartDomainVerification_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "domainName": "string",
   "id": "string",
   "status": "string",
   "txtMethodConfig": {
      "name": "string",
      "value": "string"
   }
}
```

## Response Elements
<a name="API_StartDomainVerification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_StartDomainVerification_ResponseSyntax) **   <a name="vpclattice-StartDomainVerification-response-arn"></a>
 The Amazon Resource Name (ARN) of the domain verification.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9f\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:domainverification/dv-[a-fA-F0-9]{17}`

 ** [domainName](#API_StartDomainVerification_ResponseSyntax) **   <a name="vpclattice-StartDomainVerification-response-domainName"></a>
 The domain name being verified.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.

 ** [id](#API_StartDomainVerification_ResponseSyntax) **   <a name="vpclattice-StartDomainVerification-response-id"></a>
 The ID of the domain verification.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `dv-[a-fA-F0-9]{17}`

 ** [status](#API_StartDomainVerification_ResponseSyntax) **   <a name="vpclattice-StartDomainVerification-response-status"></a>
 The current status of the domain verification process.
Type: String
Valid Values: `VERIFIED | PENDING | VERIFICATION_TIMED_OUT`

 ** [txtMethodConfig](#API_StartDomainVerification_ResponseSyntax) **   <a name="vpclattice-StartDomainVerification-response-txtMethodConfig"></a>
 The TXT record configuration used for domain verification.
Type: [TxtMethodConfig](API_TxtMethodConfig.md) object

## Errors
<a name="API_StartDomainVerification_Errors"></a>

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
<a name="API_StartDomainVerification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/StartDomainVerification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/StartDomainVerification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/StartDomainVerification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/StartDomainVerification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/StartDomainVerification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/StartDomainVerification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/StartDomainVerification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/StartDomainVerification)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/StartDomainVerification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/StartDomainVerification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
