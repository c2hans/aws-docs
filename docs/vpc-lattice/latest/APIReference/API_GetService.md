---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetService.html
---

# GetService
<a name="API_GetService"></a>

Retrieves information about the specified service.

## Request Syntax
<a name="API_GetService_RequestSyntax"></a>

```
GET /services/{{serviceIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetService_RequestParameters"></a>

The request uses the following URI parameters.

 ** [serviceIdentifier](#API_GetService_RequestSyntax) **   <a name="vpclattice-GetService-request-uri-serviceIdentifier"></a>
The ID or ARN of the service.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((svc-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_GetService_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetService_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "authType": "string",
   "certificateArn": "string",
   "createdAt": "string",
   "customDomainName": "string",
   "dnsEntry": {
      "domainName": "string",
      "hostedZoneId": "string"
   },
   "failureCode": "string",
   "failureMessage": "string",
   "id": "string",
   "idleTimeoutSeconds": number,
   "lastUpdatedAt": "string",
   "name": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetService_ResponseSyntax) **   <a name="vpclattice-GetService-response-arn"></a>
The Amazon Resource Name (ARN) of the service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}`

 ** [authType](#API_GetService_ResponseSyntax) **   <a name="vpclattice-GetService-response-authType"></a>
The type of IAM policy.
Type: String
Valid Values: `NONE | AWS_IAM`

 ** [certificateArn](#API_GetService_ResponseSyntax) **   <a name="vpclattice-GetService-response-certificateArn"></a>
The Amazon Resource Name (ARN) of the certificate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:certificate/[0-9a-z-]+)?`

 ** [createdAt](#API_GetService_ResponseSyntax) **   <a name="vpclattice-GetService-response-createdAt"></a>
The date and time that the service was created, in ISO-8601 format.
Type: Timestamp

 ** [customDomainName](#API_GetService_ResponseSyntax) **   <a name="vpclattice-GetService-response-customDomainName"></a>
The custom domain name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.

 ** [dnsEntry](#API_GetService_ResponseSyntax) **   <a name="vpclattice-GetService-response-dnsEntry"></a>
The DNS name of the service.
Type: [DnsEntry](API_DnsEntry.md) object

 ** [failureCode](#API_GetService_ResponseSyntax) **   <a name="vpclattice-GetService-response-failureCode"></a>
The failure code.
Type: String

 ** [failureMessage](#API_GetService_ResponseSyntax) **   <a name="vpclattice-GetService-response-failureMessage"></a>
The failure message.
Type: String

 ** [id](#API_GetService_ResponseSyntax) **   <a name="vpclattice-GetService-response-id"></a>
The ID of the service.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `svc-[0-9a-z]{17}`

 ** [idleTimeoutSeconds](#API_GetService_ResponseSyntax) **   <a name="vpclattice-GetService-response-idleTimeoutSeconds"></a>
The amount of time, in seconds, that a connection can remain idle before VPC Lattice closes it.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 600.

 ** [lastUpdatedAt](#API_GetService_ResponseSyntax) **   <a name="vpclattice-GetService-response-lastUpdatedAt"></a>
The date and time that the service was last updated, in ISO-8601 format.
Type: Timestamp

 ** [name](#API_GetService_ResponseSyntax) **   <a name="vpclattice-GetService-response-name"></a>
The name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!svc-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [status](#API_GetService_ResponseSyntax) **   <a name="vpclattice-GetService-response-status"></a>
The status of the service.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED`

## Errors
<a name="API_GetService_Errors"></a>

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
<a name="API_GetService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/GetService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/GetService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/GetService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/GetService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/GetService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/GetService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/GetService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/GetService)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/GetService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/GetService)
