---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DisassociateDelegationSignerFromDomain.html
---

# DisassociateDelegationSignerFromDomain
<a name="API_domains_DisassociateDelegationSignerFromDomain"></a>

Deletes a delegation signer (DS) record in the registry zone for this domain name.

## Request Syntax
<a name="API_domains_DisassociateDelegationSignerFromDomain_RequestSyntax"></a>

```
{
   "DomainName": "{{string}}",
   "Id": "{{string}}"
}
```

## Request Parameters
<a name="API_domains_DisassociateDelegationSignerFromDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainName](#API_domains_DisassociateDelegationSignerFromDomain_RequestSyntax) **   <a name="Route53Domains-domains_DisassociateDelegationSignerFromDomain-request-DomainName"></a>
Name of the domain.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [Id](#API_domains_DisassociateDelegationSignerFromDomain_RequestSyntax) **   <a name="Route53Domains-domains_DisassociateDelegationSignerFromDomain-request-Id"></a>
An internal identification number assigned to each DS record after it’s created. You can retrieve it as part of DNSSEC information returned by [GetDomainDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetDomainDetail.html).
Type: String
Required: Yes

## Response Syntax
<a name="API_domains_DisassociateDelegationSignerFromDomain_ResponseSyntax"></a>

```
{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_domains_DisassociateDelegationSignerFromDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_domains_DisassociateDelegationSignerFromDomain_ResponseSyntax) **   <a name="Route53Domains-domains_DisassociateDelegationSignerFromDomain-response-OperationId"></a>
Identifier for tracking the progress of the request. To query the operation status, use [GetOperationDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html).
Type: String
Length Constraints: Maximum length of 255.

## Errors
<a name="API_domains_DisassociateDelegationSignerFromDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateRequest **
The request is already in progress for the domain.
 ** message **
The request is already in progress for the domain.
 ** requestId **
ID of the request operation.
HTTP Status Code: 400

 ** InvalidInput **
The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For `AcceptDomainTransferFromAnotherAwsAccount`, the password might be invalid.
 ** message **
The requested item is not acceptable. For example, for an OperationId it might refer to the ID of an operation that is already completed. For a domain name, it might not be a valid domain name or belong to the requester account.
HTTP Status Code: 400

 ** OperationLimitExceeded **
The number of operations or jobs running exceeded the allowed threshold for the account.
 ** message **
The number of operations or jobs running exceeded the allowed threshold for the account.
HTTP Status Code: 400

 ** TLDRulesViolation **
The top-level domain does not support this operation.
 ** message **
The top-level domain does not support this operation.
HTTP Status Code: 400

 ** UnsupportedTLD **
Amazon Route 53 does not support this top-level domain (TLD).
 ** message **
Amazon Route 53 does not support this top-level domain (TLD).
HTTP Status Code: 400

## See Also
<a name="API_domains_DisassociateDelegationSignerFromDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/DisassociateDelegationSignerFromDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/DisassociateDelegationSignerFromDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/DisassociateDelegationSignerFromDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/DisassociateDelegationSignerFromDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/DisassociateDelegationSignerFromDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/DisassociateDelegationSignerFromDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/DisassociateDelegationSignerFromDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/DisassociateDelegationSignerFromDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/DisassociateDelegationSignerFromDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/DisassociateDelegationSignerFromDomain)
