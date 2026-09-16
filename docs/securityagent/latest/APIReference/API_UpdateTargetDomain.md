---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_UpdateTargetDomain.html
---

# UpdateTargetDomain
<a name="API_UpdateTargetDomain"></a>

Updates the verification method for a target domain.

## Request Syntax
<a name="API_UpdateTargetDomain_RequestSyntax"></a>

```
POST /UpdateTargetDomain HTTP/1.1
Content-type: application/json

{
   "targetDomainId": "{{string}}",
   "verificationMethod": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateTargetDomain_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateTargetDomain_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [targetDomainId](#API_UpdateTargetDomain_RequestSyntax) **   <a name="securityagent-UpdateTargetDomain-request-targetDomainId"></a>
The unique identifier of the target domain to update.
Type: String
Required: Yes

 ** [verificationMethod](#API_UpdateTargetDomain_RequestSyntax) **   <a name="securityagent-UpdateTargetDomain-request-verificationMethod"></a>
The updated verification method for the target domain.
Type: String
Valid Values: `DNS_TXT | HTTP_ROUTE | PRIVATE_VPC`
Required: Yes

## Response Syntax
<a name="API_UpdateTargetDomain_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "domainName": "string",
   "targetDomainId": "string",
   "verificationDetails": {
      "dnsTxt": {
         "dnsRecordName": "string",
         "dnsRecordType": "string",
         "token": "string"
      },
      "httpRoute": {
         "routePath": "string",
         "token": "string"
      },
      "method": "string"
   },
   "verificationStatus": "string",
   "verificationStatusReason": "string",
   "verifiedAt": "string"
}
```

## Response Elements
<a name="API_UpdateTargetDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_UpdateTargetDomain_ResponseSyntax) **   <a name="securityagent-UpdateTargetDomain-response-createdAt"></a>
The date and time the target domain was created, in UTC format.
Type: Timestamp

 ** [domainName](#API_UpdateTargetDomain_ResponseSyntax) **   <a name="securityagent-UpdateTargetDomain-response-domainName"></a>
The domain name of the target domain.
Type: String

 ** [targetDomainId](#API_UpdateTargetDomain_ResponseSyntax) **   <a name="securityagent-UpdateTargetDomain-response-targetDomainId"></a>
The unique identifier of the target domain.
Type: String

 ** [verificationDetails](#API_UpdateTargetDomain_ResponseSyntax) **   <a name="securityagent-UpdateTargetDomain-response-verificationDetails"></a>
The updated verification details for the target domain.
Type: [VerificationDetails](API_VerificationDetails.md) object

 ** [verificationStatus](#API_UpdateTargetDomain_ResponseSyntax) **   <a name="securityagent-UpdateTargetDomain-response-verificationStatus"></a>
The current verification status of the target domain.
Type: String
Valid Values: `PENDING | VERIFIED | FAILED | UNREACHABLE`

 ** [verificationStatusReason](#API_UpdateTargetDomain_ResponseSyntax) **   <a name="securityagent-UpdateTargetDomain-response-verificationStatusReason"></a>
The reason for the current target domain verification status.
Type: String

 ** [verifiedAt](#API_UpdateTargetDomain_ResponseSyntax) **   <a name="securityagent-UpdateTargetDomain-response-verifiedAt"></a>
The date and time the target domain was verified, in UTC format.
Type: Timestamp

## Errors
<a name="API_UpdateTargetDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_UpdateTargetDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/UpdateTargetDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/UpdateTargetDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/UpdateTargetDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/UpdateTargetDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/UpdateTargetDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/UpdateTargetDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/UpdateTargetDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/UpdateTargetDomain)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/UpdateTargetDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/UpdateTargetDomain)
