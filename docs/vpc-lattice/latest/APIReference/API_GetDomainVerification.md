---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetDomainVerification.html
---

# GetDomainVerification
<a name="API_GetDomainVerification"></a>

 Retrieves information about a domain verification.ß

## Request Syntax
<a name="API_GetDomainVerification_RequestSyntax"></a>

```
GET /domainverifications/{{domainVerificationIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDomainVerification_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainVerificationIdentifier](#API_GetDomainVerification_RequestSyntax) **   <a name="vpclattice-GetDomainVerification-request-uri-domainVerificationIdentifier"></a>
 The ID or ARN of the domain verification to retrieve.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((dv-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:domainverification/dv-[a-fA-F0-9]{17}))`
Required: Yes

## Request Body
<a name="API_GetDomainVerification_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDomainVerification_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdAt": "string",
   "domainName": "string",
   "id": "string",
   "lastVerifiedTime": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   },
   "txtMethodConfig": {
      "name": "string",
      "value": "string"
   }
}
```

## Response Elements
<a name="API_GetDomainVerification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetDomainVerification_ResponseSyntax) **   <a name="vpclattice-GetDomainVerification-response-arn"></a>
 The Amazon Resource Name (ARN) of the domain verification.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9f\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:domainverification/dv-[a-fA-F0-9]{17}`

 ** [createdAt](#API_GetDomainVerification_ResponseSyntax) **   <a name="vpclattice-GetDomainVerification-response-createdAt"></a>
 The date and time that the domain verification was created, in ISO-8601 format.
Type: Timestamp

 ** [domainName](#API_GetDomainVerification_ResponseSyntax) **   <a name="vpclattice-GetDomainVerification-response-domainName"></a>
 The domain name being verified.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.

 ** [id](#API_GetDomainVerification_ResponseSyntax) **   <a name="vpclattice-GetDomainVerification-response-id"></a>
 The ID of the domain verification.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `dv-[a-fA-F0-9]{17}`

 ** [lastVerifiedTime](#API_GetDomainVerification_ResponseSyntax) **   <a name="vpclattice-GetDomainVerification-response-lastVerifiedTime"></a>
 The date and time that the domain was last successfully verified, in ISO-8601 format.
Type: Timestamp

 ** [status](#API_GetDomainVerification_ResponseSyntax) **   <a name="vpclattice-GetDomainVerification-response-status"></a>
 The current status of the domain verification process.
Type: String
Valid Values: `VERIFIED | PENDING | VERIFICATION_TIMED_OUT`

 ** [tags](#API_GetDomainVerification_ResponseSyntax) **   <a name="vpclattice-GetDomainVerification-response-tags"></a>
 The tags associated with the domain verification.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [txtMethodConfig](#API_GetDomainVerification_ResponseSyntax) **   <a name="vpclattice-GetDomainVerification-response-txtMethodConfig"></a>
 The TXT record configuration used for domain verification.
Type: [TxtMethodConfig](API_TxtMethodConfig.md) object

## Errors
<a name="API_GetDomainVerification_Errors"></a>

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
<a name="API_GetDomainVerification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/GetDomainVerification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/GetDomainVerification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/GetDomainVerification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/GetDomainVerification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/GetDomainVerification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/GetDomainVerification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/GetDomainVerification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/GetDomainVerification)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/GetDomainVerification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/GetDomainVerification)
