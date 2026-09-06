---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateService.html
---

# CreateService
<a name="API_CreateService"></a>

Creates a service. A service is any software application that can run on instances containers, or serverless functions within an account or virtual private cloud (VPC).

For more information, see [Services](https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html) in the *Amazon VPC Lattice User Guide*.

## Request Syntax
<a name="API_CreateService_RequestSyntax"></a>

```
POST /services HTTP/1.1
Content-type: application/json

{
   "authType": "{{string}}",
   "certificateArn": "{{string}}",
   "clientToken": "{{string}}",
   "customDomainName": "{{string}}",
   "idleTimeoutSeconds": {{number}},
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateService_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateService_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authType](#API_CreateService_RequestSyntax) **   <a name="vpclattice-CreateService-request-authType"></a>
The type of IAM policy.
+  `NONE`: The resource does not use an IAM policy. This is the default.
+  `AWS_IAM`: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.
Type: String
Valid Values: `NONE | AWS_IAM`
Required: No

 ** [certificateArn](#API_CreateService_RequestSyntax) **   <a name="vpclattice-CreateService-request-certificateArn"></a>
The Amazon Resource Name (ARN) of the certificate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:certificate/[0-9a-z-]+)?`
Required: No

 ** [clientToken](#API_CreateService_RequestSyntax) **   <a name="vpclattice-CreateService-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[!-~]+.*`
Required: No

 ** [customDomainName](#API_CreateService_RequestSyntax) **   <a name="vpclattice-CreateService-request-customDomainName"></a>
The custom domain name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: No

 ** [idleTimeoutSeconds](#API_CreateService_RequestSyntax) **   <a name="vpclattice-CreateService-request-idleTimeoutSeconds"></a>
The amount of time, in seconds, that a connection can remain idle (no data sent) before VPC Lattice closes it. The valid range is 60 to 600 seconds. If you don't specify a value, the default is 60 seconds. This setting does not change the maximum connection duration of 10 minutes; connections are still closed when they reach that limit.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 600.
Required: No

 ** [name](#API_CreateService_RequestSyntax) **   <a name="vpclattice-CreateService-request-name"></a>
The name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!svc-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: Yes

 ** [tags](#API_CreateService_RequestSyntax) **   <a name="vpclattice-CreateService-request-tags"></a>
The tags for the service.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateService_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "authType": "string",
   "certificateArn": "string",
   "customDomainName": "string",
   "dnsEntry": {
      "domainName": "string",
      "hostedZoneId": "string"
   },
   "id": "string",
   "idleTimeoutSeconds": number,
   "name": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateService_ResponseSyntax) **   <a name="vpclattice-CreateService-response-arn"></a>
The Amazon Resource Name (ARN) of the service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}`

 ** [authType](#API_CreateService_ResponseSyntax) **   <a name="vpclattice-CreateService-response-authType"></a>
The type of IAM policy.
Type: String
Valid Values: `NONE | AWS_IAM`

 ** [certificateArn](#API_CreateService_ResponseSyntax) **   <a name="vpclattice-CreateService-response-certificateArn"></a>
The Amazon Resource Name (ARN) of the certificate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:certificate/[0-9a-z-]+)?`

 ** [customDomainName](#API_CreateService_ResponseSyntax) **   <a name="vpclattice-CreateService-response-customDomainName"></a>
The custom domain name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.

 ** [dnsEntry](#API_CreateService_ResponseSyntax) **   <a name="vpclattice-CreateService-response-dnsEntry"></a>
The public DNS name of the service.
Type: [DnsEntry](API_DnsEntry.md) object

 ** [id](#API_CreateService_ResponseSyntax) **   <a name="vpclattice-CreateService-response-id"></a>
The ID of the service.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `svc-[0-9a-z]{17}`

 ** [idleTimeoutSeconds](#API_CreateService_ResponseSyntax) **   <a name="vpclattice-CreateService-response-idleTimeoutSeconds"></a>
The amount of time, in seconds, that a connection can remain idle before VPC Lattice closes it.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 600.

 ** [name](#API_CreateService_ResponseSyntax) **   <a name="vpclattice-CreateService-response-name"></a>
The name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!svc-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [status](#API_CreateService_ResponseSyntax) **   <a name="vpclattice-CreateService-response-status"></a>
The status. If the status is `CREATE_FAILED`, you must delete and recreate the service.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED`

## Errors
<a name="API_CreateService_Errors"></a>

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
<a name="API_CreateService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/CreateService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/CreateService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/CreateService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/CreateService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/CreateService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/CreateService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/CreateService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/CreateService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/CreateService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/CreateService)
