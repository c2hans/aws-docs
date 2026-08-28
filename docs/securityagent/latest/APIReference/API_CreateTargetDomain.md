---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_CreateTargetDomain.html
---

# CreateTargetDomain
<a name="API_CreateTargetDomain"></a>

Creates a new target domain for penetration testing. A target domain is a web domain that must be registered and verified before it can be tested.

## Request Syntax
<a name="API_CreateTargetDomain_RequestSyntax"></a>

```
POST /CreateTargetDomain HTTP/1.1
Content-type: application/json

{
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "targetDomainName": "{{string}}",
   "verificationMethod": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateTargetDomain_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateTargetDomain_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_CreateTargetDomain_RequestSyntax) **   <a name="securityagent-CreateTargetDomain-request-tags"></a>
The tags to associate with the target domain.
Type: String to string map
Required: No

 ** [targetDomainName](#API_CreateTargetDomain_RequestSyntax) **   <a name="securityagent-CreateTargetDomain-request-targetDomainName"></a>
The domain name to register as a target domain.
Type: String
Required: Yes

 ** [verificationMethod](#API_CreateTargetDomain_RequestSyntax) **   <a name="securityagent-CreateTargetDomain-request-verificationMethod"></a>
The method to use for verifying domain ownership. Valid values are DNS\_TXT, HTTP\_ROUTE, and PRIVATE\_VPC.
Type: String
Valid Values: `DNS_TXT | HTTP_ROUTE | PRIVATE_VPC`
Required: Yes

## Response Syntax
<a name="API_CreateTargetDomain_ResponseSyntax"></a>

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
<a name="API_CreateTargetDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateTargetDomain_ResponseSyntax) **   <a name="securityagent-CreateTargetDomain-response-createdAt"></a>
The date and time the target domain was created, in UTC format.
Type: Timestamp

 ** [domainName](#API_CreateTargetDomain_ResponseSyntax) **   <a name="securityagent-CreateTargetDomain-response-domainName"></a>
The domain name of the target domain.
Type: String

 ** [targetDomainId](#API_CreateTargetDomain_ResponseSyntax) **   <a name="securityagent-CreateTargetDomain-response-targetDomainId"></a>
The unique identifier of the created target domain.
Type: String

 ** [verificationDetails](#API_CreateTargetDomain_ResponseSyntax) **   <a name="securityagent-CreateTargetDomain-response-verificationDetails"></a>
The verification details for the target domain, including the verification token and instructions.
Type: [VerificationDetails](API_VerificationDetails.md) object

 ** [verificationStatus](#API_CreateTargetDomain_ResponseSyntax) **   <a name="securityagent-CreateTargetDomain-response-verificationStatus"></a>
The current verification status of the target domain.
Type: String
Valid Values: `PENDING | VERIFIED | FAILED | UNREACHABLE`

 ** [verificationStatusReason](#API_CreateTargetDomain_ResponseSyntax) **   <a name="securityagent-CreateTargetDomain-response-verificationStatusReason"></a>
The reason for the current target domain verification status.
Type: String

 ** [verifiedAt](#API_CreateTargetDomain_ResponseSyntax) **   <a name="securityagent-CreateTargetDomain-response-verifiedAt"></a>
The date and time the target domain was verified, in UTC format.
Type: Timestamp

## Errors
<a name="API_CreateTargetDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateTargetDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/CreateTargetDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/CreateTargetDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/CreateTargetDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/CreateTargetDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/CreateTargetDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/CreateTargetDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/CreateTargetDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/CreateTargetDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/CreateTargetDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/CreateTargetDomain)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
