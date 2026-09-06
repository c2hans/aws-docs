---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_VerifyTargetDomain.html
---

# VerifyTargetDomain
<a name="API_VerifyTargetDomain"></a>

Initiates verification of a target domain. This checks whether the domain ownership verification token has been properly configured.

## Request Syntax
<a name="API_VerifyTargetDomain_RequestSyntax"></a>

```
POST /VerifyTargetDomain HTTP/1.1
Content-type: application/json

{
   "targetDomainId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_VerifyTargetDomain_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_VerifyTargetDomain_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [targetDomainId](#API_VerifyTargetDomain_RequestSyntax) **   <a name="securityagent-VerifyTargetDomain-request-targetDomainId"></a>
The unique identifier of the target domain to verify.
Type: String
Required: Yes

## Response Syntax
<a name="API_VerifyTargetDomain_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "domainName": "string",
   "status": "string",
   "targetDomainId": "string",
   "updatedAt": "string",
   "verificationStatusReason": "string",
   "verifiedAt": "string"
}
```

## Response Elements
<a name="API_VerifyTargetDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_VerifyTargetDomain_ResponseSyntax) **   <a name="securityagent-VerifyTargetDomain-response-createdAt"></a>
The date and time the target domain was created, in UTC format.
Type: Timestamp

 ** [domainName](#API_VerifyTargetDomain_ResponseSyntax) **   <a name="securityagent-VerifyTargetDomain-response-domainName"></a>
The domain name of the target domain.
Type: String

 ** [status](#API_VerifyTargetDomain_ResponseSyntax) **   <a name="securityagent-VerifyTargetDomain-response-status"></a>
The verification status of the target domain.
Type: String
Valid Values: `PENDING | VERIFIED | FAILED | UNREACHABLE`

 ** [targetDomainId](#API_VerifyTargetDomain_ResponseSyntax) **   <a name="securityagent-VerifyTargetDomain-response-targetDomainId"></a>
The unique identifier of the target domain.
Type: String

 ** [updatedAt](#API_VerifyTargetDomain_ResponseSyntax) **   <a name="securityagent-VerifyTargetDomain-response-updatedAt"></a>
The date and time the target domain was last updated, in UTC format.
Type: Timestamp

 ** [verificationStatusReason](#API_VerifyTargetDomain_ResponseSyntax) **   <a name="securityagent-VerifyTargetDomain-response-verificationStatusReason"></a>
The reason for the current target domain verification status.
Type: String

 ** [verifiedAt](#API_VerifyTargetDomain_ResponseSyntax) **   <a name="securityagent-VerifyTargetDomain-response-verifiedAt"></a>
The date and time the target domain was verified, in UTC format.
Type: Timestamp

## Errors
<a name="API_VerifyTargetDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_VerifyTargetDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/VerifyTargetDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/VerifyTargetDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/VerifyTargetDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/VerifyTargetDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/VerifyTargetDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/VerifyTargetDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/VerifyTargetDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/VerifyTargetDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/VerifyTargetDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/VerifyTargetDomain)
