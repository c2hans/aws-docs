---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchGetTargetDomains.html
---

# BatchGetTargetDomains
<a name="API_BatchGetTargetDomains"></a>

Retrieves information about one or more target domains.

## Request Syntax
<a name="API_BatchGetTargetDomains_RequestSyntax"></a>

```
POST /BatchGetTargetDomains HTTP/1.1
Content-type: application/json

{
   "targetDomainIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetTargetDomains_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetTargetDomains_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [targetDomainIds](#API_BatchGetTargetDomains_RequestSyntax) **   <a name="securityagent-BatchGetTargetDomains-request-targetDomainIds"></a>
The list of target domain identifiers to retrieve.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchGetTargetDomains_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "notFound": [ "string" ],
   "targetDomains": [
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
   ]
}
```

## Response Elements
<a name="API_BatchGetTargetDomains_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [notFound](#API_BatchGetTargetDomains_ResponseSyntax) **   <a name="securityagent-BatchGetTargetDomains-response-notFound"></a>
The list of target domain identifiers that were not found.
Type: Array of strings

 ** [targetDomains](#API_BatchGetTargetDomains_ResponseSyntax) **   <a name="securityagent-BatchGetTargetDomains-response-targetDomains"></a>
The list of target domains that were found.
Type: Array of [TargetDomain](API_TargetDomain.md) objects

## Errors
<a name="API_BatchGetTargetDomains_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_BatchGetTargetDomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchGetTargetDomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchGetTargetDomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchGetTargetDomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchGetTargetDomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchGetTargetDomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchGetTargetDomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchGetTargetDomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchGetTargetDomains)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchGetTargetDomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchGetTargetDomains)
