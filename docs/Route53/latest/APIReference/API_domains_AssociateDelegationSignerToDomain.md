---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AssociateDelegationSignerToDomain.html
---

# AssociateDelegationSignerToDomain
<a name="API_domains_AssociateDelegationSignerToDomain"></a>

 Creates a delegation signer (DS) record in the registry zone for this domain name.

Note that creating DS record at the registry impacts DNSSEC validation of your DNS records. This action may render your domain name unavailable on the internet if the steps are completed in the wrong order, or with incorrect timing. For more information about DNSSEC signing, see [Configuring DNSSEC signing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec.html) in the *Route 53 developer guide*.

## Request Syntax
<a name="API_domains_AssociateDelegationSignerToDomain_RequestSyntax"></a>

```
{
   "DomainName": "{{string}}",
   "SigningAttributes": {
      "Algorithm": {{number}},
      "Flags": {{number}},
      "PublicKey": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_domains_AssociateDelegationSignerToDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainName](#API_domains_AssociateDelegationSignerToDomain_RequestSyntax) **   <a name="Route53Domains-domains_AssociateDelegationSignerToDomain-request-DomainName"></a>
The name of the domain.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [SigningAttributes](#API_domains_AssociateDelegationSignerToDomain_RequestSyntax) **   <a name="Route53Domains-domains_AssociateDelegationSignerToDomain-request-SigningAttributes"></a>
The information about a key, including the algorithm, public key-value, and flags.
Type: [DnssecSigningAttributes](API_domains_DnssecSigningAttributes.md) object
Required: Yes

## Response Syntax
<a name="API_domains_AssociateDelegationSignerToDomain_ResponseSyntax"></a>

```
{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_domains_AssociateDelegationSignerToDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_domains_AssociateDelegationSignerToDomain_ResponseSyntax) **   <a name="Route53Domains-domains_AssociateDelegationSignerToDomain-response-OperationId"></a>
The identifier for tracking the progress of the request. To query the operation status, use [GetOperationDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html).
Type: String
Length Constraints: Maximum length of 255.

## Errors
<a name="API_domains_AssociateDelegationSignerToDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DnssecLimitExceeded **
 This error is returned if you call `AssociateDelegationSignerToDomain` when the specified domain has reached the maximum number of DS records. You can't add any additional DS records unless you delete an existing one first.
HTTP Status Code: 400

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
<a name="API_domains_AssociateDelegationSignerToDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/AssociateDelegationSignerToDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/AssociateDelegationSignerToDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/AssociateDelegationSignerToDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/AssociateDelegationSignerToDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/AssociateDelegationSignerToDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/AssociateDelegationSignerToDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/AssociateDelegationSignerToDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/AssociateDelegationSignerToDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/AssociateDelegationSignerToDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/AssociateDelegationSignerToDomain)
