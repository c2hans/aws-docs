---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ListDomains.html
---

# ListDomains
<a name="API_ListDomains"></a>

Lists Domains for a given account.

## Request Syntax
<a name="API_ListDomains_RequestSyntax"></a>

```
GET /domain?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDomains_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListDomains_RequestSyntax) **   <a name="connecthealth-ListDomains-request-uri-maxResults"></a>
Maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListDomains_RequestSyntax) **   <a name="connecthealth-ListDomains-request-uri-nextToken"></a>
Token for pagination.

 ** [status](#API_ListDomains_RequestSyntax) **   <a name="connecthealth-ListDomains-request-uri-status"></a>
Filter by Domain status.
Valid Values: `ACTIVE | DELETING | DELETED`

## Request Body
<a name="API_ListDomains_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDomains_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "domains": [
      {
         "arn": "string",
         "createdAt": number,
         "domainId": "string",
         "name": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDomains_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domains](#API_ListDomains_ResponseSyntax) **   <a name="connecthealth-ListDomains-response-domains"></a>
List of Domains.
Type: Array of [DomainSummary](API_DomainSummary.md) objects

 ** [nextToken](#API_ListDomains_ResponseSyntax) **   <a name="connecthealth-ListDomains-response-nextToken"></a>
Token for the next page of results.
Type: String

## Errors
<a name="API_ListDomains_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListDomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connecthealth-2025-01-29/ListDomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connecthealth-2025-01-29/ListDomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/ListDomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connecthealth-2025-01-29/ListDomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/ListDomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connecthealth-2025-01-29/ListDomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connecthealth-2025-01-29/ListDomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connecthealth-2025-01-29/ListDomains)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connecthealth-2025-01-29/ListDomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/ListDomains)
