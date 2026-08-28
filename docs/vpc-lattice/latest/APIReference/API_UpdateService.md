---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_UpdateService.html
---

# UpdateService
<a name="API_UpdateService"></a>

Updates the specified service.

## Request Syntax
<a name="API_UpdateService_RequestSyntax"></a>

```
PATCH /services/{{serviceIdentifier}} HTTP/1.1
Content-type: application/json

{
   "authType": "{{string}}",
   "certificateArn": "{{string}}",
   "idleTimeoutSeconds": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateService_RequestParameters"></a>

The request uses the following URI parameters.

 ** [serviceIdentifier](#API_UpdateService_RequestSyntax) **   <a name="vpclattice-UpdateService-request-uri-serviceIdentifier"></a>
The ID or ARN of the service.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((svc-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_UpdateService_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authType](#API_UpdateService_RequestSyntax) **   <a name="vpclattice-UpdateService-request-authType"></a>
The type of IAM policy.
+  `NONE`: The resource does not use an IAM policy. This is the default.
+  `AWS_IAM`: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.
Type: String
Valid Values: `NONE | AWS_IAM`
Required: No

 ** [certificateArn](#API_UpdateService_RequestSyntax) **   <a name="vpclattice-UpdateService-request-certificateArn"></a>
The Amazon Resource Name (ARN) of the certificate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:certificate/[0-9a-z-]+)?`
Required: No

 ** [idleTimeoutSeconds](#API_UpdateService_RequestSyntax) **   <a name="vpclattice-UpdateService-request-idleTimeoutSeconds"></a>
The amount of time, in seconds, that a connection can remain idle (no data sent) before VPC Lattice closes it. The valid range is 60 to 600 seconds. If you don't specify a value, the default is 60 seconds. This setting does not change the maximum connection duration of 10 minutes; connections are still closed when they reach that limit.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 600.
Required: No

## Response Syntax
<a name="API_UpdateService_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "authType": "string",
   "certificateArn": "string",
   "customDomainName": "string",
   "id": "string",
   "idleTimeoutSeconds": number,
   "name": "string"
}
```

## Response Elements
<a name="API_UpdateService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateService_ResponseSyntax) **   <a name="vpclattice-UpdateService-response-arn"></a>
The Amazon Resource Name (ARN) of the service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}`

 ** [authType](#API_UpdateService_ResponseSyntax) **   <a name="vpclattice-UpdateService-response-authType"></a>
The type of IAM policy.
Type: String
Valid Values: `NONE | AWS_IAM`

 ** [certificateArn](#API_UpdateService_ResponseSyntax) **   <a name="vpclattice-UpdateService-response-certificateArn"></a>
The Amazon Resource Name (ARN) of the certificate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:certificate/[0-9a-z-]+)?`

 ** [customDomainName](#API_UpdateService_ResponseSyntax) **   <a name="vpclattice-UpdateService-response-customDomainName"></a>
The custom domain name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.

 ** [id](#API_UpdateService_ResponseSyntax) **   <a name="vpclattice-UpdateService-response-id"></a>
The ID of the service.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `svc-[0-9a-z]{17}`

 ** [idleTimeoutSeconds](#API_UpdateService_ResponseSyntax) **   <a name="vpclattice-UpdateService-response-idleTimeoutSeconds"></a>
The amount of time, in seconds, that a connection can remain idle before VPC Lattice closes it.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 600.

 ** [name](#API_UpdateService_ResponseSyntax) **   <a name="vpclattice-UpdateService-response-name"></a>
The name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!svc-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

## Errors
<a name="API_UpdateService_Errors"></a>

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
<a name="API_UpdateService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/UpdateService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/UpdateService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/UpdateService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/UpdateService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/UpdateService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/UpdateService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/UpdateService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/UpdateService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/UpdateService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/UpdateService)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
